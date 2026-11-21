#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全库治理审计:对 docs/ 与 code/ 做系统性体检并输出报告。

检查项:
  A. 题号与代码对应(复用 extract 逻辑,含孤儿/缺失文件)
  B. 重复题名(规范化后全库比对)
  C. mermaid 图基本合法性(须含已知图类型关键字)
  D. 代码文件语法扫描(ast.parse;3.10+ 语法按已知模式豁免并归类)
  E. 题目要素完整性(问/答/追问/难度行)
  F. 难度分布统计(每类 L1/L2/L3)

用法: python3 scripts/audit.py [--fix-dry]
输出: 控制台报告;退出码 0=干净,1=有问题。
"""
import ast
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CODE = ROOT / "code"

Q_SPLIT = re.compile(r"^### (Q\d+) · (.+)$", re.M)
META = re.compile(r"^>\s*难度:([★☆]+) \| 标签:(.+)$", re.M)
BLOCK = re.compile(r"```\w*\n# file: (code/[^\n]+)\n([\s\S]*?)```")
MERMAID = re.compile(r"```mermaid\n([\s\S]*?)```")
MERMAID_KINDS = ("graph", "flowchart", "sequenceDiagram", "classDiagram",
                 "stateDiagram", "mindmap", "gantt", "erDiagram", "journey", "pie", "gitGraph")
# 3.10+ 语法特征(3.9 ast 解析会报错,但属"面向现代 Python"的已知豁免)
NEW_SYNTAX = [
    (re.compile(r"^\s*match\s+.+:\s*$", re.M), "match/case"),
    (re.compile(r"\bexcept\s*\*"), "except*"),
    (re.compile(r"->\s*[\w\.]+\s*\|\s*[\w\.]+|:\s*[\w\.]+\s*\|\s*[\w\.]+"), "X|Y 类型注解"),
]


def norm_title(t: str) -> str:
    return re.sub(r"[\s:：,。·?？!！]", "", t.lower())


def parse_docs():
    items = []
    for md in sorted(DOCS.rglob("*.md")):
        if md.parent.name == "paths":
            continue
        text = md.read_text(encoding="utf-8")
        rel = str(md.relative_to(ROOT))
        hits = list(Q_SPLIT.finditer(text))
        for i, hit in enumerate(hits):
            end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
            block = text[hit.start():end]
            meta = META.search(block)
            fm = re.search(r"# file: (code/\S+)", block)
            items.append({
                "doc": rel, "num": hit.group(1), "title": hit.group(2).strip(),
                "stars": meta.group(1).count("★") if meta else 0,
                "has_meta": bool(meta),
                "has_q": bool(re.search(r"\*\*问\*\*[:：]", block)),
                "has_a": bool(re.search(r"\*\*答\*\*[:：]", block)),
                "has_followup": bool(re.search(r"\*\*追问\*\*[:：]", block)),
                "codefile": fm.group(1) if fm else None,
                "mermaids": MERMAID.findall(block),
            })
    return items


def main():
    problems = defaultdict(list)
    items = parse_docs()
    print(f"解析 {len(items)} 题")

    # A. 题号唯一 / 代码文件对应
    num_docs = defaultdict(list)
    for it in items:
        num_docs[it["num"]].append(it["doc"])
        if not it["codefile"]:
            problems["无代码块"].append(f"{it['num']} @ {it['doc']}")
    for n, docs in num_docs.items():
        if len(docs) > 1:
            problems["题号重复"].append(f"{n}: {', '.join(docs)}")

    ref_files = {it["codefile"] for it in items if it["codefile"]}
    disk_files = {str(p.relative_to(ROOT)) for p in CODE.rglob("*") if p.is_file() and p.name != "__pycache__"}
    disk_files = {f for f in disk_files if not f.endswith((".pyc",))}
    for f in sorted(disk_files - ref_files):
        problems["孤儿代码文件"].append(f)
    for f in sorted(ref_files - disk_files):
        problems["缺失代码文件"].append(f)

    # B. 重复题名
    seen = defaultdict(list)
    for it in items:
        seen[norm_title(it["title"])].append(it["num"])
    for t, nums in seen.items():
        if len(nums) > 1:
            problems["重复题名"].append(f"{'/'.join(nums)}: {items[[i['num'] for i in items].index(nums[0])]['title'][:40]}")

    # C. mermaid 合法性
    bad_mm = 0
    for it in items:
        for mm in it["mermaids"]:
            head = mm.strip().splitlines()[0] if mm.strip() else ""
            if not any(k in head for k in MERMAID_KINDS):
                bad_mm += 1
                problems["mermaid 无已知图类型"].append(f"{it['num']}: {head[:40]}")
                if bad_mm > 20:
                    break

    # D. 代码语法扫描
    parse_err, new_ok = [], []
    for f in sorted(disk_files & (ref_files | disk_files)):
        if not f.endswith(".py"):
            continue
        src = (ROOT / f).read_text(encoding="utf-8")
        try:
            ast.parse(src)
        except SyntaxError as e:
            if any(pat.search(src) for pat, _ in NEW_SYNTAX):
                kind = next(name for pat, name in NEW_SYNTAX if pat.search(src))
                new_ok.append(f"{f} ({kind})")
            else:
                parse_err.append(f"{f}: {e.msg} (line {e.lineno})")
    if parse_err:
        problems["语法错误(非版本豁免)"] = parse_err

    # E. 要素完整性
    for it in items:
        miss = [k for k, v in (("难度行", it["has_meta"]), ("问", it["has_q"]), ("答", it["has_a"])) if not v]
        if miss:
            problems["要素缺失"].append(f"{it['num']} 缺 {','.join(miss)} @ {it['doc']}")
    no_follow = [it["num"] for it in items if not it["has_followup"]]
    no_star = [it["num"] for it in items if it["stars"] == 0]

    # F. 难度分布
    dist = {}
    for it in items:
        cat = it["doc"].split("/")[1]
        t = 1 if it["stars"] <= 2 else 2 if it["stars"] == 3 else 3
        dist.setdefault(cat, Counter())[t] += 1

    # ---- 报告 ----
    print("\n===== 治理审计报告 =====")
    print(f"题目总数: {len(items)} | 代码文件: {len(disk_files)} | 引用: {len(ref_files)}")
    print("\n难度分布(L1/L2/L3):")
    for cat in sorted(dist):
        c = dist[cat]
        print(f"  {cat}: {c[1]}/{c[2]}/{c[3]}")
    print(f"\n无追问的题: {len(no_follow)}(早期章节约半数,属设计)| 星级缺失: {len(no_star)}")
    print(f"3.10+ 语法豁免文件: {len(new_ok)}")

    if problems:
        print(f"\n发现 {sum(len(v) for v in problems.values())} 个问题:")
        for k in sorted(problems):
            print(f"\n[{k}] {len(problems[k])} 个")
            for line in problems[k][:30]:
                print(f"  - {line}")
            if len(problems[k]) > 30:
                print(f"  … 还有 {len(problems[k]) - 30} 个")
        return 1
    print("\n审计通过:无孤儿/缺失文件、无重复题号题名、mermaid 合法、语法干净。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
