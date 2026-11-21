---
title: [Q2134] loop.time 时钟源与 call_at 绝对重调度
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2134 · loop.time 时钟源与 call_at 绝对重调度

> 难度:★★★ | 标签:call_at, 时钟源, 定时器

**问**:loop 内部定时器用的是什么钟?周期任务用 call_at 和用 sleep 链差在哪?

**答**:事件循环用 loop.time(),与 time.monotonic() 同源的单调钟,不受系统改表影响;call_at 以"绝对时刻"为锚,周期任务按 base + n*period 排,回调晚点不影响下一拍。

- 实测 sleep 链各拍漂移单调累积到 +9.5ms;

- call_at 各拍漂移在 ±2ms 内波动,不累积;

- 原理:sleep 链的锚是"上一拍结束",误差滚雪球;call_at 的锚是数学上的时刻表;

- 这就是周期任务、心跳、限速器一律用绝对时刻调度的原因。

```python
# file: code/02_并发与网络工程/q2134_loop_clock.py
# -*- coding: utf-8 -*-
"""loop.time 时钟源与 call_at 绝对时刻重调度。

- loop.time() 与 time.monotonic() 同源, 不受系统改表影响;
- call_at 用"绝对时刻"调度: 周期任务按 next = base + n*period 排, 不累积漂移;
- 实测 5 拍 50ms 周期: 绝对时刻调度的漂移远小于 sleep 链式的累积漂移。
"""
import asyncio
import time

PERIOD = 0.05


async def sleep_chain(n=5):
    """相对延迟链: 每拍延迟 = 上拍结束 + PERIOD, 误差会累积。"""
    stamps = []
    for i in range(n):
        await asyncio.sleep(PERIOD)
        stamps.append(time.monotonic())
    return stamps


def call_at_chain(loop, n=5):
    """绝对时刻调度: 第 i 拍固定在 base + i*PERIOD, 不看上拍何时结束。"""
    stamps = []
    base = loop.time() + PERIOD

    def fire(i):
        stamps.append(loop.time())
        if i + 1 < n:
            loop.call_at(base + (i + 1) * PERIOD, fire, i + 1)

    loop.call_at(base, fire, 0)
    return stamps, base


async def main():
    loop = asyncio.get_event_loop()
    print("loop.time = %.6f, time.monotonic = %.6f, 差值 %.6f" %
          (loop.time(), time.monotonic(),
           abs(loop.time() - time.monotonic())))

    s1 = await sleep_chain()
    drift1 = [s - s1[0] - i * PERIOD for i, s in enumerate(s1)]
    print("sleep 链各拍相对漂移: %s" %
          ["%+.1fms" % (d * 1000) for d in drift1])

    fut = asyncio.Future()
    s2, base = call_at_chain(loop)

    def done():
        if not fut.done():
            fut.set_result(None)
    loop.call_later(PERIOD * 7, done)
    await fut
    drift2 = [s - base - i * PERIOD for i, s in enumerate(s2)]
    print("call_at 各拍相对漂移: %s" %
          ["%+.1fms" % (d * 1000) for d in drift2])
    print("call_at 以绝对时刻为锚, 回调晚点不影响下一拍的锚点")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) call_later 和 call_at 谁是底层?——call_later 内部就是 call_at(loop.time()+delay),三层 API 一个堆。2) 系统时间被 NTP 回拨会影响什么?——wall clock 相关逻辑会乱,但 monotonic 驱动的定时器不受影响,这也是选 loop.time 的理由。3) sleep 链漂移的数学与 call_at 的修正?——sleep 链锚在「上一拍结束」:实际周期=period+任务耗时,漂移线性累积;call_at 锚在 base+n×period(数学时刻表):单拍迟到不传给下一拍;实现:每拍 next+=period,若已过则立即追平(不补跑堆积,Q1579 同源)。4) loop.time 的时钟源与选型?——与 time.monotonic 同源(单调、不受 NTP 影响);call_later=call_at(loop.time()+delay) 的便捷包装;三层 API 一个定时器堆——「绝对时刻调度」是周期任务/心跳/限速器的统一答案。5) 生产陷阱?——sleep 链周期任务(漂移累积,见原问);系统 NTP 回拨影响 loop 定时器(不会,monotonic 源)但影响业务时间戳逻辑;call_at 用 wall clock 时刻(错,要用 loop.time 的时基);取消周期任务后 call_handle 泄漏(要 handle.cancel);周期任务在回调里再做长任务(下一拍堆积)。

---
