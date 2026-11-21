---
title: [Q593] 背压 backpressure:有界队列的限速本质
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q593 · 背压 backpressure:有界队列的限速本质

> 难度:★★★☆ | 标签:背压, asyncio.Queue, 流控

**问**:什么是背压?asyncio.Queue 的 maxsize 是怎么把"下游慢"传导给"上游快"的?

**答**:背压指下游处理能力不足时,压力沿着调用链向上游逐级传导,最终让数据源头减速,而不是在中途无限堆积。asyncio.Queue(maxsize=N) 的机制:`put` 在队列满时挂起,生产者自然被拖慢,消费速度成为整条管道的速率上限。没有背压的系统表现是"内存涨爆或延迟爆炸后才崩溃";有背压的系统表现为"吞吐稳定、延迟可控"。观察指标:队列水位(maxsize 的占比)、put 等待时长。逐级连接(源→队列→处理→队列→出口)时,每一跳都要有界。

```python
# file: code/02_并发与网络工程/q593_backpressure.py
import asyncio
import time

MAXSIZE = 5


async def producer(q: asyncio.Queue, stats: dict) -> None:
    for i in range(20):
        t0 = time.perf_counter()
        await q.put(i)  # 队列满时挂起: 背压发生点
        wait = time.perf_counter() - t0
        stats["max_wait"] = max(stats["max_wait"], wait)
        stats["max_size"] = max(stats["max_size"], q.qsize())
    stats["done"] = True


async def consumer(q: asyncio.Queue) -> None:
    while True:
        item = await q.get()
        await asyncio.sleep(0.03)  # 下游处理速度: 上游被它拖慢
        q.task_done()


async def main() -> None:
    q: asyncio.Queue = asyncio.Queue(maxsize=MAXSIZE)
    stats = {"max_wait": 0.0, "max_size": 0, "done": False}
    prod = asyncio.create_task(producer(q, stats))
    cons = asyncio.create_task(consumer(q))

    await asyncio.wait_for(prod, 5)  # 生产者完成(被拖慢后仍完成)
    await q.join()
    cons.cancel()
    print(f"maxsize={MAXSIZE}, 队列峰值 {stats['max_size']}, "
          f"put 最长等待 {stats['max_wait'] * 1000:.0f}ms")
    assert stats["max_size"] <= MAXSIZE, "有界队列封顶生效"


asyncio.run(main())
```

**追问**:1) 无界队列 + 限速器是不是等价于有界队列?——不等价,限速只约束生产速率不感知下游状态,下游卡死时数据照样堆积;背压必须由下游状态驱动。2) 背压的完整链路?——下游慢→队列满→生产者 put 阻塞/拒绝→上游减产;每一跳都要传递(消费者 credit、HTTP 503、TCP 窗口);任何一跳「吞下压力」(无界缓冲)链路就断。3) 实现手段?——有界 Queue put 阻塞;Semaphore 窗口(Q595);.credit/token bucket 配合水位监控;stream writer drain(Q594)。4) 生产陷阱?——无界队列伪装背压;限速器在错误层(限了应用没限协议);监控缺队列水位告警(Q564)。

---
