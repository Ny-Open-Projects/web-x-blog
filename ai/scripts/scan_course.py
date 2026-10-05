#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描课程源目录，建立「讲稿文本 ↔ 代码」的 manifest 与关系图谱。

产出（写到 work/target/<key>/）：
  _MANIFEST.json   机器可读清单（篇目/来源/字数/关联代码）
  _INDEX.md        人类可读索引（含相似标题合并分组）
  _GRAPH.json      关系图谱（篇目节点 + 代码节点 + 边）
  _GRAPH.mmd       Mermaid 图谱
  _PROGRESS.md     转换进度表（agent 逐篇把 pending 改 done）

用法：
  python3 ai/scripts/scan_course.py --key lottery \
      --src "work/source/6. mksz295 - 高并发 高性能 Go语言开发企业级抽奖项目"
  python3 ai/scripts/scan_course.py --key paas \
      --src "work/source/7.mksz535-Go开发者的涨薪通道：自主开发PaaS平台核心功能[完结]"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# 讲稿文件名里的噪音，清洗掉
NOISE_PATTERNS = [
    r"【更多IT教程[^】]*】",
    r"【[^】]*完结[^】]*】",
    r"\[更多IT教程[^\]]*\]",
    r"-迅捷文字转语音-[^.]*",
    r"迅捷文字转语音[^.]*",
    r"\[\d+\]",          # [2] 之类的分卷标记
    r"\(\d+\)",
    r"（完结[^）]*）",
]
# 合并用的序号后缀（一/二/三…、上/中/下）
SEQ_SUFFIX = re.compile(r"[（(]?(?:\d+|[一二三四五六七八九十]+|上|中|下)[)）]?\s*$")

CODE_EXT = {
    ".go", ".mod", ".sum", ".md", ".java", ".py", ".js", ".ts", ".thrift",
    ".yml", ".yaml", ".json", ".xml", ".sql", ".sh", ".proto", ".tpl",
    ".html", ".css", ".scss", ".less", ".ini", ".conf", ".cfg", ".toml",
}
# 代码索引里忽略的目录
SKIP_DIRS = {
    "node_modules", "vendor", ".git", ".idea", ".vscode", "dist", "build",
    "docs", "test", "testdata", ".svn", "__pycache__", "static", "assets",
    "font", "fonts", "images", "img", "css", "js",
}


def clean_title(stem: str) -> str:
    """从文件名 stem 清洗出干净标题。"""
    t = stem
    for p in NOISE_PATTERNS:
        t = re.sub(p, "", t)
    t = re.sub(r"\s+", " ", t).strip(" -_—·、")
    return t


def lesson_code(stem: str) -> str:
    """抽取课程序号，如 2-1 / 10-12 / 8.10。"""
    m = re.match(r"^\s*(\d+(?:[.\-]\d+)*)", stem)
    return m.group(1) if m else ""


def sort_key(code: str):
    """自然排序：把 2-1 / 10-12 拆成数字元组。"""
    parts = re.split(r"[.\-]", code)
    return tuple(int(p) if p.isdigit() else 999 for p in parts) or (999,)


def norm_group(title: str) -> str:
    """归一化标题用于「相似标题合并」：去掉尾部序号、空格、大小写。"""
    t = SEQ_SUFFIX.sub("", title).strip()
    t = re.sub(r"\s+", "", t).lower()
    return t


def ascii_tokens(text: str) -> list[str]:
    """抽取 ASCII 技术关键词（redis/mysql/thrift/k8s…），用于关联代码。"""
    out = []
    for w in re.findall(r"[A-Za-z][A-Za-z0-9_\-]{2,}", text):
        lw = w.lower()
        if lw not in out:
            out.append(lw)
    return out


def build_code_index(src: Path, code_dir: Path) -> list[dict]:
    """建立代码文件索引（相对路径 + 扩展名 + 大小）。"""
    items = []
    if not code_dir.exists():
        return items
    for p in code_dir.rglob("*"):
        if not p.is_file():
            continue
        if any(s in p.parts for s in SKIP_DIRS):
            continue
        if p.suffix.lower() not in CODE_EXT:
            continue
        try:
            size = p.stat().st_size
        except OSError:
            continue
        if size > 512 * 1024:  # 跳过超大文件
            continue
        items.append({
            "rel": str(p.relative_to(src)),
            "ext": p.suffix.lower().lstrip("."),
            "size": size,
        })
    return items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True, help="课程键，如 lottery / paas")
    ap.add_argument("--src", required=True, help="源目录（相对仓库根或绝对路径）")
    ap.add_argument("--out", default=None, help="输出目录，默认 work/target/<key>")
    ap.add_argument("--max-code-refs", type=int, default=8)
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_absolute():
        src = ROOT / src
    if not src.exists():
        print(f"[错误] 源目录不存在: {src}", file=sys.stderr)
        return 1

    out = Path(args.out) if args.out else ROOT / "work" / "target" / args.key
    out.mkdir(parents=True, exist_ok=True)

    # ---- 1. 扫描章节与讲稿
    chapters, files = [], []
    for d in sorted(src.iterdir()):
        if not d.is_dir() or d.name.lower() == "code" or d.name.startswith("."):
            continue
        txts = sorted(d.rglob("*.txt"), key=lambda p: sort_key(lesson_code(p.stem)))
        if not txts:
            continue
        chapters.append({"name": d.name, "count": len(txts)})
        for p in txts:
            title = clean_title(p.stem)
            try:
                words = len(p.read_text(encoding="utf-8", errors="ignore"))
            except OSError:
                words = 0
            files.append({
                "chapter": d.name,
                "code": lesson_code(p.stem),
                "title": title,
                "words": words,
                "path": str(p.relative_to(ROOT)),
                "group": norm_group(title),
            })

    # ---- 2. 相似标题合并分组
    groups: dict[str, list[dict]] = defaultdict(list)
    for f in files:
        groups[f["group"]].append(f)
    articles = []
    for gid, items in groups.items():
        items.sort(key=lambda x: sort_key(x["code"]))
        articles.append({
            "id": items[0]["code"] or gid,
            "title": items[0]["title"],
            "chapter": items[0]["chapter"],
            "sources": [i["path"] for i in items],
            "words": sum(i["words"] for i in items),
            "merged": len(items) > 1,
            "tokens": ascii_tokens(items[0]["title"] + " " + items[0]["chapter"]),
        })
    articles.sort(key=lambda a: sort_key(a["id"]))

    # ---- 3. 代码索引与关联
    code_index = build_code_index(src, src / "code")
    for a in articles:
        toks = set(a["tokens"])
        scored = []
        for c in code_index:
            rel_l = c["rel"].lower()
            hit = sum(1 for t in toks if t in rel_l)
            if hit:
                scored.append((hit, -c["size"], c["rel"]))
        scored.sort(reverse=True)
        a["code_refs"] = [s[2] for s in scored[: args.max_code_refs]]

    ext_stat = defaultdict(int)
    for c in code_index:
        ext_stat[c["ext"]] += 1

    manifest = {
        "course": args.key,
        "src": str(src.relative_to(ROOT)),
        "chapters": chapters,
        "file_count": len(files),
        "article_count": len(articles),
        "merged_count": sum(1 for a in articles if a["merged"]),
        "code_file_count": len(code_index),
        "code_ext_stat": dict(sorted(ext_stat.items(), key=lambda x: -x[1])),
        "articles": articles,
    }
    (out / "_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- 4. 图谱
    nodes = [{"id": f"A{a['id']}", "label": a["title"], "type": "article",
              "chapter": a["chapter"], "words": a["words"]} for a in articles]
    edges = []
    code_nodes = {}
    for a in articles:
        for rel in a["code_refs"]:
            nid = "C" + re.sub(r"\W", "_", rel)
            if nid not in code_nodes:
                code_nodes[nid] = {"id": nid, "label": rel, "type": "code"}
            edges.append({"from": f"A{a['id']}", "to": nid, "relation": "uses-code"})
    graph = {
        "meta": {"course": args.key, "articles": len(articles),
                 "code_files": len(code_index), "edges": len(edges)},
        "nodes": nodes + list(code_nodes.values()),
        "edges": edges,
    }
    (out / "_GRAPH.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- 5. Mermaid
    lines = ["%% 讲稿 ↔ 代码 关系图谱（自动生成）", "graph LR",
             f"  %% 课程：{args.key}，篇目 {len(articles)}，代码节点 {len(code_nodes)}"]
    for a in articles[:120]:  # 控制图规模
        aid = "A" + re.sub(r"\W", "_", a["id"])
        label = a["title"].replace('"', "'")[:28]
        lines.append(f'  {aid}["{label}"]')
        for rel in a["code_refs"][:3]:
            cid = "C" + re.sub(r"\W", "_", rel)
            lines.append(f'  {aid} --> {cid}["{Path(rel).name}"]')
    (out / "_GRAPH.mmd").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ---- 6. 人类可读索引
    idx = ["# %s 课程素材清单" % args.key, "",
           f"- 讲稿文件数：**{len(files)}**",
           f"- 合并后篇目：**{len(articles)}**（其中合并 {manifest['merged_count']} 组）",
           f"- 代码文件数：**{len(code_index)}**（已在 code/ 下索引）", ""]
    idx.append("## 章节分布")
    idx.append("")
    idx.append("| 章节 | 讲稿数 |")
    idx.append("| --- | --- |")
    for c in chapters:
        idx.append(f"| {c['name']} | {c['count']} |")
    idx.append("")
    idx.append("## 篇目清单（含合并与关联代码）")
    idx.append("")
    idx.append("| # | 编号 | 标题 | 字数 | 合并 | 关联代码 |")
    idx.append("| --- | --- | --- | --- | --- | --- |")
    for i, a in enumerate(articles, 1):
        merged = "**是**" if a["merged"] else "否"
        refs = ", ".join(f"`{Path(r).name}`" for r in a["code_refs"][:3]) or "—"
        idx.append(f"| {i} | {a['id']} | {a['title']} | {a['words']} | {merged} | {refs} |")
    (out / "_INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # ---- 7. 进度表（幂等：已存在则保留 done 状态）
    prog = out / "_PROGRESS.md"
    done_map = {}
    if prog.exists():
        for ln in prog.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*(\w+)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|", ln)
            if m:
                done_map[m.group(2)] = (m.group(1), m.group(3))
    rows = ["# %s 转换进度" % args.key, "",
            "状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（课程介绍、总结、未完结）",
            "**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**", "",
            "| 状态 | # | 编号 | 标题 | 字数 | 产出博客 |",
            "| --- | --- | --- | --- | --- | --- |"]
    for i, a in enumerate(articles, 1):
        st, title = done_map.get(a["id"], ("pending", a["title"]))
        rows.append(f"| {st} | {i} | {a['id']} | {title} | {a['words']} |  |")
    prog.write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"[完成] {args.key}: 讲稿 {len(files)} → 篇目 {len(articles)}"
          f"（合并 {manifest['merged_count']} 组），代码索引 {len(code_index)} 文件")
    print(f"[产出] {out}/_MANIFEST.json _GRAPH.json _GRAPH.mmd _INDEX.md _PROGRESS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
