---
title: [Q1043] between_time/at_time 时段切片
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1043 · between_time/at_time 时段切片

> 难度:★★☆☆ | 标签:pandas, 时间序列

**问**:想只看每天 9 点到 18 点的数据,或者晚上 22 点到次日 2 点的夜间流量,怎么做?

**答**:DatetimeIndex 数据用 `between_time("09:00", "18:00")` 按一天内时刻过滤,`at_time("12:00")` 取精确时刻,与日期无关、只看钟面时间,非常适合营业时段和值班时段分析。跨零点时段直接写 `between_time("22:00", "02:00")`,pandas 会理解为跨夜的区间。前提是索引为 DatetimeIndex,若是普通列先 `set_index` 或用 `.dt` 配合布尔条件;时区要先归一,否则钟面时间在 DST 期会有歧义。

```python
# file: code/05_数据分析与工程化/q1043_between_time.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import datetime
    stamps = [datetime(2026, 1, 1, h) for h in (8, 10, 12, 23, 1)]
    for t in stamps:
        ok = 9 <= t.hour <= 18
        print(t.strftime("%H:%M"), "营业时段" if ok else "非营业时段")
else:
    s = pd.Series(range(24), index=pd.date_range("2026-01-01", periods=24, freq="h"))
    print("营业时段行数:", len(s.between_time("09:00", "18:00")))
    print(s.at_time("12:00"), end="\n\n")
    print("跨零点 22 点到次日 2 点:", s.between_time("22:00", "02:00").index.strftime("%H:%M").tolist())
```

**追问**:
- 追问 1:between_time 包含端点吗?—— 两侧默认闭区间,旧版可用 include_start/include_end 调整,新版本建议比较后自行取舍。
- 追问 2:和 between 的区别?—— between 比较的是完整时间戳,之间/between_time 只比较一天内的时刻部分。
