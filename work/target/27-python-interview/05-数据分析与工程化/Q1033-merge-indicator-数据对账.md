---
title: [Q1033] merge indicator 数据对账
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1033 · merge indicator 数据对账

> 难度:★★★☆ | 标签:pandas, merge, 数据质量

**问**:两张表对不上账,怎么快速定位哪些键只在一侧存在?

**答**:用 `how="outer"` 加 `indicator=True`,结果多出 `_merge` 列,取值 `left_only`/`right_only`/`both`,一次 merge 就能把"左表独有、右表独有、两侧都有"三类分开,再分别 `value_counts` 看对账差异。典型场景:事实表里出现 `left_only` 的维度键说明维度表缺数据(产生孤儿记录),维度表 `right_only` 说明有多余主数据。对账结果建议落盘而不是只打印,方便给上游修复。

```python
# file: code/05_数据分析与工程化/q1033_merge_indicator.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    a = {"k1", "k2", "k3"}
    b = {"k2", "k3", "k4"}
    print("仅左表:", a - b, "仅右表:", b - a, "两侧都有:", a & b)
else:
    orders = pd.DataFrame({"order_id": ["o1", "o2", "o3"], "user_id": ["u1", "u2", "u9"]})
    users = pd.DataFrame({"user_id": ["u1", "u2", "u7"], "level": ["vip", "normal", "vip"]})
    m = orders.merge(users, on="user_id", how="outer", indicator=True)
    print(m, end="\n\n")
    print(m["_merge"].value_counts())
    orphans = m.loc[m["_merge"] == "left_only", "user_id"]
    print("孤儿订单的用户:", orphans.tolist())
```

**追问**:
- 追问 1:全量 outer 对账太大怎么办?—— 先在键级别做集合差再对差集明细展开,或抽样后人工核对。
- 追问 2:indicator 能自定义列名吗?—— `indicator="src"` 会把结果列命名为 src,避免与已有 `_merge` 冲突。
