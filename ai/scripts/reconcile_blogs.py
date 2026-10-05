#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""依据 target/<key>/ 下已生成的博客 .md，核对并回写 _PROGRESS.md（匹配 scan_course.py 格式）。

scan_course.py 生成的 _PROGRESS.md 列：
  | 状态 | # | 编号 | 标题 | 字数 | 产出博客 |
子 agent 只写博客 .md，不碰 _PROGRESS.md；本脚本由主控统一运行，避免并发写冲突。

匹配策略（重要）：
- 文件名前缀 = 子 agent 采用的「短编号」（如 9.6 / 5-14 / 10.1），但 manifest 中 ch9~12 的
  id 是带噪音的长串（如 "[9.6]中间件proto文件开发..."）。
- 因此按「编号核心数字」归一化（把 '.' 与 '-' 统一成空格）后比对，既兼容 lottery 的干净
  id（1-1），也兼容 paas ch9~12 的长 id。

用法：
  python3 ai/scripts/reconcile_blogs.py --key lottery [--write]
  python3 ai/scripts/reconcile_blogs.py --key paas --write
"""
from __future__ import annotations
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target"
ROW = re.compile(r"^\|\s*(done|skip|pending)\s*\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|\s*$")


def core_id(aid: str) -> str:
    """从（可能带噪音的）id 中提取编号核心数字，如 '9.6' / '5-14' / '10.1'。"""
    m = re.search(r"\d+(?:[.\-]\d+)*", aid)
    return m.group(0) if m else aid


def norm(s: str) -> str:
    """把 '.' 与 '-' 统一成空格，用于跨 '.'/'-' 归一化比对。"""
    return re.sub(r"[.\-]", " ", s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    ap.add_argument("--write", action="store_true", help="落盘；默认只打印将要做的改动")
    args = ap.parse_args()
    key = args.key
    tdir = TARGET / key
    manifest = json.loads((tdir / "_MANIFEST.json").read_text(encoding="utf-8"))
    articles = manifest["articles"]

    existing = [p for p in tdir.glob("*.md") if not p.name.startswith("_")]
    # 归一化 stem -> 文件名。stem 用「文件名里最前面的编号数字」提取，
    # 兼容两种命名：带下划线（10-6_服务端接口下.md）与不带下划线（9-2前端大转盘效果实现.md）。
    # 用 Path.stem 去掉 .md 后缀，避免「本章精华总结.md」被当成「本章精华总结 md」。
    stem_map: dict[str, str] = {}
    for p in existing:
        stem = core_id(p.stem)
        stem_map.setdefault(norm(stem), p.name)

    article_cores = {norm(core_id(a["id"])) for a in articles}
    orphans = [p.name for p in existing if norm(core_id(p.stem)) not in article_cores]

    prog = tdir / "_PROGRESS.md"
    lines = prog.read_text(encoding="utf-8").splitlines()

    fixed = 0
    for i, ln in enumerate(lines):
        m = ROW.match(ln)
        if not m:
            continue
        status, num, aid, title, wc, oc = (x.strip() for x in m.groups())
        if status == "skip":
            continue
        cand = stem_map.get(norm(core_id(aid)))
        hit = cand is not None
        if hit and status != "done":
            lines[i] = f"| done | {num} | {aid} | {title} | {wc} | `{cand}` |"
            fixed += 1
        elif not hit and status == "done":
            lines[i] = f"| pending | {num} | {aid} | {title} | {wc} |  |"
            fixed += 1

    if args.write and fixed:
        tmp = prog.with_suffix(".md.tmp")
        tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
        shutil.move(str(tmp), str(prog))
    n_done = sum(1 for l in lines if l.startswith("| done"))
    print(f"[{key}] 总 {len(articles)}，done 行 {n_done}，本轮改动 {fixed}"
          f"{'（已落盘）' if args.write and fixed else '（dry）'}")
    if orphans:
        print(f"  注意：{len(orphans)} 个 .md 未匹配到任何 manifest 篇目（孤儿文件）：")
        for o in orphans[:10]:
            print("    -", o)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
