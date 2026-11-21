---
title: [Q494] bisect:有序表的二分插入
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q494 · bisect:有序表的二分插入

> 难度:★★★☆ | 标签:bisect, 算法

**问**:向有序列表插入元素并保持有序,bisect 为什么比「append 后 sort」好?bisect_left 和 bisect_right 的区别?

**答**:bisect 用二分查找定位 O(log n),insort 定位后 memmove 插入 O(n),但全程保持有序、无重排;append+sort 是 O(n log n) 且破坏「永远有序」的不变式,不支持中途查询。bisect_left 找「第一个 ≥ x 的位置」(相同时插到左边),bisect_right 找「第一个 > x 的位置」(相同时插到右边)——去重插入用 left(存在则不插)、统计 `< x` 的个数用 left、`≤ x` 用 right。经典应用还有分数等级表:用 bisect 在断点列表里定位区间,代替一串 if-elif。

```python
# file: code/01_语言核心与底层/q494_bisect.py
import bisect

if __name__ == "__main__":
    scores = [60, 70, 80, 90]
    bisect.insort(scores, 75)
    print(scores)

    print("left of 80:", bisect.bisect_left(scores, 80))
    print("right of 80:", bisect.bisect_right(scores, 80))
    print("left of 75 :", bisect.bisect_left(scores, 75))

    def grade(score, breakpoints=[60, 70, 80, 90]):
        return "FDCBA"[bisect.bisect(breakpoints, score)]

    print([grade(s) for s in [59, 60, 71, 100]])

    def insert_unique(lst, x):
        pos = bisect.bisect_left(lst, x)
        if pos == len(lst) or lst[pos] != x:
            lst.insert(pos, x)
        return pos

    uniq = [1, 3, 5]
    insert_unique(uniq, 4)
    insert_unique(uniq, 4)
    print("unique insert:", uniq)
```

**追问**:1) 频繁在头部插入用什么?——bisect 依赖连续内存的 list,头部插入是 O(n);高频头部操作换 deque(两端 O(1))或放弃有序数组改用堆/跳表结构。2) bisect.insort 为什么是 O(n)?——二分只负责找位置 O(log n);list 底层连续数组插入必须 memmove 搬移元素,这才是大头——所以 insort 适合「低频插入、高频二分查询」。3) 二分的底层语义?——bisect_left/right 分别返回第一个可插入位/最后一个可插入位,决定相等元素插左边还是右边;3.10+ 支持 key 参数,免去构造 (key, item) 元组。4) 生产陷阱?——混用 append 破坏「始终有序」不变式,二分结果全错;把有序 list 当数据库索引用,数据量到百万级插入性能崩塌;相等元素的稳定插入方向选错导致重复键乱序。
