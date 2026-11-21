---
title: [Q1027] rolling 时间偏移窗口与 min_periods
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1027 · rolling 时间偏移窗口与 min_periods

> 难度:★★★☆ | 标签:pandas, 时间序列

**问**:rolling(7) 和 rolling("7D") 有什么区别?min_periods 什么时候必须配?

**答**:固定行数窗口 `rolling(7)` 按行数取窗口,序列缺日时窗口实际跨度会超过 7 天,口径失真;时间偏移窗口 `rolling("7D")` 要求 DatetimeIndex,按"含当天的过去 7 个自然日"取数,缺日时窗口仍是真实时间跨度,是业务报表的正确选择。`min_periods` 控制窗口最少需要多少个观测才输出:默认等于窗口大小,序列头部会全是 NaN;冷启动场景配 `min_periods=1` 可以从第一天就出数,但要明白前面的值方差很大。时间窗口默认区间是右闭,`closed` 可改。

```python
# file: code/05_数据分析与工程化/q1027_rolling_time_window.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:3 天移动平均,缺日不补")
    days = ["01-01", "01-03", "01-04", "01-05"]
    values = [1, 2, 3, 4]
    for i in range(len(values)):
        lo = max(0, i - 2)
        window = values[lo:i + 1]
        print(days[i], window, sum(window) / len(window))
else:
    idx = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-04", "2026-01-05"])
    s = pd.Series([1.0, 2.0, 3.0, 4.0], index=idx)
    print(s.rolling(3, min_periods=1).mean(), end="\n\n")
    # 时间窗:即使 01-02 缺失,窗口仍是自然 3 天跨度
    print(s.rolling("3D", min_periods=1).mean())
```

**追问**:
- 追问 1:rolling("7D") 能算过去 7 个工作日吗?—— 不能,自然日窗口包含周末,工作日口径要先按 bdate_range 重采样或过滤。
- 追问 2:窗口里想用加权平均呢?—— 用 `rolling(...).apply(自定义函数, raw=True)`,性能不如内置均值,注意冷启动 NaN。
