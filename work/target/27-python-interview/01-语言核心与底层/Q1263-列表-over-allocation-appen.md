---
title: [Q1263] 列表 over-allocation:append 的均摊与增长曲线
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1263 · 列表 over-allocation:append 的均摊与增长曲线

> 难度:★★★☆☆ | 标签:list, 内存, 性能

**问**:list.append 号称均摊 O(1),「均摊」具体是怎么来的?为什么 `list(range(n))` 比 `for + append` 省内存?

**答**:list 底层是指针数组,写满时按 `newsize + newsize >> 3 + 6` 的公式超额分配(约 12.5% 余量)重新 malloc 并搬迁,单次扩容 O(n) 但按几何级数摊薄,所以 append 均摊 O(1)。代价是「装得多、报得也多」:`sys.getsizeof` 反映的是容量不是长度,长 list 的余量可能白占 10%+ 内存;而 `list(range(n))`、列表推导式(3.12+ PEP 709 后配合 length_hint)这类「预先知道长度」的构造能一次分配到位,没有中间搬迁。反向操作 `del lst[i]` 是 O(n) 搬迁,`pop()` 从尾部走则不缩容(除非余量过大),所以「不断 pop 到空」的 list 不会自动把内存还给分配器。

```python
# file: code/01_语言核心与底层/q1263_list_overalloc.py
import sys

if __name__ == "__main__":
    lst = []
    prev = sys.getsizeof(lst)
    marks = []
    for i in range(64):
        lst.append(i)
        s = sys.getsizeof(lst)
        if s != prev:                      # 容量跳变的时刻
            marks.append((len(lst), s))
            prev = s
    print("growth marks:", marks)
    print("一次到位:", sys.getsizeof(list(range(64))))
    print("append 曲线:扩容间距越来越长,均摊 O(1)")
```

**追问**:1) 如何把 list 的余量挤掉?——`lst = lst[:]` 或 `list(lst)` 按当前长度重分配一次, shrink 的标准手法;numba/数组场景则应直接换 array(Q496)。2) 增长曲线长什么样?——CPython list 按 ~1.125 倍渐进增长(倍率随大小递减),append 均摊 O(1);已知长度时 list(it) 一次精确分配优于 append 循环。3) 底层 realloc 行为?——PyMem_Realloc 尽量原地扩展,失败才迁移拷贝;capacity 是「可容纳」,len 是逻辑长度,getsizeof 反映 capacity 而不是 len。4) 生产陷阱?——构建百万级列表用 append 反复 realloc,先 list(range)/推导式;内存敏感场景构建完挤余量;以为 del 元素会缩容(不会,capacity 保留)。
