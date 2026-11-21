---
title: [Q2136] to_thread 的边界:默认执行器容量实测
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2136 · to_thread 的边界:默认执行器容量实测

> 难度:★★★ | 标签:to_thread, 线程池, 阻塞边界

**问**:asyncio.to_thread 把同步函数丢进线程池,它有什么用、有什么边界?

**答**:它让阻塞调用不再卡事件循环,但容量由默认执行器决定:min(32, cpu+4),超出的任务排队;它也不解决 CPU 并行,GIL 还在。

- 实测 16 个 0.25s 阻塞任务 0.52s 跑完,并行度约等于执行器线程数;

- 对照实验:to_thread 窗口心跳 5 次,裸 time.sleep 窗口心跳 0 次;

- 不能包"必须主线程"的调用,如信号处理与部分 UI API;

- 大量并发 to_thread 会把线程池打满,拖累其他阻塞任务的延迟。

```python
# file: code/02_并发与网络工程/q2136_to_thread_boundary.py
# -*- coding: utf-8 -*-
"""to_thread 的边界: 默认执行器的容量与阻塞实测。

- asyncio.to_thread 把同步函数丢进默认线程池, 主循环不卡;
- 默认执行器容量 = min(32, cpu + 4), 超出的任务排队;
- 边界: 它不解决 CPU 并行 (GIL), 也不能包"必须主线程"的调用。
"""
import asyncio
import os
import time


def blocking_io(task_id, dur=0.25):
    time.sleep(dur)          # 模拟阻塞 IO (磁盘/阻塞 socket)
    return task_id


async def main():
    print("cpu_count:", os.cpu_count(),
          "-> 默认执行器线程数:", min(32, (os.cpu_count() or 1) + 4))

    t0 = time.monotonic()
    results = await asyncio.gather(*[
        asyncio.to_thread(blocking_io, i) for i in range(16)
    ])
    wall = time.monotonic() - t0
    serial = 16 * 0.25
    workers = max(1, round(serial / wall))
    print("16 个 0.25s 阻塞任务: 串行需 %.2fs, 实际 %.2fs" %
          (serial, wall))
    print("估算同时运行线程数 ≈", workers, "-> 超出容量的任务在排队")
    print("结果顺序:", results, "-> to_thread 返回原值, gather 保序")

    # 反例: 不包 to_thread, 主循环被独占, ticker 全停
    stamps = []

    async def ticker():
        end = time.monotonic() + 0.6
        while time.monotonic() < end:
            await asyncio.sleep(0.05)
            stamps.append(time.monotonic())

    tk = asyncio.ensure_future(ticker())
    await asyncio.sleep(0.05)
    w0 = time.monotonic()
    await asyncio.to_thread(blocking_io, 99, 0.2)    # 包住: 循环不卡
    w1 = time.monotonic()
    b0 = time.monotonic()
    time.sleep(0.2)                                   # 裸 sleep: 循环卡死
    b1 = time.monotonic()
    await tk
    in_window = sum(1 for s in stamps if w0 <= s <= w1)
    blocked_ticks = sum(1 for s in stamps if b0 <= s <= b1)
    print("to_thread 窗口心跳:", in_window, "| 裸阻塞窗口心跳:", blocked_ticks,
          "(0 = 循环被独占, 这就是必须包装的原因)")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) to_thread 和 run_in_executor 选哪个?——to_thread 是便捷包装(默认执行器),需要专用池、命名线程或并发上限时用 run_in_executor。2) 被包的函数抛异常去哪了?——随 Future 回到 await 处,和普通调用一样 try/except,不会被吞。3) 默认执行器容量 min(32, cpu+4) 的适用边界?——它是 ThreadPoolExecutor 的默认 max_workers(3.8+),为 IO 阻塞设计;16 个 0.25s 任务 0.52s 跑完≈并行度 8-16(核数相关)的实测印证;CPU 并行不解决(GIL),要进程池;要专用池/命名线程/上限控制用 run_in_executor+自建 executor。4) 「阻塞调用进线程池」的容量账怎么算?——池满后任务排队:排队延迟=在途耗时×队列深度/线程数;线程池被慢任务占满,其他阻塞任务(如 DB 调用)全部排队——线程池是共享资源,要按用途分舱(Q1876 舱壁)。5) 生产陷阱?——to_thread 包「必须主线程」的调用(信号处理/UI);大量并发 to_thread(池满排队,延迟暴增);把 to_thread 当 CPU 并行(GIL);异常被吞(不会,随 Future 回 await 处,但要 try);默认执行器没 shutdown(Q1859 收尾泄漏)。

---
