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
