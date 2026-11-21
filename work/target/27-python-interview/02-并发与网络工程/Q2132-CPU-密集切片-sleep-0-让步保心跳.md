---
title: [Q2132] CPU 密集切片:sleep(0) 让步保心跳
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2132 · CPU 密集切片:sleep(0) 让步保心跳

> 难度:★★★ | 标签:事件循环, CPU 密集, sleep(0)

**问**:asyncio 里跑一段 200 万次求和的计算,事件循环会发生什么?怎么救?

**答**:单线程协作调度下,不让步的计算独占循环,心跳协程全部停摆;把计算切片,片间 await asyncio.sleep(0) 把控制权交回循环,实测切片版计算窗口内心跳 3 次,不切片 0 次。

- sleep(0) 不真正睡眠,只是回到循环头,几乎零成本;

- 切片粒度是权衡:片越小越公平,调度开销越大;

- 结果两种切法完全一致,公平税只是总耗时略增;

- 更重的 CPU 任务该交给进程池,切片只救"中等粒度"。

```python
# file: code/02_并发与网络工程/q2132_cpu_slice.py
# -*- coding: utf-8 -*-
"""事件循环内的 CPU 密集切片: sleep(0) 让步保心跳。

- 事件循环是单线程协作调度, 一个不 await 的长计算会饿死一切;
- 把计算切成小片, 片间 await asyncio.sleep(0) 让控制权回到循环;
- 实测: 计算窗口内, 不切片心跳为 0, 切片后心跳均匀出现。
"""
import asyncio
import time

N = 2_000_000


def compute_chunk(lo, hi):
    return sum(i * i for i in range(lo, hi))


async def ticker(seconds, stamps):
    """每 0.02s 记一次心跳时间戳, 直到窗口结束。"""
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        await asyncio.sleep(0.02)
        stamps.append(time.monotonic())


async def blocked_run(stamps):
    tk = asyncio.ensure_future(ticker(0.8, stamps))
    await asyncio.sleep(0.05)                # 让 ticker 先跑半步
    t0 = time.monotonic()
    total = compute_chunk(0, N)              # 一整块不让步, 循环被独占
    t1 = time.monotonic()
    await tk
    return total, t0, t1


async def sliced_run(stamps, parts=10):
    tk = asyncio.ensure_future(ticker(0.8, stamps))
    await asyncio.sleep(0.05)
    t0 = time.monotonic()
    total = 0
    step = N // parts
    for k in range(parts):
        total += compute_chunk(k * step, (k + 1) * step)
        await asyncio.sleep(0)               # 让步: 心跳得以插入
    t1 = time.monotonic()
    await tk
    return total, t0, t1


def ticks_in(stamps, t0, t1):
    return sum(1 for s in stamps if t0 <= s <= t1)


async def main():
    s1 = []
    total1, a0, a1 = await blocked_run(s1)
    print("不切片: 计算 %.2fs, 窗口内心跳 %d 次 (循环被独占)" %
          (a1 - a0, ticks_in(s1, a0, a1)))

    s2 = []
    total2, b0, b1 = await sliced_run(s2)
    print("切片后 : 计算 %.2fs, 窗口内心跳 %d 次 (协作让步)" %
          (b1 - b0, ticks_in(s2, b0, b1)))
    assert total1 == total2, "两种切法必须同结果"
    print("结果一致:", total1, "| 切片的代价是总耗时略增的公平税")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 为什么 ticker 的 sleep(0.02) 在阻塞期间完全不动?——定时器到期要循环来派发,循环被占着,再早到期的回调也只能排队。2) 和把计算丢 to_thread 比怎么选?——切片保数据局部性、无序列化成本;to_thread 换真正的并行与隔离,GIL 下两者都不会更快,只有公平性差异。3) sleep(0) 的调度语义与代价?——交一次控制权回循环头,立刻重新排队(不进定时器堆);代价≈一次循环迭代;切片粒度的权衡:片太小公平税大,片太大心跳间隔长;与 to_thread 的选择(见原问):数据局部性 vs 真隔离。4) 「定时器派发被阻塞」的推论怎么用于排障?——ticker 不动+心跳停摆=事件循环被长同步段占住;定位:py-spy dump 看当前栈、debug 模式 slow_callback_duration(>100ms 回调告警)——「循环卡死」的观测入口(Q654/Q2132 原问)。5) 生产陷阱?——CPU 密集任务直接写在协程里(全连接饿死);切片粒度拍脑袋(按 P99 单片耗时<10ms 校准);把 sleep(0) 当 sleep(极短)(语义不同:0 不进定时器堆);切片版结果正确性没验证(切片引入的中间态 bug);重 CPU 该进进程池(线程池不解决 GIL)。

---
