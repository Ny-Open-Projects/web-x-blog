---
title: [Q5603] 重连风暴 Task 创建速率容量账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5603 · 重连风暴的 Task 创建速率容量账

> 难度:★★★★☆ | 标签:容量规划, asyncio, GC

**问**:1 万个客户端每 30 秒重连一次的服务，`create_task` 每秒约 300+ 个，账怎么算？什么时候会出事？

**答**:结论：单次 `create_task` 的直接成本很小（一个 Task 对象 ~KB 级 + 一次 loop 调度），但容量账要算三条曲线：① **稳态驻留**——并发任务数 = 创建速率 × 平均存活时长（Little's Law），1 万连接 × 5s 存活 = 峰值 5000 任务，内存 = 任务数 × 每任务对象图（含回调闭包捕获的缓冲）；② **GC 压力**——每次重连创建/销毁 Task、socket、buffer 三族对象，跨代晋升的回收成本随速率线性，速率上到每秒数万时 GC 停顿在慢请求上可见；③ **调度放大**——每任务的 await 链越深，单次就绪调度成本越高。危险阈值不是绝对速率，而是"速率 × 对象图大小"逼近分配带宽。降峰手段：连接对象池化复用、批量重连对齐（避免同一 tick 齐爆）、用 `asyncio.timeout` 替代自管超时任务。

```python
import asyncio, time

N, RECONNECT_S, LIFETIME_S = 10_000, 30, 5
RATE = N / RECONNECT_S                     # 每秒新建会话数
CONCURRENT = RATE * LIFETIME_S             # Little's Law 稳态并发
print(f"创建速率 {RATE:.0f}/s, 稳态并发 {CONCURRENT:.0f} 任务")

async def session(i: int):
    await asyncio.sleep(LIFETIME_S / 10)   # 演示用缩短生命周期

async def main():
    t0 = time.perf_counter()
    tasks = [asyncio.create_task(session(i)) for i in range(2000)]  # 速率放大实验
    await asyncio.gather(*tasks)
    dt = time.perf_counter() - t0
    print(f"2000 个任务创建+调度+回收 用时 {dt:.2f}s → 折算速率上限≈{2000/dt:.0f} 任务/s")
    # 经验判读：上限低于业务速率 → 必须 batching/池化

asyncio.run(main())
```

**追问一层**:为什么"创建速率上限"和"稳态并发数上限"是两条不同的容量红线？
**追二层**:每秒 5 万任务与每秒 5000 任务、10 倍对象图，GC 侧哪个更危险？怎么用 tracemalloc/gc 统计验证？

**背诵要点**
- 稳态并发 = 创建速率 × 存活时长（Little's Law）。
- 容量红线看三条：驻留内存、GC 分配带宽、调度成本。
- 降峰靠池化复用、错峰重连、砍每任务对象图。

**复盘追问**
- 重连齐爆（同一 tick 全量断线重连）如何用抖动打散？提示：指数退避+全抖动（Q2901）。
- 如何在线上观测 Task 生命周期分布？提示：loop 级 instrumentation 或 gc.get_objects 采样。
