"""异步管道: fan-out 分工与 fan-in 汇聚。

- fan-out: 生产者把任务轮流分发到每个 worker 的有界队列(maxsize=3),
  队列满则生产者挂起 -> 背压自动限速上游;
- fan-in: 所有 worker 把结果写进同一个有界汇聚队列, 汇聚者统一收集。
有界是关键: 无界队列会把背压推迟到内存爆炸。
"""
import asyncio

N_ITEMS = 20
N_WORKERS = 3


async def producer(worker_queues):
    for i in range(N_ITEMS):
        q = worker_queues[i % N_WORKERS]         # 轮询分发
        await q.put(i)                           # 队列满 -> 挂起, 背压生效
    for q in worker_queues:
        await q.put(None)                        # 逐个通知收工


async def worker(in_q, agg_q, wid, stats):
    while True:
        item = await in_q.get()
        if item is None:
            return
        await asyncio.sleep(0.01)                # 模拟处理耗时
        await agg_q.put((wid, item))
        stats[wid] += 1


async def collector(agg_q, n):
    results = []
    while len(results) < n:
        results.append(await agg_q.get())
    return results


async def main():
    worker_queues = [asyncio.Queue(maxsize=3) for _ in range(N_WORKERS)]
    agg_q = asyncio.Queue(maxsize=8)             # 汇聚队列同样有界
    stats = [0] * N_WORKERS

    prod = asyncio.create_task(producer(worker_queues))
    workers = [asyncio.create_task(worker(worker_queues[i], agg_q, i, stats))
               for i in range(N_WORKERS)]
    results = await collector(agg_q, N_ITEMS)
    await prod
    await asyncio.gather(*workers)

    items = sorted(x for _, x in results)
    print("各 worker 处理量:", stats)
    assert items == list(range(N_ITEMS)), "20 个任务一个都不能丢"
    assert len(set((w, x) for w, x in results)) == N_ITEMS, "结果不应重复"
    print("结论: fan-out 分担算力, fan-in 收拢结果, 有界队列兜住背压")


if __name__ == "__main__":
    asyncio.run(main())
