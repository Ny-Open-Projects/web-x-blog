---
title: [Q1549] pairwise 与滑动窗口:相邻差分的实现与版本兼容
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1549 · pairwise 与滑动窗口:相邻差分的实现与版本兼容

> 难度:★★★★☆ | 标签:itertools, 滑动窗口, 版本兼容

**问**:3.9 还没有 itertools.pairwise,怎么优雅实现相邻对与滑动窗口?窗口生成有哪些工程用法?

**答**:相邻对的惰性实现是经典 recipe:tee 一份迭代器,next(b, None) 错开一格后 zip——O(1) 内存且吃任意迭代器;3.10 起标准库自带 itertools.pairwise,工程代码用 sys.version_info 守卫双实现。宽 k 的滑动窗口首选 deque(maxlen=k) 滚动:填满窗口后每来一个元素 append 并产出当前快照,内存 O(k)。工程用法:相邻差分(监控曲线变化率)、连续重复检测、窗口特征提取、逆序对扫描。要点:① zip(seq, seq[1:]) 版本要求序列可二次遍历,迭代器场景必须 tee/islice;② 窗口宽大于序列长时静默产出空,要报错就在入口校验;③ 窗口宽 1 退化成单元素元组流。

```python
# file: code/01_语言核心与底层/q1549_pairwise_window.py
import sys
from collections import deque
from itertools import islice, tee


def pairwise(iterable):
    """3.9 兼容实现,3.10+ 可直接用 itertools.pairwise。"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def sliding_window(iterable, width):
    it = iter(iterable)
    window = deque(islice(it, width), maxlen=width)
    if len(window) == width:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def deltas(seq):
    return [b - a for a, b in pairwise(seq)]


if __name__ == "__main__":
    if sys.version_info >= (3, 10):
        from itertools import pairwise as std_pairwise
        print("stdlib pairwise:", list(std_pairwise([1, 2, 3, 4])))
    else:
        print("python", sys.version_info[:3], "uses the recipe above")

    print("pairwise:", list(pairwise([1, 2, 3, 4])))
    print("deltas  :", deltas([10, 12, 9, 15, 15]))

    print("window 3:", list(sliding_window(range(5), 3)))
    print("window 1:", list(sliding_window("abc", 1)))

    # 相邻重复检测:监控指标连续相等要合并
    readings = [42, 42, 42, 43, 43, 44]
    repeats = sorted({a for a, b in pairwise(readings) if a == b})
    print("consecutive equal:", repeats)
```

**追问**:1) 滑动窗口宽 k 大于序列长怎么办?——deque 版静默产出空(初始 islice 不满 width 直接不 yield),zip 版也是空;要报错就在入口校验宽度。2) pairwise 的语义与版本?——相邻对 (it[0],it[1])...首元素不出现在任何对里(差分场景先想清楚);3.10+ 内建,3.9- 用 zip(it, islice(it, 1, None)) 兼容。3) 宽 k 窗口的实现?——deque(maxlen=k) 边迭代边产出(满员后每步一个快照)或 zip(*(islice(it, i, None) for i in range(k)));头尾「不满不产出」是统一语义。4) 生产陷阱?——差分首元素丢失未在文档说明;k > len 静默空结果当成功;把窗口数据物化成 list 而不是流式。
