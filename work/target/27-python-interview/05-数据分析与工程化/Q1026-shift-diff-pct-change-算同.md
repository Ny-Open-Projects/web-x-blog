---
title: [Q1026] shift/diff/pct_change 算同比环比
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1026 · shift/diff/pct_change 算同比环比

> 难度:★★★☆ | 标签:pandas, 时间序列

**问**:日报要算指标的环比和同比,用 pandas 怎么实现?最容易踩的坑是什么?

**答**:环比用 `pct_change()`(等价于 `s / s.shift(1) - 1`),同比用 `s / s.shift(周期数) - 1`,月度数据周期是 12、周报表是 52。最大的坑是数据缺口:序列只要缺一期,`shift(12)` 错的就是位置而不是真正的"去年同期",所以同比前必须先把索引 reindex 成完整日历轴;另一个坑是首期/同比基期缺失产生的 NaN 和除零(`fill_method` 与 `fill_value` 按需处理)。工程上建议同比环比统一封装成一个函数,口径只写一遍。

```python
# file: code/05_数据分析与工程化/q1026_shift_yoy_mom.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [100, 110, 105, 120, 130]
    for i, v in enumerate(values):
        mom = v / values[i - 1] - 1 if i > 0 else None
        print(f"day{i} 值 {v} 环比 {mom if mom is None else f'{mom:.1%}'}")
else:
    s = pd.Series(
        [100, 110, 105, 120, 130],
        index=pd.date_range("2026-01-01", periods=5, freq="D"),
        name="gmv",
    )
    mom = s.pct_change()                 # 环比
    wow = s / s.shift(7) - 1             # 周同比思路,月度数据用 shift(12)
    diff = s.diff()                      # 绝对增量
    out = pd.DataFrame({"gmv": s, "mom": mom, "wow": wow, "delta": diff})
    print(out)
    # 有缺日时先补齐日历轴再算,否则 shift 的是位置不是时间
    s2 = s.drop(s.index[1])
    fixed = s2.reindex(pd.date_range(s2.index[0], s2.index[-1], freq="D"))
    print("缺日时 pct_change 错位:", fixed.pct_change().tolist())
```

**追问**:
- 追问 1:为什么同比前必须 reindex?—— shift 按位置移动,缺一期时 shift(12) 拿到的是第 11 期前的值,同口径比较就错了。
- 追问 2:基期为 0 或负数怎么办?—— 环比无意义,改算差值 diff,或声明为 NaN 而不是 inf。
