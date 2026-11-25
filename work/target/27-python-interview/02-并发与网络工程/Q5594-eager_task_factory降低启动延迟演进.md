---
title: "[Q5594] eager_task_factory 降低任务启动延迟（3.12）"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5594 · eager_task_factory 与任务启动延迟（3.12 演进）

难度：P6-P7 | 标签：版本演进 | asyncio | Task

**问**：3.12 引入 `asyncio.eager_task_factory`。传统 Task 的启动流程为什么要绕一圈事件循环？eager 执行改变了什么？它对"大量微小任务"和"RPC 内联子调用"的收益怎么量化，又有什么坑？

**答**：
结论：传统 `asyncio.create_task(coro)` 只是把协程包成 Task 并 `loop.call_soon` 排队，真正的第一步 `Task.__step` 要等**下一轮循环**才跑——任务从创建到第一条语句执行隔了一个完整事件循环周期，还附带一次循环切换。`eager_task_factory` 在 `create_task` 当场同步执行协程：如果协程在首次 await 前就完成（同步路径），根本不进调度队列，省掉一整个循环轮次和 Task 队列开销；需要挂起时再按普通 Task 继续调度。3.12 为此引入 `eager_start` 的内部状态，未完成时行为与普通 Task 完全一致。
取舍：收益场景是"大量小任务"+"内联调用链"（比如把协程函数包成 task 传给工具函数）：实测可显著降低微任务延迟与调度开销；坑是同步段过长会阻塞调用方——eager 执行意味着 create_task 的那一刻就在当前栈上跑用户代码，同步段里的异常抛出时机也变了（可能在 create_task 调用栈中直接冒出）。
实战：`loop.set_task_factory(asyncio.eager_task_factory)` 全局开启，或按调用点构造；用 `Task.get_coro()` 的完成时机与 perf 对比验证收益，压测以"创建→首次挂起"延迟为指标。

```python
import asyncio, time

done_markers = []

async def leaf(i):
    done_markers.append(i)
    return i * 2

async def plain_demo():
    t = asyncio.create_task(leaf(1))
    # 传统调度：此刻 leaf 尚未执行，任务在队列里等下一轮循环
    print("create_task 后 leaf 是否已跑:", bool(done_markers))
    await asyncio.sleep(0)
    print("一轮 sleep(0) 后:", bool(done_markers))
    print("结果:", await t)

async def eager_demo():
    loop = asyncio.get_running_loop()
    t = asyncio.create_task(leaf(2))  # 工厂换成 eager 后当场同步执行
    print("eager: create_task 返回时 leaf 已跑:", bool(done_markers))
    print("结果:", await t)

async def main():
    await plain_demo()
    asyncio.get_running_loop().set_task_factory(asyncio.eager_task_factory)
    done_markers.clear()
    await eager_demo()

    # 微任务批量：eager 让同步完成的任务根本不排队
    loop = asyncio.get_running_loop()
    N = 200_000
    async def tiny():
        return 1
    loop.set_task_factory(None)
    t0 = time.perf_counter()
    await asyncio.gather(*[asyncio.create_task(tiny()) for _ in range(N)])
    t_plain = time.perf_counter() - t0

    loop.set_task_factory(asyncio.eager_task_factory)
    t0 = time.perf_counter()
    await asyncio.gather(*[asyncio.create_task(tiny()) for _ in range(N)])
    t_eager = time.perf_counter() - t0
    loop.set_task_factory(None)
    print(f"20万微任务: 传统 {t_plain:.3f}s vs eager {t_eager:.3f}s")

if __name__ == "__main__":
    asyncio.run(main())
```

**追问 1**：eager 执行的异常抛出时机有什么不同？
- 追问 2 层：传统模式协程异常在 Task 内部捕获存进 Future，调用方 await 时才收到；eager 模式同步段异常可能在 `create_task` 调用栈直接抛出（同步完成的 Task 把异常立即定局）。
- 追问 3 层：这改变错误传播路径，外层 `try: create_task()` 的假设要重新验证，混合版本迁移要加回归用例。

**追问 2**：eager 与 `TaskGroup`、`asyncio.timeout` 怎么协作？
- 追问 2 层：eager 只是改变了"第一次 step 的时机"，Task 状态机不变，与结构化并发 API 兼容；但同步完成意味着 TaskGroup 的 gather 可能少一轮上下文切换。
- 追问 3 层：3.14+ 还提供了 `asyncio.Queue` shut down 等配套演进；任务工厂链（自定义 factory 包 eager）注意别破坏 `_eager_start` 私有语义，升级 Python 要回归。

## 背诵要点
1. 传统 Task 首次执行要等下一轮事件循环（call_soon 排队）；eager_task_factory 在 create_task 当场同步执行。
2. 收益场景：大量微小任务、内联子调用——同步完成根本不进队列；开销一整轮循环被省掉。
3. 坑：同步段在调用方栈上执行，异常抛出时机改变，set_task_factory 全局开启要回归测试。

## 复盘追问
1. 为什么 3.12 才做这个优化？——依赖 Task 内部状态机增加 eager_start 分支，且要保证与既有 Future/Task 语义完全兼容。
2. 什么场景 eager 反而有害？——create_task 的调用点在持锁/关键区中，同步段用户代码被拉进关键区，造成意外串行。
