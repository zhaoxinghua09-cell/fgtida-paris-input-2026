#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_package_integrity.py —— 投稿件结构完整性（离线，标准库）。

只验结构与可重建性前提，**不验内容是否正确、不验是否被 ITU 采纳**。

跑法：python tests/test_package_integrity.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REBUILT = ROOT / "docs-rebuilt"
RST = ROOT / "sources-rst"
EVID = ROOT / "evidence-pack"
WG = ("WG0", "WG1", "WG2")
EVID_FILES = ("citation-check.md", "external-ai-review.md", "redteam.md", "publish-manifest.json")

def main():
    failures = []

    # 1. 三个工作组各有源文件
    for wg in WG:
        if not list(RST.glob(f"*{wg.lower()}*.rst")):
            failures.append(f"sources-rst 缺 {wg} 的 rst 源")

    # 2. 每个 .docx 都要有同名 .b64 副本（可重建前提）
    docx = sorted(DOCS.glob("*.docx"))
    if not docx:
        failures.append("docs/ 下没有 .docx")
    for d in docx:
        if not (REBUILT / (d.name + ".b64")).exists():
            failures.append(f"docs-rebuilt 缺 {d.name}.b64")

    # 3. 三份稿件版本号必须能解析出来（引用要带版本）
    for wg in WG:
        items = [p.name for p in DOCS.glob(f"*{wg}*.docx")]
        if not items:
            failures.append(f"docs/ 缺 {wg} 成品")
            continue
        for name in items:
            if not re.search(r"v\d+\.\d+(\.\d+)?", name):
                failures.append(f"{name} 文件名不含版本号")

    # 4. 证据包四件齐
    for f in EVID_FILES:
        if not (EVID / f).exists():
            failures.append(f"evidence-pack 缺 {f}")

    if failures:
        print("FAIL")
        for f in failures:
            print("  -", f)
        return 1
    print(f"OK: {len(docx)} 份成品均有可重建副本；3 个 WG 源/版本/证据包齐全")
    return 0

if __name__ == "__main__":
    sys.exit(main())
