#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""「人人都能学会数据分析」生产质检守卫（课程专属，不改其他课程的入库逻辑）。

用法:
    /usr/local/bin/python3 ai/scripts/qc_data_analysis.py            # 全量检查
    /usr/local/bin/python3 ai/scripts/qc_data_analysis.py --selftest # 注入缺陷验证守卫可证伪

检查项均为确定性断言；`--selftest` 会对每条规则注入一个缺陷并确认它真的会报红。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "work" / "target" / "data-analysis"

REQUIRED = [
    ("## 纲要", "纲要"),
    ("## 读前须知（名词与环境）", "读前须知"),
    ("## 能力速览", "能力速览"),
    ("## 可运行示例", "可运行示例"),
    ("## 📎 文本↔代码关联", "文本与代码关联"),
    ("## 常见坑", "常见坑"),
    ("## 面试官会问什么", "面试官会问什么"),
    ("## 总结", "总结"),
]

# 生产红线：面向内部流水线的措辞 / 品牌水印 / 质检脚手架，读者不该看到
BLACKLIST = [
    (r"相关度：", "质检脚手架「相关度」"),
    (r"是否需要继续", "质检脚手架「是否需要继续」"),
    (r"代码是否可运行", "质检脚手架「代码是否可运行」"),
    (r"源文", "内部措辞「源文」"),
    (r"口播", "内部措辞「口播」"),
    (r"成文", "内部措辞「成文」"),
    (r"下一节|上一节|前面几节", "跨篇引用未自足"),
    (r"微信\s*\d+|更多IT资源|迅捷文字转语音|ruike|2268731", "品牌或转写工具水印"),
    (r"deltaf|dotaf|deltf|dottf", "讲师自称"),
]

SECTION_RE = re.compile(r"^## ", re.M)
QA_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", re.M)


def check_article(text: str, name: str = "?") -> list[str]:
    bad: list[str] = []

    # ── front-matter ────────────────────────────────────────────────
    if not text.startswith("---\n"):
        bad.append("缺 front-matter 开头")
        return bad
    end = text.find("\n---", 3)
    if end < 0:
        bad.append("front-matter 未闭合")
        return bad
    fm, body = text[4:end], text[end + 4:]

    if "disableNunjucks: true" not in fm:
        bad.append("缺 disableNunjucks: true（mermaid 与模板语法会冲突）")
    m = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    if not m:
        bad.append("title 未用双引号包住")
    elif '"' in m.group(1):
        bad.append("title 内部有直双引号，会提前闭合外层引号")
    m = re.search(r"^categories:\s*\[(.*)\]\s*$", fm, re.M)
    if not m:
        bad.append("categories 不是行内列表")
    elif re.search(r"[A-Za-z]", m.group(1)):
        bad.append("categories 含英文标识，与发布区纯中文分类不一致")

    # ── 必需栏目与顺序 ──────────────────────────────────────────────
    for marker, label in REQUIRED:
        n = body.count(marker)
        if n != 1:
            bad.append(f"栏目「{label}」出现 {n} 次（应为 1 次）")
    if "## 纲要" in body and "## 读前须知" in body:
        if body.index("## 纲要") > body.index("## 读前须知"):
            bad.append("读前须知必须排在纲要之后")
    if "## 面试官会问什么" in body and "## 总结" in body:
        if body.index("## 面试官会问什么") > body.index("## 总结"):
            bad.append("面试官会问什么必须排在总结之前")

    # ── 面试栏目内容 ────────────────────────────────────────────────
    im = re.search(r"^## 面试官会问什么\s*$", body, re.M)
    if im:
        nm = SECTION_RE.search(body, im.end())
        seg = body[im.end(): nm.start() if nm else len(body)]
        rows = QA_ROW_RE.findall(seg)
        nums = [int(r[0]) for r in rows]
        if len(rows) < 4:
            bad.append(f"面试问题仅 {len(rows)} 条（要求 >=4）")
        if nums != list(range(1, len(rows) + 1)):
            bad.append(f"面试问题编号不连续: {nums}")
        for n, q, a, f in rows:
            if not (q.strip() and a.strip() and f.strip()):
                bad.append(f"第 {n} 问存在问题/回答/追问为空")
        if len({r[1] for r in rows}) != len(rows):
            bad.append("面试问题重复")
        if "**红旗答案**" not in seg or len(re.findall(r"^- ", seg, re.M)) < 2:
            bad.append("面试栏目缺红旗答案或条数不足")
        if "**加分点**" not in seg:
            bad.append("面试栏目缺加分点")

    # ── 生产红线（剥离代码块后扫描，避免代码注释误报） ──────────────
    stripped = re.sub(r"```.*?```", "", body, flags=re.S)
    for pat, label in BLACKLIST:
        if re.search(pat, stripped):
            bad.append(f"残留 {label}")

    # ── 格式契约 ────────────────────────────────────────────────────
    if "```mermaid" not in body:
        bad.append("缺 mermaid 流程图")
    if not re.search(r"^\|[\s:|-]+\|", body, re.M):
        bad.append("缺 markdown 表格分隔行")
    if "├──" not in body and "└──" not in body:
        bad.append("缺 ASCII 目录树")
    if body.count("```") % 2:
        bad.append("代码围栏数为奇数")
    if re.search(r"^\s*'''", stripped, re.M):
        bad.append("行首残留 ''' 围栏")

    # ── 代码块语法可编译 ────────────────────────────────────────────
    for i, blk in enumerate(re.findall(r"```python\n(.*?)\n```", body, re.S), 1):
        try:
            compile(blk, f"{name}#block{i}", "exec")
        except SyntaxError as e:
            bad.append(f"第 {i} 个 python 块语法错误: {e.msg}")

    return bad


def selftest() -> int:
    """对每条规则注入缺陷，确认守卫真的会报红（可证伪）。"""
    base = sorted(COURSE.glob("[0-9]_*.md"))[0].read_text(encoding="utf-8")
    assert not check_article(base, "base"), "基准文章本身就不合格，先修文章"

    cases = [
        ("删面试栏目", lambda t: t.replace("## 面试官会问什么", "## 占位栏目"),
         "栏目「面试官会问什么」"),
        ("面试问题删到 3 条", lambda t: t.replace("| 5 |", "| 占位 |", 1)
         .replace("| 4 |", "| 占位 |", 1), "面试问题仅"),
        ("加回质检脚手架", lambda t: t + "\n相关度：98%。是否需要继续：是。代码是否可运行：是。\n",
         "质检脚手架"),
        ("categories 改英文", lambda t: t.replace(
            "categories: [人人都能学会数据分析]", "categories: [data-analysis]"), "含英文标识"),
        ("注入内部措辞", lambda t: t.replace("## 总结", "## 总结\n\n源文提到这一点。"),
         "内部措辞"),
        ("title 去引号", lambda t: re.sub(r'^title:\s*"(.*)"\s*$', r"title: \1", t, flags=re.M),
         "title 未用双引号"),
        ("破坏围栏", lambda t: t.replace("```mermaid", "``mermaid", 1), "围栏数为奇数"),
        ("删 ASCII 树", lambda t: t.replace("├──", "--").replace("└──", "--"), "缺 ASCII 目录树"),
    ]
    failed = 0
    for label, mutate, expect in cases:
        mutated = mutate(base)
        errs = check_article(mutated, label)
        hit = any(expect in e for e in errs)
        print(f"  {'会红 OK' if hit else '不会红 FAIL'}  {label}"
              + ("" if hit else f"  | 实得: {errs[:2]}"))
        failed += 0 if hit else 1
    print(f"\n负向自检: {len(cases) - failed}/{len(cases)} 项可证伪")
    return 1 if failed else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    files = sorted(COURSE.glob("[0-9]_*.md"))
    if not files:
        print("没有待检查的文章")
        return 1
    total = 0
    for p in files:
        errs = check_article(p.read_text(encoding="utf-8"), p.name)
        if errs:
            total += len(errs)
            print(f"[不合格] {p.name}")
            for e in errs:
                print(f"    - {e}")
        else:
            print(f"[合格] {p.name}")
    print(f"\n检查 {len(files)} 篇，问题 {total} 条 → {'全绿' if total == 0 else '未通过'}")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
