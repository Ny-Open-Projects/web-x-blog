---
title: [Q1028] expanding 累计指标与阈值监控
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1028 · expanding 累计指标与阈值监控

> 难度:★★☆☆ | 标签:pandas, 时间序列

**问**:运营要"从上线到当前的累计 GMV"和"历史新高告警",这类逐日累计口径怎么算?

**答**:累计口径用 `expanding()`:它是一个左端固定、右端随时间增长的特殊窗口,`expanding().sum()/.mean()/.max()` 分别给累计和、累计均值、历史最高。历史新高检测可以用 `s >= s.cummax()` 或 `expanding().max()` 对比;阈值监控则把累计序列与预警线做比较并输出触发时点。注意累计序列对早期数据极其敏感,起始点选择(灰度期是否计入)本身就是口径决策,要在指标文档里写死。

```python
# file: code/05_数据分析与工程化/q1028_expanding_metrics.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [10, 12, 9, 15]
    run_sum = run_max = 0
    for i, v in enumerate(values):
        run_sum += v
        run_max = max(run_max, v)
        print(f"day{i} 累计 {run_sum} 历史最高 {run_max} 是否新高 {v == run_max}")
else:
    s = pd.Series([10, 12, 9, 15], index=pd.date_range("2026-01-01", periods=4, freq="D"))
    out = pd.DataFrame({
        "gmv": s,
        "cum_gmv": s.expanding().sum(),
        "cum_avg": s.expanding().mean().round(2),
        "hist_max": s.expanding().max(),
    })
    out["is_record"] = s >= out["hist_max"]
    print(out)
    # CUSUM 累积偏移,常用于漂移监控
    print("cusum:", s.sub(s.mean()).cumsum().round(2).tolist())
```

**追问**:
- 追问 1:累计指标想按月重置怎么写?—— 先 `groupby(年月)` 再 expanding,或在分组键里加入账期。
- 追问 2:expanding 和 cumsum 的区别?—— cumsum 只有求和;expanding 是窗口对象,能套任意聚合函数。
