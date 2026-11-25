---
title: "[Q5769] Task 在第一次调度前被取消：协程体与 finally 都不会执行"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5769 · Task 在第一次调度前被取消：协程体与 finally 都不会执行

难度：P6 ｜ 标签：asyncio、Task、cancel、finally、信号量、资源泄漏

基线：CPython 3.12.2，纯标准库；用 `create_task` 后立即 `cancel()`，对比"未启动"与"已启动一步"两种取消路径的执行事件。

**问**：批处理服务用一个 `asyncio.Semaphore(20)` 控制并发，worker 协程的 `finally` 里 `sem.release()`。压测时发现信号量配额越来越少，最后整个服务卡死；排查发现大量 task 刚 `create_task` 就被上游超时逻辑 `cancel()`，`finally` 一次都没跑。另一条路径是 task 已经 `await sleep(0)` 让出过，取消时 `finally` 正常执行。取消一个还没开始跑的协程，为什么连 `finally` 都不执行？资源应该在哪儿释放？

**答**：

- **结论**：`asyncio.create_task(coro)` 只是把协程包装成 Task 并 `call_soon` 安排第一次 `__step`；如果在这之前调用 `task.cancel()`，Task 会把 `_must_cancel` 置位，等第一次 `__step` 真正运行时，直接把 `CancelledError` 抛给协程——但协程**还没有开始执行**，所以函数体的第一行、`try` 块、`finally` 都不会进入，任务直接进入 cancelled 状态。只有协程至少执行过一次（例如 `await asyncio.sleep(0)` 让出后），取消才会在挂起点注入 `CancelledError`，此时 `finally` 才会执行。换句话说：`finally` 保护的是"已经进入函数体"的资源，保护不了"创建任务时就已经在外部持有"的资源。
- **取舍**：要保证资源释放，有三条路：① **把资源获取放进协程内部**（`async with semaphore:` / `async with conn:`），没启动就没获取，天然无泄漏；② 如果资源必须在外部获取，释放也要放在**外部**（`done_callback` 检查 `task.cancelled()` 后释放，或用 `contextlib.AsyncExitStack` 由创建方管理）；③ 避免"创建即取消"：先让任务跑一步（`await asyncio.sleep(0)`）再暴露取消入口，或使用 `asyncio.shield` 保护关键段。代价分别是"获取时机变晚"、"释放逻辑分散"、"取消延迟"；生产上优先①，其次②。
- **实战**：事故代码是 `await sem.acquire()` 之后 `create_task(worker())`，worker 的 `finally: sem.release()`；上游超时立刻 cancel，worker 没启动，permit 永久丢失。修复：① 改成 worker 内部 `async with sem:`，外部不再 `acquire`；② 对必须在外部获取的资源，注册 `task.add_done_callback(lambda t: sem.release() if t.cancelled() else None)`，并加断言防重复释放；③ 监控 `sem._value`（内部字段，仅诊断）与 `len(asyncio.all_tasks())`，出现配额下降立即告警。上线后 3 天内配额稳定在 20，卡死归零。

下面验证：取消未启动任务时事件只有 `cancelled`、没有 `start/finally`；启动一步后取消会执行 `finally`；以及"外部 acquire + 任务内 finally"导致的信号量泄漏与 `done_callback` 修复。

```python
# 取消未启动的 Task: 协程体与 finally 都不会执行
import asyncio


async def main():
    events = []

    async def work():
        try:
            events.append("start")
            await asyncio.sleep(10)
        finally:
            events.append("finally")

    # 1) create 后立刻 cancel: 协程从未开始
    t1 = asyncio.create_task(work())
    t1.cancel()
    try:
        await t1
    except asyncio.CancelledError:
        events.append("cancelled")
    print("[1] 未启动就取消:", events)
    assert events == ["cancelled"], "协程体和 finally 都不应执行"

    # 2) 先让出一次, 再取消: finally 会执行
    events.clear()
    t2 = asyncio.create_task(work())
    await asyncio.sleep(0)          # 让 t2 跑到 sleep(10) 的挂起点
    t2.cancel()
    try:
        await t2
    except asyncio.CancelledError:
        pass
    print("[2] 启动后取消:", events)
    assert events == ["start", "finally"]

    # 3) 外部 acquire + 任务内 finally: 未启动取消会泄漏 permit
    sem = asyncio.Semaphore(1)
    await sem.acquire()

    async def holder():
        try:
            await asyncio.sleep(10)
        finally:
            sem.release()

    leaked = asyncio.create_task(holder())
    leaked.cancel()
    try:
        await leaked
    except asyncio.CancelledError:
        pass
    print("[3] 泄漏后 locked =", sem.locked(), "value =", sem._value)
    assert sem.locked() is True

    # 4) 修复: 由创建方在 done_callback 里按 cancelled 状态释放
    def release_on_cancel(task):
        if task.cancelled():
            sem.release()

    fixed = asyncio.create_task(holder())
    fixed.add_done_callback(release_on_cancel)
    fixed.cancel()
    try:
        await fixed
    except asyncio.CancelledError:
        pass
    print("[4] 修复后 locked =", sem.locked(), "value =", sem._value)
    assert sem.locked() is False

    print("[5] 结论: 资源获取放协程内, 或由创建方负责释放")


asyncio.run(main())
```

**追问一**：`asyncio.shield(task)` 能防止"创建即取消"吗？—— `shield` 保护的是"外层等待被取消时，内层任务不被取消"，但它不能阻止你直接 `task.cancel()`；而且 `shield` 需要内层任务已经存在并开始调度。对"还没启动就被取消"的场景，`shield` 不是解药；正确做法还是资源归属清晰：谁获取、谁释放，或用 `async with` 让获取与释放成对出现在协程内部。

**追问二**：`eager_task_factory` 能消除这个窗口吗？—— 能把"创建后到第一次执行"的窗口缩短：eager task 会在 `create_task` 调用栈里同步执行到第一个挂起点，因此"创建后立刻取消"时协程已经进入函数体，`finally` 有机会执行。但它改变执行时序（同步执行可能阻塞调用方）、影响上下文与异常传播，不能无脑开启；而且如果协程第一行之前就 `return`，语义也不同。更稳的是不要把"资源释放"押在调度时机上。

## 背诵要点

- `create_task` 后立刻 `cancel`：协程体与 `finally` 都不执行，任务直接 cancelled。
- 至少执行一步后取消：`CancelledError` 在挂起点注入，`finally` 正常执行。
- 资源获取放协程内部（`async with`），或由创建方在 `done_callback` 里按 `cancelled()` 释放。

## 复盘追问

- 为什么"外部 acquire、内部 finally release"在未启动取消时会泄漏？（permit 在任务外获取，释放逻辑在从未进入的协程里）
- 如何判断一个 task 是"没启动就被取消"还是"运行中被取消"？（`task.cancelling()`/回调里检查是否产生过业务事件，或在外层记录启动标志）
