---
title: [Q076] asyncio 的 Lock / Semaphore / Queue
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q076 · asyncio 的 Lock / Semaphore / Queue

> 难度:★★★ | 标签:asyncio, Lock, Semaphore, Queue

**问**:asyncio.Lock 和 threading.Lock 能混用吗?asyncio.Queue 适合什么场景?

**答**:不能混用:threading.Lock 的 acquire 是阻塞线程的,会卡死事件循环;asyncio.Lock 在协程内 await 加锁,排队时不阻塞线程。同理,协程间通信用 asyncio.Queue(put/get 都是协程),跨线程投递任务则用 `loop.call_soon_threadsafe` 或 run_coroutine_threadsafe。典型场景是限制对下游的并发请求数、单飞(single-flight)缓存。

```python
# file: code/02_并发与网络工程/q076_async_lock_sem_queue.py
import asyncio


async def limited_call(i: int, sem: asyncio.Semaphore) -> int:
    async with sem:  # 最多 2 个并发
        print(f"请求 {i} 发出")
        await asyncio.sleep(0.2)
        return i * 2


async def single_flight(key: str, lock: asyncio.Lock, cache: dict) -> str:
    async with lock:
        if key not in cache:
            print(f"计算 {key}")
            await asyncio.sleep(0.2)
            cache[key] = f"value-{key}"
        return cache[key]


async def main() -> None:
    sem = asyncio.Semaphore(2)
    results = await asyncio.gather(*(limited_call(i, sem) for i in range(5)))
    print("限流结果:", results)

    lock = asyncio.Lock()
    cache: dict[str, str] = {}
    vals = await asyncio.gather(*(single_flight("k1", lock, cache) for _ in range(3)))
    print("单飞结果:", vals)

    q: asyncio.Queue[int] = asyncio.Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    print("队列已满, 再 put 会等待, 当前 qsize:", q.qsize())
    print("get:", await q.get(), await q.get())


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- asyncio.Lock 能跨线程用吗?——不能,它是事件循环内的协程同步原语;跨线程唤醒要 `loop.call_soon_threadsafe` 投递回循环线程。
- asyncio.Semaphore 的典型用法?——`async with sem:` 把对下游的并发限制在 N 以内,超出排队而非报错,是爬虫/网关标配。
- 在协程里误用 threading.Lock 会怎样?——acquire 阻塞整个事件循环线程,所有协程停摆;这是异步代码的第一类事故。

---
