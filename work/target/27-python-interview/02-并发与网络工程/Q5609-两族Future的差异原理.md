---
title: [Q5609] 两族 Future 的差异原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5609 · asyncio.Future 与 concurrent.futures.Future 差异原理

> 难度:★★★★☆ | 标签:原理深挖, Future, 跨界

**问**:名字都叫 Future，`asyncio.Future` 和 `concurrent.futures.Future` 能混用吗？桥在哪、坑在哪？

**答**:结论：两个类同名不同命——`concurrent.futures.Future` 是**线程侧**结果句柄（`executor.submit` 返回，`add_done_callback` 在完成时于执行线程同步调用），`asyncio.Future` 是**loop 侧**可 await 对象（回调被 `call_soon` 调度回事件循环线程）。它们不互认：把一个塞给另一个的 API 直接报错或死等。桥接层：`asyncio.wrap_future()`（线程 Future → 可 await）、`asyncio.run_coroutine_threadsafe(coro, loop)`（协程 → 线程侧返回 concurrent Future，Q598/Q2406）、`loop.run_in_executor()`（内部自动 wrap）。原理差异的根子在调度模型：loop Future 的完成必须"回到循环"，线程 Future 的完成发生在任意线程——这正是 `run_coroutine_threadsafe` 必须存在的原因。坑点：`add_done_callback` 在 executor.Future 上是**回调线程**执行，抛异常没人接；在 asyncio.Future 上是 loop 里执行，异常进异常处理器。

```python
import asyncio, concurrent.futures as cf

def io_work(x):
    return x * 2

async def main():
    loop = asyncio.get_running_loop()

    # 1) executor 的线程 Future 经 run_in_executor 自动桥接
    fut = loop.run_in_executor(None, io_work, 21)     # 返回 wrap 后的可 await 对象
    print("线程 Future 桥接:", await fut)

    # 2) 协程跨界给线程：run_coroutine_threadsafe 得到 concurrent.futures.Future
    #    注意必须从"别的线程"调用；在同一线程里 .result() 会等死自己
    import threading
    async def coro():
        await asyncio.sleep(0)
        return "from-loop"
    holder = {}
    def from_thread():
        cf_fut = asyncio.run_coroutine_threadsafe(coro(), loop)
        holder["r"] = cf_fut.result(timeout=5)          # 阻塞的是 worker 线程，不影响 loop
    t = threading.Thread(target=from_thread); t.start()
    for _ in range(50):                       # 等线程结果期间必须让出 loop
        if "r" in holder:
            break
        await asyncio.sleep(0.05)
    print("线程侧拿 loop 结果:", holder.get("r"))

    # 3) 直接互用会翻车：await 一个线程 Future 类型
    ex = cf.ThreadPoolExecutor()
    raw = ex.submit(io_work, 1)
    print("raw 类型:", type(raw).__module__, type(raw).__name__, "≠ asyncio.Future")
    ex.shutdown()

asyncio.run(main())

# 对比：两族的回调执行线程
f2 = cf.ThreadPoolExecutor().submit(int)
f2.add_done_callback(lambda f: print("executor 回调在执行线程里同步跑"))
f2.exception()
```

**追问一层**:`wrap_future` 内部做了什么？为什么不能直接把 concurrent.Future 塞进 `await`？
**追二维**:两个 Future 的 cancelled/cancel 语义差异在哪（asyncio 的 cancel 会触发取消传播，concurrent 的呢）？

**背诵要点**
- 线程 Future：完成于执行线程，add_done_callback 同步直调；loop Future：完成必须回事件循环。
- 桥接三 API：run_in_executor、wrap_future、run_coroutine_threadsafe。
- 混用不互认：直接 await 线程 Future 无效，跨界必须过桥。

**复盘追问**
- 回调闭包在 executor.Future 里抛异常为什么"无声"？提示：回调异常只打印不进 result。
- 混合架构（线程池+loop）里如何统一超时语义？提示：线程侧用 result(timeout)，loop 侧用 asyncio.timeout（Q5505）。
