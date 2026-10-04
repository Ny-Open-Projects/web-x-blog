#!/usr/bin/env python3
"""删除 target 下所有课程文章末尾的 QA 脚手架行：
    相关度：xx%。是否需要继续：[否]。代码是否可运行：[是]。
这些是流水线自检用的，发布成生产参考文档前应剥离（专业评审 R3/R5 的 Blocker）。
只删以这些短语开头的整行，正文里出现的同类词不受影响。
"""
import re
from pathlib import Path

ROOT = Path("/Users/Wang/Code/github/web-x-blog")
TARGET = ROOT / "work" / "target"
PAT = re.compile(r"^(相关度：|是否需要继续：|代码是否可运行：)")

total = 0
for f in sorted(TARGET.rglob("*.md")):
    lines = f.read_text(encoding="utf-8").splitlines()
    new = [l for l in lines if not PAT.match(l.strip())]
    if len(new) != len(lines):
        f.write_text("\n".join(new) + "\n", encoding="utf-8")
        total += 1

print(f"stripped footer from {total} files")
