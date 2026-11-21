---
title: [Q2675] deadline 的时钟陷阱:墙钟回拨会让超时判定失效
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2675 · deadline 的时钟陷阱:墙钟回拨会让超时判定失效

> 难度:★★★ | 标签:单调时钟, deadline, 墙钟

**问**:做超时预算时用 time.time() 记 deadline,会有什么坑?

**答**:墙钟会被 NTP 校时与手动改表拨动:回拨之后 now 永远追不上 deadline,超时熔断失效。实测模拟时钟:预算 1 秒的工作干了 1.2 秒,期间墙钟被回拨 2 秒,墙钟方案判定"预算内完成",单调钟方案正确熔断。超时数学必须用 time.monotonic 或 loop.time——它们只前进,不回头。

- 实测 5 万次采样,monotonic 与 loop.time 严格不减;

- 墙钟只配给人类看(日志时间戳),不配给机器算 deadline;

- 墙钟回拨不是罕见事件:NTP 小步校准、夏令时、手动改表都会发生;

- 所有超时、租约、限速的时间锚点统一走单调钟,是底线纪律。

```python
# file: code/02_并发与网络工程/q2675_monotonic_clock.py
# -*- coding: utf-8 -*-
"""deadline 的时钟陷阱: 墙钟回拨会让超时判定失效。

- 超时数学必须用单调时钟: 循环的 loop.time 与 time.monotonic 同源;
- 墙钟 time.time 会被 NTP 校时与手动改表拨动, 回拨后 deadline 永远不到;
- 用模拟时钟复现: 同一段预算逻辑, 墙钟被回拨后超时熔断失效。
"""
import asyncio
import time


def sample_monotonic():
    prev = -1.0
    for _ in range(50000):
        t = time.monotonic()
        assert t >= prev, "monotonic 竟然倒退"
        prev = t
    print("实测 5 万次采样: time.monotonic 严格不减")


async def sample_loop_time():
    loop = asyncio.get_running_loop()
    samples = []
    for _ in range(1000):
        samples.append(loop.time())
        await asyncio.sleep(0)
    assert samples == sorted(samples), "loop.time 竟然倒退"
    print("实测 1000 次采样: loop.time 严格不减")


class SimClock:
    """模拟时钟: kind 决定校时是否拨动它。"""

    def __init__(self, kind):
        self.kind = kind
        self.t = 1000.0

    def now(self):
        return self.t

    def advance(self, s):
        self.t += s

    def ntp_adjust(self):
        if self.kind == "wall":
            self.t -= 2.0                    # 墙钟被校时回拨 2 秒


def guarded_work(clock, budget, steps):
    """预算内干活, 每步之后检查 deadline; 期间系统校了一次时。"""
    deadline = clock.now() + budget
    used = 0.0
    for i in range(steps):
        clock.advance(0.4)                   # 每步 0.4s 的活
        used += 0.4
        clock.ntp_adjust()                   # 第一步之后校时
        if clock.now() > deadline:
            return "第 %d 步超时熔断(实际已用 %.1fs > 预算 %.1fs)" % (i + 1, used, budget)
    return "预算内完成"


if __name__ == "__main__":
    sample_monotonic()
    asyncio.run(sample_loop_time())

    budget, steps = 1.0, 3                   # 干 1.2s 的活, 预算只有 1s
    wall = SimClock("wall")
    mono = SimClock("mono")
    print("墙钟方案:", guarded_work(wall, budget, steps))
    print("单调钟方案:", guarded_work(mono, budget, steps))
    print("要点: deadline 只能用 monotonic 做, 墙钟只配给人类看")
```

**追问**:1) perf_counter 和 monotonic 什么区别?——都单调,perf_counter 分辨率更高且含进程级基准,测耗时用它,算 deadline 用 monotonic 或 loop.time。2) 单调钟的值能跨进程比较吗?——不能,起点是任意的,跨机器对时仍是墙钟的职责。3) 底层机制:loop.time 和 monotonic 什么关系?——默认事件循环的 time() 就是 time.monotonic(),call_later 与定时器堆同源;deadline 若用墙钟,与循环定时器比较就是两个时钟系混用,回拨后超时永不触发;底层由 clock_gettime(CLOCK_MONOTONIC) 保证不减。4) 生产陷阱?——租约/限速/重试预算用 time.time,NTP 回拨后熔断失效;把单调钟数值跨进程序列化比较;日志时间戳用单调钟,人类无法对时。

---
