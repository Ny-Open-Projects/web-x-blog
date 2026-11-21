---
title: [Q1855] asyncio.Queue 的 task_done/join:精确排空靠计数
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1855 · asyncio.Queue 的 task_done/join:精确排空靠计数

> 难度:★★☆ | 标签:asyncio.Queue, task_done, 排空

**问**:生产者放完数据后,怎么确定消费者把队列 '全部处理完' 而不只是 '取完了'?

**答**:queue.join() 等的是未完成计数归零:每次 put 计数加一,每次 task_done 减一,归零意味着 '取走且处理完',这正是 join 与 '队列空了' 的本质区别。

- 标准排空三步:put 全部、await q.join()、然后 cancel 还堵在 get() 上的 worker 并 gather 收尸;

- 纪律是每个 get 配对恰好一次 task_done,多调少调都会让计数永久失真;

- 演示二十四条数据三个 worker,join 在所有 task_done 后返回,取消 worker 收尾,一条不丢。

注意顺序:必须先 join 再 cancel,反过来取消时队列里可能还有未处理数据。

```python
# file: code/02_并发与网络工程/q1855_queue_join_drain.py
# -*- coding: utf-8 -*-
"""asyncio.Queue 的 task_done/join 精确排空: 计数制, 不是猜。

- put 让未完成计数加一, task_done 让它减一, join 等它归零;
- 排空三步: 先 put 全部, 再 join, 最后 cancel 还堵在 get() 上的 worker;
- 关键纪律: 每个 get 必须配对恰好一次 task_done, 多调少调都会让 join 永远失真。
"""
import asyncio


async def worker(q, results, wid):
    while True:
        item = await q.get()
        await asyncio.sleep(0.005)                 # 模拟处理
        results.append((wid, item))
        q.task_done()                              # 与 get 一一配对


async def main():
    q = asyncio.Queue()
    results = []
    n_items = 24
    workers = [asyncio.create_task(worker(q, results, i)) for i in range(3)]
    for i in range(n_items):
        await q.put(i)

    loop = asyncio.get_running_loop()
    t0 = loop.time()
    await q.join()                                 # 未完成计数归零才返回
    cost = loop.time() - t0
    for w in workers:                              # join 已完成, 回头收掉 worker
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)

    print("排空 %d 条 耗时 %.3fs, worker 分布: %s"
          % (len(results), cost,
             {i: sum(1 for w, _ in results if w == i) for i in range(3)}))
    assert len(results) == n_items, "每条都被恰好处理一次"
    assert sorted(it for _, it in results) == list(range(n_items))
    print("结论: join 是计数器语义, put/task_done 必须严格配对")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) worker 阻塞在 get() 上,cancel 会成功吗?——会,get 是 await 点,可被取消;worker 内部若已 get 到数据正在处理,取消会打断处理,所以严谨的排空都是 join 完成后再收 worker。2) join 与「队列空了」的差异在哪些场景致命?——消费者 get 后处理时崩溃、或处理完忘 task_done:队列空了但计数不为零;反过来 task_done 多调,计数提前归零(数据还没处理完);「精确排空」的所有场景(优雅关闭、批处理完成判定)都要 join 而不是 empty() 判断。3) 排空三步的次序为什么不能乱?——put 全部→join→cancel:先 cancel 再 join 会打断在处理的数据;join 前 cancel 会漏计数;「cancel 后 gather 收尸」让 worker 的 finally(task_done 补账)执行——次序即正确性。4) 生产陷阱?——task_done 多调少调(计数永久失真,join 失效);empty() 当排空判据(竞态);worker 循环里 get 被 cancel 后没补 task_done(账目事故,Q1856);join 无超时(永久阻塞,Q1856 的 wait_for 兜底)。


---
