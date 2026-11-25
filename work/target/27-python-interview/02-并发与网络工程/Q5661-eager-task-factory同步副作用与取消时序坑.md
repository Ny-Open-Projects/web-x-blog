---
title: "[Q5661] eager_task_factory 的同步副作用与取消时序坑"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5661 · eager_task_factory 的同步副作用与取消时序坑

难度：P7 ｜ 标签：asyncio、eager_task_factory、取消语义、任务启动、3.12

**问**：默认的 `create_task` 为什么"先挂起、下个循环迭代才执行"？`asyncio.eager_task_factory`（3.12）让任务在 `create_task()` 调用栈里**同步跑到第一个 `await`**，这对"启动延迟"是好事，但对取消时序意味着什么——`t = create_task(coro); t.cancel()` 这两行之间，eager 模式下已经发生了哪些副作用？它和 `TaskGroup`、`shield` 混用时有什么反直觉行为？

**答**：
结论：默认 task factory 把协程包成 Task 后只是 `call_soon` 排进下一轮循环，所以 `create_task()` 返回时协程体**一行未执行**；`eager_task_factory` 则在 `create_task` 内**立即驱动协程直到第一次真正让出控制权**（遇到阻塞的 `await`），之后才退回事件循环。收益是消除"提交到首次执行"的一次循环往返（冷启动/短任务延迟更低），代价是**取消窗口前移**：`create_task()` 返回时，第一个 `await` 之前的副作用（写库、打日志、自增计数、发消息）**已经同步发生**，此时再 `t.cancel()` 只能取消后续部分，拦不住已发生的副作用——这叫"取消泄露到同步段"。更微妙的是：如果协程在同步段里**从不 await**（纯 CPU 或直接 return），eager 模式会在 `create_task` 里一路跑完并直接产出结果，`cancel()` 完全无效；默认模式则仍保留"可取消"的语义窗口。

取舍：用 eager 的前提是"任务开头到第一个 await 之间无不可回滚副作用"——把 `append`/日志/计数/外部调用都放到第一个 `await` 之后，或干脆用 `asyncio.shield` 包住关键副作用段。和 `TaskGroup` 混用时要注意：`TaskGroup.create_task` 同样受 loop 的 task factory 影响，eager 会让子任务在 `create_task` 调用点就开始跑，**异常也可能在 `tg.create_task(...)` 这一行就抛出**（而不是等 `__aexit__` 聚合）——这改变了异常出现的时点，但 `TaskGroup` 的聚合语义不变。追求极低延迟的短请求路径收益最大；长阻塞 I/O 任务收益趋近于零。

实战：事故形态是"请求取消后仍产生了一条下单记录"——因为 eager 下 `create_task` 同步段已经写了库，`cancel()` 晚了一步。排查记住：默认模式 `create_task` 后立刻 `cancel()` 能完全阻止执行，eager 模式阻止不了同步段。下面直接对照两种模式下 `create_task` 返回瞬间的状态与取消结果。

```python
import asyncio

async def work(log):
    log.append("side-effect-before-await")     # 第一个 await 前的副作用
    await asyncio.sleep(0.05)
    log.append("after-await")

async def main():
    for eager in (False, True):
        log = []
        loop = asyncio.get_running_loop()
        loop.set_task_factory(asyncio.eager_task_factory if eager else None)
        t = asyncio.create_task(work(log))
        print(f"eager={eager!s:5} after create_task: {list(log)}")
        t.cancel()
        await asyncio.sleep(0.1)
        print(f"          after cancel      : {list(log)}  cancelled={t.cancelled()}")
        loop.set_task_factory(None)            # 复位，避免污染后续 demo

    # 同步段无 await：eager 在 create_task 里直接跑完 -> cancel 无效
    async def instant():
        return 42
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)
    t = asyncio.create_task(instant())
    print("instant done at create:", t.done())
    t.cancel()
    print("cancel after done     :", t.cancelled(), "result:", t.result())
    loop.set_task_factory(None)

asyncio.run(main())
```

**追问一**：为什么 eager 模式让异常可能在 `tg.create_task(...)` 这一行就出现？——因为 `TaskGroup.create_task` 内部也是 `asyncio.create_task`，受同一 task factory 控制；eager factory 会同步驱动协程，若协程在第一个 await 前就抛异常，这个异常在 `create_task` 调用栈里直接冒出。但 TaskGroup 的契约是"子任务异常由 `__aexit__` 聚合成 ExceptionGroup 抛出"——实现上 eager factory 捕获了该异常并存入 Task，再由 TaskGroup 聚合，所以调用点一般不会真抛；正确心智模型是"**副作用时点前移，异常聚合时点不变**"。

**追问二**：eager 真的"更快"吗、什么场景反而更慢？——它省掉一次 `call_soon` 往返，对"创建后立即需要结果"的短任务（如缓存命中的快速返回）有微秒级收益；但若任务同步段很长（CPU 密集），它会**阻塞 `create_task` 的调用者**（事件循环线程）直到第一个 await，把本可并发的点变成串行，反而抬高延迟。所以 eager 适合"短、I/O 前置、副作用可控"的任务，长同步段任务必须避开。

## 背诵要点
- 默认 `create_task` 排到下一轮循环；`eager_task_factory` 在调用栈内同步跑到第一个 await。
- 代价：取消窗口前移——`create_task` 后立刻 `cancel()` 拦不住同步段副作用；无 await 的任务会直接跑完、cancel 无效。
- 与 TaskGroup 混用副作用时点前移但异常仍聚合；短任务收益、长同步段反而阻塞调用者。

## 复盘追问
- 请求取消后仍产生了一条订单记录，如何用 eager task 的"同步段已执行"解释并给出防线？（副作用移到首个 await 后 / shield 关键段 / 评估是否需要 eager，讨论取消语义变化）
- 为什么"eager 一定更快"是错的？（长同步段阻塞 create_task 调用者、把并发点变串行，讨论适用边界）
