---
title: [Q582] Task 的创建流程:create_task 之后发生了什么
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q582 · Task 的创建流程:create_task 之后发生了什么

> 难度:★★★☆ | 标签:asyncio, Task, 调度

**问**:asyncio.create_task 返回时,协程运行了吗?ensure_future 和 create_task 到底什么关系?

**答**:没有。create_task 把协程包成 Task,Task.__init__ 里 call_soon(self.__step) 把第一次执行排进就绪队列,然后立刻返回 Task 对象——真正开始跑要等当前协程让出控制权(遇到 await 或 main 结束当前迭代)。ensure_future 是更老更泛化的 API:传协程就转 Task(等价 create_task),传 Future 就原样返回,传 awaitable 就包装;新代码统一用 create_task。推论:创建后必须保存引用并尽快 await,否则任务可能被 GC 或异常无人收割(见 Q603)。

```python
# file: code/02_并发与网络工程/q582_task_create.py
import asyncio

trace = []


async def job(name: str) -> str:
    trace.append(f"run:{name}")
    return name.upper()


async def main() -> None:
    t = asyncio.create_task(job("A"))
    trace.append("created")
    print("创建后 Task 状态:", "已调度未运行" if not t.done() else "?")

    await asyncio.sleep(0)  # 让出控制权: Task 的第一步 __step 此时才执行
    print("sleep(0) 后 trace:", trace)

    result = await t
    trace.append(f"awaited:{result}")
    print("最终 trace:", trace)

    # ensure_future 对三种输入的行为
    coro = job("B")
    t2 = asyncio.ensure_future(coro)   # 协程 → Task
    fut = asyncio.ensure_future(t2)    # Task → 原样返回
    print("ensure_future(Task) 返回同一对象:", fut is t2)
    print("ensure_future 结果:", await t2)


asyncio.run(main())
```

**追问**:1) 为什么 async 函数直接调用(不 await)只会得到警告而不执行?——调用 async 函数只是创建协程对象,不进入函数体;没人 await 它就会触发 "coroutine was never awaited" 警告并泄漏。2) create_task 的完整流程?——loop.create_task(coro):包装 Task→call_soon(__step)→进入就绪队列;Task 持强引用(必须自己再存,Q603 的 GC 陷阱);异常在 result 收取或 Task 异常处理器(Q1561)。3) ensure_future 与 create_task?——ensure_future 接受 awaitable(Future 直接返回,协程包 Task);create_task 只接协程(3.10+ 起推荐)。4) 生产陷阱?——未 await 的协程(无声丢弃);create_task 后不持引用被 GC;在非异步上下文调 create_task RuntimeError。

---
