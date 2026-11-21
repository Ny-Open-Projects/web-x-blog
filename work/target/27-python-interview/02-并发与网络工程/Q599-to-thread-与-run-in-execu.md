---
title: [Q599] to_thread 与 run_in_executor 选型
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q599 · to_thread 与 run_in_executor 选型

> 难度:★★☆ | 标签:to_thread, run_in_executor, 选型

**问**:asyncio.to_thread 和 loop.run_in_executor 功能重叠,工程上怎么选?

**答**:to_thread(3.9+)是高层封装:自动用 loop 的默认执行器、支持 kwargs、自动传播 contextvars,写起来最省事,适合"偶发的阻塞调用"。run_in_executor 是底层接口:接受任意 concurrent.futures.Executor,能自定义线程数、命名、池复用,适合要精细控制并发的场景(比如把所有 DB 调用固定在一个 5 线程池里限流)。语义差异:to_thread 用的默认池随 loop 存活,run_in_executor 的池生命周期由你管理;混用时注意默认池线程数(min(32, cpu+4))可能撑不起高并发阻塞调用。

```python
# file: code/02_并发与网络工程/q599_to_thread.py
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_io(n: int, factor: int = 2) -> int:
    time.sleep(0.1)  # 模拟阻塞 IO
    return n * factor


async def main() -> None:
    # 场景一: 偶发调用 → to_thread 简洁
    t0 = time.perf_counter()
    r1 = await asyncio.to_thread(blocking_io, 10, factor=3)  # 支持 kwargs
    print(f"to_thread 单次: {r1}, {time.perf_counter() - t0:.2f}s")

    # 场景二: 大量并发 → 默认池够用性检查
    t0 = time.perf_counter()
    rs = await asyncio.gather(*[asyncio.to_thread(blocking_io, i) for i in range(10)])
    print(f"to_thread 10 并发: 完成 {len(rs)}, {time.perf_counter() - t0:.2f}s")

    # 场景三: 需要限流 → 自定义 2 线程池, 10 个任务分 5 批
    pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="db")
    try:
        loop = asyncio.get_running_loop()
        t0 = time.perf_counter()
        rs = await asyncio.gather(
            *[loop.run_in_executor(pool, blocking_io, i) for i in range(10)]
        )
        print(f"run_in_executor(max_workers=2): {len(rs)} 个, "
              f"{time.perf_counter() - t0:.2f}s (被 2 线程限流)")
    finally:
        pool.shutdown()


asyncio.run(main())
```

**追问**:1) 默认 executor 的线程数在哪看、怎么改?——`loop.get_default_executor()` 可查看;Python 3.8+ 默认 min(32, os.cpu_count() + 4),要改就在循环启动后 `loop.set_default_executor(ThreadPoolExecutor(...))`。2) 选型的完整决策树?——阻塞 IO/库调用:to_thread(默认池);重阻塞高频:自定义线程池(命名线程、独立上限,隔离长任务);CPU 密集:ProcessPoolExecutor;常驻并发服务:自管池 + 队列水位(Q564)。3) 与默认池的风险?——默认池共享,一个慢库占满饿死别人;线程命名便于 dump 排查(Q571);线程数不是越大越好(上下文切换+GIL)。4) 生产陷阱?——所有阻塞共享默认池;池无上限任务堆积;线程池被取消语义误解(无法真取消)。

---
