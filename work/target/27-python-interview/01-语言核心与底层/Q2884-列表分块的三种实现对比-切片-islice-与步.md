---
title: [Q2884] 列表分块的三种实现对比:切片、islice 与步进生成器
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2884 · 列表分块的三种实现对比:切片、islice 与步进生成器

> 难度:★★★☆☆ | 标签:itertools, islice, 分块

**问**:把序列按固定大小分块,至少能写出三种实现,各自的适用边界是什么?

**答**:三种实现代表三个流派:**切片法**一行出列表,依赖 len 与下标,只吃序列,但对 list 输入速度最快;**islice 法**把 `iter(iterable)` 包住,循环里 `list(islice(it, size))` 直到取空,是唯一能吃任意迭代器(生成器、文件、网络流)的版本,数据不必先进内存;**步进生成器**与切片法等价但惰性产出,适合「是序列但很大」的场景。实测一万元素分块,切片法略快于 islice 法,差距来自 islice 的调用开销与块构造方式,量级上可以忽略。选型口诀:手里是 list 就切片,手里是流就 islice,要惰性就包一层生成器。islice 法还有一个语义细节:它每次消费的都是同一个迭代器,游标位置由 islice 自己推进,这正是它能处理无长度流的原因。

```python
# file: code/01_语言核心与底层/q2884_chunk_list.py
"""列表分块的三种实现对比:切片、islice 与步进生成器。"""
import timeit
from itertools import islice


def chunk_slice(seq, size):
    """切片法:简单直观,每次产生新列表,仅接受序列。"""
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def chunk_islice(iterable, size):
    """islice 法:吃任意迭代器,惰性产出块,流式友好。"""
    it = iter(iterable)
    while True:
        block = list(islice(it, size))
        if not block:
            return
        yield block


def chunk_step(seq, size):
    """步进生成器:仅适合序列,切片语义与切片法一致但惰性。"""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


if __name__ == "__main__":
    data = list(range(10))
    print("切片法:", chunk_slice(data, 3))
    print("islice 法:", [b for b in chunk_islice(data, 3)])
    print("步进法:", list(chunk_step(data, 3)))

    print("islice 能吃生成器:", [b for b in chunk_islice((x * x for x in range(7)), 3)])
    print("尾部不足一块:", chunk_slice(data, 4))

    t1 = timeit.timeit(lambda: chunk_slice(list(range(10000)), 100), number=50)
    t2 = timeit.timeit(lambda: list(chunk_islice(list(range(10000)), 100)), number=50)
    print(f"1 万元素 50 次:切片 {t1:.3f}s,islice {t2:.3f}s")
```

**追问**:1) islice 版为什么不能改写成推导式?——推导式里没有地方保存「上一次消费到哪里」的游标,islice 的分块必须依赖同一个被反复消费的迭代器,这正是它与切片法的本质差别。2) 三种实现的取舍?——切片法:仅适用 list/序列(可下标);islice 法:任意迭代器,游标隐藏在迭代器状态;步进生成器:range(i, len, n) 取样式分块;数据形态决定选型。3) 流式场景的意义?——文件/网络流不能 materialize,islice 分块是「固定批次消费」的标准姿势;配合 chunked 上传/批处理。4) 生产陷阱?——对生成器用切片法(TypeError);最后一块不足静默(要显式校验);islice 在循环外复用同一迭代器的并发竞态。
