---
title: [Q2014] oncall 值班表公平性:加权轮转与负载均衡
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2014 · oncall 值班表公平性:加权轮转与负载均衡

> 难度:★★★☆ | 标签:oncall, 排班

**问**:值班表按名单轮流排,为什么总有抱怨?怎么把"公平"变成可计算的?

**答**:按名单顺序转,节假日总砸在同几个人头上。加权负载轮转:每期值班有权重(工作日 1、周末 1.5、节假日 2),轮转时挑累计加权负载最小的人。实测 4 人 8 周含一个节假日周,负载极差只有 1.0,判定公平。三个配套:权重系数公开并经团队确认,这是公平感的来源;调班必须记回负载账本,私下互换不记账会让账目失效;负载按季度结算或滚动清零,避免有人背着一年前的债。特殊豁免(休假、健康)走显式冻结名单,而不是悄悄跳过——值班系统的可信度建立在账目透明上。

```python
# file: code/05_数据分析与工程化/q2014_oncall_fair.py
"""值班表公平性:按累计加权负载挑人,节假日加倍计入"""

from datetime import date, timedelta

MEMBERS = ["Alice", "Bob", "Carol", "Dave"]
START = date(2026, 11, 2)      # 周一开始
WEEKS = 8
HOLIDAYS = {date(2026, 11, 26)}        # 含一个节假日
WEEKEND_W, HOLIDAY_W, NORMAL_W = 1.5, 2.0, 1.0


def week_load(day):
    total = 0.0
    for i in range(7):
        d = day + timedelta(days=i)
        if d in HOLIDAYS:
            total += HOLIDAY_W
        elif d.weekday() >= 5:
            total += WEEKEND_W
        else:
            total += NORMAL_W
    return total


def schedule(members, start, weeks):
    load = {m: 0.0 for m in members}
    shifts = []
    for w in range(weeks):
        week_start = start + timedelta(days=7 * w)
        person = min(members, key=lambda m: (load[m], members.index(m)))
        load[person] += week_load(week_start)
        shifts.append((f"第{w + 1}周({week_start})", person))
    return shifts, load


if __name__ == "__main__":
    shifts, load = schedule(MEMBERS, START, WEEKS)
    for week, person in shifts:
        print(f"{week}: {person}")
    print("累计加权负载:", load)
    spread = max(load.values()) - min(load.values())
    verdict = "公平" if spread <= 3 else "需要调班"
    print(f"负载极差 {spread:.1f} -> {verdict}")
    print("要点:节假日与周末权重更高,轮转看累计负载而不是按名单循环;调班必须记回负载账本,否则公平性账目失效")
```

**追问**:
- 追问 1:按周指派还是按天指派?—— 按周连续性更好(上下文完整),跨节假日周允许拆分,把节假日单独加权指派。
- 追问 2:负载不均到什么程度要干预?—— 极差超过一期值班权重就触发调班建议,阈值随团队规模标定。
