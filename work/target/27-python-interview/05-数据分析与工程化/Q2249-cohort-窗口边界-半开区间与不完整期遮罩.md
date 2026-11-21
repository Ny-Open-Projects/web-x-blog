---
title: [Q2249] cohort 窗口边界:半开区间与不完整期遮罩
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2249 · cohort 窗口边界:半开区间与不完整期遮罩

> 难度:★★★★ | 标签:cohort, 口径边界

**问**:留存矩阵大家都会算,但同一份数据两个人算出两套数,问题往往出在哪?

**答**:出在窗口边界。三个必须冻结的规则:一是半开区间,第 i 期是 [起始日+i×窗口, 起始日+(i+1)×窗口),边界日归下一期,实测 1 月 12 日对 1 月 5 日 cohort 属于 P1 而不是 P0,取整方向不同结果就不同;二是 cohort 起点归属,首日活跃用户同时出现在 cohort 期与活跃期,必须明确 M0 是"起始日当天到当天+窗口";三是不完整期遮罩,窗口还没有走完的期列不参与留存对比,实测观测截止 1 月 20 日时 P2、P3 列必须标"未到期",否则越近的 cohort 留存天然虚低。这些规则要写成带自测的公共函数,谁调用都是同一个答案。

```python
# file: code/05_数据分析与工程化/q2249_cohort_boundary.py
"""cohort 窗口边界: 半开区间归属与不完整期遮罩"""

from datetime import date, timedelta

COHORT_START = {"a": date(2026, 1, 5), "b": date(2026, 1, 5), "c": date(2026, 1, 12)}
ACTIVITIES = [
    ("a", date(2026, 1, 5)), ("a", date(2026, 1, 11)), ("a", date(2026, 1, 12)),
    ("b", date(2026, 1, 5)), ("b", date(2026, 1, 6)),
    ("c", date(2026, 1, 12)), ("c", date(2026, 1, 19)),
]
TODAY = date(2026, 1, 20)      # 数据观测截止日
PERIOD_DAYS = 7
MAX_PERIOD = 4                 # 想看 P0..P3


def period_index(cohort_start, active_day):
    """半开区间 [start+i*d, start+(i+1)*d) 归第 i 期, 边界日归下一期"""
    delta = (active_day - cohort_start).days
    if delta < 0:
        return None
    return delta // PERIOD_DAYS


if __name__ == "__main__":
    for user, start in sorted(COHORT_START.items()):
        cells = []
        for i in range(MAX_PERIOD):
            users = {u for u, day in ACTIVITIES
                     if u == user and period_index(start, day) == i}
            window_end = start + timedelta(days=(i + 1) * PERIOD_DAYS - 1)
            cells.append(f"{len(users)}人" if window_end <= TODAY else "未到期")
        print(f"cohort {user} 起始 {start}: " + " | ".join(
            f"P{i}={c}" for i, c in enumerate(cells)))
    assert period_index(date(2026, 1, 5), date(2026, 1, 12)) == 1, "边界日应归下一期"
    assert period_index(date(2026, 1, 5), date(2026, 1, 11)) == 0, "窗口最后一日归本期"
    print("边界自测通过: 1月11日属 P0, 1月12日属 P1, 半开区间方向唯一")
    print("遮罩规则: 窗口未走完的期只可看不可比, 报表上必须标'未到期'")
```

**追问**:
- 追问 1:cohort 按注册日还是首单日?—— 看分析目的,注册日 cohort 回答获客质量,首单日 cohort 回答付费质量,换定义等于换指标必须换名字。
- 追问 2:7 日窗口和自然周窗口哪个好?—— 业务节奏按周走就用自然周,但要写进口径字典;两者混用是留存对不上的常见根因。
