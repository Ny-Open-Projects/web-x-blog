---
title: [Q2671] asyncio.Lock 的公平性实测:先到先得吗
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2671 · asyncio.Lock 的公平性实测:先到先得吗

> 难度:★★★ | 标签:asyncio.Lock, 公平性, 调度

**问**:8 个协程按顺序创建并抢同一把 asyncio.Lock,获取顺序会是创建顺序吗?

**答**:实测 5 轮全部严格按创建顺序获得锁。原因在调度模型:事件循环单线程,先创建的 Task 先被调度,先跑到 lock.acquire 的先进入等待队列;释放时按队列头唤醒,没有线程世界的抢占与抖动。公平性在 asyncio 里是调度模型给的,不是锁额外承诺的。

- 排队顺序 = 首次尝试 acquire 的顺序,与创建顺序一致的前提是中间没有别的让步点;

- 持锁时间仍要短,长持锁会让队列整体后移;

- 想要确定性顺序就别在 acquire 前插入不同时长的 await;

- 公平不等于无饥饿:反复重新排队的高频小任务仍可能挤占长任务的排队位。

```python
# file: code/02_并发与网络工程/q2671_async_lock_fair.py
# -*- coding: utf-8 -*-
"""asyncio.Lock 的公平性实测: 先到先得吗。

- asyncio.Lock 内部维护等待者队列, 释放时按排队顺序唤醒;
- 实测: 8 个协程按创建顺序抢锁, 记录获取顺序;
- 多轮统计: 事件循环下顺序高度确定, 这是调度模型决定的。
"""
import asyncio

TRIALS = 5


async def worker(i, lock, order):
    async with lock:                     # 排队点
        order.append(i)
        await asyncio.sleep(0.002)       # 持锁一点时间, 让后面真的排队


async def trial():
    lock = asyncio.Lock()
    order = []
    tasks = []
    for i in range(8):                   # 按序创建, 即按序排队
        tasks.append(asyncio.create_task(worker(i, lock, order)))
    await asyncio.gather(*tasks)
    return order


async def main():
    fifo = 0
    for k in range(TRIALS):
        order = await trial()
        print("第 %d 轮获取顺序: %s" % (k + 1, order))
        if order == list(range(8)):
            fifo += 1
    print("严格按创建序获得锁的轮数: %d/%d" % (fifo, TRIALS))
    print("要点: 事件循环单线程调度, 排队顺序就是唤醒顺序, 无锁竞争抖动")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) threading.Lock 为什么做不到这一点?——线程由操作系统抢占调度,唤醒后还要重新抢锁,顺序天然抖动。2) acquire 之后再 await 会让出锁吗?——不会,锁跟随 Task,await 只是让出 CPU 不让出锁。3) 底层机制:公平性从调度模型哪来?——Lock 内部的 Condition 维护等待者队列,release 时从队头唤醒;事件循环单线程、无抢占,先 ready 的 Task 先执行到 acquire、先入队,排队序即唤醒序;这是调度模型的副产品,文档并未把它写成契约。4) 生产陷阱?——把"创建顺序=获得顺序"写进正确性依赖,acquire 前插入不等长的 await 就破序;持锁路径里 await 慢 IO,队列整体后移放大长尾;在 uvloop 等替代循环上把这一行为当契约,实现差异直接翻车。

---
