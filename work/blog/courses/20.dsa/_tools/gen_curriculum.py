#!/usr/bin/env python3
# gen_curriculum.py — 生成博客课程顺序（由浅入深，253题编号）
# 输出: _meta/curriculum.json  [{order, blog_id, problem, topic, stage, difficulty}]
import os, json, re

dsa = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
inv = json.load(open(f"{dsa}/_meta/inventory.json"))

# 10 阶段学习路径（由浅入深）
STAGES = [
    ("一", "线性结构入门", ["array", "hash", "queue", "stack"]),
    ("二", "链表",        ["linked_list"]),
    ("三", "字符串",      ["string"]),
    ("四", "查找与排序",  ["binary_search", "sort"]),
    ("五", "贪心策略",    ["greedy"]),
    ("六", "二叉树",      ["tree"]),
    ("七", "堆与优先队列",["heap"]),
    ("八", "矩阵与图",    ["matrix", "graph"]),
    ("九", "回溯与递归",  ["backtrack"]),
    ("十", "动态规划",    ["dp"]),
    ("附", "专题补充",    ["concurrency", "other", "notes"]),
]

# 各主题内经典难度锚点（LC 题号 -> 难度权重 0easy 1medium 2hard）
HARDNESS = {
    # dp 中的难题靠后
    "lc_10_":2, "lc_44_":2, "lc_72_":2, "lc_115_":2, "lc_1494_":2, "lc_2050_":2, "lc_2407_":2,
    "lc_32_":2, "lc_123_":2, "lc_188_":2,
    # 经典 easy
    "lc_1_":0, "lc_26_":0, "lc_27_":0, "lc_35_":0, "lc_53_":0, "lc_70_":0, "lc_88_":0, "lc_104_":0,
    "lc_121_":0, "lc_155_":0, "lc_169_":0, "lc_226_":0, "lc_237_":0, "lc_344_":0, "lc_509_":0,
    "lc_905_":0, "lc_933_":0, "lc_1108_":0,
    # 经典 hard
    "lc_23_":2, "lc_41_":2, "lc_42_":2, "lc_124_":2, "lc_295_":2, "lc_895_":2,
}

def hardness(prob, topic):
    for k, v in HARDNESS.items():
        if prob.startswith(k): return v
    # notes 类按主题估计：排序笔记中等偏易
    if topic == "notes": return 1
    return 1  # 默认 medium

rows = []
for stage_no, stage_name, topics in STAGES:
    probs = [(p, v) for p, v in inv.items() if v["topic"] in topics]
    # 主题内排序：难度升序，同难度按 LC 编号/字典序
    probs.sort(key=lambda x: (hardness(x[0], x[1]["topic"]), x[0]))
    for p, v in probs:
        rows.append({
            "stage": f"第{stage_no}阶段 · {stage_name}",
            "topic": v["topic"],
            "problem": p,
            "id": v["id"],
            "n_solutions": v["n_solutions"],
            "hardness": ["Easy","Medium","Hard"][hardness(p, v["topic"])],
        })
# 全局编号
for i, r in enumerate(rows, 1):
    r["order"] = i
    r["blog_id"] = f"{i:03d}"

json.dump(rows, open(f"{dsa}/meta_curriculum.json" if False else f"{dsa}/_meta/curriculum.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter(r["stage"] for r in rows)
print(f"共 {len(rows)} 篇博客已排序")
for s, n in c.items(): print(f"  {s}: {n} 篇")
