---
title: [Q1030] ewm 指数加权与 halflife
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1030 · ewm 指数加权与 halflife

> 难度:★★★☆ | 标签:pandas, 时间序列

**问**:移动平均对突发变化反应慢,有没有更跟手的平滑方法?ewm 的参数怎么选?

**答**:指数加权平均 `ewm()` 对近样本给高权重、远样本按指数衰减,响应速度和平滑度可调。三种参数等价互通:`alpha` 直接给衰减系数,`span=n` 约等于 n 期 SMA 的平滑度,`halflife=h` 表示 h 期后权重减半,业务上 halflife 最直观(半衰期 3 天就是 3 天前的样本权重掉一半)。`adjust=True` 用精确加权起点更准,`adjust=False` 是递推形式,常用于在线更新。ewm 不需要窗口长度、天然处理冷启动,组内使用时同样套 transform。

```python
# file: code/05_数据分析与工程化/q1030_ewm_halflife.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [10.0, 11.0, 11.0, 30.0, 12.0]
    alpha = 0.5
    ema = values[0]
    for v in values:
        ema = alpha * v + (1 - alpha) * ema
        print(round(ema, 2), end=" ")
    print("\n标准库递推即 adjust=False 语义")
else:
    s = pd.Series([10, 11, 11, 30, 12], dtype="float64")
    out = pd.DataFrame({
        "raw": s,
        "ewm_span4": s.ewm(span=4, adjust=False).mean().round(2),
        "ewm_hl2": s.ewm(halflife=2).mean().round(2),
        "sma3": s.rolling(3, min_periods=1).mean().round(2),
    })
    print(out)
```

**追问**:
- 追问 1:ewm 能做组内平滑吗?—— 能,`groupby(键)[列].transform(lambda s: s.ewm(halflife=3).mean())`。
- 追问 2:ewm 和 rolling 的本质差异?—— rolling 是等权有限窗口,ewm 是无限窗口指数权重,前者抗离群点传播、后者响应快。
