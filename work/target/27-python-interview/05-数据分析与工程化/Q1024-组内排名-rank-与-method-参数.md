---
title: [Q1024] 组内排名 rank 与 method 参数
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1024 · 组内排名 rank 与 method 参数

> 难度:★★★☆ | 标签:pandas, groupby

**问**:需求是"每个城市销量前 3 的商品",组内排名你会怎么写?并列名次怎么处理?

**答**:用 `groupby(键)[值].rank()`,配 `ascending=False` 降序。关键是 `method` 参数:`average` 并列取平均(默认)、`min` 并列取最小名次(竞赛排名)、`first` 按出现顺序强分先后、`dense` 并列占一个名次且不跳号。业务上"并列同分"和"先到先得"是两种口径,选错 method 会直接影响 Top-N 名单;pct=True 还能拿到百分位排名。排名后再 `rank <= 3` 过滤即得各组前三。

```python
# file: code/05_数据分析与工程化/q1024_group_rank.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", "A", 100), ("bj", "B", 100), ("bj", "C", 80), ("sh", "A", 90)]
    g = defaultdict(list)
    for city, product, amount in rows:
        g[city].append((amount, product))
    for city, items in g.items():
        items.sort(key=lambda x: -x[0])
        print(city, [(p, i + 1) for i, (a, p) in enumerate(items)])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "sh"],
        "product": ["A", "B", "C", "A"],
        "amount": [100, 100, 80, 90],
    })
    df["rank_dense"] = df.groupby("city")["amount"].rank(method="dense", ascending=False)
    df["rank_first"] = df.groupby("city")["amount"].rank(method="first", ascending=False)
    df["rank_min"] = df.groupby("city")["amount"].rank(method="min", ascending=False)
    df["rank_pct"] = df.groupby("city")["amount"].rank(pct=True)
    print(df)
    top3 = df[df.groupby("city")["amount"].rank(method="first", ascending=False) <= 3]
    print(top3[["city", "product", "amount"]])
```

**追问**:
- 追问 1:并列时想严格分先后按什么排?—— `method="first"`,内部按原表顺序;要先按二级指标再排,先 sort_values 再 rank。
- 追问 2:rank 和 nlargest 的取舍?—— 每组取少量 Top 用 `groupby.head`/`nlargest` 更省,需要完整名次列时用 rank。
