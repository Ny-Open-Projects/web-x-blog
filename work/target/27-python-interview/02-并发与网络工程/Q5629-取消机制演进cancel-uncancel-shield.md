---
title: [Q5629] 取消机制演进：cancel(msg)、uncancel 与 shielding
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5629 · 取消机制演进：cancel(msg)、uncancel 与取消计数（3.9→3.11→3.12）

> 难度:★★★★☆ | 标签:版本演进, asyncio, 取消语义

**问**:3.11 为什么要给 Task 加 `uncancel()` 和"取消计数"？`Task.uncancel()` 是给业务代码调的吗？`asyncio.shield` 与 `Task.uncancel` 的语义边界在哪？写出"捕获取消后继续收尾"代码的两个版本（旧式 vs 结构化并发）。

**答**:结论：演进脉络三步：a) **3.9**：`Task.cancel(msg)` 支持给 CancelledError 带上下文，便于排障；b) **3.11**：结构化并发（TaskGroup/timeout）需要区分"谁取消了谁"——引入**取消计数** `cancelling()/uncancel()`：外层 scope 取消子任务时计数 +1，子任务的收尾代码里若因**自己的**清理逻辑再次 await 被取消，计数会错乱，所以规定"仅在捕获 CancelledError 的地方"由框架配对调用 uncancel；**业务代码不应该调 uncancel**——那是框架（TaskGroup/timeout）的职责，手动调会破坏取消传播（这是 3.11+ 最常见的误用）。c) `asyncio.shield`：保护"内部协程不被外部取消波及"，但外层 Future 仍立即抛 CancelledError——shield 保护的是协程不是等待者。3.12 后建议：清理逻辑直接用 TaskGroup/timeout 上下文，取消语义由框架配对管理，`uncancel` 只出现在库源码里。

```python
import asyncio

# ---- 1) 取消计数的基本语义 ----
async def child():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("child 被取消, cancelling =", asyncio.current_task().cancelling())
        raise                                # 必须重抛：吞取消会破坏结构化并发

async def main():
    t = asyncio.create_task(child())
    await asyncio.sleep(0.05)
    t.cancel("演示取消")
    try:
        await t
    except asyncio.CancelledError as e:
        print("main 捕获取消, msg =", e.args)

asyncio.run(main())

# ---- 2) uncancel 的归属：框架配对，业务勿调（演示框架视角） ----
async def framework_style():
    """模拟框架：进入保护区前记录计数，清理完成后配对 uncancel。"""
    task = asyncio.current_task()
    task.uncancel()                          # 框架在'取消已处理'后配对调用
    await asyncio.sleep(0)                   # 清理期间的 IO
    print("清理完成, cancelling =", task.cancelling())
    # 注意: 这里不重抛是因为演示'框架接管取消'的语义; 业务代码必须重抛

asyncio.run(asyncio.wait_for(framework_style(), 0.05))

# ---- 3) shield：保护协程不被取消，但等待者立刻被打断 ----
async def inner():
    await asyncio.sleep(0.2)
    return "inner-done"

async def demo_shield():
    it = asyncio.ensure_future(inner())
    try:
        await asyncio.wait_for(asyncio.shield(it), 0.05)
    except asyncio.TimeoutError:
        pass
    print("等待者 0.05s 被打断, 内部协程仍在跑:", await it)

asyncio.run(demo_shield())

# ---- 4) 错误示范：吞取消（必须重抛） ----
async def swallow():
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        return "swallowed"                   # 反面教材: TaskGroup 会报 uncancel 不配对/取消丢失

asyncio.run(asyncio.wait_for(swallow(), 0.05) if False else asyncio.sleep(0))
print("规则: except CancelledError 只能做清理然后 raise; 框架类(TimeoutError)与取消(3.11+)已分流")
```

**追问一层**:为什么 `cancelling()` 返回的是计数而不是布尔？（嵌套 scope 场景：多个外层（timeout 包 TaskGroup）都可能取消同一任务，配对 uncancel 才能在多层 scope 下正确判断"是否还有未处理的取消"）。
**追问二层**:`wait_for` 在 3.11+ 超时时任务未真正取消完成会怎样？（wait_for 会等待取消完成再抛 TimeoutError；若任务吞取消，wait_for 挂死风险由 `asyncio.timeout` 重写解决——它用 uncancel 配对保证 scope 退出即恢复）。
**追问三层**:库作者何时才该手动调 uncancel？（实现"取消后必须完成一段不可中断清理"的框架语义时；且必须在文档中声明该区域吞掉了哪次取消，等价于自己承担 TaskGroup 的配对职责）。

## 背诵要点
- 演进：3.9 cancel(msg) → 3.11 cancelling()/uncancel() 取消计数 + timeout/TaskGroup → 3.12 结构化并发成为默认范式。
- `uncancel` 是框架配对调用，业务代码只做"清理 + raise"；吞取消会破坏传播与计数配对。
- shield 保护内部协程不被取消、不保护等待者（立即抛取消/超时）；与 Q5516 取消风暴、Q5505 timeout 嵌套互为表里。

## 复盘追问
- 升级 3.11 后出现 "Task was destroyed but it is pending" 变多，如何定位到"吞取消 + 手动 uncancel"的组合误用？
- 设计一个"取消后必须完成审计落库"的组件：用 TaskGroup 与 shield 两种方案各写一版并比较取消语义。
