#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 scan_course.py 建立的「文本↔代码」知识图谱落到最终博客里（满足"在 blog 中使用 graph 关系"）。

两部分产出：
  1) 给 work/target/<key>/ 下每篇博客注入一个紧凑的「## 📎 文本↔代码关联」小节，
     列出本讲在 _GRAPH.json 中 uses-code 指向的代码文件；幂等（已注入则跳过）。
     注入位置：固定总结行（相关度：...）之前，保证 QC 的"总结行在末尾"仍成立。
  2) 生成 work/target/<key>/知识图谱总览.md：课程级文本↔代码关联概览。

匹配策略：博客文件名最前面的编号（如 2-3 / 11.10 / 本章精华总结）归一化（. - 统一空格）
后，与 graph 文章节点 id 去掉前缀 A 后的编号比对。兼容 lottery 的 '-' 与 paas ch9-12 的 '.'。

用法：
  python3 ai/scripts/build_relations.py --key lottery [--write]
  python3 ai/scripts/build_relations.py --key paas --write
  python3 ai/scripts/build_relations.py --all --write
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "work" / "target"
SUMMARY = re.compile(r"相关度：\d+%。*?是否需要继续：\[?(?:是|否).*?代码是否可运行：\[?(?:是|否)")
MARK = "## 📎 文本↔代码关联"


def core_id(aid: str) -> str:
    m = re.search(r"\d+(?:[.\-]\d+)*", aid)
    return m.group(0) if m else aid


def norm(s: str) -> str:
    return re.sub(r"[.\-]", " ", s)


def load_graph(key: str):
    g = json.loads((ROOT / key / "_GRAPH.json").read_text(encoding="utf-8"))
    # 文章节点索引：归一化编号 -> node
    idx: dict[str, dict] = {}
    for n in g["nodes"]:
        if n["type"] == "article":
            core = norm(core_id(n["id"][1:] if n["id"].startswith("A") else n["id"]))
            idx.setdefault(core, n)
    # 代码 label 查找
    code_label = {n["id"]: n.get("label", n["id"]) for n in g["nodes"] if n["type"] != "article"}
    # 文章节点 id -> 关联代码 label 列表
    edges_map: dict[str, list[str]] = {}
    for e in g["edges"]:
        if e.get("relation") == "uses-code":
            edges_map.setdefault(e["from"], []).append(code_label.get(e["to"], e["to"]))
    return g, idx, edges_map


def build_block(codes: list[str]) -> str:
    lines = [MARK, "", "本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：", ""]
    for c in codes:
        lines.append(f"- `{c}`")
    lines.append("")
    lines.append("> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。")
    return "\n".join(lines)


def inject(key: str, write: bool) -> dict:
    g, idx, edges_map = load_graph(key)
    tdir = ROOT / key
    blogs = [p for p in tdir.glob("*.md") if not p.name.startswith("_") and p.name != "_知识图谱总览.md"]
    matched = 0
    injected = 0
    skipped_noedge = 0
    for p in blogs:
        core = norm(core_id(p.stem))
        node = idx.get(core)
        if node is None:
            continue  # 未在图谱中找到（理论不应发生）
        matched += 1
        codes = edges_map.get(node["id"], [])
        if not codes:
            skipped_noedge += 1
            continue
        text = p.read_text(encoding="utf-8")
        if MARK in text:
            continue  # 已注入，幂等跳过
        block = build_block(codes)
        m = None
        for mm in SUMMARY.finditer(text):
            m = mm
        if m is None:
            # 没有总结行：追加到末尾（QC 可能在其它环节已保证）
            new = text.rstrip() + "\n\n" + block + "\n"
        else:
            # 在总结行之前插入
            pos = m.start()
            new = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:]
        if write:
            p.write_text(new, encoding="utf-8")
        injected += 1
    print(f"[{key}] 博客 {len(blogs)} | 图谱命中 {matched} | 注入 {injected} | 无代码边跳过 {skipped_noedge}")
    return {"key": key, "blogs": len(blogs), "matched": matched, "injected": injected}


def overview(key: str, write: bool) -> str:
    g, idx, edges_map = load_graph(key)
    arts = [n for n in g["nodes"] if n["type"] == "article"]
    codes = [n for n in g["nodes"] if n["type"] != "article"]
    n_edges = sum(1 for e in g["edges"] if e.get("relation") == "uses-code")
    # Top 关联讲次
    ranked = sorted(edges_map.items(), key=lambda kv: len(kv[1]), reverse=True)[:10]
    id2label = {n["id"]: n.get("label", n["id"]) for n in arts}
    lines = [
        f"# 知识图谱总览：{key}（文本↔代码关联）",
        "",
        f"- 文章节点：**{len(arts)}**　代码节点：**{len(codes)}**　关联边（uses-code）：**{n_edges}**",
        f"- 平均每讲关联代码文件：{n_edges / max(len(arts),1):.1f}",
        "- 完整图谱：Mermaid 源见 `_GRAPH.mmd`；结构化数据见 `_GRAPH.json`。",
        "",
        "## 关联代码最多的讲次（Top 10）",
        "",
        "| 讲次 | 标题 | 关联代码数 |",
        "| --- | --- | --- |",
    ]
    for nid, cs in ranked:
        label = id2label.get(nid, nid)
        title = label.split(" ", 1)[-1] if " " in label else label
        lines.append(f"| {nid} | {title[:40]} | {len(cs)} |")
    lines.append("")
    lines.append("## 说明")
    lines.append("")
    lines.append("- 本总览由 `build_relations.py` 依据 `scan_course.py` 产出自动生成。")
    lines.append("- 每篇博客文末「📎 文本↔代码关联」小节列出该讲直接引用的代码文件，与下方图谱一致。")
    out = "\n".join(lines)
    if write:
        (ROOT / key / "_知识图谱总览.md").write_text(out + "\n", encoding="utf-8")
        print(f"[{key}] 已生成 _知识图谱总览.md")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    keys = ["lottery", "paas"] if args.all else [args.key]
    for k in keys:
        if not k:
            continue
        inject(k, args.write)
        overview(k, args.write)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
