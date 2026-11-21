---
title: [Q418] asyncio 任务泄漏:fire-and-forget 的代价
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q418 · asyncio 任务泄漏:fire-and-forget 的代价

> 难度:★★★★★ | 标签:asyncio, 任务泄漏, 协程

**问**:`asyncio.create_task(coro())` 返回值随手一扔会发生什么?"Task exception was never retrieved" 警告哪来的?怎么系统地防任务泄漏?

**答**:`create_task` 返回的 `Task` 是对运行中协程的唯一强引用——事件循环只持弱引用集合(`asyncio.all_tasks` 内部是 WeakSet)。扔掉返回值意味着:(1) 任务仍会跑,但没有任何句柄可以 `cancel`/`await`;(2) 任务抛出的异常存在 `Task` 里无人取,GC 回收 Task 时打印 "Task exception was never retrieved";(3) 任务可能引用大对象,生命周期失控导致内存滞留。正确姿势:保存任务集合 + `add_done_callback` 做 discard 与异常日志,或用 `TaskGroup`(3.11+,结构化并发,退出时保证子任务全部收尾并把异常聚合为 `ExceptionGroup`)。协程对象还有一个坑:`create_task` 前协程未被调度,`loop.close` 或解释器退出时未 await 的协程会触发 "coroutine was never awaited"。注意 TaskGroup 与 except* 均为 3.11+ 引入,低版本运行演示文件时该段自动跳过。

```python
# file: code/01_语言核心与底层/q418_task_leak.py
import asyncio
import sys

async def risky(i):
    await asyncio.sleep(0.01)
    if i % 2 == 0:
        raise ValueError(f"boom {i}")
    return i

async def leaky():
    for i in range(4):
        asyncio.create_task(risky(i))      # 返回值丢弃:异常无人取

async def main():
    await leaky()
    await asyncio.sleep(0.05)   # 给泄漏任务跑完并触发 never-retrieved 警告

asyncio.run(main())

# TaskGroup 与 except* 都是 3.11+;except* 是新语法,低版本解释器无法解析,
# 因此这段演示放在字符串里按需编译执行,低于 3.11 时打印说明跳过
if sys.version_info >= (3, 11):
    structured_demo = """
async def structured():
    results = []
    async with asyncio.TaskGroup() as tg:       # 3.11+ 结构化并发
        for i in range(4):
            tg.create_task(risky(i)).add_done_callback(
                lambda t: results.append(f"err: {t.exception()}" if t.exception() else t.result())
            )
    return results

async def main2():
    try:
        await structured()
    except* ValueError as eg:                   # ExceptionGroup 解包
        print("group caught:", [str(x) for x in eg.exceptions])

asyncio.run(main2())
"""
    exec(structured_demo, globals())
else:
    print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
```

**追问**:1) `asyncio.wait_for` 超时后原任务状态?——任务被取消(`CancelledError` 注入),但如果任务吞掉取消或内部 shield,任务会继续在后台跑——"cancel 不是同步终止"。2) `TaskGroup` 与 `gather` 的关键差别?——TaskGroup 中任一子任务失败即取消其余全部并等待收尾,gather 默认 `return_exceptions=False` 时直接抛出,其余任务仍在跑。
