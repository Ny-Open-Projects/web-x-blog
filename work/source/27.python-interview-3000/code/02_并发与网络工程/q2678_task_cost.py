# -*- coding: utf-8 -*-
"""万级 Task 的成本账: 任务不是免费的。

- 每个任务都要分配协程对象、Task 包装、事件循环里的句柄;
- 实测创建 1 万个任务的时间与内存, 以及全部跑完的时间;
- 结论: 批量场景该用批量结构(如队列)而不是无脑一任务一连接。
"""
import asyncio
import time
import tracemalloc


async def noop():
    await asyncio.sleep(0)


async def main():
    loop = asyncio.get_running_loop()
    tracemalloc.start()

    t0 = time.perf_counter()
    tasks = [loop.create_task(noop()) for _ in range(10000)]
    t1 = time.perf_counter()
    cur, peak = tracemalloc.get_traced_memory()
    await asyncio.gather(*tasks)
    t2 = time.perf_counter()
    tracemalloc.stop()

    print("创建 10000 个任务: %.0f ms" % ((t1 - t0) * 1000))
    print("任务对象内存: 已分配 %.1f MB, 峰值 %.1f MB" % (cur / 1e6, peak / 1e6))
    print("全部跑完: %.0f ms" % ((t2 - t1) * 1000))
    print("要点: 任务对象常驻到完成, 万级是常态可扛, 十万级要开始算账")


if __name__ == "__main__":
    asyncio.run(main())
