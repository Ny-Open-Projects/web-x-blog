---
title: [Q1049] 月末口径 MonthEnd 与 BusinessMonthEnd
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1049 · 月末口径 MonthEnd 与 BusinessMonthEnd

> 难度:★★★☆ | 标签:pandas, 重采样

**问**:月报取"月末快照",2 月取到 3 月 1 日的数据是怎么回事?自然月末和工作日月末怎么选?

**答**:月末是滚动的(28/29/30/31),用 `pd.offsets.MonthEnd(0)` 把任意时间戳归到当月最后一个自然日,`BMonthEnd(0)` 归到最后一个工作日,前者用于账期快照、后者用于交易口径。resample 频率里 `ME` 是自然月末、`BME` 是工作日月末(旧版本写作 `M`/`BM`)。经典坑:拿"月初加一个月"当月末会跳过短月,2 月、4 月全错,必须用 offset 归位;跨月数据别用 `between("02-01", "02-28")` 手写边界,让日历函数负责边界。

```python
# file: code/05_数据分析与工程化/q1049_month_end.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from calendar import monthrange
    from datetime import date
    for y, m in ((2026, 2), (2026, 4)):
        last = monthrange(y, m)[1]
        print(f"{y}-{m:02d} 自然月末 {last} 日")
else:
    daily = pd.Series(
        range(10),
        index=pd.date_range("2026-02-20", periods=10, freq="D"),
    )
    print("按自然月聚合:", daily.groupby(daily.index.to_period("M")).sum().to_dict())
    ts = pd.Timestamp("2026-02-05")
    print("自然月末:", ts + pd.offsets.MonthEnd(0).normalize())
    print("工作日月末:", ts + pd.offsets.BMonthEnd(0).normalize())
    print("resample ME:", daily.resample("ME").sum().to_dict())
```

**追问**:
- 追问 1:快照要"月末最后一个工作日的收盘值"怎么取?—— 用 BMonthEnd 定位日期后再按该日期过滤明细,而不是聚合。
- 追问 2:SemiMonthEnd 什么场景用?—— 半月结账(15 号/月末)的账期切分,双周报也常用它对齐。
