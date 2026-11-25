---
title: "[Q5764] Future/Task 的异常谁消费：never retrieved 与回调异常归因"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5764 · Future/Task 的异常谁消费：never retrieved 与回调异常归因

难度：P6 ｜ 标签：asyncio、Task、Future、异常、never retrieved、fire-and-forget

基线：CPython 3.12.2，纯标准库；用 `create_task`、`add_done_callback`、`gc.collect` 与 asyncio logger 捕获未取异常与回调异常。

**问**：审计服务用 `asyncio.create_task(send_audit(event))` 做 fire-and-forget，任务对象没保存。某次下游 500，任务抛了 `ConnectionError`，业务日志里什么都没有；直到几十分钟后 GC 触发，才在 stderr 看到一条 `Task exception was never retrieved`，此时早已过了告警窗口。另一条链路给任务加了 `add_done_callback`，回调里又抛了 `KeyError`，结果任务本身的异常和回调的异常只出现了一条。Task 的异常到底"被谁消费"了？为什么 fire-and-forget 会静默？回调异常又去了哪？

**答**：

- **结论**：`asyncio.Future`/`Task` 会把异常保存在 `_exception` 里，并设置 `_log_traceback=True`；只有当你通过 `await task`、`task.result()` 或 `task.exception()` **取走**异常时，才清除这个标记。如果直到对象被 GC 都没人取，`Task.__del__` 会用 `asyncio` logger 打一条 `Task exception was never retrieved`，并附上 traceback——这条日志的时机由 GC 决定，可能在几分钟后，不能当告警。`add_done_callback` 的回调只是"通知"，它**不会自动消费**异常：回调里不调用 `task.exception()`，标记仍在；回调自己抛异常，则走 `loop.call_exception_handler`，默认打印 `Exception in callback ...`，和任务异常是两条独立通道。
- **取舍**：fire-and-forget 必须显式做三件事：① **保存强引用**（事件循环只持弱引用，任务可能在完成前被 GC）；② 在 `done_callback` 里调用 `task.exception()` 并记录/告警；③ 在回调结束时从集合里 `discard`，避免泄漏。另一种选择是不做 fire-and-forget，用 `TaskGroup`/`gather` 把子任务纳入父任务的生命周期，异常自然聚合为 `ExceptionGroup`；代价是父任务必须等子任务，吞吐型旁路（审计、埋点）不适合。第三个取舍是"吞异常"：旁路失败不应影响主流程，但必须可观测，正确做法是"捕获 + 计数 + 采样日志"，而不是让异常消失在 GC 里。
- **实战**：事故后加了统一的 `spawn(coro, name)`：创建任务、加入模块级 `set`、`add_done_callback` 里 `discard` 并检查 `task.cancelled()`/`task.exception()`，异常用 `logger.exception` 带 `task.get_name()` 打出。上线一周抓到 37 次审计下游超时，全部在 1 秒内告警；另有一条回调异常被 `call_exception_handler` 捕获后接入 Sentry，才发现是回调里假设 `task.result()` 一定非空。修复后"never retrieved"日志归零。

下面验证三条路径：任务异常无人取 → GC 时打日志；`done_callback` 调用 `exception()` → 不再打；回调自身抛异常 → 走 `loop.set_exception_handler`，任务结果不受影响。

```python
# Task 异常消费: await/result/exception 取走才清除 _log_traceback
import asyncio
import gc
import io
import logging


async def main():
    loop = asyncio.get_running_loop()

    # 捕获 asyncio logger 的 "never retrieved"
    log_buffer = io.StringIO()
    asyncio_logger = logging.getLogger("asyncio")
    asyncio_logger.handlers = [logging.StreamHandler(log_buffer)]
    asyncio_logger.setLevel(logging.DEBUG)
    asyncio_logger.propagate = False

    async def boom():
        raise ValueError("task lost")

    # 1) 创建后不 await、不取异常, 删除引用触发 GC
    task = loop.create_task(boom())
    await asyncio.sleep(0)          # 让任务跑完并保存异常
    del task
    gc.collect()
    text = log_buffer.getvalue()
    print("[1] GC 日志首行:", text.splitlines()[0])
    assert "Task exception was never retrieved" in text
    assert "task lost" in text

    # 2) done_callback 里消费异常 -> 不再打 never retrieved
    log_buffer.seek(0)
    log_buffer.truncate(0)

    async def boom2():
        raise ValueError("consumed")

    task2 = loop.create_task(boom2())
    await asyncio.sleep(0)

    def consume(t):
        exc = t.exception()        # 关键: 取走异常
        print("[2] 回调取到:", type(exc).__name__, exc)

    task2.add_done_callback(consume)
    del task2
    gc.collect()
    print("[3] 消费后日志:", repr(log_buffer.getvalue()))
    assert log_buffer.getvalue() == ""

    # 3) 回调自身抛异常 -> loop.call_exception_handler, 任务结果不受影响
    handler_calls = []
    loop.set_exception_handler(
        lambda lp, ctx: handler_calls.append((ctx["message"], type(ctx["exception"]).__name__))
    )

    async def ok():
        return 42

    task3 = loop.create_task(ok())
    await asyncio.sleep(0)

    def bad_callback(t):
        raise KeyError("callback failed")

    task3.add_done_callback(bad_callback)
    await asyncio.sleep(0.01)
    print("[4] handler 记录:", handler_calls)
    assert handler_calls and handler_calls[0][1] == "KeyError"
    assert "Exception in callback" in handler_calls[0][0]
    print("[5] 任务本身结果仍可读:", task3.result())
    assert task3.result() == 42


asyncio.run(main())
```

**追问一**：`gather(return_exceptions=True)` 会消费异常吗？—— 会。它把每个子任务的异常作为结果收集起来，等价于对每个子任务调用了 `exception()`，所以不会触发 `never retrieved`；但这也意味着异常被"降级"成返回值，调用方必须自己检查哪个结果是异常，否则同样会静默。`gather()` 默认（`return_exceptions=False`）在第一个异常时向父任务抛出，但**其他子任务不会被取消**，它们后续的异常仍可能进入 `never retrieved`，除非你显式取消并等待。

**追问二**：为什么事件循环只持任务的弱引用？—— 这是为了避免"任务永远不被回收"：如果 loop 强引用所有 task，任何忘记 `await` 的任务都会泄漏到进程结束。弱引用带来的是"必须自己保活"的责任：fire-and-forget 要把 task 放进集合/字典，并在 done callback 里移除；否则任务可能在执行中途被 GC，出现 `Task was destroyed but it is pending!`。这也是 `asyncio.create_task` 文档反复强调"保存引用"的原因。

## 背诵要点

- 异常只有被 `await`/`result()`/`exception()` 取走才清除标记；否则 GC 时打 `Task exception was never retrieved`，时机不可控。
- `add_done_callback` 不会自动消费异常；回调自身异常走 `loop.call_exception_handler`，与任务异常是两条通道。
- fire-and-forget 三件套：保存强引用、done callback 取异常并告警、回调里 discard 防泄漏。

## 复盘追问

- 为什么 `gather(return_exceptions=False)` 仍可能产生 never retrieved？（第一个异常抛出后其他子任务继续跑，没人取它们的异常）
- `Task was destroyed but it is pending!` 和 `never retrieved` 分别对应什么？（前者是任务没跑完就被 GC；后者是跑完了但异常没人取）
