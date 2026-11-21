---
title: [Q1568] set vs list 成员检测:实测与阈值
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1568 · set vs list 成员检测:实测与阈值

> 难度:★★★☆☆ | 标签:性能, set, 实测

**问**:成员检测 set 比 list 快多少?什么时候小 list 反而赢?字典 key 视图算 set 吗?

**答**:成员检测复杂度:set/dict 平均 O(1)(哈希定位),list/tuple O(n) 线性扫描。实测规律:n 上千时 list 的 miss 慢 set 两三个数量级;n 小于 10 左右 list 反而更快——常数小、免哈希,「小集合硬转 set」是负优化。三条工程纪律:① set 构造是 O(n),必须摊销——建一次查多次才赚,热循环里反复 set(data) 现造现查是最常见反模式;② 常量集合提为模块级 frozenset;③ dict.keys() 视图成员检测也是 O(1) 且支持集合运算;④ 元素必须可哈希,list 不可直接进 set。选型口诀:少而频改用 list,多而稳定建 set。

```python
# file: code/01_语言核心与底层/q1568_set_vs_list.py
import timeit


def bench(size, reps=2000):
    data = list(range(size))
    needle_in, needle_out = size - 1, -1
    frozen = frozenset(data)
    per_miss = timeit.timeit(lambda: needle_out in data, number=reps) / reps
    per_build = timeit.timeit(lambda: needle_out in set(data), number=reps) / reps
    per_frozen = timeit.timeit(lambda: needle_out in frozen, number=reps) / reps
    per_hit = timeit.timeit(lambda: needle_in in data, number=reps) / reps
    return per_miss, per_build, per_frozen, per_hit


if __name__ == "__main__":
    for size in (8, 100, 5000):
        per_miss, per_build, per_frozen, per_hit = bench(size)
        print("n=%5d: list miss %8.2fus | set built per call %7.2fus | "
              "frozenset ready %6.3fus | list hit %7.2fus"
              % (size, per_miss * 1e6, per_build * 1e6,
                 per_frozen * 1e6, per_hit * 1e6))

    print("结论: 小 n 用 list, 大 n 建一次 set/frozenset 再查")
    print("dict.keys 视图成员检测也是 O(1):", "b" in {"a": 1, "b": 2}.keys())
```

**追问**:1) in 对 str 子串判断也是哈希吗?——不是,str 的 in 是子串搜索(带优化的近似 O(nm)),与容器成员检测是两套算法;别把「in 快」一概而论。2) 怎么实测?——timeit 取 min(Q401 官方口径),同一进程多轮;阈值经验:n 小(<10)list 常数更小,大集合 set 摊销赢;构造 set 的成本要摊进总账。3) 算法差异?——list O(n) 线性比较;set O(1) 哈希探测;str 子串搜索有 Crochemore-Perrin 类混合算法;三种「in」不可互相推论。4) 生产陷阱?——循环体内反复建 set(应提到循环外);小集合换 set 反而慢;把 `"a" in choices(str)` 当成员检测用,子串误命中("at" in "cat")。
