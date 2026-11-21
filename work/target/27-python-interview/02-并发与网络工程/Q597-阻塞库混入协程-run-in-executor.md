---
title: [Q597] 阻塞库混入协程:run_in_executor 的正确姿势
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q597 · 阻塞库混入协程:run_in_executor 的正确姿势

> 难度:★★★☆ | 标签:run_in_executor, 阻塞, 混合栈

**问**:手头只有一个同步 SDK(阻塞 50ms),在 async 服务里直接调用会怎样?怎么改造成本最低?

**答**:直接调用会阻塞整个事件循环 50ms,期间所有协程(包括心跳、其他请求)全部冻结,这是 async 服务最常见的性能事故。改造成本最低的方案是 `loop.run_in_executor`:把阻塞调用丢进线程池,协程 await 它,循环继续跑别的任务;SDK 线程安全性未知时,给每个调用加 threading.Lock 或用单线程 executor 串行化。对于 CPU 密集的同步代码,换 ProcessPoolExecutor。判断口诀:阻塞 IO → to_thread,CPU → process pool,能改异步原生 → 最好。

```python
# file: code/02_并发与网络工程/q597_blocking_in_async.py
import asyncio
import threading
import time


class LegacySDK:
    """模拟只提供同步接口的第三方 SDK。"""

    def __init__(self) -> None:
        self._lock = threading.Lock()  # 线程安全性未知时按不安全处理
        self.calls = 0

    def blocking_query(self, key: str) -> str:
        with self._lock:
            time.sleep(0.05)  # 阻塞 50ms
            self.calls += 1
            return f"value-of-{key}"


async def main() -> None:
    sdk = LegacySDK()
    loop = asyncio.get_running_loop()

    # 错误姿势: 直接调用, 冻结事件循环 — 用心跳协程观察
    heartbeat_ticks = [0]

    async def heartbeat() -> None:
        while True:
            heartbeat_ticks[0] += 1
            await asyncio.sleep(0.01)

    hb = asyncio.create_task(heartbeat())
    t0 = time.perf_counter()
    sdk.blocking_query("direct")  # 阻塞 50ms, 心跳完全停止
    direct_dt = time.perf_counter() - t0
    ticks_during_direct = heartbeat_ticks[0]
    print(f"直接调用 {direct_dt * 1000:.0f}ms, 期间心跳仍在: {ticks_during_direct > 0}")

    # 正确姿势: run_in_executor + 显式线程池 (线程安全未知时按串行化处理)
    from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix="sdk")
    t0 = time.perf_counter()
    results = await asyncio.gather(
        *[loop.run_in_executor(executor, sdk.blocking_query, f"k{i}")
          for i in range(3)]
    )
    par_dt = time.perf_counter() - t0
    hb.cancel()
    print(f"executor 并行 3 次: {par_dt * 1000:.0f}ms (约等于单次耗时)")
    print("结果:", results)
    executor.shutdown()


asyncio.run(main())
```

**追问**:1) to_thread 和 run_in_executor 选哪个?——to_thread 是 3.9+ 的一步到位封装(用默认 executor),简单场景首选;需要自定义线程数/命名/复用池时用 run_in_executor + 显式 ThreadPoolExecutor。2) 正确姿势的完整清单?——默认 executor 线程数有限(min(32, cpu+4),Q599);阻塞调用永远不裸放进循环;CPU 密集用进程池;混用线程要处理 GIL 对纯 Python 的限制(Q576);异常经 Future 回传(Q565)。3) 与取消的边界?——线程内任务无法真正取消(await 取消只是不等它);长期阻塞调用要有自身超时。4) 生产陷阱?——默认 executor 被长任务占满饿死其他 to_thread;阻塞库(ORM 同步驱动)直接 await;线程内再操作循环对象。

---
