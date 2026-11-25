---
title: "[Q5674] gather 首个异常不取消兄弟任务"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5674 · gather 首个异常不取消兄弟任务

难度：P6-P7 ｜ 标签：asyncio、gather、TaskGroup、结构化并发、取消传播

**问**：批量接口用 `asyncio.gather(*tasks)` 并发查 10 个下游，其中一个立刻 500，`gather` 马上抛出异常、接口返回 500；但监控显示另外 9 个请求还在继续跑，甚至继续写库。为什么 `gather` 不取消它们？这和 `asyncio.wait_for(gather(...))` 超时会取消子任务的行为为什么不一样？什么场景必须换 `TaskGroup`？本题与 Q074（gather/wait/as_completed 选型）的边界在哪？`return_exceptions=True` 又能解决什么、不能解决什么？

**答**：
结论：`gather(return_exceptions=False)` 的契约只是"**第一个异常向上传播**"，它不会取消其余 awaitable——这是为了兼容"部分任务需要继续完成"的旧语义。gather 返回的 Future 在首个异常时完成，但子 Task 仍在 loop 里跑，引用只被 gather 内部/调用方持有；如果你不保存 task 引用，它们可能变成"孤儿任务"，异常在 GC 时才以 `Task exception was never retrieved` 出现。`wait_for(gather(...), timeout)` 不同：超时取消的是 **gather 这个 Future**，gather 的取消会传播给所有子任务（它实现了取消聚合），所以看起来"超时会取消兄弟"。真正为此设计的原语是 3.11 的 `TaskGroup`：任一子任务失败 → 取消同组其余任务 → 以 `ExceptionGroup` 汇总，这就是结构化并发。

取舍：需要"失败即整体失败、不留后台副作用"的扇出，用 `TaskGroup`；需要"收集所有结果、失败也继续"的批处理，用 `gather(return_exceptions=True)` 并显式检查每个结果；需要"先到先得、其余取消"，用 `asyncio.wait(FIRST_COMPLETED)` 后手动 cancel 剩余。用 gather 又不想泄漏，就在 `except`/`finally` 里遍历 tasks 逐个 `cancel()` 并 `await asyncio.gather(*tasks, return_exceptions=True)` 收敛。

实战：事故形态是"批量扣款接口一个下游失败返回 500，用户重试，另外 9 个已经成功的扣款又跑了一遍/继续写审计"。下面复现：gather 抛异常时 `sibling.done()` 仍是 False，0.2s 后它才自己完成；TaskGroup 则在首个失败时立刻取消兄弟（兄弟的 `finally` 在 0.01s 后就执行）。

```python
import asyncio


async def work(name, delay, fail=False):
    try:
        await asyncio.sleep(delay)
        if fail:
            raise RuntimeError(name)
        print("  done", name)
        return name
    finally:
        print("  finally", name)


async def main():
    tasks = [
        asyncio.create_task(work("fast-fail", 0.01, True)),
        asyncio.create_task(work("sibling", 0.2, False)),
    ]
    try:
        await asyncio.gather(*tasks)
    except RuntimeError as e:
        print("gather 抛出:", e)

    print("gather 返回时 sibling.done():", tasks[1].done())
    await asyncio.sleep(0.3)
    print("稍后 sibling.done():", tasks[1].done())

    async def taskgroup():
        async with asyncio.TaskGroup() as g:
            g.create_task(work("tg-fail", 0.01, True))
            g.create_task(work("tg-sibling", 0.2, False))

    try:
        await taskgroup()
    except* RuntimeError as eg:
        print("TaskGroup 抛出:", [str(e) for e in eg.exceptions])


asyncio.run(main())
```

**追问一**：`gather(return_exceptions=True)` 会不会取消失败任务的兄弟？——不会。它只是把每个子任务的异常（包括 `CancelledError`？）当作结果收集，仍然等所有任务结束；如果某个任务永不结束，gather 也永不返回。它适合"我确实要所有结果，失败也算结果"，不适合"失败就止损"。另外，gather 本身被取消时，即使 `return_exceptions=True`，取消仍会传播给子任务——这是"外部取消"与"子任务异常"两条不同的路径。

**追问二**：TaskGroup 的 `ExceptionGroup` 和 `except*` 怎么处理多个失败？——TaskGroup 在退出 `async with` 时，若有子任务失败，会把所有失败（包括取消引发的 `CancelledError` 之外的异常）打包成 `ExceptionGroup` 抛出；用 `except* RuntimeError as eg` 可以只捕获其中一类，`eg.exceptions` 是匹配的异常列表。注意：首个失败会触发取消，其他任务可能以 `CancelledError` 结束，不会都进 ExceptionGroup；不要把"取消"误当成"业务失败"统计。

## 背诵要点
- `gather(return_exceptions=False)` 只传播首个异常，**不取消**兄弟任务；兄弟继续跑，可能泄漏/产生副作用。
- `wait_for(gather(...))` 超时取消的是 gather 聚合 Future，取消会传播给子任务，行为不同。
- 失败即止损用 `TaskGroup`（取消兄弟 + ExceptionGroup）；要全量结果用 `gather(return_exceptions=True)`。

## 复盘追问
- 批量接口一个下游 500，其余 9 个仍在写库，如何解释并改成结构化并发？（gather 不取消、TaskGroup 取消传播）
- 为什么 `wait_for(gather(...))` 超时会取消子任务，而普通异常不会？（取消的是聚合 Future，gather 实现取消传播；异常只完成 Future）
