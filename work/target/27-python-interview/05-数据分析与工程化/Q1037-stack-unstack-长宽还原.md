---
title: [Q1037] stack/unstack 长宽还原
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1037 · stack/unstack 长宽还原

> 难度:★★★☆ | 标签:pandas, 透视

**问**:unstack 和 stack 分别把数据变成什么样?生成的多级列怎么管理?

**答**:`unstack` 把行索引的最内层"旋转"成列索引,长表变宽表;`stack` 是逆操作,把列索引压回行索引。可以传 `level` 指定旋转哪一层、`fill_value` 填充旋转产生的缺失、`dropna=False` 保留全空组合。宽表便于报表和对比,长表便于画图和继续 groupby,两者互转要形成肌肉记忆;转出来的多层列在导出 Excel 前记得拍平,否则表头嵌套且某些工具读不了。

```python
# file: code/05_数据分析与工程化/q1037_stack_unstack.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    rows = [("bj", 1, 10), ("bj", 2, 20), ("sh", 1, 30)]
    wide = {}
    for city, month, v in rows:
        wide[(city, month)] = v
    cities = sorted({c for c, _ in wide})
    months = sorted({m for _, m in wide})
    for c in cities:
        print(c, [wide.get((c, m), None) for m in months])
else:
    long = pd.DataFrame({
        "city": ["bj", "bj", "sh", "sh"],
        "month": [1, 2, 1, 2],
        "sales": [10, 20, 30, 40],
    })
    wide = long.pivot(index="city", columns="month", values="sales")
    print(wide, end="\n\n")
    print(wide.stack(), end="\n\n")
    print(wide.stack().unstack(level="month"))
```

**追问**:
- 追问 1:unstack 后出现 NaN 说明什么?—— 该行列组合在原长表不存在,业务上想补零用 fill_value=0,想保留缺失就别填。
- 追问 2:stack 默认会丢全 NaN 行吗?—— 会,`dropna=True` 是默认行为,审计口径时要显式关掉。
