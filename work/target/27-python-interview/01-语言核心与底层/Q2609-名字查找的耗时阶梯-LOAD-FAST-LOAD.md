---
title: [Q2609] 名字查找的耗时阶梯:LOAD_FAST、LOAD_DEREF、LOAD_GLOBAL 与内建
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2609 · 名字查找的耗时阶梯:LOAD_FAST、LOAD_DEREF、LOAD_GLOBAL 与内建

> 难度:★★★★☆ | 标签:名字查找, 性能实测, 字节码

**问**:局部变量、闭包变量、全局变量、内建函数,访问速度差多少?为什么?

**答**:四层名字的查找机制完全不同:局部变量是 `LOAD_FAST`,直接按编译期定死的槽位下标取数组元素;闭包变量是 `LOAD_DEREF`,解一层 cell 指针;全局变量是 `LOAD_GLOBAL`,要在模块 `__dict__` 里做一次哈希查找;内建名是全局查不到后回退到 builtins 字典再查一次。本机实测(含循环骨架开销):局部与闭包同档约 33-36ns/次,全局与内建同档约 49-51ns/次,热路径上把反复使用的全局名提为局部变量能省约 30%。3.11 的内联缓存会大幅压缩全局与属性查找成本,但「槽位快于字典」的层级关系不变。要点是:这是微优化,先测再改,别为 20ns 牺牲可读性。

```python
# file: code/01_语言核心与底层/q2609_name_lookup_ladder.py
"""名字查找阶梯:局部、闭包、全局、内建的耗时实测。"""
import timeit

N = 200000
x_global = 1234567


def use_local():
    x = x_global                   # 进入局部槽
    total = 0
    for _ in range(N):
        total = x                  # LOAD_FAST
    return total


def use_global():
    total = 0
    for _ in range(N):
        total = x_global           # LOAD_GLOBAL
    return total


def make_closure():
    y = 1234567

    def use_deref():
        total = 0
        for _ in range(N):
            total = y              # LOAD_DEREF
        return total
    return use_deref


def use_builtin():
    total = 0
    for _ in range(N):
        total = len                # LOAD_GLOBAL 未命中,回退 builtins
    return total


if __name__ == "__main__":
    for fn in (use_local, make_closure(), use_global, use_builtin):
        per_iter = timeit.timeit(fn, number=20) / 20 / N * 1e9
        print(f"{fn.__name__:12s} {per_iter:5.0f} ns/次")
```

**追问**:1) 为什么 `LOAD_DEREF` 和 `LOAD_FAST` 几乎一样快?——cell 是编译期确定的固定槽位,解引用只是一次指针跳转,没有哈希查找,所以闭包变量不必刻意「摊平」成局部变量。2) 完整阶梯的排序?——LOAD_FAST ≈ LOAD_DEREF < LOAD_GLOBAL(带 3.11 内联缓存)< LOAD_NAME(类体/顶层);LOAD_ATTR 特化后接近 LOAD_GLOBAL;结论到常数级,算法优先(Q548)。3) 与优化的关系?——循环不变量外提把 LOAD_GLOBAL 提到循环外仍是零成本习惯(Q2367);微基准用 timeit 取 min(Q2093)。4) 生产陷阱?——按「名字查找类型」做架构决策;热路径全局/属性访问不外提;以为 LOAD_DEREF 贵而重构闭包破坏封装。
