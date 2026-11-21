# -*- coding: utf-8 -*-
"""to_thread 的边界: 默认执行器的容量与阻塞实测。

- asyncio.to_thread 把同步函数丢进默认线程池, 主循环不卡;
- 默认执行器容量 = min(32, cpu + 4), 超出的任务排队;
- 边界: 它不解决 CPU 并行 (GIL), 也不能包"必须主线程"的调用。
"""
import asyncio
import os
import time


def blocking_io(task_id, dur=0.25):
    time.sleep(dur)          # 模拟阻塞 IO (磁盘/阻塞 socket)
    return task_id


async def main():
    print("cpu_count:", os.cpu_count(),
          "-> 默认执行器线程数:", min(32, (os.cpu_count() or 1) + 4))

    t0 = time.monotonic()
    results = await asyncio.gather(*[
        asyncio.to_thread(blocking_io, i) for i in range(16)
    ])
    wall = time.monotonic() - t0
    serial = 16 * 0.25
    workers = max(1, round(serial / wall))
    print("16 个 0.25s 阻塞任务: 串行需 %.2fs, 实际 %.2fs" %
          (serial, wall))
    print("估算同时运行线程数 ≈", workers, "-> 超出容量的任务在排队")
    print("结果顺序:", results, "-> to_thread 返回原值, gather 保序")

    # 反例: 不包 to_thread, 主循环被独占, ticker 全停
    stamps = []

    async def ticker():
        end = time.monotonic() + 0.6
        while time.monotonic() < end:
            await asyncio.sleep(0.05)
            stamps.append(time.monotonic())

    tk = asyncio.ensure_future(ticker())
    await asyncio.sleep(0.05)
    w0 = time.monotonic()
    await asyncio.to_thread(blocking_io, 99, 0.2)    # 包住: 循环不卡
    w1 = time.monotonic()
    b0 = time.monotonic()
    time.sleep(0.2)                                   # 裸 sleep: 循环卡死
    b1 = time.monotonic()
    await tk
    in_window = sum(1 for s in stamps if w0 <= s <= w1)
    blocked_ticks = sum(1 for s in stamps if b0 <= s <= b1)
    print("to_thread 窗口心跳:", in_window, "| 裸阻塞窗口心跳:", blocked_ticks,
          "(0 = 循环被独占, 这就是必须包装的原因)")


if __name__ == "__main__":
    asyncio.run(main())
