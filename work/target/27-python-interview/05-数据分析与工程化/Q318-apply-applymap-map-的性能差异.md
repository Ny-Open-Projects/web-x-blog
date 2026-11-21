---
title: [Q318] apply / applymap / map 的性能差异
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q318 · apply / applymap / map 的性能差异

> 难度:★★★ | 标签:pandas, 性能

**问**:apply、applymap、map 分别作用于什么?为什么说它们慢?

**答**:map 是 Series 方法,对每个元素应用函数或做字典映射;applymap(新版本 DataFrame.map)对 DataFrame 的每个元素应用函数;apply 较通用,Series 上逐元素、DataFrame 上按行或按列。它们慢的根源是逐元素走 Python 回调,无法利用 numpy 向量化,数据量大时比向量化写法慢一到两个数量级。工程建议:能用向量化运算、np.where、字典 map、cut 分箱解决的,绝不手写 apply;apply 只留给它处理真正无法向量化的复杂逻辑。

```python
# file: code/05_数据分析与工程化/q318_apply_map_perf.py
try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    s = pd.Series([1, 2, 3, 4])
    print(s.map(lambda x: x * 10).tolist())          # 逐元素
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    print(df.applymap(lambda x: x + 1).to_dict())    # 全表逐元素
    print(df.apply("sum", axis=0).to_dict())         # 按列
    # 向量化替代方案对比
    big = pd.Series(np.arange(1_000_000))
    import time
    t0 = time.perf_counter()
    big.map(lambda x: x * 2)
    t1 = time.perf_counter()
    big * 2
    t2 = time.perf_counter()
    print(f"map: {t1 - t0:.3f}s  vectorized: {t2 - t1:.4f}s")

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        s = [1, 2, 3, 4]
        print([x * 10 for x in s])                   # 逐元素映射
        print([sum(col) for col in zip(s, s)])       # 按列聚合
```

**追问**:
- apply(axis=1) 有多慢?每行都会构造一个 Series 对象,开销巨大;逐行逻辑优先考虑拆成向量化列运算或用 numpy 的广播解决。
- 元素级映射的最佳替代?——`Series.map(dict)` 走 C 层哈希,比 apply 匿名函数快一个数量级;map 不上的键产生 NaN,注意 fillna。
- apply 真正适合的场景?——确实无法向量化的复杂行逻辑(多列协同计算)、或作为 groupby 的自定义聚合;写入前先试 np.where/map。
- 怎么量化慢在哪?——%timeit 对比向量化与 apply 两版;没有对比数据,评审时说服力为零。
