---
title: [Q1021] groupby 多键聚合与结果层级还原
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1021 · groupby 多键聚合与结果层级还原

> 难度:★★★☆ | 标签:pandas, groupby

**问**:多列 groupby 之后结果索引变成了 MultiIndex,报表要一维平铺,你一般怎么处理?有哪些坑?

**答**:多键 groupby 默认 `as_index=True`,分组键会变成行上的 MultiIndex。报表导出场景推荐直接 `as_index=False`,让分组键回到普通列,一步到位;已经拿到 MultiIndex 结果时用 `reset_index()` 事后还原。两个常见坑:一是分组键顺序决定结果排序与层级结构,`sort=False` 可以保留原始出现顺序;二是分组键为 category 类型时,groupby 默认会输出所有类别组合(包括空组),要用 `observed=True` 只输出实际出现的组合,否则笛卡尔组合会让结果行数暴涨。

```python
# file: code/05_数据分析与工程化/q1021_multikey_groupby.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    # 标准库降级:多键分组求和,输出平铺行
    from collections import defaultdict
    rows = [("华东", "A", 10), ("华东", "B", 20), ("华东", "A", 5), ("华北", "A", 40)]
    agg = defaultdict(float)
    for region, product, amount in rows:
        agg[(region, product)] += amount
    for key in sorted(agg):
        print(key[0], key[1], agg[key])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华东", "华北", "华北"],
        "product": ["A", "A", "B", "A", "B"],
        "amount": [10, 20, 5, 40, 50],
    })
    # 默认 as_index=True,分组键进 MultiIndex
    multi = df.groupby(["region", "product"])["amount"].sum()
    print(multi, end="\n\n")
    # 平铺方案一:as_index=False,键回到普通列,报表场景首选
    print(df.groupby(["region", "product"], as_index=False)["amount"].sum(), end="\n\n")
    # 平铺方案二:事后 reset_index 还原
    print(multi.reset_index())
```

**追问**:
- 追问 1:聚合后列名和顺序不规范怎么办?—— 用下一题的命名聚合,或聚合完立刻 `rename` 成业务列名。
- 追问 2:聚合结果行数远超预期像笛卡尔积?—— 先查键列是否有脏值,再用 `drop_duplicates` 检查每键唯一性,category 键记得加 `observed=True`。
