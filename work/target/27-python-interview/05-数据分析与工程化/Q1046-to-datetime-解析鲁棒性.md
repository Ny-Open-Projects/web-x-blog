---
title: [Q1046] to_datetime 解析鲁棒性
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1046 · to_datetime 解析鲁棒性

> 难度:★★★☆ | 标签:pandas, 时间序列

**问**:上游 CSV 的日期格式五花八门还混着脏数据,解析怎么写得既快又稳?

**答**:三条原则:显式、可审计、快。显式指尽量传 `format`(如 `"%Y/%m/%d"`),避免 pandas 猜测造成 `05-01-2026` 被当 5 月 1 日的歧义,来源约定日优先就加 `dayfirst=True`;可审计指用 `errors="coerce"` 把脏值变 NaT,再统计 NaT 行落审计表,而不是让异常中断整条管道;快指 format 显式后走快速路径,千万行级别差距明显。混合时区字符串加 `utc=True` 统一;多格式混杂时按格式分组分别解析再 concat。

```python
# file: code/05_数据分析与工程化/q1046_to_datetime_robust.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import datetime
    raw = ["2026-01-05", "2026/01/06", "not-a-date"]
    for v in raw:
        try:
            print(v, "->", datetime.strptime(v, "%Y-%m-%d").date())
        except ValueError:
            try:
                print(v, "->", datetime.strptime(v, "%Y/%m/%d").date())
            except ValueError:
                print(v, "-> NaT(脏数据进审计表)")
else:
    raw = pd.Series(["2026-01-05", "2026/01/06", "05-01-2026", "not-a-date"])
    parsed = pd.to_datetime(raw, errors="coerce")
    out = pd.DataFrame({"raw": raw, "parsed": parsed})
    print(out)
    print("脏值数量:", parsed.isna().sum())
    print("显式 format 提示:01-05 这类要用 dayfirst 与来源方约定")
```

**追问**:
- 追问 1:coerce 会把哪些值变 NaT?—— 无法按推断格式解析的字符串、越界日期,以及空串;空串常需 fillna 处理。
- 追问 2:为什么不建议 format="mixed" 一把梭?—— 它按元素猜测,慢且可能猜错歧义格式,优先按格式分组解析。
