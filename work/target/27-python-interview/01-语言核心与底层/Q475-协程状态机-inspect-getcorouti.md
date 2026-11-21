---
title: [Q475] 协程状态机:inspect.getcoroutinestate
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q475 · 协程状态机:inspect.getcoroutinestate

> 难度:★★★☆ | 标签:协程, inspect

**问**:协程对象有哪几种状态?如何在不运行它的情况下观察它在哪挂起?

**答**:原生协程有四个状态:CORO_CREATED(已创建未启动)、CORO_RUNNING(正在执行)、CORO_SUSPENDED(挂在 await 上)、CORO_CLOSED(已结束)。inspect.getcoroutinestate 读取状态;inspect.getcoroutinelocals 看挂起帧的局部变量;coro.cr_frame 是底层帧对象。状态机是单向的:created → running ⇄ suspended → closed,且协程是一次性对象,closed 后不能复用。调试事件循环卡死时,「哪些协程处于 SUSPENDED、挂在哪个 await」是关键线索。

```python
# file: code/01_语言核心与底层/q475_coroutine_states.py
import inspect
import types

@types.coroutine
def suspend_once():
    yielded = yield "suspended"           # 挂起点
    return "wake value"

async def worker():
    got = await suspend_once()
    return f"got {got}"

if __name__ == "__main__":
    coro = worker()
    print(inspect.getcoroutinestate(coro))   # CORO_CREATED
    print(coro.send(None))                   # 穿透 yield,协程挂起
    print(inspect.getcoroutinestate(coro))   # CORO_SUSPENDED
    try:
        coro.send("resumed")
    except StopIteration as stop:
        print("result:", stop.value)
    print(inspect.getcoroutinestate(coro))   # CORO_CLOSED
```

**追问**:1) closed 的协程再 send 会怎样?——RuntimeError: cannot reuse already awaited coroutine;协程不是可重置对象,重试必须重新调用协程函数。2) 协程状态与 Task 状态什么关系?——Task 是协程的调度壳,有自己的 pending/cancelled/finished 状态,内部协程独立走 created/suspended/closed 状态机;SUSPENDED 的协程一定挂在某个 await 链上,沿 cr_await 可看到它在等谁。3) 如何观察挂起位置?——coro.cr_frame 是底层帧,f_lineno 即当前行、f_locals 即局部变量,inspect.getcoroutinelocals 是包装;aiomonitor/调试器都基于这条链做「协程在哪一行等谁」的展示。4) 生产陷阱?——诊断「事件循环卡死」只会 dump 线程栈看不到协程挂起点,要开 loop.set_debug(True) 并定期巡检 pending task;同一协程对象 await 两次第二处报 cannot reuse,重试要重建协程。
