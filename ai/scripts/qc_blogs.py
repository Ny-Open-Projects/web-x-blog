#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""博客质量门禁（QC）：针对 work/target/<key>/ 下由子 agent 生成的 .md。

检查项：
  1. 孤儿文件：文件名编号无法匹配 _MANIFEST.json 中任何篇目（说明漏生成或命名错位）。
  2. 三单引号围栏：''' 属于错误代码围栏（规范要求标准三反引号 ```）。
  3. 总结行：每篇末尾必须有「相关度：XX%。是否需要继续：[是/否]。代码是否可运行：[是/否]。」
     —— 兼容「否」(无括号) 与「[是]」(括号包单字) 两种写法。
  4. 标题行：文件首非空行必须是 Markdown 标题（# 开头）。

用法：
  python3 ai/scripts/qc_blogs.py --key lottery
  python3 ai/scripts/qc_blogs.py --key paas
  python3 ai/scripts/qc_blogs.py --all
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "work" / "target"
# 兼容三种写法：
#   是否需要继续：否。           （无括号）
#   是否需要继续：[是]。          （括号包单字）
#   是否需要继续：是（下一篇...）。 （括号后带说明文字）
SUMMARY = re.compile(r"相关度：\d+%。*?是否需要继续：\[?(?:是|否).*?代码是否可运行：\[?(?:是|否)")


def core_id(aid: str) -> str:
    m = re.search(r"\d+(?:[.\-]\d+)*", aid)
    return m.group(0) if m else aid


def norm(s: str) -> str:
    return re.sub(r"[.\-]", " ", s)


def qc(key: str) -> dict:
    tdir = ROOT / key
    manifest = json.loads((tdir / "_MANIFEST.json").read_text(encoding="utf-8"))
    articles = manifest["articles"]
    files = [p for p in tdir.glob("*.md") if not p.name.startswith("_")]

    cores = {norm(core_id(a["id"])) for a in articles}
    orphans = [f.name for f in files
               if norm(core_id(f.stem)) not in cores]

    triple, nosum, notitle = [], [], []
    for f in files:
        t = f.read_text(encoding="utf-8")
        if "'''" in t:
            triple.append(f.name)
        if not SUMMARY.search(t):
            nosum.append(f.name)
        if not t.lstrip().startswith("#"):
            notitle.append(f.name)

    print(f"=== {key} ===")
    print(f"  文件数 {len(files)} | manifest 篇目 {len(articles)}")
    print(f"  孤儿文件: {len(orphans)}", orphans if orphans else "")
    print(f"  三单引号围栏: {len(triple)}", triple[:5] if triple else "")
    print(f"  缺总结行: {len(nosum)}", nosum[:5] if nosum else "")
    print(f"  缺标题行: {len(notitle)}", notitle[:5] if notitle else "")
    clean = not (orphans or triple or nosum or notitle)
    print("  结论:", "✅ 全部通过" if clean else "⚠️ 存在问题需修复")
    return {"key": key, "files": len(files), "orphans": orphans,
            "triple": triple, "nosum": nosum, "notitle": notitle, "clean": clean}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", help="lottery / paas")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    keys = ["lottery", "paas"] if args.all else [args.key]
    res = [qc(k) for k in keys if k]
    bad = [r["key"] for r in res if not r["clean"]]
    print("\n=== 汇总 ===")
    print("通过:", [r["key"] for r in res if r["clean"]])
    print("未通过:", bad or "无")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
