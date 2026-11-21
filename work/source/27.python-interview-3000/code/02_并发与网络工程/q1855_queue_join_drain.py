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
