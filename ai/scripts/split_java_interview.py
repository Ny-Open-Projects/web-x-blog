#!/usr/bin/env python3
"""把 source/33.java-interview 拆成题目卡片，落 target/33-java-interview/。

三层拆解（源：Windows 侧交付的「阿里 P10 面试准备全库」成品题库，160 文件 / 45.4M）：
A. 体系精讲 docs/01-10 + 25-mongodb + 11-appendix（12 章）→ 按 ### 题 / ### 卡片 拆卡，
   无子题的 ## 段（考察雷达 / 追问链图谱 / 速记卡 / 参考资料）整段成卡。
B. 实战演练：手写代码 10 题 / Agent 手写笔试 10 题 / 对话剧 10 篇 / 闭卷笔试 7 卷 /
   模拟卷 20 份 / 快问快答 7 组 / 追问地图+补漏 / 方法论与实录 8 册 / 全卷速记卡 / 导览。
C. 背诵卡 notes/quiz/facts/ 13 域 2550 条事实矩阵 → 一条一卡（事实/原理/误区/用法/锚点）。

已知源缺陷（拆题时修正，source 不动）：
- agent-dev.txt 第 37 行 ID 误写 JA-033（前后为 AD-031/032/034），归一化为 AD-033。
- INDEX.md 统计是陈旧版（6145 题），实际题库 20908 条，以 DELIVERY.md 为准。
"""
import re
from pathlib import Path

SRC = Path("/Users/Wang/Code/github/web-x-blog/work/source/33.java-interview")
DST = Path("/Users/Wang/Code/github/web-x-blog/work/target/33-java-interview")
DATE = "2026-11-18"
COURSE_TAG = "33"

H2_RE = re.compile(r"^## .+")
H3_RE = re.compile(r"^### .+")


def slugify(text, limit=24):
    keep = []
    for ch in text:
        if ch.isalnum() or ("\u4e00" <= ch <= "\u9fff"):
            keep.append(ch)
        elif keep and keep[-1] != "-":
            keep.append("-")
    return "".join(keep).strip("-")[:limit].strip("-") or "untitled"


def fm(title, category, tags, qtype):
    # title 一律双引号包裹，防 YAML 冒号炸裂
    t = title.replace("\\", "\\\\").replace('"', '\\"')
    return (
        "---\n"
        f'title: "{t}"\n'
        f"date: {DATE}\n"
        f"categories: [Java面试, {category}]\n"
        f"tags: [{', '.join(tags)}]\n"
        f"type: {qtype}\n"
        "disableNunjucks: true\n"
        "---\n\n"
    )


def split_fenced(lines):
    """按 H2/H3 切分段落，围栏代码块内的 # 行不算标题。
    返回 [(level, heading, body_lines)]，level=2|3。"""
    blocks = []
    fence = False
    cur_level, cur_head, cur_body = 0, "", []
    for ln in lines:
        if ln.strip().startswith("```"):
            fence = not fence
            if cur_level:
                cur_body.append(ln)
            continue
        if not fence and H2_RE.match(ln):
            if cur_level:
                blocks.append((cur_level, cur_head, cur_body))
            cur_level, cur_head, cur_body = 2, ln, []
        elif not fence and H3_RE.match(ln):
            if cur_level:
                blocks.append((cur_level, cur_head, cur_body))
            cur_level, cur_head, cur_body = 3, ln, []
        elif cur_level:
            cur_body.append(ln)
    if cur_level:
        blocks.append((cur_level, cur_head, cur_body))
    return blocks


def clean_heading(head):
    return head.lstrip("#").strip()


def infer_type(head):
    """从标题推断 (type, 额外tag)。"""
    if re.search(r"入门题", head):
        return "面试题", "基础题"
    if re.search(r"进阶题", head):
        return "面试题", "进阶题"
    if re.search(r"压轴题", head):
        return "面试题", "压轴题"
    if re.search(r"题\s*\d", head):
        return "面试题", ""
    if re.search(r"卡片", head):
        return "概念卡", ""
    if re.search(r"速记", head):
        return "速记卡", ""
    if re.search(r"追问链", head):
        return "追问链", ""
    if re.search(r"地图|开局|中段|收尾|增值|不补", head):
        return "追问地图", ""
    if re.search(r"^### G\d", head):
        return "补漏卡", ""
    if re.search(r"卷", head):
        return "笔试题", ""
    if re.search(r"组[:：]", head):
        return "快问快答", ""
    if re.search(r"心法|策略|使用|建议|结论", head):
        return "方法论", ""
    return "讲义", ""


def write_card(outdir, name, title, category, tags, qtype, body_lines):
    outdir.mkdir(parents=True, exist_ok=True)
    body = "\n".join(body_lines).rstrip() + "\n"
    # 源缺陷机械归一：模板拼接产生的重复句号（java-basics bank 769 处 + 模拟卷零星）
    body = re.sub(r"。{2,}", "。", body)
    (outdir / f"{name}.md").write_text(fm(title, category, tags, qtype) + body, encoding="utf-8")


def demote(lines, n=1):
    """整体降 n 级标题（围栏感知），用于整文件卡。"""
    fence, out = False, []
    for ln in lines:
        if ln.strip().startswith("```"):
            fence = not fence
            out.append(ln)
            continue
        if not fence and re.match(r"^#{1,5} ", ln):
            out.append("#" * (len(ln) - len(ln.lstrip("#")) + n) + ln.lstrip("#"))
        else:
            out.append(ln)
    return out


def chapter_mode(src, outdir, prefix, category, default_type=None):
    """体系章模式：H3 子块成卡，无 H3 的 H2 段整段成卡，文档头并入首卡。
    空壳 H2 容器段（如「## 1.2 入门题（P4-P6）」）只作难度上下文，不产卡。"""
    lines = src.read_text(encoding="utf-8").splitlines()
    blocks = split_fenced(lines)
    # 文档头 = H1 + 首个标题前的引言
    head_end = 0
    for i, ln in enumerate(lines):
        if H2_RE.match(ln) or H3_RE.match(ln):
            head_end = i
            break
    doc_head = lines[:head_end]
    stats, seq, ctx = [], 0, ""
    for bi, (level, head, body) in enumerate(blocks):
        content = [l for l in body if l.strip()]
        # 空壳容器段 / 仅一行且后面跟 H3 的过渡段：记为上下文，跳过
        if level == 2 and not content or (
            level == 2 and len(content) < 2 and bi + 1 < len(blocks) and blocks[bi + 1][0] == 3
        ):
            ctx = clean_heading(head)
            continue
        seq += 1
        title = clean_heading(head)
        if default_type is None:
            if level == 3:
                qtype, extra = infer_type(head) if re.search(r"G\d", head) else infer_type(ctx + " " + head)
            else:
                qtype, extra = infer_type(head)
                ctx = title  # 实卡 H2 之后跟随的 H3 以它为上下文
        else:
            qtype, extra = default_type, ""
        if extra:
            tags = ["Java面试", qtype, extra, COURSE_TAG]
        else:
            tags = ["Java面试", qtype, COURSE_TAG]
        name = f"{prefix}{seq:03d}-{slugify(title)}"
        body_out = ([*doc_head, ""] if not stats and doc_head else []) + [head] + body
        write_card(DST / outdir, name, title, category, tags, qtype, body_out)
        stats.append((name, qtype))
    return stats


def whole_mode(src, outdir, prefix, category, qtype):
    """整文件一卡：标题取 H1，正文整体降一级。"""
    lines = src.read_text(encoding="utf-8").splitlines()
    title = ""
    for ln in lines:
        if ln.startswith("# "):
            title = ln[2:].strip()
            break
    if not title:
        title = src.stem
    body = demote(lines)
    name = f"{prefix}-{slugify(title)}"
    write_card(DST / outdir, name, title, category, ["Java面试", qtype, COURSE_TAG], qtype, body)
    return [(name, qtype)]


# ---------------- 单元配置 ----------------
CH = [  # 体系 12 章 (src_rel, outdir, prefix, category)
    ("docs/01-java-fundamentals/README.md", "01-语言基础与集合", "ch01", "Java语言基础"),
    ("docs/02-jvm-concurrency/README.md", "02-并发与JUC", "ch02", "Java并发"),
    ("docs/03-jvm/README.md", "03-JVM与调优", "ch03", "JVM"),
    ("docs/04-spring-ecosystem/README.md", "04-Spring生态", "ch04", "Spring"),
    ("docs/05-mysql-storage/README.md", "05-MySQL与存储", "ch05", "MySQL"),
    ("docs/06-redis-cache/README.md", "06-Redis与缓存", "ch06", "Redis"),
    ("docs/07-messaging/README.md", "07-消息队列", "ch07", "消息队列"),
    ("docs/08-distributed-microservices/README.md", "08-分布式与微服务", "ch08", "分布式"),
    ("docs/09-system-design/README.md", "09-高并发系统设计", "ch09", "系统设计"),
    ("docs/10-ai-agent/README.md", "10-AI与Agent", "ch10", "AI与Agent"),
    ("docs/25-mongodb/README.md", "11-MongoDB", "ch11", "MongoDB"),
    ("docs/11-appendix/README.md", "12-软实力与流程", "ch12", "软实力"),
]

FACT_DOMAINS = {  # domain -> (outdir, category)
    "java-basics": ("22-背诵-Java语言基础", "Java语言基础"),
    "concurrency": ("23-背诵-Java并发", "Java并发"),
    "jvm": ("24-背诵-JVM", "JVM"),
    "spring": ("25-背诵-Spring", "Spring"),
    "mysql": ("26-背诵-MySQL", "MySQL"),
    "redis": ("27-背诵-Redis", "Redis"),
    "mongodb": ("28-背诵-MongoDB", "MongoDB"),
    "mq": ("29-背诵-消息队列", "消息队列"),
    "distributed": ("30-背诵-分布式", "分布式"),
    "ai": ("31-背诵-AI应用", "AI应用"),
    "algorithm": ("32-背诵-算法", "算法"),
    "agent-dev": ("33-背诵-Agent开发", "Agent开发"),
    "java-ai": ("34-背诵-Java+AI工程", "Java+AI工程"),
}


def facts_mode():
    """事实矩阵 → 背诵卡。一条一卡，卡身五件套：事实/原理/误区/用法/锚点。"""
    stats, defects = {}, []
    seen_ids = set()
    for dom, (outdir, category) in FACT_DOMAINS.items():
        n = 0
        for ln in (SRC / "notes/quiz/facts" / f"{dom}.txt").read_text(encoding="utf-8").splitlines():
            if not re.match(r"^[A-Z]{1,3}-\d{3}", ln) or "|" not in ln:
                continue
            fields = ln.split("|")
            if len(fields) < 12:
                defects.append(f"{dom}: 字段数{len(fields)}<12: {ln[:60]}")
                continue
            fid, topic, dim, term = fields[0], fields[2], fields[3], fields[4]
            why, usage, version = fields[-6], fields[-2], fields[-1]
            fact = "|".join(fields[5 : len(fields) - 6])
            miscon = [m for m in fields[-5:-2] if m.strip()]
            if dom == "agent-dev" and fid.startswith("JA-"):
                defects.append(f"agent-dev: {fid} 前缀归一化为 AD-{fid[3:]}（源笔误，AD-031/032/034 序列）")
                fid = "AD-" + fid[3:]
            if fid in seen_ids:
                defects.append(f"重复ID: {fid}（{dom}）")
            seen_ids.add(fid)
            title = f"[{fid}] {topic}·{term}（{dim}）"
            bullets = [f"## {topic} · {term}（{dim}）", "", f"- **事实**：{fact}", f"- **原理**：{why}"]
            if miscon:
                bullets.append("- **常见误区**：")
                bullets += [f"  {i+1}. {m}（错）" for i, m in enumerate(miscon)]
            bullets += [f"- **工程用法**：{usage}", f"- **版本锚点**：{version}", ""]
            name = f"{fid}-{slugify(term, 20)}"
            write_card(DST / outdir, name, title, category, ["Java面试", "背诵卡", COURSE_TAG], "背诵卡", bullets)
            n += 1
        stats[dom] = n
    return stats, defects


def main():
    report = []
    total = 0
    per_dir = {}

    def run(stats, label):
        nonlocal total
        for name, qtype in stats:
            d = name.split("-")[0]
            per_dir.setdefault(label, 0)
            per_dir[label] += 1
            total += 1

    for rel, outdir, prefix, category in CH:
        run(chapter_mode(SRC / rel, outdir, prefix, category), outdir)

    run(chapter_mode(SRC / "docs/13-coding-lab/README.md", "13-手写代码", "code", "手写代码", default_type="手写题"), "13-手写代码")
    for f in sorted((SRC / "docs/agent-written-exam").glob("题*.md")):
        run(whole_mode(f, "14-Agent手写笔试", "awx", "Agent笔试", "手写题"), "14-Agent手写笔试")
    for f in sorted((SRC / "docs/23-dialog").glob("*.md")):
        if f.name == "README.md":
            continue
        run(whole_mode(f, "15-对话剧", "dlg", "面试对话", "对话剧"), "15-对话剧")
    run(chapter_mode(SRC / "docs/24-written-exam/README.md", "16-闭卷笔试", "wx", "笔试", default_type="笔试题"), "16-闭卷笔试")
    for i in range(1, 11):
        run(whole_mode(SRC / f"notes/quiz/exams/笔试模拟卷-{i:02d}.md", "17-模拟卷", f"mock{i:02d}", "模拟卷", "笔试卷"), "17-模拟卷")
        run(whole_mode(SRC / f"notes/quiz/exams/面试模拟问答卷-{i:02d}.md", "17-模拟卷", f"viva{i:02d}", "模拟卷", "问答卷"), "17-模拟卷")
    run(chapter_mode(SRC / "docs/15-rapid-fire/README.md", "18-快问快答", "rf", "快问快答", default_type="快问快答"), "18-快问快答")
    run(chapter_mode(SRC / "docs/22-interviewer-coverage/README.md", "19-追问地图", "map", "追问地图"), "19-追问地图")
    for rel, qtype in [
        ("docs/12-arthas-lab/README.md", "实操手册"),
        ("docs/14-mock-interview/README.md", "模拟剧本"),
        ("docs/16-daily-plan/README.md", "打卡计划"),
        ("docs/17-process/README.md", "流程定级"),
        ("docs/18-annotated-transcript/README.md", "面试实录"),
        ("docs/19-transcript-r2r3/README.md", "面试实录"),
        ("docs/21-transcript-final/README.md", "面试实录"),
        ("docs/20-source-code/README.md", "源码精读"),
    ]:
        run(whole_mode(SRC / rel, "20-方法论与实录", "jb", "方法论与实录", qtype), "20-方法论与实录")
    run(chapter_mode(SRC / "SPEED-CARDS.md", "21-全卷速记卡", "sc", "速记卡", default_type="速记卡"), "21-全卷速记卡")
    run(whole_mode(SRC / "docs/00-outline.md", "00-课程导览", "ov", "课程导览", "导览"), "00-课程导览")
    run(whole_mode(SRC / "DELIVERY.md", "00-课程导览", "ovd", "课程导览", "导览"), "00-课程导览")
    run(whole_mode(SRC / "STUDY-TRACKER.md", "00-课程导览", "ovt", "课程导览", "打卡表"), "00-课程导览")

    fstats, defects = facts_mode()
    for dom, n in fstats.items():
        per_dir[FACT_DOMAINS[dom][0]] = n
        total += n

    # 索引
    idx = ["# 33 java-interview · 拆题索引", "",
           f"合计 **{total} 卡**：体系精讲 + 实战演练 + 背诵卡 2550（源 13 域事实矩阵）", "",
           "| 目录 | 卡数 |", "|---|---|"]
    for k in sorted(per_dir):
        idx.append(f"| {k} | {per_dir[k]} |")
    DST.mkdir(parents=True, exist_ok=True)
    (DST / "_INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # 报告
    rep = DST / "reports"
    rep.mkdir(parents=True, exist_ok=True)
    lines = ["# scan1 · 拆题报告（2026-11-18）", "",
             f"- 总卡片：**{total}**", "- 层次：体系精讲 12 章 / 实战演练 9 类 / 背诵卡 13 域 2550 条", "",
             "## 源缺陷与处置", ""]
    lines += [f"- {d}" for d in defects] or ["- 无"]
    lines += ["", "## 备注", "",
              "- INDEX.md（源）统计为陈旧版 6145 题，实际 quiz 题库 20908 条，以 DELIVERY.md 为准；未按 INDEX 拆分。",
              "- 源 notes/quiz/exams 两块 HTML 面板（interactive-quiz / interview-manual）为自测工具，不拆卡，留在 source。",
              "- source 归档排除 maven target/ 构建产物与 ._* AppleDouble，160 文件 / 45.4M 与 live 逐字节 cmp 一致。"]
    (rep / "scan1-split.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"total cards: {total}")
    for k in sorted(per_dir):
        print(f"{per_dir[k]:5d}  {k}")
    if defects:
        print("defects:")
        for d in defects:
            print("  -", d)


if __name__ == "__main__":
    main()
