---
title: "[Q5700] create_task 的 contextvars 是创建时快照，不是执行时读取"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5700 · create_task 的 contextvars 是创建时快照，不是执行时读取

难度：P7 ｜ 标签：contextvars、create_task、上下文传播、trace_id、后台任务

**问**：请求进来时 `trace_id.set(...)`，然后 `create_task(后台任务())`，紧接着又更新了 `trace_id`，结果后台任务日志里打的是**旧值**。协程不是"运行时读取当前上下文"吗？`ContextVar` 的可见性到底按什么边界隔离？`await` 一个普通协程和 `create_task` 有什么区别？

**答**：
结论：每个 Task 在创建时通过 `contextvars.copy_context()` 拿到当前上下文的**快照**，之后在属于自己的 Context 里运行；对父任务后续的 `set()` 不可见，子任务内的 `set()` 也不会回流到父任务。所以"创建 task 之后再改值"不会影响它。直接 `await coro` 则不同：它在**当前** Context 里执行，读到的是最新的值。`asyncio.to_thread`/`run_in_executor` 会复制当前上下文到线程，同样在"提交时"定格。

取舍：a) trace_id 这类"随任务传播"的值，应该在创建 Task **之前**设置好，或者用参数显式传递，别指望后续修改能穿透；b) 需要子任务影响父级状态时，不能用 `ContextVar` 当共享变量，应该用队列/返回值/Future 回传；c) 需要"恢复某个上下文"时用 `contextvars.copy_context().run(fn)`，但注意一个 Context 不能被并发进入（同一 Context 同时被两个线程 run 会抛 `RuntimeError: cannot enter context`）；d) 后台任务要在响应结束后仍带 trace_id，就在创建任务时把它作为参数或闭包捕获，而不是运行时读全局。

实战：事故形态是"网关中间件给每个请求设 trace_id，异步审计任务在响应后落库，日志里一半请求的 trace_id 串到了别的请求——因为任务创建早于中间件对 trace_id 的最终赋值"。下面演示 Task 的快照语义、`await` 的当前上下文语义、子任务修改不回流，以及提交到线程时的复制时机。

```python
import asyncio
import contextvars

trace_id = contextvars.ContextVar("trace_id", default="-")


async def worker(tag):
    await asyncio.sleep(0)
    return f"{tag}={trace_id.get()}"


async def main():
    trace_id.set("req-1")
    task = asyncio.create_task(worker("task"))
    trace_id.set("req-2")                 # 创建之后再改，不影响已建 Task
    print("[1] Task 快照:", await task)

    print("[2] 直接 await 读当前上下文:", await worker("inline"))

    trace_id.set("req-3")

    async def child():
        trace_id.set("child")
        return trace_id.get()

    print("[3] 子任务内 set:", await asyncio.create_task(child()))
    print("[4] 父任务不受影响:", trace_id.get())

    # 线程池：提交时复制上下文
    trace_id.set("req-4")

    def blocking():
        return trace_id.get()

    print("[5] to_thread 复制提交时上下文:", await asyncio.to_thread(blocking))
    trace_id.set("req-5")
    print("[6] 提交后再改不影响线程内:", await asyncio.to_thread(blocking))


asyncio.run(main())
```

**追问一**：为什么 `ContextVar` 不用 `threading.local`？—— `threading.local` 按线程隔离，一个线程里跑多个协程会互相覆盖；`ContextVar` 按"上下文"隔离，`asyncio` 给每个 Task 一份 Context，才能在单线程内正确区分并发请求。这也是为什么 `ContextVar` 的 `set()` 返回 `Token`，可以 `reset(token)` 精确回滚——中间件常靠这个在 `finally` 里恢复现场。

**追问二**：`copy_context()` 之后在子线程 `run`，父线程能改吗？—— 不能，复制之后是两个独立 Context，互不影响；这也意味着"在子线程里 set，父线程看不到"。如果确实要跨线程回传，用 `queue.Queue`/`Future`/`loop.call_soon_threadsafe`。另外同一个 Context 对象不允许被两个线程同时 `run`，会抛 `RuntimeError`，需要每个线程各自 `copy_context()`。

## 背诵要点
- Task 在 `create_task` 时复制上下文快照；创建后再 `set()` 不影响该 Task。
- `await coro` 在当前 Context 执行，读最新值；子任务内 `set()` 不回流父任务。
- `to_thread`/`run_in_executor` 在提交时复制上下文；一个 Context 不能被并发进入。

## 复盘追问
- 后台任务日志里 trace_id 串号，如何从 Task 快照语义解释？（创建早于赋值）
- 需要在响应结束后保留请求上下文，正确做法是什么？（创建前设值 / 显式传参 / copy_context）
