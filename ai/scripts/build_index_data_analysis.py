#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为「按周分目录」的课程素材生成 _INDEX.md / _PROGRESS.md（断点续跑骨架）。

为什么单独写而不用 ai/scripts/build_source_index.py：
原脚本用 ``src.glob("*.txt")`` 只扫顶层，而「人人都能学会数据分析」的 208 篇
逐字稿全部位于 16 个「第N周 …」子目录里，直接跑会得到空索引。
这里改为 rglob 递归，并按 (周, 节) 分组——文件名的 ``N-M 标题`` 中 N 是周内节号，
正好是天然的主题边界，比按标题相似度聚类更稳定。

用法:
    /usr/local/bin/python3 ai/scripts/build_index_data_analysis.py
产出:
    work/target/data-analysis/_INDEX.md
    work/target/data-analysis/_PROGRESS.md   （已存在则不覆盖，保护断点）
"""
from __future__ import annotations

import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE_SLUG = "data-analysis"
SRC = ROOT / "work/source/20.体系课_人人都能学会数据分析[完结]"
OUT_DIR = ROOT / "work/target" / COURSE_SLUG

# 文件名噪音：课程推广、转写工具痕迹、重复副本标记（~1[16]）。
NOISE = re.compile(
    r"【[^】]*】"
    r"|\[\d+\]"
    r"|~?\d*\[\d+\]"                      # ~1[16] 这类重复副本后缀
    r"|（\s*更多IT[^）]*）"
    r"|_\s*更多IT资源[^\-]*"              # _更多IT资源微信2268731
    r"|\b更多IT资源\S*"
    r"|微信号[：:]?\s*\d+"
    r"|-\s*迅捷文字转语音-\d+zh"
    r"|-?\s*迅捷文字转语音"
)
# 形如 "1-1" / "2-9" / "10.10" 的课时编号前缀
NUM_PREFIX = re.compile(r"^\s*(\d+)\s*[-.]\s*(\d+)\s*")
WEEK_DIR = re.compile(r"^第(\d+)周\s+(.*)$")
# 导学 / 小结 / 未完结一律 skip（流水线约定，不写文）
SKIP_WORDS = ("导学", "本章小结", "课程总结", "未完结", "学习指导")


def clean_title(filename: str) -> tuple[int, int, str]:
    """拆出 (节号, 课时号, 清洗后的标题)。

    Args:
        filename: 源 .txt 文件名（含扩展名）。

    Returns:
        (section, lesson, title)；无法解析编号时 section/lesson 为 0。
    """
    base = filename[:-4] if filename.endswith(".txt") else filename
    m = NUM_PREFIX.match(base)
    if m:
        section, lesson = int(m.group(1)), int(m.group(2))
        base = base[m.end():]
    else:
        section, lesson = 0, 0
    title = NOISE.sub("", base).strip(" -–—_、，") or base.strip()
    return section, lesson, title


def collect() -> OrderedDict[tuple[int, str], list[dict]]:
    """递归收集素材并按 (周号, 周名) 聚合。

    Returns:
        有序字典 (week_no, week_name) -> 课时条目列表（按 节/课时 排序）。
    """
    groups: OrderedDict[tuple[int, str], list[dict]] = OrderedDict()
    for week_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        m = WEEK_DIR.match(week_dir.name)
        if not m:
            print(f"[warn] 跳过无法解析的目录: {week_dir.name}", file=sys.stderr)
            continue
        key = (int(m.group(1)), m.group(2).strip())
        rows: list[dict] = []
        for f in sorted(week_dir.rglob("*.txt")):
            section, lesson, title = clean_title(f.name)
            text = f.read_text(encoding="utf-8", errors="ignore")
            rows.append({
                "week": key[0],
                "week_name": key[1],
                "section": section,
                "lesson": lesson,
                "title": title,
                "chars": len(text),
                "file": str(f.relative_to(SRC)),
            })
        rows.sort(key=lambda r: (r["section"], r["lesson"]))
        groups[key] = rows
    return OrderedDict(sorted(groups.items(), key=lambda kv: kv[0][0]))


def build_index(groups: OrderedDict[tuple[int, str], list[dict]]) -> str:
    """生成全量素材清单 _INDEX.md。"""
    all_rows = [r for rows in groups.values() for r in rows]
    lines = [
        "# 人人都能学会数据分析 · 素材清单",
        "",
        f"- 源目录：`work/source/20.体系课_人人都能学会数据分析[完结]`",
        f"- 总文件数：**{len(all_rows)}**",
        f"- 周数：**{len(groups)}**（第 1–16 周，编号无缺口）",
        f"- 总字数：{sum(r['chars'] for r in all_rows):,}",
        f"- 空文件：{sum(1 for r in all_rows if r['chars'] == 0)}",
        "",
        "## 分组口径",
        "",
        "按 **(周, 节)** 分组：文件名 `N-M 标题` 的 `N` 是周内节号，天然主题边界。",
        "导学 / 本章小结 / 未完结一律 `skip`，不写文。",
        "",
        "## 各周概览",
        "",
        "| 周 | 主题 | 课时数 | 节号 | 字数 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for (week, week_name), rows in groups.items():
        secs = sorted({r["section"] for r in rows})
        lines.append(
            f"| 第 {week} 周 | {week_name} | {len(rows)} | {', '.join(map(str, secs))} "
            f"| {sum(r['chars'] for r in rows):,} |"
        )
    lines += ["", "## 全量课时清单", "", "| 周 | 编号 | 标题 | 字数 | 文件 |", "| --- | --- | --- | --- | --- |"]
    for r in all_rows:
        lines.append(
            f"| {r['week']} | {r['section']}-{r['lesson']} | {r['title']} "
            f"| {r['chars']:,} | `{r['file']}` |"
        )
    return "\n".join(lines) + "\n"


def build_progress(groups: OrderedDict[tuple[int, str], list[dict]]) -> str:
    """生成断点进度表 _PROGRESS.md，一行一个主题组。"""
    lines = [
        "# 人人都能学会数据分析 → 博客 转换进度",
        "",
        "状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、本章小结、未完结）",
        "**agent 每写完一组，把该行状态改成 `done` 并填上产出文件名。**",
        "",
        "节流约定（防 429）：一次只推进**一组**；短素材（1~5 千字）一次最多连写 3 组；",
        "大素材（>1 万字）单独处理。写完用脚本批量改进度行，别一篇一手改。",
        "",
        "质量红线：源内容全部保留，合并只合并「同节相邻薄篇」，不得削减质量或字数；",
        "去品牌化（微信/IT 资源/迅捷文字转语音等水印）必须清干净。",
        "",
        "| 状态 | # | 周 | 节 | 组名 | 源篇 | 总字数 | 产出博客 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    idx = 0
    for (week, week_name), rows in groups.items():
        by_section: OrderedDict[int, list[dict]] = OrderedDict()
        for r in rows:
            by_section.setdefault(r["section"], []).append(r)
        for section, sec_rows in sorted(by_section.items()):
            idx += 1
            name = f"第{week}周 {week_name} · 第{section}节"
            # 只剔除「导学/本章小结」这些单篇，不因一篇小结丢掉整节内容。
            # 早期版本写成 any(...) 导致整节 skip，会静默损失上万字，已修。
            kept = [r for r in sec_rows
                    if not any(w in r["title"] for w in SKIP_WORDS)]
            dropped = len(sec_rows) - len(kept)
            stat = "skip" if not kept else "pending"
            nums = "+".join(f"{r['section']}-{r['lesson']}" for r in kept) or "—"
            total = sum(r["chars"] for r in kept)
            suffix = f"（剔除 {dropped} 篇导学/小结）" if dropped else ""
            lines.append(
                f"| {stat} | {idx} | {week} | {section} | {name}{suffix} | {nums} "
                f"| {total:,} | — |"
            )
    lines += [
        "",
        "## 计数",
        "",
        f"- 主题组总数：**{idx}**",
        f"- 待写（pending）：{sum(1 for l in lines if l.startswith('| pending'))}",
        f"- 跳过（skip）：{sum(1 for l in lines if l.startswith('| skip'))}",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """生成索引；进度表仅在不存在时创建（或用 --force 覆盖），避免覆盖已有断点。"""
    if not SRC.is_dir():
        raise SystemExit(f"源目录不存在: {SRC}")
    force = "--force" in sys.argv
    groups = collect()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    index_path = OUT_DIR / "_INDEX.md"
    index_path.write_text(build_index(groups), encoding="utf-8")
    print(f"[1] 索引已生成: {index_path}")

    prog_path = OUT_DIR / "_PROGRESS.md"
    if prog_path.exists() and not force:
        print(f"[2] 进度表已存在，跳过（保护断点）: {prog_path}")
    else:
        prog_path.write_text(build_progress(groups), encoding="utf-8")
        print(f"[2] 进度表已生成{'（--force 覆盖）' if force else ''}: {prog_path}")

    all_rows = [r for rows in groups.values() for r in rows]
    sections = {(w, r["section"]) for (w, _), rows in groups.items() for r in rows}
    print(f"\n源文 {len(all_rows)} 篇 / {len(groups)} 周 / {len(sections)} 个主题组 "
          f"/ 总字数 {sum(r['chars'] for r in all_rows):,}")


if __name__ == "__main__":
    main()
