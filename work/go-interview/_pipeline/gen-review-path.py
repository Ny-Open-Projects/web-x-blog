#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen-review-path.py —— 生成「复习路线」（按优先级 + 主题，**不动任何卡号**）。

为什么需要它：
    卡号是**引用锚点**（591 处卡间引用 + ERRORS.md 台账 + 归档目录都绑在号上），
    所以「号段跨三代、手工分配、不重编」——号**不承载主题信息**，不能当复习顺序。
    真正可用于排序的信号有三个，本脚本把它们**归一化**后重排：
      ① 频率（面试频率）→ 决定「先背哪些」
      ② 章（来源 `NN-MM`）→ 决定「怎么成片」
      ③ 被引用次数（in-degree）→ 决定「章内从哪张先读」（被引越多＝越多卡靠它＝越基础）

用法：
    python3 _pipeline/gen-review-path.py            # 写 复习路线.md / .txt
    python3 _pipeline/gen-review-path.py --dry-run  # 只打印统计
"""
import argparse
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
TGT = PROJ / "target" / "go"

CH_NAMES = {
    "2": "Go 语言概览与特性", "4": "Go 基础语法与标准库", "5": "Go 语言进阶",
    "6": "Go 语言高级特性", "7": "常用库与框架", "8": "并发模型与调度器",
    "9": "数据类型底层原理", "10": "并发编程", "11": "性能优化", "12": "数据库",
    "13": "Elasticsearch", "14": "消息中间件", "15": "微服务", "16": "设计模式",
    "17": "数据结构与算法", "18": "Linux / 网络", "19": "项目与系统设计", "20": "求职与录用",
}
# 推荐章序：由语言内核 → 并发/底层 → 性能 → 库 → 存储/中间件 → 架构 → 系统 → 算法 → 软技能
CH_ORDER = ["2", "4", "5", "6", "9", "8", "10", "11", "7", "12", "14", "13", "15", "16", "18", "17", "19", "20"]

# 引用形态：见 N 卡 / N 卡 / N 号卡 / 见卡 N（与 fix-card-refs.py 同口径）
REF = re.compile(r"见\s*(\d{3,4})\s*卡|(?<![0-9])(\d{3,4})\s*号?卡|(?<![本该])卡\s*(\d{3,4})")


def ndiff(s):
    s = s.strip()
    if re.match(r"^L?4|资深|^高级", s):
        return 4
    if re.match(r"^L?3|进阶|中高|中等偏进阶", s):
        return 3
    if re.match(r"^L?2|中级|中等|基础偏上", s):
        return 2
    if re.match(r"^L?1|入门|基础|^简单", s):
        return 1
    return 0


def nfreq(s):
    s = s.strip()
    if "极高" in s[:4]:
        return 5
    if "很高" in s[:4]:
        return 4
    if "中高" in s[:4] or s.startswith("高"):
        return 3
    if s.startswith("中"):
        return 2
    if s.startswith("低"):
        return 1
    return 0


DIFF_LABEL = {4: "L4", 3: "L3", 2: "L2", 1: "L1", 0: "—"}
FREQ_LABEL = {5: "极高", 4: "很高", 3: "高", 2: "中", 1: "低", 0: "—"}


def load():
    indeg = Counter()
    raw = []
    for p in sorted(TGT.glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        num = p.name.split("-")[0]
        title = p.name.split("-", 1)[1][:-3]
        raw.append((num, title, txt))
        for line in txt.split("\n"):
            for m in REF.finditer(line):
                for g in m.groups():
                    if g:
                        indeg[g] += 1
    cards = []
    for num, title, txt in raw:
        m = re.search(r"^>\s*来源：`?(\d{1,2})-", txt, re.M)
        ch = (m.group(1).lstrip("0") or "0") if m else "?"
        d = re.search(r"难度[：:]\s*([^\n｜|]+)", txt)
        f = re.search(r"面试频率[：:]\s*([^\n｜|]+)", txt) or re.search(r"频率[：:]\s*([^\n｜|]+)", txt)
        cards.append({"num": num, "title": title, "ch": ch,
                      "diff": ndiff(d.group(1)) if d else 0,
                      "freq": nfreq(f.group(1)) if f else 0,
                      "indeg": indeg[num]})
    return cards


def sortkey(c):
    # 章内：先地基（被引多）、再高频、再易到难、最后按号稳定
    return (-c["indeg"], -c["freq"], c["diff"], int(c["num"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cards = load()
    bych = {}
    for c in cards:
        bych.setdefault(c["ch"], []).append(c)
    hot = [c for c in cards if c["freq"] >= 4]
    hot.sort(key=lambda c: (-c["freq"], -c["indeg"], int(c["num"])))
    cold = [c for c in cards if c["freq"] <= 1]
    leaf = [c for c in cards if c["indeg"] == 0]

    if a.dry_run:
        print("总卡数", len(cards), "| 章数", len(bych), "| 高频(≥很高)", len(hot),
              "| 低频", len(cold), "| 零引用叶子", len(leaf))
        for ch in CH_ORDER:
            if ch in bych:
                print(f"  章{ch:>2} {CH_NAMES.get(ch,'?'):<18} {len(bych[ch]):>3} 张")
        return

    L = []
    L.append("# Go 面试复习路线（378 张 · 不动卡号）")
    L.append("")
    L.append("> 自动生成：`_pipeline/gen-review-path.py`。**号只是身份证，复习顺序看这里。**")
    L.append("")
    L.append("## 为什么号不能当顺序")
    L.append("")
    L.append("卡号是**引用锚点**——591 处卡间引用（「见 545 卡」）、`ERRORS.md` 纠错台账、")
    L.append("实测归档目录全都绑在号上，所以号段跨三代、手工分配、**故意不重编**。")
    L.append("它**不承载主题/难度/频率**（例：500–599 段 83 张横跨 7 个主题章）。")
    L.append("")
    L.append("本路线把三个真正有用的信号**归一化**后重排：")
    L.append("")
    L.append("| 信号 | 从哪读 | 决定什么 |")
    L.append("|---|---|---|")
    L.append("| 面试频率 | 卡头 `面试频率：` | **先背哪些**（第 1 遍） |")
    L.append("| 主题章 | 卡头 `来源：NN-MM` | **怎么成片**（第 2 遍走章） |")
    L.append("| 被引用次数 | 全库「见 N 卡」计数 | **章内从哪张先读**（被引越多＝越基础） |")
    L.append("")
    L.append("## 三遍法")
    L.append("")
    L.append(f"1. **第 1 遍 · 冲刺必背**：{len(hot)} 张高频（极高/很高）。只看 🎯速记区，先拿分。")
    L.append(f"2. **第 2 遍 · 按章成片**：{len(bych)} 章，章内按「被引用次数」从地基到上层。")
    L.append("3. **第 3 遍 · 查漏**：低频 + 零依赖叶子 + `ERRORS.md` 错题。")
    L.append("")
    L.append("**每张卡怎么用（约 3 分钟）**：① 只看 🎯速记区，合上卡自己讲一遍；")
    L.append("② 讲不出再展开 📖原理区（先说结论 → 逐行讲透 → 实测验证）；")
    L.append("③ 卡里有【实测】数字的，被追问时用它兜底；有「原文哪里错了」的，那是面试官埋的坑。")
    L.append("")
    L.append("## ⚠️ 一个数据偏差，先看这条再定你的顺序")
    L.append("")
    L.append("第 1 遍那 19 张是**跨 worker 的「极高/很高」评级**，天然偏基础设施")
    L.append("（数据库 12 / 网络 18 / 中间件 14 / ES 13 / 微服务 15）——**里面一张 Go 语言的卡都没有**。")
    L.append("这不是漏，是当年的评级分布就是这样（Go 语言卡普遍被评「高」，223 张）。")
    L.append("")
    L.append("**所以按你的岗位调权重**：")
    L.append("")
    L.append("| 岗位 | 第 2 遍先走这几章 | 张数 |")
    L.append("|---|---|---|")
    L.append("| **Go 后端 / 高级 Go** | 9 数据类型底层 → 10 并发编程 → 8 并发模型与调度 → 11 性能优化 → 6 高级特性 | 103 |")
    L.append("| 数据库 / 存储 | 12 数据库 → 14 消息中间件 → 13 ES | 101 |")
    L.append("| 后端架构 / 微服务 | 15 微服务 → 16 设计模式 → 19 项目与系统设计 | 41 |")
    L.append("| 网络 / 运维 | 18 Linux / 网络 | 53 |")
    L.append("| 算法岗 | 17 数据结构与算法 → 9/10 的 map/slice/sync 底层 | 23+ |")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## 第 1 遍 · 冲刺必背（{len(hot)} 张 · 频率极高/很高）")
    L.append("")
    L.append("| 序 | 卡号 | 标题 | 章 | 频率 | 被引 |")
    L.append("|---|---|---|---|---|---|")
    for i, c in enumerate(hot, 1):
        L.append(f"| {i} | **{c['num']}** | {c['title']} | {c['ch']}. {CH_NAMES.get(c['ch'],'?')} | {FREQ_LABEL[c['freq']]} | {c['indeg']} |")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 第 2 遍 · 按章成片（推荐章序，章内＝地基在前）")
    L.append("")
    L.append("章序按「由语言内核 → 并发/底层 → 性能 → 库 → 存储/中间件 → 架构 → 系统 → 算法 → 软技能」排。")
    L.append("")
    for ch in CH_ORDER:
        if ch not in bych:
            continue
        cs = sorted(bych[ch], key=sortkey)
        L.append(f"### 章 {ch} · {CH_NAMES.get(ch,'?')}（{len(cs)} 张）")
        L.append("")
        L.append("| 序 | 卡号 | 标题 | 难度 | 频率 | 被引 |")
        L.append("|---|---|---|---|---|---|")
        for i, c in enumerate(cs, 1):
            L.append(f"| {i} | **{c['num']}** | {c['title']} | {DIFF_LABEL[c['diff']]} | {FREQ_LABEL[c['freq']]} | {c['indeg']} |")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## 第 3 遍 · 查漏")
    L.append("")
    L.append(f"**① 低频（频率＝低/未标，共 {len(cold)} 张）**——最后扫，或按需跳过：")
    L.append("")
    L.append("　　" + "、".join(c["num"] for c in sorted(cold, key=lambda c: int(c["num"]))))
    L.append("")
    L.append(f"**② 零依赖叶子（无人引用，共 {len(leaf)} 张）**——这些是「末端知识」，不支撑别的卡；")
    L.append("　　时间紧时可**只背 🎯速记区**。完整清单：")
    L.append("")
    L.append("　　" + "、".join(c["num"] for c in sorted(leaf, key=lambda c: int(c["num"]))))
    L.append("")
    L.append("**③ 方法论 / 非技术卡**（求职、路线图、答题技巧）：章 19「项目与系统设计」、章 20「求职与录用」。")
    L.append("")
    L.append("**④ 错题**：`_pipeline/ERRORS.md` 是原始素材的技术纠错台账——被纠过的点，正是面试官爱埋的坑。")
    L.append("")
    L.append("## 附：背之前先看这三份（已生成）")
    L.append("")
    L.append("| 文件 | 用途 |")
    L.append("|---|---|")
    L.append("| `背诵清单-全库.md` | 自测区（只看标题＋要点骨架）＋ 答案区（按卡号对答案）；带 ★ 频率分级 |")
    L.append("| `读物-学习路径/` | 章内**依赖序**（按「见 N 卡」建图拓扑排序，被引用的先读） |")
    L.append("| `读物-精读篇/` `读物-速览篇/` | 按章的完整读物（正文取自原卡，未改写） |")
    L.append("")
    txt = "\n".join(L) + "\n"
    (PROJ / "复习路线.md").write_text(txt, encoding="utf-8")
    (PROJ / "复习路线.txt").write_text(txt, encoding="utf-8")
    print(f"→ 复习路线.md / .txt　（{len(cards)} 张 / {len(bych)} 章 / 第1遍 {len(hot)} 张 / 第3遍低频 {len(cold)} 张）")


if __name__ == "__main__":
    main()
