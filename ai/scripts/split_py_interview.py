#!/usr/bin/env python3
"""把 source/27.python-interview-3000 的章节 md 拆成题目卡片，落 target/27-python-interview/。

题头形如 `### Q001 · 标题`（正文）与 `### A001 · 标题`（算法专题，type: 笔试题）。
前作 13 号课（work/py-interview，238 卡）偏服务端速查；本课为工程向原理+追问链题库，编号口径 Q001-Q3000 / A001+。
"""
import re
from pathlib import Path

SRC = Path("/Users/Wang/Code/github/web-x-blog/work/source/27.python-interview-3000")
DST = Path("/Users/Wang/Code/github/web-x-blog/work/target/27-python-interview")

# 章节目录 -> (大类目录, hexo 分类)
DIR_MAP = {
    "01_语言核心与底层": ("01-语言核心与底层", "Python语言核心"),
    "02_并发与网络工程": ("02-并发与网络工程", "Python并发与网络"),
    "03_Web后端开发": ("03-Web后端开发", "PythonWeb后端"),
    "04_数据库与缓存": ("04-数据库与缓存", "Python数据库与缓存"),
    "05_数据分析与工程化": ("05-数据分析与工程化", "Python工程化"),
    "06_Agent与LLM及系统设计": ("06-Agent与LLM及系统设计", "PythonAgent与系统设计"),
    "07_算法专题": ("07-算法专题", "Python算法笔试"),
}

Q_RE = re.compile(r"^### ([QA]\d{3,4}) · (.+?)\s*$")

def slugify(text, limit=24):
    keep = []
    for ch in text:
        if ch.isalnum() or ("\u4e00" <= ch <= "\u9fff"):
            keep.append(ch)
        elif keep and keep[-1] != "-":
            keep.append("-")
    slug = "".join(keep).strip("-")[:limit].strip("-")
    return slug or "untitled"

def main():
    stats = {}
    for chdir, (catdir, category) in sorted(DIR_MAP.items()):
        outdir = DST / catdir
        outdir.mkdir(parents=True, exist_ok=True)
        for md in sorted((SRC / "docs" / chdir).glob("*.md")):
            if md.name.startswith("._") or "总览" in md.name:
                continue
            text = md.read_text(encoding="utf-8")
            lines = text.splitlines()
            # 找每题起点
            starts = [i for i, ln in enumerate(lines) if Q_RE.match(ln)]
            if not starts:
                continue
            count = 0
            for si, start in enumerate(starts):
                m = Q_RE.match(lines[start])
                qid, title = m.group(1), m.group(2).strip()
                end = starts[si + 1] if si + 1 < len(starts) else len(lines)
                body = "\n".join(lines[start:end]).rstrip() + "\n"
                is_bishi = qid.startswith("A")
                qtype = "笔试题" if is_bishi else "面试题"
                tags = ["Python面试", qtype, "27"]
                fm = (
                    "---\n"
                    f"title: [{qid}] {title}\n"
                    "date: 2026-11-17\n"
                    f"categories: [{category}]\n"
                    f"tags: [{', '.join(tags)}]\n"
                    f"type: {qtype}\n"
                    "---\n\n"
                )
                slug = f"{qid}-{slugify(title)}"
                (outdir / f"{slug}.md").write_text(fm + body, encoding="utf-8")
                count += 1
            stats[f"{chdir}/{md.name}"] = count
    # 索引
    total = sum(stats.values())
    idx = ["# 27 python-interview-3000 · 拆题索引", "",
           f"合计 **{total} 卡**（Q 系面试题 / A 系笔试题，源 3000+15 题）", "",
           "| 文件 | 拆出题数 |", "|---|---|"]
    for k, v in stats.items():
        idx.append(f"| {k} | {v} |")
    (DST / "_INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"total cards: {total}")
    for k, v in stats.items():
        print(f"{v:4d}  {k}")

if __name__ == "__main__":
    main()
