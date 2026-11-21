---
title: [Q1029] 组内滚动 groupby 与 rolling 连用
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1029 · 组内滚动 groupby 与 rolling 连用

> 难度:★★★★ | 标签:pandas, groupby

**问**:要给每个城市算自己的 7 日移动平均,直接 `df.groupby("city").rolling(7)` 会得到什么结构?怎么对齐回原表?

**答**:groupby 加 rolling 会按组独立滑动,结果索引变成"分组键 + 时间"的双层 MultiIndex,直接赋值回原表会报索引不匹配。两种工程写法:一是链式结果 `reset_index()` 拍平成新表;二是 `groupby(键)[列].transform(lambda s: s.rolling(n).mean())`,transform 返回与原表同长同序的序列,可直接赋新列。前提都是先把数据按时间排好,组内 rolling 不会替你排序。

```python
# file: code/05_数据分析与工程化/q1029_groupby_rolling.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", 10), ("bj", 12), ("bj", 11), ("sh", 20), ("sh", 22), ("sh", 21)]
    g = defaultdict(list)
    for city, t in rows:
        g[city].append(t)
    for city, values in g.items():
        ma = [sum(values[max(0, i - 1):i + 1]) / len(values[max(0, i - 1):i + 1]) for i in range(len(values))]
        print(city, values, "ma2:", [round(x, 2) for x in ma])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "sh", "sh", "sh"],
        "t": [10, 12, 11, 20, 22, 21],
    })
    # 写法一:链式 rolling 后拍平
    chained = df.groupby("city")["t"].rolling(2, min_periods=1).mean().reset_index()
    print(chained, end="\n\n")
    # 写法二:transform 对齐回原表,报表常用
    df["ma2"] = df.groupby("city")["t"].transform(lambda s: s.rolling(2, min_periods=1).mean())
    print(df)
```

**追问**:
- 追问 1:transform 里能直接写 `s.rolling(7).mean()` 吗?—— 能,lambda 拿到的是每组独立 Series,滚动在组内完成。
- 追问 2:组内时间窗呢?—— 需要把时间设为索引后 `groupby(键).resample("7D")`,或组内 rolling("7D") 要求每组都是 DatetimeIndex,一般先 set_index 再分组。
