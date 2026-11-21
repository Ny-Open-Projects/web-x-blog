---
title: [Q2534] 字段级 diff 的分布画像
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2534 · 字段级 diff 的分布画像

> 难度:★★★★ | 标签:分布漂移, 数据画像

**问**:两天行数一模一样、守恒也对,就一定安全吗?

**答**:不安全,行数 diff 抓不到"字段悄悄变空"。给每列建画像三件套:空值率、基数、数值均值,跨期比较并设容忍带,实测 amount 列空值率从 2% 飙到 40%、基数从 98 掉到 60,均值几乎没动,行数守恒完全无感知,画像层直接标 DRIFT;uid 和 city 两列无漂移标 OK。这类事故的典型来源是上游把某个错误吞成了 NULL,或枚举值悄悄合并,守恒和行数都对,数已经坏了。所以门禁是三层递进:行数守恒答"行去哪了",行级 diff 答"哪些行变了",列画像答"分布变没变",缺一层就有盲区。容忍带按列业务属性定:金额空值率零容忍,自由文本基数波动放宽。画像要落历史,连续多期缓慢漂移比单期跳变更值得警惕。

```python
# file: code/05_数据分析与工程化/q2534_field_profile_drift.py
"""字段级 diff 的分布画像: 行数守恒也要查分布漂移"""

try:
    import pandas as pd
except ImportError:
    pd = None

N = 100
TOLERANCE = 0.05      # 空值率漂移容忍 5 个百分点


def make_rows(null_rule):
    rows = []
    for i in range(N):
        rows.append({
            "uid": f"u{i:03d}",
            "city": ["北京", "上海", "广州", "深圳", "杭州"][i % 5],
            "amount": None if null_rule(i) else 100.0 + i,
        })
    return rows


def profile(rows):
    cols = {}
    for f in rows[0]:
        vals = [r[f] for r in rows]
        nulls = sum(1 for v in vals if v is None)
        numeric = [v for v in vals if isinstance(v, (int, float))]
        cols[f] = {
            "null_rate": nulls / len(vals),
            "distinct": len({v for v in vals if v is not None}),
            "mean": sum(numeric) / len(numeric) if numeric else None,
        }
    return cols


if __name__ == "__main__":
    p1 = profile(make_rows(lambda i: i % 50 == 0))     # 昨日: amount 空值率 2%
    p2 = profile(make_rows(lambda i: (i % 5) < 2))     # 今日: amount 空值率 40%
    print(f"两日行数一致: {N} == {N}, 守恒断言无感知")
    for f in p1:
        d_null = abs(p2[f]["null_rate"] - p1[f]["null_rate"])
        verdict = "DRIFT" if d_null > TOLERANCE else "OK"
        print(f"  [{verdict}] {f}: 空值率 {p1[f]['null_rate']:.0%} -> {p2[f]['null_rate']:.0%}, "
              f"基数 {p1[f]['distinct']} -> {p2[f]['distinct']}, 均值 {p1[f]['mean'] and round(p1[f]['mean'], 1)}"
              f" -> {p2[f]['mean'] and round(p2[f]['mean'], 1)}")
    assert p2["amount"]["null_rate"] - p1["amount"]["null_rate"] > TOLERANCE
    if pd is not None:
        df2 = pd.DataFrame(make_rows(lambda i: (i % 5) < 2))
        print("pandas 视角: 空值率", df2.isna().mean().round(2).to_dict())
    print("要点: 行数 diff 抓不到'字段悄悄变空', 列画像把空值率 基数 均值三件套纳入门禁")
```

**追问**:
- 追问 1:基数骤降一定是坏事吗?—— 不一定,枚举合并是正常演进,但必须有人确认;画像只负责把变化顶到明面上。
- 追问 2:数值列还要看什么?—— 分位数比均值抗重尾,最小最大值能抓单位错误(分与元),直方图相似度可量化整体漂移。
