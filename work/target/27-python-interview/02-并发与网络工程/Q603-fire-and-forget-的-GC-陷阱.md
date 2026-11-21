---
title: [Q603] fire-and-forget 的 GC 陷阱:任务引用必须持有
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q603 · fire-and-forget 的 GC 陷阱:任务引用必须持有

> 难度:★★★☆ | 标签:Task, GC, 生命周期

**问**:`asyncio.create_task(coro())` 不接收返回值会怎样?官方文档为什么警告这一点?

**答**:事件循环只通过弱引用(以及调度中的临时引用)持有 Task,如果没有任何强引用,GC 可能在任务执行中途把它回收,协程"人间蒸发",异常也无人收割——文档明确要求保存 create_task 的返回值。工程模式:维护一个 `set` 存后台任务,任务完成回调里 `tasks.discard(t)` 自动清理;或集中到一个 TaskManager 统一 await/cancel。另外"没引用但侥幸跑完"的行为依赖 GC 时机,所以这个 bug 表现是偶发的,极难排查——评审时 fire-and-forget 必须有引用或有注释说明。

```python
# file: code/02_并发与网络工程/q603_task_ref.py
import asyncio
import gc
import weakref

log: list = []


async def background_job() -> None:
    await asyncio.sleep(0.05)
    log.append("job-done")  # 如果 Task 被 GC, 这行永远不会执行


async def main() -> None:
    # 陷阱: 创建后立刻丢弃唯一引用
    weak = weakref.ref(asyncio.create_task(background_job()))
    gc.collect()  # 触发一轮回收, 观察无强引用任务的命运
    alive = weak() is not None
    await asyncio.sleep(0.1)
    print(f"无引用任务: 存活={alive}, 日志={log}")
    print("(能否侥幸跑完取决于 GC 时机与 await 对象的引用链, 不能依赖 —— 这正是文档警告的原因)")

    # 正确姿势: 引用集合 + done callback 自清理
    bg_tasks: set = set()
    for i in range(3):
        t = asyncio.create_task(background_job())
        bg_tasks.add(t)
        t.add_done_callback(bg_tasks.discard)
    await asyncio.sleep(0.1)
    print(f"受保护任务: 完成 {len(log)} 个, 集合剩 {len(bg_tasks)} 个已自动清理")
    assert log.count("job-done") >= 3


asyncio.run(main())
```

**追问**:1) gather 里的任务需要额外持引用吗?——gather 内部会持有,但 gather 本身要是没人 await 也一样有整个 Future 被回收的问题;规则是"任何并发执行的东西都要有归属"。2) 持引用的工程模式?——模块级/类级任务集合 + done 回调自删(discard);asyncio.all_tasks() 巡检;TaskGroup 的树形归属(Q589);fire-and-forget 三宗罪(Q603 正文):不可取消、异常无人取、内存滞留。3) 与取消的关系?——持有的集合要在 shutdown 时统一 cancel 并 gather(return_exceptions=True);引用持有让 cancel 有对象可找。4) 生产陷阱?——create_task 后不存引用(运行中被 GC);任务集合忘记清理(完成不 discard 泄漏);异常处理器未配(Q1561)。

---
