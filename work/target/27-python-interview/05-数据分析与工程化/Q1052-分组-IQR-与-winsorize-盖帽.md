---
title: [Q1052] 分组 IQR 与 winsorize 盖帽
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1052 · 分组 IQR 与 winsorize 盖帽

> 难度:★★★☆ | 标签:统计, 异常检测

**问**:整体 IQR 会把小城市的正常高值误杀,怎么按组做异常边界?删除和盖帽怎么选?

**答**:分组 IQR 用 `groupby(组键)[值].transform(lambda s: s.quantile(0.25/0.75))` 把组内 Q1/Q3 广播回原表,再算各组自己的上下须,边界随组自适应,避免大城市小城市共用一把尺。处理方式上,盖帽(winsorize,`clip` 到上下须)优于删除:保留样本量与排序结构,下游分组统计不失真;删除只用于明显是录入错误的点。落地规范:原值列保留、新增 `*_capped` 列与审计标记列,报表口径声明用的是哪个版本。

```python
# file: code/05_数据分析与工程化/q1052_group_iqr_winsorize.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", 10), ("bj", 12), ("bj", 11), ("bj", 500), ("sh", 8), ("sh", 9), ("sh", 40)]
    g = defaultdict(list)
    for city, v in rows:
        g[city].append(v)
    for city, values in g.items():
        s = sorted(values)

        def q(p):
            i = p * (len(s) - 1)
            lo, hi = int(i), min(int(i) + 1, len(s) - 1)
            return s[lo] + (s[hi] - s[lo]) * (i - lo)
        q1, q3 = q(0.25), q(0.75)
        iqr = q3 - q1
        low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        print(city, "边界", round(low, 2), round(high, 2), "盖帽后", [min(max(v, low), high) for v in values])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "bj", "sh", "sh", "sh"],
        "amount": [10, 12, 11, 500, 8, 9, 40],
    })
    q1 = df.groupby("city")["amount"].transform(lambda s: s.quantile(0.25))
    q3 = df.groupby("city")["amount"].transform(lambda s: s.quantile(0.75))
    iqr = q3 - q1
    df["amount_capped"] = df["amount"].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
    print(df)
```

**追问**:
- 追问 1:分组只有一个样本点时 IQR 是什么?—— Q1=Q3=值本身,IQR 为 0,边界退化为该值,需要按组设最小样本量再启用盖帽。
- 追问 2:winsorize 影响下游什么统计量?—— 压缩方差与极值敏感度,均值更稳但尾部分析失效,极端值研究要回到原列。
