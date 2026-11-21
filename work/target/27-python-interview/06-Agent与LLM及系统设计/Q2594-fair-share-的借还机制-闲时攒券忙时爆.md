---
title: [Q2594] fair-share 的借还机制:闲时攒券忙时爆量封顶
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2594 · fair-share 的借还机制:闲时攒券忙时爆量封顶

> 难度:★★★☆ | 标签:LLM 运维, 调度, 多租户

**问**:纯 fair-share 对突发流量不友好,怎么给突发开一扇受控的门?

**答**:信用券机制:租户闲置期每轮攒一张券,突发期一次性消耗,相当于向未来的自己借容量;封顶限制最大借用量,本例攒满 6 张,突发 8 个也只能放 6 个,剩下按每轮一张的节奏排队补给。封顶的价值是防两件事:防长期闲置者瞬间打满全场伤害他人,防攒券机制被当成免费的大额突进通道。对照实验能看清封顶的作用:无封顶时十轮闲置攒十张,突发全放还剩余量可继续透支;封顶 6 时同样的闲置只攒到 6,突发被压平。券的语义要明确:借的是自己的份额,不是公共池,所以不产生跨租户债务。参数就两个——积累速率与上限,都按租户档位配置,治理路径与限流阈值同构。

```python
# file: code/06_Agent与LLM及系统设计/q2594_credit_borrow.py
"""Q2594 fair-share 的借还机制:闲时攒券,忙时爆量,封顶防抖。

纯 fair-share 对突发不友好;给租户发可积累的信用券,闲置期
攒券、突发期一次性消耗,封顶限制最大借用量,防长期闲置者
瞬间打满全场,防抖且可解释。
"""


def simulate(demand, cap, regen=1):
    credit = 0
    timeline = []
    served_total = 0
    for r, want in enumerate(demand):
        credit = min(cap, credit + regen)   # 闲置攒券,封顶
        use = min(want, credit)
        credit -= use
        served_total += use
        timeline.append((r, want, use, credit))
    return timeline, served_total


def main():
    demand = [0] * 10 + [8] + [0] * 3
    timeline, total = simulate(demand, cap=6)
    assert timeline[9] == (9, 0, 0, 6), timeline[9]     # 攒券封顶在 6
    assert timeline[10] == (10, 8, 6, 0), timeline[10]  # 突发 8 只放 6
    assert total == 6
    uncapped, total2 = simulate(demand, cap=100)
    assert uncapped[9] == (9, 0, 0, 10), uncapped[9]    # 无封顶攒到 10
    assert uncapped[10] == (10, 8, 8, 3), uncapped[10]  # 突发 8 全放,余 3 券
    print("时间线 轮 需求 放行 余券(封顶 6):")
    for row in timeline[8:11]:
        print("  ", row)
    print("封顶:突发只放 6;无封顶对照:一次放 8,余券 2 还能继续透支")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:券要不要过期?答:要,设衰减或有效期,否则租户囤券跨月突进,与封顶的初衷相悖。
- 追问二:突发被压掉的请求去哪?答:进本租户的排队队列按券节奏消化,或转降级档处理,别静默丢弃。
