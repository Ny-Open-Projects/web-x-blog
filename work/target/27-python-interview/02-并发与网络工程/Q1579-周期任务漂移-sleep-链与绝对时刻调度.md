---
title: [Q1579] 周期任务漂移:sleep 链与绝对时刻调度
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1579 · 周期任务漂移:sleep 链与绝对时刻调度

> 难度:★★☆☆ | 标签:定时, 漂移, 调度

**问**:周期任务每 0.2s 跑一次,跑了十分钟发现实际周期是 0.25s——漂移从哪来的?

**答**:sleep(period) 和 threading.Timer 链都是"上一次结束后再等一个周期":任务本身耗时被累计进周期,漂移等于任务耗时乘以轮数,线性增长。正确姿势是把锚定在绝对时刻:start 时刻记下来,第 n 轮睡到 start + n * period,任务耗时被周期的富余吸收而不是叠加。演示里 6 轮后 sleep 链漂移 0.37s,绝对时刻调度只有 0.03s。两个补充:目标时刻已过(任务耗时超过周期)时不要补跑堆积,直接追平到下一个未来时刻;锚一律用 monotonic 时钟,避免系统改时间导致跳变。

```python
# file: code/02_并发与网络工程/q1579_periodic_drift.py
"""周期任务的漂移账: sleep 链 vs 绝对时刻调度。

threading.Timer 链和 sleep(period) 都是"上一次结束后再等一个周期",
任务自身耗时累计进周期 -> 漂移线性增长。正确姿势: 记住绝对时刻表
next = start + n * period, 睡到点为止, 任务耗时被吸收而非叠加。
"""
import time

PERIOD = 0.2
JOB_COST = 0.05
ROUNDS = 6


def job():
    time.sleep(JOB_COST)        # 模拟每轮任务自身的耗时


def naive_schedule():
    stamps = []
    for _ in range(ROUNDS):
        job()
        stamps.append(time.monotonic())
        time.sleep(PERIOD)      # 错误: 周期被 JOB_COST 拉长
    return stamps


def absolute_schedule():
    stamps = []
    start = time.monotonic()
    for n in range(1, ROUNDS + 1):
        target = start + n * PERIOD
        delta = target - time.monotonic()
        if delta > 0:
            time.sleep(delta)
        stamps.append(time.monotonic())
        job()                   # 任务耗时占用下一个周期的富余
    return stamps


def drift(stamps, period):
    return max(abs((t - stamps[0]) - i * period)
               for i, t in enumerate(stamps))


def main():
    naive = naive_schedule()
    absolute = absolute_schedule()
    d1 = drift(naive, PERIOD)
    d2 = drift(absolute, PERIOD)
    print("sleep 链 各轮触发时刻:", [round(t - naive[0], 3) for t in naive])
    print("绝对时刻 各轮触发时刻:", [round(t - absolute[0], 3) for t in absolute])
    print("sleep 链最大漂移: %.3fs | 绝对时刻最大漂移: %.3fs" % (d1, d2))
    assert d1 > d2 + 0.1, "sleep 链的漂移应显著大于绝对时刻调度"
    assert d2 < 0.1, "绝对时刻调度应几乎无漂移"
    print("结论: 周期调度的锚必须是绝对时刻, 而不是'上一轮结束'")


if __name__ == "__main__":
    main()
```

**追问**:1) 任务耗时偶尔超过周期怎么办?——记录超限并告警,下一轮立即执行不 sleep;持续超限说明周期该调大或任务该拆分。2) 「目标时刻已过」为什么不能补跑堆积?——任务持续超周期时,补跑会让积压线性增长(每轮欠账越滚越多),系统永远在追历史;正确做法是跳到下一个未来时刻并告警——调度器的职责是「按时」不是「补课」。3) 绝对时刻锚定的实现细节?——锚用 time.monotonic(不可回拨);第 n 轮睡到 start+n×period;sleep 返回后重新校准(剩余为负就立即跑)——与事件循环超时计算(Q1581)、时间轮节拍(Q1578)是同一原理的三处应用。4) 生产陷阱?——sleep 链漂移(见原问);用 time.time 锚定,NTP 跳变让任务瞬间连跑或大停;周期任务里嵌套阻塞调用让「实际周期」永远超限而没人告警;多实例部署各自跑周期任务(要分布式锁或租约,Q1310)。

---
