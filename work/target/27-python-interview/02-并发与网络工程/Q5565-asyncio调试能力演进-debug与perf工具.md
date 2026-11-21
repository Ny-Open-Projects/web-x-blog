---
title: [Q5565] asyncio 调试能力演进：debug 模式到新工具
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5565 · asyncio 调试能力演进：debug 模式到新工具

> 难度:★★★★ | 标签:版本演进, asyncio, 调试, 可观测

**问**："这个协程为什么没执行完"是线上最难排查的问题之一。asyncio 的调试能力从 3.x 到 3.12/3.13 演进了哪些？debug 模式、slow callback 日志、Task 装饰器、asyncio新工具各解决什么问题？生产上怎么组合？

**答**：按版本演进梳理：a) **3.4-3.6 原始态**：没 debug，回调异常靠 `loop.call_exception_handler`，未 await 的协程只给 "coroutine was never awaited" 警告；b) **3.7 debug 模式成型**：`asyncio.run(main(), debug=True)` / `PYTHONASYNCIODEBUG=1`——开启三件事：**慢回调日志**（`loop.slow_callback_duration` 默认 0.1s，超过打 warning 且记录回调起点 traceback）、协程未 await 即销毁的更早告警、非线程安全 API 跨线程调用检查（`loop.call_soon_threadsafe` 之外的直接调用报错）；c) **3.8+ Task 异常不吞**：Task 的异常 GC 时若从未 retrieve，解释器打印 "Task exception was never retrieved" 并附创建位置；d) **3.12 asyncio 工具库**：`python -m asyncio ps PID` / `pstree PID`——**不重启进程**列出现场所有 Task 树与栈，是生产排障分水岭；e) **3.13+**：Task 类的 `cancelling()/uncancel()` 计数器使取消传播可观测（见既有 Q5516），eagertask factory（Q5502）提供调度路径分析。生产组合拳：**日常** debug 事件子集（CI/预发全开 debug，生产只开 slow callback 日志因为 debug 全开有 20-50% 开销）；**应急** `asyncio pstree PID` 抓卡死 Task 树 + py-spy 看线程栈 + APM 的 span 覆盖率定位"哪类协程消失"。复盘要点：debug 模式是**发现**工具，pstree 是**现场**工具，缺"历史"维度——所以关键路径要自己埋点（Task 创建/完成时长直方图）。

```python
# file: code/02_并发与网络工程/q5565_asyncio_debug.py
import asyncio, sys

# 1) debug 模式: 慢回调日志 (3.7+)
async def blocking_handler():
    time.sleep_sync = __import__("time").sleep(0.3)   # 模拟同步阻塞 300ms
    return "done"

async def main_debug():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.05                 # 降到 50ms 更敏感
    with __import__("contextlib").suppress(ValueError):
        await asyncio.wait_for(asyncio.to_thread(lambda: None), 1)

asyncio.run(main_debug(), debug=True)
print("debug 模式: >slow_callback_duration 的回调打日志+起点 traceback")

# 2) Task 异常未消费: GC 时提示 (3.8+)
async def failing():
    raise ValueError("business boom")
async def main_leak():
    asyncio.create_task(failing())       # 没 await
    await asyncio.sleep(0.05)            # 等 GC 打 "never retrieved"

asyncio.run(main_leak())

# 3) 忘记 await 的裸协程: 编译期警告
async def forgotten():
    await asyncio.sleep(0)

def wrong_call():
    forgotten()                          # RuntimeWarning: never awaited

import warnings
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter("always")
    wrong_call()
print("裸协程警告:", [str(w.message)[:40] for w in ws][:1])

# 4) 3.12+ 工具: 不重启抓 Task 树 (需单独进程演示, 这里演示 cencel 计数)
async def cancellable():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("cancelling 计数:", asyncio.current_task().cancelling() if sys.version_info >= (3, 11) else "3.11+")
        raise

async def main_cancel():
    t = asyncio.create_task(cancellable())
    await asyncio.sleep(0.01)
    t.cancel()
    try:
        await t
    except asyncio.CancelledError:
        print("取消传播可观测 (3.11+ cancelling/uncancel)")

asyncio.run(main_cancel())
print("生产组合: 预发开 debug / 生产只留慢回调日志 / 应急 asyncio pstree PID / 关键路径自埋 Task 时长")
```

**追问**：1) 生产全开 debug 的代价具体在哪？——每个回调记录起点 traceback（分配+格式化）、Task 对象记录创建栈（多一份引用，还可能延缓 GC）、跨线程检查加锁——实测 20-50% 吞吐下降，所以生产只开 `slow_callback_duration` 这一项（不记录栈开销小得多）。2) `asyncio pstree` 的原理与限制？——读目标进程 `/proc/PID/` 下的解释器状态（3.12 通过 debug 工具协议），只支持活着的同版本 CPython、Windows/嵌入解释器受限；它列"现存 Task"，已完成的 Task 不会出现，所以"协程消失"要靠创建/完成埋点补历史维度。3) "Task exception was never retrieved" 为什么不能代替监控？——打印时机不可控（依赖 GC 时机且在 stderr），生产要兜底 `loop.set_exception_handler` 统一采集进 APM，同时 CI 阶段用 debug 跑测试让异常在测试期暴露。

## 背诵要点
- 3.7 debug 模式三件事：慢回调日志（slow_callback_duration）、未 await 更早告警、跨线程 API 检查；全开有 20-50% 开销，生产只留慢回调日志。
- 3.8+ Task 异常未消费 GC 提示 "never retrieved"；3.12+ `python -m asyncio pstree/ps PID` 不重启抓 Task 树，是排障分水岭。
- debug=发现、pstree=现场、埋点=历史：关键路径自埋 Task 创建/完成时长直方图，set_exception_handler 统一采集。

## 复盘追问
- 你们的 asyncio 服务 CI/预发开 debug 了吗？生产有没有慢回调日志？（提示：对照成本分级开关；演练一次 PSTree 抓卡死现场的 runbook）
- "协程悄悄消失"类问题现在怎么发现？有没有 Task 时长埋点和 never-retrieved 异常采集？（提示：补 set_exception_handler 进 APM；复盘最近一次卡死的定位耗时）
