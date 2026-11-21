---
title: [Q311] pandas 两大核心数据结构 Series 与 DataFrame
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q311 · pandas 两大核心数据结构 Series 与 DataFrame

> 难度:★☆☆ | 标签:pandas, Series, DataFrame

**问**:pandas 的 Series 和 DataFrame 分别是什么?它们和 numpy ndarray 的关系是什么?

**答**:Series 是带索引的一维数组,由 values(ndarray)+ index(标签)+ dtype 组成;DataFrame 是共享同一个 index 的多个 Series 的集合,本质是"带行标签和列标签的二维表"。两者底层都基于 numpy ndarray,因此能享受向量化计算;但多出的 index 层使得对齐运算(alignment)成为 pandas 区别于 numpy 的核心特性。理解"DataFrame 是 Series 的容器"这一模型,是理解 loc/groupby/merge 行为的基础。

```python
# file: code/05_数据分析与工程化/q311_series_dataframe.py
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="score")
    df = pd.DataFrame({
        "city": ["BJ", "SH", "SZ"],
        "score": [88, 92, 79],
    }, index=["r1", "r2", "r3"])
    print(type(s.values), s.dtype, s.index.tolist())
    print(df.shape, df.columns.tolist(), df.dtypes.to_dict())
    print(df["score"])          # 取出一列就是 Series

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        # 标准库降级:Series 概念上就是 值 + 标签索引 的组合
        series = dict(zip(["a", "b", "c"], [10, 20, 30]))
        dataframe = {"city": ["BJ", "SH", "SZ"], "score": [88, 92, 79]}
        print("Series-like:", series)
        print("DataFrame-like columns:", {k: len(v) for k, v in dataframe.items()})
```

**追问**:
- DataFrame 的列可以类型不同吗?可以,每列是独立的 Series,dtype 可以互不相同,这正是它区别于二维 ndarray 的地方。
- index 对齐在运算中怎么体现?——两 Series 相加按标签对齐,不重叠的标签产生 NaN;不想对齐就 `.values` 运算或先对齐索引。
- DataFrame 的本质模型是什么?——共享 index 的多个 Series 容器;理解这个才能解释为什么列操作快、为什么 loc 是标签语义。
- dtype 查看与转换的入口?——`df.dtypes` 总览、`astype`/`to_numeric`/`to_datetime` 转换;读入数据先看 dtype 是纪律。
