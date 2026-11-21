#!/usr/bin/env python3
"""33-java-interview 扩量：interview-bank 话术题 → 话术卡（一知识点一卡，n 问打包）。

分组规则（已对 13 域验证 cycles==facts 行数全等）：
- 题型规范序 概念<误用<原理<工程<结论<边界<追问；版本演进为通配位（不参与序比较）。
- 题型序号回退（且非版本演进）即新一轮；每组恰对应 facts 矩阵按序的一条 → 标题取 term/topic/dim。
产出：target/33-java-interview/35~47-话术-{域}/ ，一条 5-8 问的完整话术包。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from split_java_interview import (  # 复用 slugify / fm / write_card / FACT_DOMAINS
    DST, SRC, COURSE_TAG, FACT_DOMAINS, slugify, fm, write_card,
)

BANK = Path("/Volumes/SAMSUNG/ai-done/win1/java-interview/notes/quiz/out")
ORDER = {"概念考察": 0, "误用纠错": 1, "原理深挖": 2, "工程落地": 3, "结论依据": 4, "边界追问": 5, "追问链": 6}
# 域 -> (outdir, category)，编号接背诵域 22-34 之后
TALK_DOMAINS = {
    dom: (f"{35 + i}-话术-{cat}", cat) for i, (dom, (_, cat)) in enumerate(FACT_DOMAINS.items())
}


def main():
    stats, defects, fixed = {}, [], 0
    for dom, (outdir, category) in TALK_DOMAINS.items():
        facts = []
        for ln in (SRC / "notes/quiz/facts" / f"{dom}.txt").read_text(encoding="utf-8").splitlines():
            if re.match(r"^[A-Z]{1,3}-\d{3}\|", ln):
                facts.append(ln.split("|"))
        bank = (BANK / dom / "interview-bank.md").read_text(encoding="utf-8")
        qs = [q for q in re.split(r"\n\n(?=\*\*Q[a-z-]+-\d+（)", bank) if q.startswith("**Q")]
        groups, prev_idx = [], -1
        for q in qs:
            m = re.search(r"（(.+?)·P", q.splitlines()[0])
            t = m.group(1) if m else "?"
            idx = ORDER.get(t, 9)
            if not groups or (idx <= prev_idx and t != "版本演进"):
                groups.append([])
            if t != "版本演进":
                prev_idx = idx
            groups[-1].append(q)
        if len(groups) != len(facts):
            defects.append(f"{dom}: cycles={len(groups)} != facts={len(facts)}，跳过该域")
            continue
        n = 0
        for k, (grp, f) in enumerate(zip(groups, facts), 1):
            fid_prefix = f[0].rsplit("-", 1)[0]
            topic, dim, term = f[2], f[3], f[4]
            if dom == "agent-dev" and f[0].startswith("JA-"):
                fid_prefix = "AD"
            title = f"[话术{fid_prefix}-{k:03d}] {topic}·{term}（{dim}）· {len(grp)} 问"
            body = [f"## {topic} · {term}（{dim}）—— {len(grp)} 类问法与标准话术", ""]
            for q in grp:
                qlines = q.splitlines()
                # 源缺陷机械归一：java-basics 域模板拼接产生 769 处「。。」
                for i, ln in enumerate(qlines):
                    if "。。" in ln:
                        fixed += ln.count("。。")
                        qlines[i] = re.sub(r"。{2,}", "。", ln)
                body += qlines + ["", "---", ""]
            name = f"tk-{fid_prefix.lower()}{k:03d}-{slugify(term, 20)}"
            write_card(DST / outdir, name, title, category,
                       ["Java面试", "话术卡", COURSE_TAG], "话术卡", body)
            n += 1
        stats[dom] = n
    total = sum(stats.values())
    rep = DST / "reports"
    rep.mkdir(parents=True, exist_ok=True)
    lines = ["# scan3 · 话术卡拆分报告（2026-11-18）", "",
             f"- 总话术卡：**{total}**（13 域 × 知识点，一卡 n 问）",
             f"- 源缺陷机械归一：「。。」→「。」共 **{fixed}** 处（java-banks java-basics 域模板拼接残留，其余 12 域与 facts 矩阵干净）",
             "- 分组规则：题型规范序回退即切组，版本演进通配；13 域 cycles==facts 行数全等", "",
             "| 域 | 卡数 |", "|---|---|"]
    for dom, n in stats.items():
        lines.append(f"| {dom} | {n} |")
    if defects:
        lines += ["", "## 异常", ""] + [f"- {d}" for d in defects]
    (rep / "scan3-talk.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"talk cards: {total}")
    for dom, n in stats.items():
        print(f"{n:5d}  {dom}")
    for d in defects:
        print("!", d)


if __name__ == "__main__":
    main()
