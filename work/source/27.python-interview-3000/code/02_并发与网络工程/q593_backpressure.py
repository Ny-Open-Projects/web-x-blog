import asyncio
import time

MAXSIZE = 5


async def producer(q: asyncio.Queue, stats: dict) -> None:
    for i in range(20):
        t0 = time.perf_counter()
        await q.put(i)  # 队列满时挂起: 背压发生点
        wait = time.perf_counter() - t0
        stats["max_wait"] = max(stats["max_wait"], wait)
        stats["max_size"] = max(stats["max_size"], q.qsize())
    stats["done"] = True


async def consumer(q: asyncio.Queue) -> None:
    while True:
        item = await q.get()
        await asyncio.sleep(0.03)  # 下游处理速度: 上游被它拖慢
        q.task_done()


async def main() -> None:
    q: asyncio.Queue = asyncio.Queue(maxsize=MAXSIZE)
    stats = {"max_wait": 0.0, "max_size": 0, "done": False}
    prod = asyncio.create_task(producer(q, stats))
    cons = asyncio.create_task(consumer(q))

    await asyncio.wait_for(prod, 5)  # 生产者完成(被拖慢后仍完成)
    await q.join()
    cons.cancel()
    print(f"maxsize={MAXSIZE}, 队列峰值 {stats['max_size']}, "
          f"put 最长等待 {stats['max_wait'] * 1000:.0f}ms")
    assert stats["max_size"] <= MAXSIZE, "有界队列封顶生效"


asyncio.run(main())
