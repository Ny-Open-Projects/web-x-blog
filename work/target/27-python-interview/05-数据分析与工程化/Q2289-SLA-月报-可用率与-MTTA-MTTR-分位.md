---
title: [Q2289] SLA 月报:可用率与 MTTA MTTR 分位
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2289 · SLA 月报:可用率与 MTTA MTTR 分位

> 难度:★★★☆ | 标签:SLA, 报告

**问**:月底要向业务方交代服务稳定性,SLA 月报里放什么数字才既诚实又有用?

**答**:四个口径:月度可用率(1 减停机时长除以总时长),实测 4 起事故共停机 313 分钟,可用率 99.276%,未达 99.9% 的 SLO;错误预算消耗,停机 313 分钟对 43.2 分钟的月度预算是 724%——预算击穿要触发冻结发布,这是 SLO 机制的牙齿;MTTA 与 MTTR 用分位数不用平均,实测 MTTA 中位 15 分钟、P90 31.4 分钟,平均会被一起小事故拉低造成"看起来很快"的错觉。报告三个纪律:停机时长按对用户的影响计算而不是按修复时长,灰度期间只有部分用户受影响要按比例折算;每起事故附一行根因归类,月报按类别聚合指向最该投入的改进方向;分位数样例少时注明方法,别用小样本分位数装精确。

```python
# file: code/05_数据分析与工程化/q2289_sla_report.py
"""SLA 月报: 可用率, 错误预算与 MTTA MTTR 分位"""

from statistics import quantiles

MONTH_MINUTES = 30 * 24 * 60
INCIDENTS = [
    # id, 起止(同日内简化), 确认耗时分钟
    ("I1", "03-04 02:10", "03-04 02:55", 8),
    ("I2", "03-11 14:00", "03-11 15:40", 22),
    ("I3", "03-19 09:30", "03-19 09:48", 5),
    ("I4", "03-27 21:00", "03-27 23:30", 35),
]
BUDGET_MIN = 43.2   # 99.9% SLO 的月度错误预算


def minutes_of(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


if __name__ == "__main__":
    downtime, acks, repairs = 0.0, [], []
    for inc_id, start, end, acked in INCIDENTS:
        mins = minutes_of(end.split(" ")[1]) - minutes_of(start.split(" ")[1])
        downtime += mins
        acks.append(acked)
        repairs.append(mins)
    avail = 1 - downtime / MONTH_MINUTES
    q_ack = quantiles(acks, n=10, method="inclusive")
    q_rep = quantiles(repairs, n=10, method="inclusive")
    print(f"月可用率 {avail:.3%} (SLO 99.9%, 预算 {BUDGET_MIN} 分钟)")
    print(f"停机 {downtime:.0f} 分钟, 错误预算消耗 {downtime / BUDGET_MIN:.0%}")
    print(f"MTTA 中位 {q_ack[4]:.1f} 分钟, P90 {q_ack[8]:.1f} 分钟")
    print(f"MTTR 中位 {q_rep[4]:.1f} 分钟, P90 {q_rep[8]:.1f} 分钟")
    print("要点: 停机按用户影响折算; 预算击穿触发冻结发布; 分位数不平均, 小样本注明方法")
```

**追问**:
- 追问 1:预算击穿后冻结发布的豁免怎么给?—— 走紧急审批带条件(只许修不允许新功能),豁免记录与预算恢复挂钩,复盘时检查豁免是否被滥用。
- 追问 2:错误预算和告警阈值什么关系?—— 预算消耗速率是多窗口燃烧率告警的输入,消耗过快提前升级,比月终算总账更早发现问题。
