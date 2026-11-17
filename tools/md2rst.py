#!/usr/bin/env python3
"""Markdown -> reStructuredText, for the three contributions in this repository.

  python tools/md2rst.py --src sources --out sources-rst

Written because ITU's guidance for FG contributions marks .docx as discouraged
and names plain text or reStructuredText instead, and no converter was available
on the machine where this was prepared.

Scope: exactly the Markdown this repository contains - headings, pipe tables,
lists, fenced code blocks, blockquotes, horizontal rules, bold, inline code.
It is not a general Markdown converter and should not be used as one.

Requires Python 3 and docutils if you want the self-check to run; the conversion
itself needs only the standard library.
"""

import argparse
import os
import re
import sys

UNDER = {1: "=", 2: "-", 3: "~", 4: "^"}


def inline(s):
    return re.sub(r"`([^`]+)`", r"``\1``", s)


def split_row(ln):
    ln = ln.strip()
    if ln.startswith("|"):
        ln = ln[1:]
    if ln.endswith("|"):
        ln = ln[:-1]
    return [c.strip() for c in ln.split("|")]


def is_sep(ln):
    return bool(re.match(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", ln.strip()))


def convert(md):
    lines = md.splitlines()
    out = []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]

        m = re.match(r"^```(.*)$", ln.strip())
        if m:
            lang = m.group(1).strip()
            i += 1
            body = []
            while i < n and not lines[i].strip().startswith("```"):
                body.append("    " + lines[i].rstrip() if lines[i].strip() else "")
                i += 1
            i += 1
            out.append(f".. code-block:: {lang}" if lang else "::")
            out.append("")
            out.extend(body)
            out.append("")
            continue

        if ln.strip().startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                if not is_sep(lines[i]):
                    rows.append([inline(c) for c in split_row(lines[i])])
                i += 1
            if rows:
                ncol = max(len(r) for r in rows)
                for r in rows:
                    while len(r) < ncol:
                        r.append("")
                w = [max(3, max(len(r[c]) for r in rows)) for c in range(ncol)]
                sep = "  ".join("=" * x for x in w)
                out.append(sep)
                for k, r in enumerate(rows):
                    out.append("  ".join(r[c].ljust(w[c]) for c in range(ncol)).rstrip())
                    if k == 0:
                        out.append(sep)
                out.append(sep)
                out.append("")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            lvl = min(len(m.group(1)), 4)
            title = inline(m.group(2).strip())
            out.append(title)
            out.append(UNDER[lvl] * max(len(title), 4))
            out.append("")
            i += 1
            continue

        if re.match(r"^-{3,}$", ln.strip()):
            out.append("----")
            out.append("")
            i += 1
            continue

        if ln.strip().startswith(">"):
            body = []
            while i < n and lines[i].strip().startswith(">"):
                body.append(inline(lines[i].strip()[1:].strip()))
                i += 1
            out.append("")
            out.append("   " + " ".join(body))
            out.append("")
            continue

        if re.match(r"^\s*[-*+]\s+", ln):
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                out.append("- " + inline(re.sub(r"^\s*[-*+]\s+", "", lines[i]).strip()))
                i += 1
            out.append("")
            continue

        if re.match(r"^\s*\d+\.\s+", ln):
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                out.append("#. " + inline(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()))
                i += 1
            out.append("")
            continue

        if not ln.strip():
            out.append("")
            i += 1
            continue

        out.append(inline(ln.rstrip()))
        i += 1

    res = []
    for ln in out:
        if ln == "" and res and res[-1] == "":
            continue
        res.append(ln)
    return "\n".join(res).strip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="sources")
    ap.add_argument("--out", default="sources-rst")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    bad = 0
    for f in sorted(os.listdir(a.src)):
        if not f.endswith(".md"):
            continue
        md = open(os.path.join(a.src, f), encoding="utf-8").read()
        rst = convert(md)
        dst = os.path.join(a.out, f[:-3] + ".rst")
        open(dst, "w", encoding="utf-8", newline="\n").write(rst)
        status = ""
        try:
            from docutils.core import publish_doctree
            import io as _io
            err = []
            publish_doctree(rst, settings_overrides={
                "report_level": 2, "halt_level": 5,
                "warning_stream": _io.StringIO(),
                "file_insertion_enabled": False})
            status = "  parsed ok"
        except ImportError:
            status = "  (docutils not installed; not parsed)"
        except Exception as e:
            status = f"  PARSE FAILED: {e}"
            bad += 1
        print(f"  {f} -> {os.path.basename(dst)}  {len(rst)} chars{status}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
