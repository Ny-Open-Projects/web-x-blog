#!/usr/bin/env python3
"""面试课卡片 -> hexo source/_posts 的轻量 front-matter 适配器（抽检用）。

面试课用六段式模板、无 front-matter，ingest_target.py 的目标课门禁不适用。
本脚本只做：提 H1 标题 + 关键词 tags -> 生成 front-matter -> 加 {course}- 前缀落盘。
全量入站前先用它抽检渲染。
"""
import re
import sys
from pathlib import Path

ROOT = Path("/Users/Wang/Code/github/web-x-blog")
POSTS = ROOT / "work" / "blog" / "source" / "_posts"
SRC = {
    "py-interview": ROOT / "work/py-interview/target",
    "campus": ROOT / "work/target/campus",
    "mysql-interview": ROOT / "work/mysql-interview/target",
}
DATE = "2026-10-22 12:00:00"

def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')

def yaml_list(items):
    return "[" + ", ".join('"' + esc(x) + '"' for x in items) + "]"

def build(course: str, fname: str) -> str:
    text = (SRC[course] / fname).read_text(encoding="utf-8")
    # title = first H1
    m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    title = m.group(1) if m else fname
    # tags from 关键词 line
    tags = []
    km = re.search(r"关键词[:：]\s*(.+?)\s*$", text, re.M)
    if km:
        tags = [t.strip().strip("*").strip() for t in re.split(r"[/、,，]", km.group(1)) if t.strip().strip("*").strip()]
    fm = (
        "---\n"
        f'title: "{esc(title)}"\n'
        f"date: {DATE}\n"
        f"categories: {yaml_list([course])}\n"
        f"tags: {yaml_list(tags)}\n"
        "disableNunjucks: true\n"
        "---\n\n"
    )
    dst = POSTS / f"{course}-{fname}"
    dst.write_text(fm + text, encoding="utf-8")
    return dst.name

# curated spot-check sample covering python/go/sql/mermaid/table/blockquote
SAMPLE = [
    ("py-interview", ["63_functools-lru-cache.md", "93_nested-empty-input.md",
                      "100_python-class-definition.md", "105_classmethod-vs-staticmethod.md",
                      "168_generational-gc.deep.md"]),
    ("campus", ["10_TCP三次握手流程与细节.md", "14_TCP粘包问题与解决.md",
                "26_编程实现LRU页面置换算法.md"]),
    ("mysql-interview", ["001-mysql-three-distributions.md", "002-distribution-four-dimension-compare.md"]),
]

def main():
    n = 0
    for course, files in SAMPLE:
        for f in files:
            p = SRC[course] / f
            if not p.exists():
                print(f"[MISS] {course}/{f}"); continue
            name = build(course, f)
            print(f"[OK] {name}")
            n += 1
    print(f"\ningested {n} sample posts")

if __name__ == "__main__":
    main()
