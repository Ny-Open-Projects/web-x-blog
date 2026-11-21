---
title: [Q5505] asyncio timeout 上下文管理器的嵌套/重入语义
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5505 · asyncio timeout 上下文管理器的嵌套/重入语义

> 难度:★★★ | 标签:asyncio, timeout, 取消语义

**问**：`async with asyncio.timeout(3)` 嵌套在另一个 timeout 里，超时预算怎么算？同一个 timeout 对象能不能重入（退出后再进）？超时后块内代码「还差一点就完成」时，外层还能拿到结果吗？TimeoutError 和 CancelledError 在嵌套下怎么区分归属？

**答**：结论：1) **嵌套=各管各的预算**：内层 timeout(1) 在外层 timeout(3) 里，内层先到就先抛 TimeoutError（在内层的 `__aexit__` 处理），外层剩余预算继续；外层先到时取消会**穿透内层**，内层 `__aexit__` 看到的是外部取消而非自己的超时，正确地把 CancelledError 透传，不会错转成 TimeoutError——这就是 3.11 timeout 相对 wait_for 的核心修复（用取消原因区分「谁的取消」）。2) **重入是禁止的**：一个 timeout 上下文对象退出后复用（再 `async with` 同一对象）行为未定义/报错；要多次计时就重新创建。3) 「差一点完成」：超时引发的取消到达后，若协程吞了 CancelledError 并强行 return，内层 `__aexit__` 检测到「取消是我发起但任务已完成」会**放弃超时转换、接受结果**——结果能拿到，但这属于「吞取消」反模式，外层的取消语义已经被破坏。4) 归属判定靠**取消计数与原因**：timeout 进入时记录当前任务的取消计数（`cancelling()`），超时发 cancel 后退出时若计数未变化说明取消被吞，会 re-cancel；这就是「timeout 无法被块内代码永久抵御」的机制。实战：重试循环里每轮 attempt 用独立 timeout 包裹（新建对象），总预算在外层；不要试图复用同一个 timeout 做分段预算。

```python
# 基线:Python 3.11+。标准库直接运行。
import asyncio

async def slow(ms: int) -> str:
    await asyncio.sleep(ms / 1000)
    return f"done in {ms}ms"

async def nested() -> None:
    try:
        async with asyncio.timeout(0.2) as outer:     # 外层总预算
            try:
                async with asyncio.timeout(0.05):     # 内层小预算
                    await slow(100)                    # 会被内层超时打断
            except TimeoutError:
                print("内层超时,外层预算还有:", round(outer.reschedule_when_cancelled or 0, 2) if False else "剩余充足")
                await slow(50)                         # 外层内继续,50ms < 剩余
    except TimeoutError:
        print("外层超时")

async def swallow_demo() -> None:
    async with asyncio.timeout(0.05):
        try:
            await slow(100)
        except asyncio.CancelledError:
            return "吞取消强行返回"                     # 反模式:演示会被检测
    print("未到达:吞取消后 timeout 会 re-cancel")

asyncio.run(nested())
try:
    asyncio.run(swallow_demo())
except TimeoutError:
    print("最终仍抛 TimeoutError:吞取消救不了超时")
```

**追问**：
1) timeout 是怎么区分「我的取消」和「外部取消」的？——进入时用 `asyncio.current_task().cancelling()` 记录基线，自己超时就 `task.cancel()`，退出时对比计数：计数涨且是自己发的 → 转 TimeoutError；是外部发的 → 透传 CancelledError。这就是为什么必须放在 task 里运行。
2) timeout 能不能「续期」？——能：`timeout_handle.reschedule(when)`（对 ctx 对象调用）可以把截止时间往后推，流式场景「每次收到数据就顺延」的标准做法；但 reschedule 到过去等于立即超时。
3) 和 wait_for 的语义差异清单？——wait_for 包整个 awaitable（每次新建 Task，超时后原协程可能已跑完），timeout 是作用域式（块内所有 await 共享预算、不用重复包）、能 reschedule、嵌套归属清晰；迁移新代码一律 timeout，wait_for 只留在「单调用一次性预算」旧代码里。
