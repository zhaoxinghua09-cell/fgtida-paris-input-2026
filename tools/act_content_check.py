#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Act-content binding check (minimal, dependency-free).

A decision record satisfies "act-content binding" iff:
  1. it contains the act-describing fields it decided on (action, resource,
     parameters, principal, audience), with instance-level values (no
     class-level placeholders such as "*" or "any");
  2. it carries a digest recomputed from those fields under the stated
     byte rule, and the digest matches a recomputation;
  3. an assignable label alone (e.g. a random UUID) is not accepted as binding.

Precondition (stated in the document, not enforced here): the binding value is
fixed at decision time and the record is protected (signed, or held in an
append-only store). Without that anchor, an attacker who rewrites both the act
and the digest passes the check; the check detects substitution against a
pinned binding, not record forgery.

Exit codes
  0  all conditions satisfied
  1  record does not carry act-content binding (missing/invalid binding,
     or an assignable label only)
  2  substitution detected: missing act-describing field, class-level
     placeholder value, or digest mismatch
  3  value cannot be canonicalized under the byte rule (floating-point
     number; the rule admits strings and integers only)
  4  input is not valid JSON / not a mapping

Usage
  python act_content_check.py <record.json>
  python act_content_check.py --selftest
"""
import hashlib
import json
import sys

ACT_FIELDS = ["action", "resource", "parameters", "principal", "audience"]
PLACEHOLDERS = {"*", "any", "all", "default", "tbd", "n/a", "none"}


def has_float(value):
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(has_float(v) for v in value.values())
    if isinstance(value, list):
        return any(has_float(v) for v in value)
    return False


def _placeholder_token(text):
    t = text.strip().lower()
    if t in PLACEHOLDERS:
        return True
    for sep in (":", "/", "#", "@"):
        if sep in t and t.rsplit(sep, 1)[1].strip() in PLACEHOLDERS:
            return True
    return False


def has_placeholder(value):
    if isinstance(value, str):
        return _placeholder_token(value)
    if isinstance(value, dict):
        return any(has_placeholder(v) for v in value.values())
    if isinstance(value, list):
        return any(has_placeholder(v) for v in value)
    return False


def canonical(obj):
    """Deterministic bytes: JSON, keys in Unicode code-point order, no spaces.

    The byte rule admits strings, integers, booleans, null, lists and objects.
    Floating-point numbers are rejected (exit 3) because their JSON rendering
    differs between languages and would break cross-implementation digests.
    """
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def normalize_act(act):
    """Keep only act-describing fields. Returns (normalized, missing)."""
    if not isinstance(act, dict):
        return None, ["<act is not an object>"]
    normalized = {}
    missing = []
    for f in ACT_FIELDS:
        if f in act and act[f] is not None and act[f] != "":
            normalized[f] = act[f]
        else:
            missing.append(f)
    return normalized, missing


def digest(normalized):
    return "sha256:" + hashlib.sha256(canonical(normalized)).hexdigest()


def check(record):
    """Return (exit_code, message)."""
    if not isinstance(record, dict):
        return 4, "input is not a JSON object"

    binding = record.get("act_binding")
    act = record.get("act")

    if not isinstance(binding, dict):
        return 1, "no act_binding object: record does not identify the act content"

    algo = binding.get("algorithm")
    claimed = binding.get("digest")
    if algo == "uuid" or (isinstance(claimed, str) and claimed.startswith("uuid:")):
        return 1, "assignable label only (uuid) is not act-content binding"
    if algo != "sha256" or not isinstance(claimed, str) or not claimed.startswith("sha256:"):
        return 1, "unsupported or missing binding algorithm (expected sha256)"

    normalized, missing = normalize_act(act)
    if normalized is None:
        return 2, "act is not an object; cannot recompute"
    if missing:
        return 2, "act is missing act-describing field(s): " + ", ".join(missing)

    if has_placeholder(normalized):
        return 2, "act value is a class-level placeholder; instance-level values are required"

    if has_float(normalized):
        return 3, "floating-point value cannot be canonicalized under the byte rule"

    recomputed = digest(normalized)
    if recomputed != claimed:
        return 2, "binding mismatch: record does not bind the act content it presents"
    return 0, "act-content binding satisfied"


def selftest():
    base_act = {
        "action": "release-model",
        "resource": "model:fraud-v3",
        "parameters": {"threshold": "0.82", "region": "eu"},
        "principal": "org-a/agent-01",
        "audience": "org-b",
    }

    def rec(act, digest_value, algo="sha256"):
        return {"act": act, "act_binding": {"algorithm": algo, "digest": digest_value}}

    good = rec(base_act, digest(base_act))

    tampered = json.loads(json.dumps(good))
    tampered["act"]["resource"] = "model:fraud-v9"  # same digest, different act

    uuid_only = rec(base_act, "uuid:6f1c2a9e", algo="uuid")

    missing = json.loads(json.dumps(good))
    del missing["act"]["principal"]

    placeholder = rec({**base_act, "resource": "model:any"}, "sha256:" + "0" * 64)
    placeholder["act_binding"]["digest"] = digest({**base_act, "resource": "model:any"})

    floaty = json.loads(json.dumps(good))
    floaty["act"]["parameters"] = {"threshold": 0.82}
    floaty["act_binding"]["digest"] = "sha256:" + "0" * 64

    reordered_act = {k: base_act[k] for k in reversed(list(base_act.keys()))}
    reordered = rec(reordered_act, digest(reordered_act))

    cases = [
        ("valid", good, 0),
        ("substituted-act", tampered, 2),
        ("uuid-only", uuid_only, 1),
        ("missing-principal", missing, 2),
        ("class-level-placeholder", placeholder, 2),
        ("float-value", floaty, 3),
        ("reordered-fields", reordered, 0),
    ]
    failures = 0
    for name, record, expected in cases:
        code, msg = check(record)
        if code != expected:
            failures += 1
        print("[%s] %-24s exit=%d expected=%d  %s" % (
            "PASS" if code == expected else "FAIL", name, code, expected, msg))
    print("SELFTEST %s (%d vectors)" % ("OK" if failures == 0 else "FAILED", len(cases)))
    return 0 if failures == 0 else 1


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    if sys.argv[1] == "--selftest":
        return selftest()
    try:
        record = json.load(open(sys.argv[1], encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print("invalid JSON: %s" % exc)
        return 4
    code, msg = check(record)
    print("exit=%d %s" % (code, msg))
    return code


if __name__ == "__main__":
    sys.exit(main())

