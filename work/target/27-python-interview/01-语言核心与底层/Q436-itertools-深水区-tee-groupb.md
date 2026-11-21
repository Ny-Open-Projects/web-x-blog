---
title: [Q436] itertools 深水区:tee、groupby、islice 的陷阱
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q436 · itertools 深水区:tee、groupby、islice 的陷阱

> 难度:★★★★ | 标签:itertools, 迭代器

**问**:itertools.groupby 的分组结果为什么「用一次就没了」?tee 什么情况下会吃掉大量内存?

**答**:groupby 返回的 (key, group) 里 group 是与主迭代器共享进度的迭代器:主迭代器一旦前进(哪怕只是取下一组),上一组的 group 就作废,所以必须立即 `list(g)` 物化。tee 把一个迭代器复制成 n 个,内部用 FIFO 缓冲对齐进度,一旦某个副本落后太多,落后的部分全部滞留在缓冲里,内存退化为 O(总量)。islice 则是「带偏移的截断窗口」,它推进底层迭代器但不缓存被跳过的元素,适合切无穷流。

```python
# file: code/01_语言核心与底层/q436_itertools_pitfalls.py
from itertools import groupby, tee, islice, count

if __name__ == "__main__":
    # 1. groupby:分组键前进后,未消费的组即作废
    data = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
    saved = {k: list(g) for k, g in groupby(data, key=lambda w: w[0])}
    print(saved)                          # 立即物化才安全

    # 2. tee:副本进度差异大时靠缓存对齐
    src = iter(range(5))
    a, b = tee(src, 2)
    print(list(a))                        # a 先走完
    print(list(b))                        # b 靠 tee 内部缓冲补齐

    # 3. islice 切无穷迭代器:窗口语义,跳过的部分不缓存
    naturals = count()
    print(list(islice(naturals, 3, 8)))   # [3, 4, 5, 6, 7]
    print(next(naturals))                 # 8:islice 的推进被保留
```

**追问**:1) groupby 前先 `list(g)` 再前进主迭代器会发生什么?——什么都不会丢;反过来的顺序(先前进主迭代器)会导致当前组被静默丢弃,这是 groupby 最常见的线上 bug。2) 为什么 groupby 必须先排序?——分组只在「相邻键相等」处切分,不排序同一键会被切成多组;这是 Unix groupby 语义,不是全局哈希分组。3) tee 的内存行为底层机制?——各副本共享一个 FIFO 缓冲,落后副本从缓冲补齐,进度差无上界则缓冲退化为全量;CPython 对单副本请求直接返回原迭代器做优化。4) 生产陷阱?——`dict(groupby(data, key))` 是经典 bug:构造 dict 时主迭代器已走完,每个组的 group 全空;必须 `dict((k, list(g)) for ...)` 或先物化。
