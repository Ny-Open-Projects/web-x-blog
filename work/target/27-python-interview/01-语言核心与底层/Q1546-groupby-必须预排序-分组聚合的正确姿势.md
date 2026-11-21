---
title: [Q1546] groupby 必须预排序:分组聚合的正确姿势
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1546 · groupby 必须预排序:分组聚合的正确姿势

> 难度:★★★★☆ | 标签:itertools, groupby, 聚合

**问**:groupby 对未排序数据会发生什么?为什么「先 sorted 再 groupby」几乎总是必需?分组键必须满足什么条件?

**答**:groupby 只对「连续相同」的键分组:数据未按同一把 key 排序时,同键被切成多段、组数虚高、聚合结果错——这是 itertools 第一大坑(Q436 讲 group 迭代器共享进度的陷阱,本题讲排序前提与聚合姿势)。正确姿势:先 sorted(data, key=同一把 key) 再 groupby(data, key=该 key),排序序与分组等价必须来自同一把尺子。要点:① group 是与主迭代器共享进度的迭代器,取下一组前必须 list() 物化;② 不排序的合法用法只有「连续段统计」(run-length encoding)——这是特性不是 bug;③ 数值型键先归一化再作 key(分箱、大小写、时区),保证相邻性成立;④ 分组聚合时在消费组内完成 min/max/sum,避免二次遍历。

```python
# file: code/01_语言核心与底层/q1546_groupby_presorted.py
from itertools import groupby
from operator import itemgetter

EVENTS = [
    ("web", 1), ("db", 1), ("web", 2), ("db", 2), ("web", 3),
]


def count_by_key_naive(events):
    """未排序直接分组:web 与 db 被切碎,组数虚高。"""
    return [(k, len(list(g))) for k, g in groupby(events, key=itemgetter(0))]


def count_by_key_sorted(events):
    """先按同一把 key 排序,再分组聚合。"""
    ordered = sorted(events, key=itemgetter(0))
    return {k: sum(1 for _ in g) for k, g in groupby(ordered, key=itemgetter(0))}


def run_length(seq):
    """不排序的合法用法:连续段编码。"""
    return [(k, len(list(g))) for k, g in groupby(seq)]


if __name__ == "__main__":
    print("naive :", count_by_key_naive(EVENTS))
    print("sorted:", count_by_key_sorted(EVENTS))

    print("runs of aabbbc:", run_length("aabbbc"))

    # 分组聚合:按分数段统计(先分箱再分组)
    scores = [88, 92, 79, 61, 55, 73, 95, 67]

    def band(s):
        return "pass" if s >= 60 else "fail"

    ordered = sorted(scores, key=band)
    summary = {}
    for k, g in groupby(ordered, key=band):
        items = list(g)
        summary[k] = {"count": len(items), "min": min(items), "max": max(items)}
    print("bands:", summary)
```

**追问**:1) groupby 的 key 函数必须和 sorted 的 key 一致吗?——必须来自同一把尺子,否则「同键相邻」不成立;键是数值区间时先分箱再排序。2) 预排序的原理?——分组只在相邻相等处切分:先 sorted(data, key=k) 再 groupby(data, key=k);多级分组用元组 key((dept, level));不排序的结果是同键被切成多组。3) 与 dict 分组的取舍?——groupby 流式、有序、内存低(逐组消费);defaultdict 分组不需要排序但乱序;大批量流式数据 groupby 是内存正解。4) 生产陷阱?——忘记预排序(最常见);key 尺子不一致(如排序用小写、分组用原值);组迭代器没立即物化(Q436);排序本身 O(n log n) 在超大数据上要先分桶。
