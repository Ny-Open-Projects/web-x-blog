---
title: [Q1045] Period 与多级频率换算
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1045 · Period 与多级频率换算

> 难度:★★★☆ | 标签:pandas, 时间序列

**问**:月度账期和日明细混在一张表里,用 Timestamp 还是 Period?怎么互转?

**答**:Period 表示"一段区间"(月、季),账期、月度 KPI 这类口径用 PeriodIndex 更语义化,天然不会把 2 月当成 28 号的具体时刻。互转:`Timestamp.to_period("M")` 把时刻归入账期,`Period.to_timestamp(how="start"/"end")` 还原成期初/期末时刻;`asfreq` 能跨频率换算,比如季度转月取期初月。聚合时最稳的做法是先 `index.to_period("M")` 再 groupby,避免月末日 resample 标签漂移;混用时明确"哪一侧是账期口径",不要拿 Timestamp 直接和 Period 相等比较。

```python
# file: code/05_数据分析与工程化/q1045_period_freq.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:日期归入账期")
    from datetime import date
    for d in (date(2026, 2, 20), date(2026, 3, 1)):
        print(d, "->", f"{d.year}-{d.month:02d}")
else:
    q = pd.period_range("2026Q1", periods=4, freq="Q")
    print("季度:", q.tolist())
    print("季度 -> 期初月:", q.asfreq("M", how="start").tolist())
    print("Q1 期末时刻:", q[0].to_timestamp(how="end"))
    ts = pd.Timestamp("2026-03-15")
    print("时刻 -> 月账期:", ts.to_period("M"), "季账期:", ts.to_period("Q"))
```

**追问**:
- 追问 1:to_timestamp 的 how 参数决定什么?—— how="start" 取期初、"end" 取期末,月末对账时别选错。
- 追问 2:Period 和 resample 怎么配合?—— resample 输出 DatetimeIndex,再 `.to_period()` 就得到账期索引,两者可互转。
