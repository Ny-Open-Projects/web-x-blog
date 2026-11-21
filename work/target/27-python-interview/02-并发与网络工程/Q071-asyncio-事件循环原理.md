---
title: [Q071] asyncio 事件循环原理
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q071 · asyncio 事件循环原理

> 难度:★★★ | 标签:asyncio, 事件循环

**问**:事件循环是怎么工作的?单线程如何实现并发?

**答**:事件循环是单线程调度器:维护就绪回调队列和定时器堆,反复执行"取一个就绪的回调执行到下一个 await 点、向 selector 注册感兴趣的 IO、阻塞等 IO 事件、把完成的 IO 唤醒为就绪回调"这一循环。并发来自协程在 await 处主动让出控制权,本质是协作式调度,任何一个协程长时间不让出,整个循环都会卡住。

```python
# file: code/02_并发与网络工程/q071_event_loop.py
import asyncio


async def worker(name: str, delay: float) -> str:
    print(f"{name} 开始")
    await asyncio.sleep(delay)  # 让出控制权给事件循环
    print(f"{name} 结束")
    return f"{name} 的结果"


async def main() -> None:
    # 三个协程在同一个线程里交错执行
    results = await asyncio.gather(
        worker("A", 0.3),
        worker("B", 0.2),
        worker("C", 0.1),
    )
    print(results)
    print("运行线程:", __import__("threading").current_thread().name)


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:
- 协程和线程的调度差异?——协程是协作式,切换点由 await 显式声明,无锁竞争;线程是抢占式,随时可能被打断,需要锁。
- 事件循环一帧具体做什么?——执行就绪回调到下一个 await、向 selector 注册 IO、阻塞等事件、把完成事件转成回调;理解它才能解释阻塞调用的危害。
- 协程会被抢占吗?——不会,只在 await 处让出;没有 await 的死循环无法被打断,这是协作式调度的根本约束。
- 怎么测量事件循环延迟?——后台协程周期性 `await asyncio.sleep(dt)` 并比较实际耗时与 dt,差值即延迟,可上报为监控指标。
