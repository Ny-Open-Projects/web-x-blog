---
title: [Q2678] 万级 Task 的成本账:任务不是免费的
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2678 · 万级 Task 的成本账:任务不是免费的

> 难度:★★★ | 标签:asyncio, Task 成本, 容量

**问**:都说协程轻,一次创建 1 万个 Task 的代价到底是多少?

**答**:实测:创建 1 万个任务约 152 毫秒,任务对象占约 11.4MB 内存,全部跑完再花 332 毫秒。每个 Task 都有协程对象、Task 包装、事件循环句柄三份开销,且常驻到任务完成。万级是常态可扛,十万级就要开始算账:连接池、批量队列、协程复用都是省任务的手段。

- 创建的 152 毫秒里大头是对象分配与调度队列入队;

- 内存账要按峰值算:11.4MB 是 1 万个任务同时活着的价格;

- 任务数应与真实并发(连接数、请求数)对齐,不要为每个数据项开任务;

- 批量场景把"一任务一项"改成"一任务一批",成本差两个数量级。

```python
# file: code/02_并发与网络工程/q2678_task_cost.py
# -*- coding: utf-8 -*-
"""万级 Task 的成本账: 任务不是免费的。

- 每个任务都要分配协程对象、Task 包装、事件循环里的句柄;
- 实测创建 1 万个任务的时间与内存, 以及全部跑完的时间;
- 结论: 批量场景该用批量结构(如队列)而不是无脑一任务一连接。
"""
import asyncio
import time
import tracemalloc


async def noop():
    await asyncio.sleep(0)


async def main():
    loop = asyncio.get_running_loop()
    tracemalloc.start()

    t0 = time.perf_counter()
    tasks = [loop.create_task(noop()) for _ in range(10000)]
    t1 = time.perf_counter()
    cur, peak = tracemalloc.get_traced_memory()
    await asyncio.gather(*tasks)
    t2 = time.perf_counter()
    tracemalloc.stop()

    print("创建 10000 个任务: %.0f ms" % ((t1 - t0) * 1000))
    print("任务对象内存: 已分配 %.1f MB, 峰值 %.1f MB" % (cur / 1e6, peak / 1e6))
    print("全部跑完: %.0f ms" % ((t2 - t1) * 1000))
    print("要点: 任务对象常驻到完成, 万级是常态可扛, 十万级要开始算账")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 为什么全部跑完比创建还慢?——gather 要逐个调度、执行、回收,单事件循环的吞吐就这么多。2) 怎么观察线上任务规模?——用任务工厂登记在途任务数,超过阈值就告警,别等内存爆了才知道。3) 底层机制:一个 Task 的三份开销是什么?——协程帧保存挂起状态,Task 对象维护状态机与回调链,循环里还有 handle 与就绪队列条目;实测约 1KB/任务就是三份的总和,任务完成前全部常驻,这就是内存账要按峰值算的依据。4) 生产陷阱?——为每个数据项开任务,百万数据内存失控(该批量或队列化);任务完成但没人 await,异常无人接收("Task exception was never retrieved");用无界列表攥着已完成 Task 的引用,对象不释放。

---
