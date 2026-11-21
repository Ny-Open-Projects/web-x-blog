---
title: [Q1042] CustomBusinessDay 与节假日历
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1042 · CustomBusinessDay 与节假日历

> 难度:★★★★ | 标签:pandas, 时间序列

**问**:国内有调休(周六上班)和法定节假日,怎么生成"真正的工作日"序列算 SLA 时效?

**答**:内置 `bdate_range` 只会跳过周末,处理不了调休。正确姿势是 `CustomBusinessDay`:用 `weekmask` 定义每周哪几天上班(调休的周六把它加进去),`holidays` 列出法定假日,再喂给 `bdate_range(freq=custom)` 或加减日期;更系统的做法是继承 `AbstractHolidayCalendar` 用规则定义节假日,便于按年维护。业务口径要点:调休逻辑每年变,节假日历要做成配置表由专人维护并进版本管理,别把日历硬编码在脚本里。

```python
# file: code/05_数据分析与工程化/q1042_custom_business_day.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    holidays = {"2026-01-01", "2026-01-02", "2026-01-03"}
    workdays = []
    from datetime import date, timedelta
    d = date(2026, 1, 1)
    while len(workdays) < 3:
        if d.weekday() < 5 and d.isoformat() not in holidays:
            workdays.append(d.isoformat())
        d += timedelta(days=1)
    print("前 3 个工作日:", workdays)
else:
    from pandas.tseries.offsets import CustomBusinessDay
    # 1 月 1 日至 3 日放假,1 月 10 日周六调休上班
    cbd = CustomBusinessDay(
        holidays=["2026-01-01", "2026-01-02", "2026-01-03"],
        weekmask="Mon Tue Wed Thu Fri Sat" if False else "Mon Tue Wed Thu Fri",
    )
    days = pd.bdate_range("2026-01-01", periods=3, freq=cbd)
    print(days.date.tolist())
    # 单独演示调休:把 2026-01-10 周六设为工作日
    cbd2 = CustomBusinessDay(weekmask="Mon Tue Wed Thu Fri Sat", holidays=["2026-01-01"])
    d = pd.Timestamp("2026-01-09") + cbd2
    print("周五加一个工作日 ->", d.date, d.day_name())
```

**追问**:
- 追问 1:算两个日期间的有效工作日数?—— 两端都落到工作日后,`len(bdate_range(start, end, freq=cbd))` 或 `(end - start) // cbd`。
- 追问 2:节假日历怎么与数据管道协作?—— 日历做成维度表/dim_date,管道按日历驱动调度,而不是写死日期。
