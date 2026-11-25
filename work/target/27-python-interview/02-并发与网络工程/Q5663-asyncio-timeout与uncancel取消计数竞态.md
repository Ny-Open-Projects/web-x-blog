---
title: "[Q5663] asyncio.timeout 与 uncancel 取消计数竞态"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5663 · asyncio.timeout 与 uncancel 取消计数竞态

难度：P7 ｜ 标签：asyncio.timeout、uncancel、cancelling、取消计数、超时失效

**问**：`asyncio.timeout()` 是用"到点 `task.cancel()`"实现的，这和对 Task 手动 `cancel()`/`uncancel()` 的 API 在同一套计数上打架——在 `async with asyncio.timeout(...)` 块里捕获 `CancelledError` 后调用 `current_task().uncancel()`，超时还会生效吗？`task.cancelling()` 这个计数到底记录了什么、为什么需要"计数"而不是布尔标志？要延长截止时间，正确做法是 `uncancel()` 还是 `Timeout.reschedule()`？

**答**：
结论：`asyncio.timeout` 的到期动作就是**对当前 Task 调用 `cancel()`**，并把"这是我发的取消"记账在 Task 的取消计数里；它在 `__aexit__` 时检查"取消是否由我且未被消费"，是则抛 `TimeoutError`、否则把 `CancelledError` 原样放过。一旦你在块内捕获 `CancelledError` 并调用 `uncancel()`，计数被清零，`timeout` 在退出时**看不到自己的取消痕迹**——结果就是超时被"静默解除"，块内代码可以在超过 deadline 后继续跑，既不抛 `TimeoutError` 也不抛 `CancelledError`。这是"超时失效"事故最隐蔽的一类：表面看超时配置正确，实则被业务代码里的 `uncancel`（常见于 `finally` 清理、`asynccontextmanager` 的退出处理、或第三方库"吞取消"）抵消了。取消计数而非布尔，是因为 Task 可能被多方重复取消又部分消费（`cancelling()` 返回尚未被 `uncancel()` 抵消的次数），`task.cancel()` 每调用一次计数 +1。

取舍：要"延长 deadline"必须用 `async with asyncio.timeout(...) as cm:` 拿到 Timeout 对象，调 `cm.reschedule(loop.time() + new_budget)`——它只改截止时间、不碰取消计数，语义干净；绝不用 `uncancel()` 去"假装没超时"。在库代码里**不要随意 `uncancel()`**：它只应在你明确"消费掉自己发出的那次取消"时使用（如实现 `wait_for` 语义），并且要成对管理计数。给关键超时加一层"墙钟兜底"（外层再套一个不可被内层 uncancel 影响的大 timeout 或 `asyncio.wait_for`），防止内层被抵消后无限挂住。

实战：事故形态是"接口配了 200ms timeout，偶发请求跑了几秒才返回且没有超时日志"——排查看 timeout 块内有没有 `except CancelledError: ... uncancel()` 或把取消吞掉的助手函数。下面跑出对照：正常超时抛 `TimeoutError`，而在块内 `uncancel()` 后超时被解除、代码越过 deadline 继续执行。

```python
import asyncio

async def normal():
    print("=== normal timeout ===")
    try:
        async with asyncio.timeout(0.02):
            await asyncio.sleep(10)
    except TimeoutError:
        print("  TimeoutError as expected")

async def defeated():
    print("=== uncancel defeats timeout ===")
    try:
        async with asyncio.timeout(0.05) as cm:
            loop = asyncio.get_running_loop()
            print("  deadline in:", round(cm.when() - loop.time(), 3), "s")
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                t = asyncio.current_task()
                print("  cancelling():", t.cancelling())
                t.uncancel()                       # 清零 -> timeout 看不到自己的取消
                print("  after uncancel:", t.cancelling())
                await asyncio.sleep(0.1)
                print("  kept running past deadline -> timeout defeated")
    except TimeoutError:
        print("  TimeoutError")
    except asyncio.CancelledError:
        print("  CancelledError")
    else:
        print("  no exception at all")

async def reschedule():
    print("=== reschedule (正确延长) ===")
    try:
        async with asyncio.timeout(0.02) as cm:
            await asyncio.sleep(0.01)
            cm.reschedule(asyncio.get_running_loop().time() + 0.2)  # 延长
            await asyncio.sleep(0.05)
            print("  finished within extended budget")
    except TimeoutError:
        print("  TimeoutError")

async def main():
    await normal()
    await defeated()
    await reschedule()

asyncio.run(main())
```

**追问一**：为什么 `cancelling()` 是计数而不是布尔——举一个需要"部分消费"取消的场景？——比如一个任务被上下游各 `cancel()` 一次（计数 2），内部某个可取消的子操作只该消费其中一次（调一次 `uncancel()`，计数变 1），任务整体仍应保持"已取消"状态直至完全退出；布尔无法表达"取消来源被部分吸收"。`asyncio.timeout` 正是靠"发出时计数 +1、退出时比对计数是否回到自己的净值"来判断超时是否该抛 `TimeoutError`。

**追问二**：第三方库在 `finally` 里 `uncancel()` 为什么是危险行为？——它可能是在实现自己的"吞取消"语义（如 `wait_for` 想返回 partial result），但它无法知道外层还有没有 `timeout`/`TaskGroup` 也在用同一个取消计数；一次 `uncancel()` 会把外层的取消凭证一并抹掉，导致外层超时/取消判定失效。正确做法是库只消费**自己发出**的取消（记录发出前后的计数差），并文档化取消语义，而不是无条件清零。

## 背诵要点
- `asyncio.timeout` 靠到点 `task.cancel()` + 退出时检查取消计数归属决定是否抛 `TimeoutError`。
- 块内 `except CancelledError` 后 `uncancel()` 会清零计数 → timeout 失效、代码越过 deadline 继续跑。
- 延长 deadline 用 `Timeout.reschedule()`，不用 `uncancel()`；库代码别无条件 uncancel，外层加墙钟兜底。

## 复盘追问
- 接口配了 200ms timeout 却偶发跑几秒且无超时日志，如何用取消计数视角定位？（块内 uncancel/吞取消排查、`cancelling()` 观测、外层墙钟兜底，讨论第三方库的取消语义）
- 为什么"取消用计数而非布尔"对 timeout 与 TaskGroup 共存是必要的？（多方取消/部分消费语义，讨论取消凭证归属判定）
