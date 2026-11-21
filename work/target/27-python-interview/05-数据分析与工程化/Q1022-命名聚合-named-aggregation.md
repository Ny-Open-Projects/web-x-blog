---
title: [Q1022] 命名聚合 named aggregation
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1022 · 命名聚合 named aggregation

> 难度:★★☆☆ | 标签:pandas, groupby

**问**:写 `df.groupby("region").agg(("amount", "sum"))` 这类代码时列名经常变成自动拼接的乱码,怎么优雅解决?

**答**:用命名聚合:`agg(新列名=("列名", "函数"))`,输出列名完全由你控制,不再出现 `amount_sum` 这种隐式拼接,也不再依赖字典写法在 Python 3.8+ 下的兼容问题。它还允许对同一列取多个指标、对不同列取不同指标混在同一个 agg 里,可读性远高于传统写法。命名聚合是 pandas 0.25+ 的官方推荐,代码评审时可以当作团队规范固定下来。

```python
# file: code/05_数据分析与工程化/q1022_named_aggregation.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("华东", 10, "o1"), ("华东", 20, "o2"), ("华北", 40, "o3")]
    total, cnt, mx = defaultdict(float), defaultdict(int), defaultdict(lambda: float("-inf"))
    for region, amount, _ in rows:
        total[region] += amount
        cnt[region] += 1
        mx[region] = max(mx[region], amount)
    for region in sorted(total):
        print(region, total[region], total[region] / cnt[region], cnt[region], mx[region])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北", "华北"],
        "order_id": ["o1", "o2", "o3", "o4"],
        "amount": [10, 20, 40, 50],
    })
    out = df.groupby("region").agg(
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
        n_orders=("order_id", "count"),
        max_amount=("amount", "max"),
    )
    print(out.reset_index())
```

**追问**:
- 追问 1:命名聚合和 `NamedAgg` 什么关系?—— `total=("amount", "sum")` 是 `total=pd.NamedAgg("amount", "sum")` 的语法糖。
- 追问 2:聚合结果列顺序由什么决定?—— 由 agg 里关键字参数的书写顺序决定,正好符合"写什么顺序出什么列"的直觉。
