#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Consistency checks: README <-> manifest <-> filenames <-> DOCX cover.

Exit 0 only when all checks pass. Dependency-free (stdlib only).
"""
import argparse
import hashlib
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def docx_text(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    return re.sub(r"<[^>]+>", " ", xml)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=os.path.join(ROOT, "manifest-3items.json"))
    ap.add_argument("--readme", default=os.path.join(ROOT, "README.md"))
    a = ap.parse_args()

    manifest = json.load(open(a.manifest, encoding="utf-8"))
    readme = open(a.readme, encoding="utf-8").read()
    version = manifest.get("version")
    check(version in readme, "README does not state manifest version %r" % version)

    for item in manifest.get("items", []):
        path = os.path.join(ROOT, item["docx"])
        check(os.path.exists(path), "missing file: " + item["docx"])
        if not os.path.exists(path):
            continue
        data = open(path, "rb").read()
        check(len(data) == item["bytes"], "size mismatch: %s (%d != %d)" % (item["docx"], len(data), item["bytes"]))
        check(hashlib.sha256(data).hexdigest() == item["sha256"], "sha256 mismatch: " + item["docx"])
        check(item["docx"] in readme, "README does not list " + item["docx"])
        token = re.search(r"v(\d+\.\d+\.\d+)", os.path.basename(item["docx"]))
        if token:
            cover = docx_text(path)
            check(("revision v%s" % token.group(1)) in cover.replace("  ", " "),
                  "DOCX cover revision does not match filename version: " + item["docx"])

    if errors:
        print("CONSISTENCY: FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("CONSISTENCY: PASS (%d documents)" % len(manifest.get("items", [])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
