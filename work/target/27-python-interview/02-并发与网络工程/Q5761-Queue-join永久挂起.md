---
title: "[Q5761] asyncio.Queue.join 永久挂起：task_done 漏调与取消路径"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5761 · asyncio.Queue.join 永久挂起：task_done 漏调与取消路径

难度：P6 ｜ 标签：asyncio、Queue、join、task_done、优雅停机、取消

基线：CPython 3.12.2，纯标准库；用 `asyncio.Queue` 的 `join`/`task_done` 与 `wait_for` 复现未完成计数泄漏。

**问**：订单消费服务用 `asyncio.Queue` 做进程内缓冲，停机流程是"停止收单 → `await queue.join()` → 关闭下游"。某次一条脏数据让 worker 在 `process()` 里抛了 `KeyError`，任务直接结束，`task_done()` 没执行；停机脚本等 `join()` 等了 90 秒，最后被 K8s SIGKILL，队列里其实早就空了，但 1.2 万条已处理订单的 ACK 全部丢失。另一条路径是发布重启时 worker 被取消，`get()` 已经拿到消息、还没 `task_done()`，计数同样泄漏。`join()` 到底在等什么？取消为什么也会泄漏？怎么写出不会挂的消费循环？

**答**：

- **结论**：`asyncio.Queue` 内部维护 `_unfinished_tasks`：每次 `put` 加一，每次 `task_done()` 减一，`join()` 等到它归零。`get()` 只负责把元素从 `_queue` 取走，**不会**自动减计数；如果消费者拿到元素后抛异常、被取消、或忘记调用 `task_done()`，计数永远停在 1，`join()` 就永远不返回。取消路径也一样：`await q.get()` 成功返回后，元素已经出队，此时任务被取消，若 `task_done()` 不在 `finally` 里，就没有人再减计数。注意 `join()` 是**全局屏障**，不是"等这一条处理完"，一条毒消息能让整个停机流程挂死。
- **取舍**：`join()` 适合"所有生产完成、所有消费确认"的批处理收尾，语义简单但粒度粗；如果业务需要"每条消息独立确认/重试"，应该给每条消息配 `Future` 或显式 ack 表，而不是靠全局计数。另一个取舍是异常策略：消费失败时可以选择"记录后 `task_done` 并丢弃"、"`task_done` 后重新入队重试（要防死循环）"、"不 `task_done` 让 `join` 暴露问题"，三者对应不同的可观测性；生产上通常选"失败落盘 + `task_done`"，并在停机时用超时兜底（`asyncio.wait_for(q.join(), timeout)`），超时后打印剩余计数和未确认消息 ID，而不是无限等。
- **实战**：修复分三层：① 消费循环改成 `try: handle(item) finally: q.task_done()`，保证异常/取消路径都减计数；② `handle` 内部把"业务失败"转成"记录到死信 + 返回"，只有真正的编程错误才向上抛；③ 停机 `join` 包 `wait_for(30s)`，超时后 dump `q.qsize()`、`q._unfinished_tasks`（内部字段，仅诊断）和正在处理的消息 ID，再强制退出。上线后停机 P99 从 90s 降到 1.8s，ACK 丢失归零。

下面复现三条路径：消费者抛异常不 `task_done` 导致 `join` 超时、消费者被取消导致计数泄漏、以及 `finally: task_done()` 的正确写法。

```python
# asyncio.Queue.join 等的是 _unfinished_tasks 归零, 不是 qsize 归零
import asyncio


async def bad_consumer(q):
    item = await q.get()
    raise RuntimeError(f"处理失败: {item}")   # 没有 task_done


async def cancelled_consumer(q, started):
    item = await q.get()
    started.set()
    await asyncio.sleep(10)                   # 模拟处理中被取消, 没有 finally
    q.task_done()


async def safe_consumer(q):
    item = await q.get()
    try:
        if item == "bad":
            raise ValueError("业务失败")
    finally:
        q.task_done()                         # 异常/取消都会减计数


async def main():
    # 1) 消费者抛异常, 计数停在 1
    q1 = asyncio.Queue()
    await q1.put("job-1")
    t1 = asyncio.create_task(bad_consumer(q1))
    try:
        await t1
    except RuntimeError as exc:
        print("[1] 消费者异常:", exc)
    print("[2] qsize =", q1.qsize(), "unfinished =", q1._unfinished_tasks)
    assert q1.qsize() == 0 and q1._unfinished_tasks == 1

    try:
        await asyncio.wait_for(q1.join(), 0.05)
        raise AssertionError("join 本应挂起")
    except asyncio.TimeoutError:
        print("[3] join 在 50ms 后仍未返回（计数泄漏）")

    # 2) 消费者拿到消息后被取消, 同样泄漏
    q2 = asyncio.Queue()
    await q2.put("job-2")
    started = asyncio.Event()
    t2 = asyncio.create_task(cancelled_consumer(q2, started))
    await started.wait()
    t2.cancel()
    try:
        await t2
    except asyncio.CancelledError:
        print("[4] 消费者被取消")
    print("[5] qsize =", q2.qsize(), "unfinished =", q2._unfinished_tasks)
    assert q2._unfinished_tasks == 1

    # 3) finally: task_done 让 join 正常返回
    q3 = asyncio.Queue()
    await q3.put("ok")
    await q3.put("bad")
    for _ in range(2):
        worker = asyncio.create_task(safe_consumer(q3))
        try:
            await worker
        except ValueError as exc:
            print("[6] 业务失败但 finally 已 task_done:", exc)
    await asyncio.wait_for(q3.join(), 1)
    print("[7] finally 版 join 返回, unfinished =", q3._unfinished_tasks)
    assert q3._unfinished_tasks == 0


asyncio.run(main())
```

**追问一**：`q.join()` 被取消后，计数会重置吗？—— 不会。`join()` 只是在 `_unfinished_tasks == 0` 时返回，取消它只是取消等待者，计数仍由生产/消费两侧维护；下次 `join()` 仍会等到归零。也正因为如此，`wait_for(q.join(), timeout)` 超时后队列状态没有变化，你可以继续消费，但不能假设"超时等于队列空了"。

**追问二**：为什么不能在 `except` 里直接 `task_done()` 然后 `raise`？—— 可以，但要保证**每条消息恰好一次** `task_done()`。如果 `try` 里已经调用过、`except` 又调一次，会抛 `ValueError('task_done() called too many times')`，并让计数变成负数，`join()` 的行为不可预测。最稳的写法是"获取消息后立刻进入 `try/finally`，`task_done` 只在 `finally` 里调用一次"；重试逻辑放在 `try` 内部，不要把 `task_done` 分散到多个分支。

## 背诵要点

- `put` 加计数、`task_done` 减计数、`join` 等归零；`get` 不自动减，异常/取消路径必须在 `finally` 里 `task_done`。
- `join` 是全局屏障，一条毒消息能让停机永久挂起；停机用 `wait_for` 超时并 dump 未确认计数。
- `task_done` 必须恰好一次，重复调用抛 `ValueError` 并破坏计数。

## 复盘追问

- 为什么 `qsize()==0` 不代表 `join()` 会返回？（元素已出队但未确认，`_unfinished_tasks` 仍大于 0）
- 消费失败时"不 `task_done`"和"`task_done` + 死信"各自的观测后果是什么？（前者让 `join` 暴露卡点但会挂死停机；后者可停机但需要死信可观测）
