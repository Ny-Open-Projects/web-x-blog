#!/usr/bin/env python3
"""把 source/26.前端面试工程 的专题 md 拆成题目卡片，落 target/26-fe-interview/。

题目行形如 `### WEB-001：...`，按编号前缀映射到大类目录。
"""
import re, sys, unicodedata
from pathlib import Path

SRC = Path("/Users/Wang/Code/github/web-x-blog/work/source/26.前端面试工程")
DST = Path("/Users/Wang/Code/github/web-x-blog/work/target/26-fe-interview")

# 文件 -> (大类目录, hexo 分类, 笔试题?)
FILE_MAP = {
    "01-web-network-browser.md": ("01-语言与基础", "Web协议与浏览器", False),
    "02-html5.md": ("01-语言与基础", "HTML5", False),
    "03-css.md": ("01-语言与基础", "CSS", False),
    "04-javascript.md": ("01-语言与基础", "JavaScript", False),
    "05-typescript.md": ("01-语言与基础", "TypeScript", False),
    "10-basics.md": ("01-语言与基础", "前端基础速答", False),
    "06-vue3.md": ("02-框架与业务", "Vue3", False),
    "07-react19.md": ("02-框架与业务", "React19", False),
    "13-framework-principles.md": ("02-框架与业务", "框架原理", False),
    "19-miniprogram.md": ("02-框架与业务", "小程序", False),
    "11-scenario.md": ("03-场景实战", "场景实战", False),
    "08-engineering.md": ("04-工程化与构建", "工程化", False),
    "16-ops-release.md": ("04-工程化与构建", "运维与上线", False),
    "18-build-tools.md": ("04-工程化与构建", "构建工具", False),
    "09-performance-security.md": ("05-性能与安全", "性能与安全", False),
    "12-performance-optimization.md": ("05-性能与安全", "性能优化", False),
    "15-algorithms.md": ("06-算法与手写", "场景算法", True),
    "24-handwrite.md": ("06-算法与手写", "手写代码", True),
    "17-architecture.md": ("07-架构与设计", "前端架构", False),
    "21-design-patterns.md": ("07-架构与设计", "设计模式", False),
    "23-mock-interviews.md": ("07-架构与设计", "模拟面试", False),
    "20-nodejs-bff.md": ("08-服务端与全栈", "Node.js与BFF", False),
    "25-visualization.md": ("09-垂直方向", "数据可视化", False),
    "26-av-rtc.md": ("09-垂直方向", "音视频RTC", False),
    "27-cross-platform.md": ("09-垂直方向", "跨端", False),
    "14-agent-development.md": ("10-AI与Agent", "Agent开发", False),
    "22-soft-skills.md": ("11-软技能与求职", "软技能", False),
    "28-flashcards.md": ("11-软技能与求职", "速记卡", False),
    "29-study-plan.md": ("11-软技能与求职", "学习计划", False),
    "30-company-styles.md": ("11-软技能与求职", "大厂风格", False),
}

Q_RE = re.compile(r"^### ((?:[A-Z0-9]{1,4}-\d{1,4})|[A-Z0-9]{1,4}-\d{1,4})\s*[：:]\s*(.+?)\s*$")

def cat_of(fname):
    base = fname.name
    if base in FILE_MAP:
        return FILE_MAP[base]
    if base.startswith("REVIEW"):
        return None
    return None

def slugify(text, limit=24):
    keep = []
    for ch in text:
        if ch.isalnum() or ("\u4e00" <= ch <= "\u9fff"):
            keep.append(ch)
        elif ch in " /、，,（）()·":
            keep.append("-")
        if len("".join(keep)) >= limit:
            break
    s = "".join(keep).strip("-")
    return s or "q"

def main():
    stats = {}
    for f in sorted(SRC.glob("*.md")):
        info = cat_of(f)
        if not info:
            continue
        subdir, category, is_written = info
        outdir = DST / subdir
        outdir.mkdir(parents=True, exist_ok=True)
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        # 找题目起始行
        starts = [i for i, ln in enumerate(lines) if Q_RE.match(ln)]
        if not starts:
            stats[f.name] = 0
            continue
        # body 是从第一题开始；文件头（总览/目录）留在 index
        header_end = starts[0]
        (outdir / f"_{f.stem}-index.md").write_text(
            f"---\ntitle: {category} · 题库总览\n categories: [{category}]\ntags: [前端面试, 总览]\n---\n\n"
            + "\n".join(lines[:header_end]) + "\n",
            encoding="utf-8",
        )
        count = 0
        for idx, s in enumerate(starts):
            e = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
            block = lines[s:e]
            m = Q_RE.match(block[0])
            qid, qtitle = m.group(1), m.group(2)
            body = "\n".join(block).rstrip() + "\n"
            body = re.sub(r"^### ", "## ", body)
            # 类型判定：笔试题文件 或 标题含手写/实现
            title_has_hw = bool(re.search(r"手写|实现一个|实现\s", qtitle))
            qtype = "笔试题" if (is_written or title_has_hw) else "面试题"
            fname = f"{qid}-{slugify(qtitle)}.md"
            fm = (
                "---\n"
                f"title: [{qid}] {qtitle}\n"
                "date: 2026-11-17\n"
                f"categories: [{category}]\n"
                f"tags: [前端面试, {qtype}, {f.stem.split('-')[0]}]\n"
                "type: " + qtype + "\n"
                "---\n\n"
            )
            (outdir / fname).write_text(fm + body, encoding="utf-8")
            count += 1
        stats[f.name] = count

    total = 0
    for k, v in stats.items():
        print(f"{k}: {v}")
        total += v
    print(f"TOTAL: {total}")
    # 生成总索引
    with (DST / "_INDEX.md").open("w", encoding="utf-8") as w:
        w.write("# 26 前端面试工程 · 拆题索引\n\n| 文件 | 拆出题数 |\n|---|---|\n")
        for k, v in stats.items():
            w.write(f"| {k} | {v} |\n")
        w.write(f"| **合计** | **{total}** |\n")

if __name__ == "__main__":
    main()
