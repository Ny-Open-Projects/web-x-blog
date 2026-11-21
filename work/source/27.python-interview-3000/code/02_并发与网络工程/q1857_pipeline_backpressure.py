# -*- coding: utf-8 -*-
"""流式处理管道背压实测: 有界队列让整条管道的速率等于最慢一级。

- 三级管道, 中间一级最慢, 各级之间用 maxsize=3 的有界队列连接;
- 实测两个结论: 总吞吐被瓶颈级拖住; 上游队列长期顶满, 背压真实生效;
- 无界队列只会把内存吃爆并把延迟越堆越高, 背压必须靠有界队列+阻塞写。
"""
import asyncio
import time

N_ITEMS = 40
SLOW_MS = 0.05                                # 瓶颈级: 20 条/秒


async def stage1(q1, watermark):
    for i in range(N_ITEMS):
        depth = q1.qsize()                    # 写之前看一眼队列深度
        if depth > watermark["max"]:
            watermark["max"] = depth
        await q1.put(i)                       # 满了就挂起, 背压在这里
    watermark["done"] = True


async def stage2(q1, q2):
    for _ in range(N_ITEMS):
        i = await q1.get()
        await asyncio.sleep(SLOW_MS)          # 瓶颈: 每条 50ms
        await q2.put(i)


async def stage3(q2, out):
    for _ in range(N_ITEMS):
        out.append(await q2.get())


async def main():
    q1 = asyncio.Queue(maxsize=3)
    q2 = asyncio.Queue(maxsize=3)
    out = []
    watermark = {"max": 0}
    t0 = time.monotonic()
    await asyncio.gather(stage1(q1, watermark), stage2(q1, q2), stage3(q2, out))
    cost = time.monotonic() - t0
    throughput = N_ITEMS / cost
    print("耗时 %.2fs, 实际吞吐 %.1f 条/s, 瓶颈级理论 %.1f 条/s"
          % (cost, throughput, 1.0 / SLOW_MS))
    print("q1 最大深度 %d (maxsize=3), 输出 %d 条" % (watermark["max"], len(out)))
    assert len(out) == N_ITEMS, "一条不丢"
    assert watermark["max"] == 3, "上游队列必然长期顶满, 背压真实发生"
    assert cost >= N_ITEMS * SLOW_MS * 0.9, "总耗时被瓶颈级拖住"
    assert cost <= N_ITEMS * SLOW_MS * 1.8, "但不应比瓶颈慢得离谱"
    print("结论: 管道的速率方程是 min(各级速率), 队列深度是背压的仪表盘")


if __name__ == "__main__":
    asyncio.run(main())
