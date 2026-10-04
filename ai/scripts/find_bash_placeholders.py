#!/usr/bin/env python3
"""列出所有课程 target 下、bash/shell/sh 代码块里残留的尖括号占位符 <word>。
只扫 bash 块（与 qc_articles 口径一致），```text 说明块里的 <res> 不视为问题。
先 dry-run 列出，人工确认都是 CLI 参数占位符后再做替换。
"""
import re
import sys
from pathlib import Path

ROOT = Path("/Users/Wang/Code/github/web-x-blog")
TARGET = ROOT / "work" / "target"
PAT = re.compile(r"<([A-Za-z][A-Za-z0-9_-]*)>")
FENCE = re.compile(r"^```(bash|shell|sh)\s*$")
END = re.compile(r"^```\s*$")


def scan(f: Path):
    rows = []
    inb = False
    for i, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        s = ln.rstrip("\n")
        if FENCE.match(s):
            inb = True
            continue
        if END.match(s) and inb:
            inb = False
            continue
        if inb and not s.strip().startswith("#"):
            for m in PAT.finditer(s):
                rows.append((f, i, m.group(0)))
    return rows


def main():
    files = sorted(TARGET.rglob("*.md"))
    all_rows = []
    for f in files:
        all_rows += scan(f)
    print(f"扫描 {len(files)} 个 target md，命中占位符 {len(all_rows)} 处：\n")
    for f, i, tok in all_rows:
        rel = f.relative_to(ROOT)
        print(f"  {rel}:{i}  {tok}")


if __name__ == "__main__":
    main()
