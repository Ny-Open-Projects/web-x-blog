---
title: [Q1048] resample 自然周口径 label 与 closed
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1048 · resample 自然周口径 label 与 closed

> 难度:★★★★ | 标签:pandas, 重采样

**问**:周报口径是"周一为一周起点",但 resample 默认周口径是周日结束,怎么改?label 和 closed 到底控制什么?

**答**:resample 频率 `W-SUN` 表示"以周日为边界切周"(默认),要"周一起点"用 `W-MON`,或者直接按账期 `groupby(index.to_period("W-SUN"))`。两个参数:`closed` 决定边界值归左桶还是右桶,`label` 决定桶打的时间标签是边界左端还是右端;日数据聚合到周时 closed 影响不大,但 label 决定报表显示的是"周起点日期"还是"周结束日期",口径混乱是周对不上的头号原因。多指标周报建议把口径(起点星期几、标签端)写成配置,所有报表共用。

```python
# file: code/05_数据分析与工程化/q1048_resample_week.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import date
    values = {date(2026, 1, 5): 10, date(2026, 1, 11): 20, date(2026, 1, 12): 30}
    # 周一起点口径:01-05 属于 01-05 那周,01-12 起新周
    print("01-05 与 01-11 同周,01-12 开新周")
    print({str(k): v for k, v in values.items()})
else:
    s = pd.Series(
        range(1, 15),
        index=pd.date_range("2026-01-05", periods=14, freq="D"),  # 01-05 是周一
    )
    print("默认 W-SUN 标签在周日:")
    print(s.resample("W-SUN").sum(), end="\n\n")
    print("周一起点,label=left 标签在周一:")
    print(s.resample("W-MON", label="left").sum())
```

**追问**:
- 追问 1:closed 什么时候真的影响结果?—— 聚合粒度高于数据粒度时有共享边界,如 3 小时桶聚合秒级数据,`closed="left"` 让 00:00 归前桶。
- 追问 2:周口径和账期口径冲突怎么办?—— 以业务定义为准,通常账期优先,周报拆到账期内展示而不是另立口径。
