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
