---
title: [Q598] 跨线程投递协程:run_coroutine_threadsafe
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q598 · 跨线程投递协程:run_coroutine_threadsafe

> 难度:★★★★ | 标签:asyncio, 线程混用, 线程安全

**问**:一个普通线程拿到了计算结果,怎么安全地交给 asyncio 侧处理并拿到返回值?

**答**:用 `asyncio.run_coroutine_threadsafe(coro, loop)`:它把协程包装后通过 `call_soon_threadsafe` 投递到事件循环线程执行,返回 concurrent.futures.Future(不是 asyncio.Future),普通线程可以直接 `.result(timeout=)` 阻塞等待。方向反过来是 `loop.call_soon_threadsafe` 调普通函数。铁律有三:绝不能在其他线程直接调 loop 的非 threadsafe 方法;协程对象只能在所属循环里驱动,跨线程传递的是"待执行的协程"而不是"执行中的协程";主协程绝不能 `t.join()` 干等投递线程——join 会阻塞事件循环线程,线程侧 `result()` 又要等 loop 派发结果,自己把自己锁死到超时,循环侧要用 `while t.is_alive(): await sleep` 让出控制权。另外 3.9 里 `concurrent.futures.TimeoutError` 与内建 `TimeoutError` 是两个类,except 写错会漏接直接炸线程(3.11 才合并)。典型场景:回调式 SDK 的回调线程与主循环交互。

```python
# file: code/02_并发与网络工程/q598_threadsafe.py
import asyncio
import concurrent.futures
import threading

table: dict = {}


async def update_and_read(key: str) -> int:
    await asyncio.sleep(0.01)  # 模拟异步处理
    table[key] = table.get(key, 0) + 1
    return table[key]


def callback_thread(loop, n: int) -> None:
    """模拟第三方 SDK 的回调线程。"""
    for i in range(n):
        fut = asyncio.run_coroutine_threadsafe(update_and_read(f"k{i % 3}"), loop)
        try:
            value = fut.result(timeout=2)  # concurrent.futures.Future
            print(f"[thread] 回调 {i} 处理完成, 值={value}")
        except concurrent.futures.TimeoutError:
            # 3.9 里它不是内建 TimeoutError, 捕错类型会漏接并炸掉线程
            print("[thread] 投递超时: loop 卡死或未运行")


async def main() -> None:
    loop = asyncio.get_running_loop()
    t = threading.Thread(target=callback_thread, args=(loop, 6))
    t.start()
    # 同时 loop 自己也在跑别的协程, 证明共享同一个循环。
    # 不能直接 t.join(): join 阻塞事件循环线程, 线程侧 fut.result()
    # 就永远等不到派发, 自我死锁到超时; 循环侧必须让出控制权轮询。
    while t.is_alive():
        await asyncio.sleep(0.01)
    t.join()
    print("最终 table:", table)
    assert all(v == 2 for v in table.values()), "每个 key 被处理 2 次"


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) futures.Future 和 asyncio.Future 能互相转吗?——asyncio.wrap_future 可以把前者包成后者,反之用 asyncio.futures._chain_future;日常记"跨线程边界用 futures.Future,循环内用 asyncio.Future"即可。2) run_coroutine_threadsafe 的契约?——从线程投递协程到循环,返回 concurrent.futures.Future(线程侧可 result(timeout));循环侧正常执行;这是线程→异步的唯一正门(Q600)。3) 结果回传的双 Future 设计?——线程侧等 concurrent Future;循环侧 asyncio Future 由 _chain_future 桥接;超时与取消的语义差异(线程侧 cancel 不一定能停循环内任务)。4) 生产陷阱?——在线程里 await(语法/语义都不成立);拿 asyncio.Future 跨线程 result() 死等;取消语义误解。

---
