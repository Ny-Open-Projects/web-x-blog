---
title: "[Q5681] asyncio 任务泄漏检测：all_tasks 差分与取消后的残留"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5681 · asyncio 任务泄漏检测：all_tasks 差分与取消后的残留

难度：P6 ｜ 标签：asyncio、Task、all_tasks、优雅停机、可观测

**问**：服务停机时偶发"卡住不退"或"退了但还有后台任务在写日志"。怎么证明"没有任务泄漏"？`asyncio.all_tasks()` 到底返回什么、不含什么？为什么 cancel 之后任务还赖在 all_tasks 里？能给一套能落地的检测与收尾模板吗？

**答**：
结论：`all_tasks()` 返回当前 loop 上**所有未完成**的 Task 快照（不含已完成、也不含当前正在执行的那个——所以通常要减去 `current_task()`）。它看不到"协程对象但没被 create_task"的东西，也看不到线程池/子进程里的活。cancel 只是投递取消请求：任务要跑到下一个 await 点抛出 `CancelledError`、并且**被 await/gather** 之后才真正结束，从 all_tasks 里消失；所以"cancel 后还剩 1 个"是正常中间态，收尸必须 await。

取舍：最便宜的防泄漏投入是给每个 `create_task(..., name="xxx")` 命名，停机时按名字归类输出；进一步是"登记表 + 集合差分"（启动时记录基线，停机时 diff）。要根治就用 `asyncio.TaskGroup`（3.11+）或 anyio 的 task group，作用域内创建的任务由作用域负责取消与等待，压根不会漏。代价是 TaskGroup 是 fail-fast 的：一个任务抛错会取消同组其他任务，不适合"互不影响的常驻任务"，那类要自己管生命周期。

实战：事故形态是"每个请求 fire-and-forget 一个审计任务，压测后停机要 30 秒，日志里可见一批任务在停机后才写完"。下面演示：已完成任务不在 all_tasks 里、泄漏任务能在停机时被点名、cancel 后仍残留、gather 收尸后才归零。

```python
import asyncio


async def worker(name, secs):
    try:
        await asyncio.sleep(secs)
    finally:
        print(f"  {name} 收尾")


async def main():
    awaited = asyncio.create_task(worker("awaited", 0.05), name="awaited")
    leaked = asyncio.create_task(worker("leaked", 30), name="leaked")
    await awaited

    pending = asyncio.all_tasks() - {asyncio.current_task()}
    print("awaited done:", awaited.done(), "| 仍在 all_tasks:", awaited in pending)
    print("停机时残留任务:", sorted(t.get_name() for t in pending))

    for t in pending:
        t.cancel()
    print("cancel 后仍在 all_tasks:", len(asyncio.all_tasks() - {asyncio.current_task()}))
    results = await asyncio.gather(*pending, return_exceptions=True)
    print("gather 收尸:", [type(r).__name__ for r in results])
    print("收尸后残留:", len(asyncio.all_tasks() - {asyncio.current_task()}))


asyncio.run(main())
```

**追问一**：为什么不能靠 gc 判断任务泄漏？—— 只要任务还在 await，loop 就持有它的回调与引用，gc 看不到"没人引用"；`asyncio.all_tasks` 正是为此维护的注册表。反过来，`asyncio.run` 退出时会取消所有残留任务并跑一轮 loop，所以"进程能退出"不代表"没有泄漏"——被取消任务里未处理的异常会被吞掉（`CancelledError` 不打印）。

**追问二**：`all_tasks()` 在多个 loop 的场景下会不会串？—— 不传 loop 时返回**当前运行 loop** 的任务；多 loop（多线程各自 `new_event_loop`）里必须显式传对应的 loop 才能看到该 loop 的任务。这也是为什么"每个线程一个 loop"的旧架构里，泄漏检测脚本经常误报无泄漏——它查的是错的 loop。

## 背诵要点
- `all_tasks()` 是当前 loop 未完成任务的快照，不含已完成和 current_task；线程池/子进程不在其中。
- cancel 只是请求，必须 await/gather 收尸才从 all_tasks 消失；停机要"打名 + 差分 + 收尸"。
- 根治用 TaskGroup/结构化并发；常驻互不干扰的任务要自己管生命周期，别用 fail-fast 的组。

## 复盘追问
- 停机卡住 30 秒且日志在退出后才出现，如何用 all_tasks 定位并收尾？（差分点名、cancel、gather）
- 为什么"进程正常退出"不能证明没有任务泄漏？（asyncio.run 的取消与异常吞掉）
