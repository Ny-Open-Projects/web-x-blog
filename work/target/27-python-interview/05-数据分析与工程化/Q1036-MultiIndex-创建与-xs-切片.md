---
title: [Q1036] MultiIndex 创建与 xs 切片
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1036 · MultiIndex 创建与 xs 切片

> 难度:★★★☆ | 标签:pandas, 索引

**问**:拿到一个双层索引的 DataFrame,想取"华东下所有产品"或"华东-产品 A"这一格,xs 怎么用?

**答**:MultiIndex 常由 `set_index([列1, 列2])` 或 groupby 多键产生。`xs` 是按层取子集的利器:`df.xs("华东", level="region")` 拿某层的一个值的所有行,`df.xs(("华东", "A"))` 可以一次传多层元组,`drop_level=False` 保留被取走的那一层。xs 与布尔掩码相比写法更短且语义清晰,但它一次只能对每层给一个具体值;要取列表集合还是得 `.loc[滑片/掩码]` 或 `IndexSlice`。

```python
# file: code/05_数据分析与工程化/q1036_multiindex_xs.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    rows = {("华东", "A"): 10, ("华东", "B"): 20, ("华北", "A"): 30}
    print("华东层:", {k: v for k, v in rows.items() if k[0] == "华东"})
    print("华东-A:", rows.get(("华东", "A")))
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北"],
        "product": ["A", "B", "A"],
        "amount": [10, 20, 30],
    })
    mi = df.set_index(["region", "product"]).sort_index()
    print(mi, end="\n\n")
    print(mi.xs("华东", level="region"), end="\n\n")
    print(mi.xs(("华东", "B")), end="\n\n")
    print(mi.xs("A", level="product", drop_level=False))
```

**追问**:
- 追问 1:想一次取多层中的多个值呢?—— `mi.loc[pd.IndexSlice[:, ["A", "B"]], :]` 或布尔掩码。
- 追问 2:xs 能取列层吗?—— 能,`axis=1` 时对列索引切片,透视表场景常用。
