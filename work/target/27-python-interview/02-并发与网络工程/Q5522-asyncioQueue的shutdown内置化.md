---
title: [Q5522] asyncio.Queue.shutdown()：3.13 把关停协议内置化
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5522 · asyncio.Queue.shutdown()：3.13 把关停协议内置化

> 难度:★★★☆ | 标签:3.13, asyncio.Queue, 优雅关闭

**问**：3.13 之前"关闭一个 asyncio.Queue"要靠什么约定？新 API `Queue.shutdown()` 的精确语义是什么——存量消息还取得到吗？`put` 和 `get` 各抛什么？它解决了哨兵方案的哪三类缺陷？

**答**：3.13 前的关停协议是**哨兵（None/毒丸）+ 事件标志**：生产者发 `None`，消费者 `while item is not None`——缺陷：1) 哨兵会被当成业务数据泄漏给类型检查（`Queue[str]` 里混进 None），2) 多消费者时哨兵只关一个，3) 消费者阻塞在 `get` 时没人唤醒、排空与退出逻辑要手写（Q614 的三态关闭全靠自研）。`asyncio.Queue.shutdown()`（3.13+）把语义内置化：调用后**存量消息仍可继续取**（先排空），`put`（含 `put_nowait`）立即抛 `asyncio.QueueShutDown`；队列取空后 `get`/`get_nowait` 抛 `QueueShutDown`——消费循环用 `except QueueShutDown` 收尾，生产者用"shutdown 后写入必炸"硬约束停流。注意排空语义是"先到先得"，多消费者下存量分配仍是竞争关系，要按任务数关停用 task_done/join 配合。版本演进视角：这是 asyncio 把"社区十年哨兵实践"升格为原语，与 `TaskGroup`（3.11）同一条"结构化收尾"主线。

```python
# file: code/02_并发与网络工程/q5522_queue_shutdown.py
import asyncio, sys

async def main():
    q: asyncio.Queue = asyncio.Queue()

    if sys.version_info < (3, 13):
        # 降级: 3.12- 的哨兵协议演示(生产用 Q614 的三态关闭封装)
        await q.put("task-a")
        await q.put(None)                      # 毒丸哨兵
        got = []
        while (item := await q.get()) is not None:
            got.append(item)
        print("哨兵协议排空:", got)
        print("降级说明: 当前版本无 Queue.shutdown,3.13+ 才有内置语义")
        return

    await q.put("task-a")
    q.shutdown()                               # 3.13+: 关闭,存量仍可排空

    try:
        await q.put("task-b")
    except asyncio.QueueShutDown:
        print("put 被拒: QueueShutDown(生产者立即感知停流)")

    print("存量仍可取:", await q.get())
    try:
        await q.get()
    except asyncio.QueueShutDown:
        print("排空后 get 抛 QueueShutDown: 消费循环干净退出")

asyncio.run(main())
```

**追问**：1) shutdown 之后还能往队列塞"最后一条通知"吗？——不能，put 已封死；要"关停前的最后广播"应在 shutdown 前入队，或改用 `asyncio.Event`/发布订阅通道。2) 多消费者怎么优雅收尾？——先停生产者 → `shutdown()` → 各消费者循环 `try: get() except QueueShutDown: return`；存量会被竞争取完，无需发 N 个哨兵。3) 和 `Queue.join()`/`task_done()` 的配合？——`join` 等待"入队项全部 task_done"，shutdown 后新入队封死，join 的收敛条件变得确定；注意 shutdown 不替代 join，排空完成仍要 join 兜底计数。

## 背诵要点
1. `Queue.shutdown()`（3.13+）：put 立即抛 QueueShutDown，get 先排空存量再抛。
2. 取代哨兵协议：解决类型污染、多消费者广播、排空收尾三类缺陷。
3. 多消费者收尾 = 停生产者 → shutdown → except QueueShutDown 退出，配 join/task_done 兜底。

## 复盘追问
1. 低版本运行时的代码要预留这个 API，怎么写兼容层最干净？（提示：封装 `closeable_queue()` 工厂——3.13+ 走原生 shutdown，低版本用哨兵+Event 模拟同语义，调用面只见异常类型）
2. shutdown 的瞬间有生产者正阻塞在满队列的 put 上，它醒得来吗？（提示：3.13 实现会唤醒等待中的 put 并抛 QueueShutDown，但自己代码要防"先满后关"的窗口，压测验证）
