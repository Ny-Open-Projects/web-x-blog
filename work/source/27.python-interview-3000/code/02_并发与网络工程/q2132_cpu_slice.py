# -*- coding: utf-8 -*-
"""事件循环内的 CPU 密集切片: sleep(0) 让步保心跳。

- 事件循环是单线程协作调度, 一个不 await 的长计算会饿死一切;
- 把计算切成小片, 片间 await asyncio.sleep(0) 让控制权回到循环;
- 实测: 计算窗口内, 不切片心跳为 0, 切片后心跳均匀出现。
"""
import asyncio
import time

N = 2_000_000


def compute_chunk(lo, hi):
    return sum(i * i for i in range(lo, hi))


async def ticker(seconds, stamps):
    """每 0.02s 记一次心跳时间戳, 直到窗口结束。"""
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        await asyncio.sleep(0.02)
        stamps.append(time.monotonic())


async def blocked_run(stamps):
    tk = asyncio.ensure_future(ticker(0.8, stamps))
    await asyncio.sleep(0.05)                # 让 ticker 先跑半步
    t0 = time.monotonic()
    total = compute_chunk(0, N)              # 一整块不让步, 循环被独占
    t1 = time.monotonic()
    await tk
    return total, t0, t1


async def sliced_run(stamps, parts=10):
    tk = asyncio.ensure_future(ticker(0.8, stamps))
    await asyncio.sleep(0.05)
    t0 = time.monotonic()
    total = 0
    step = N // parts
    for k in range(parts):
        total += compute_chunk(k * step, (k + 1) * step)
        await asyncio.sleep(0)               # 让步: 心跳得以插入
    t1 = time.monotonic()
    await tk
    return total, t0, t1


def ticks_in(stamps, t0, t1):
    return sum(1 for s in stamps if t0 <= s <= t1)


async def main():
    s1 = []
    total1, a0, a1 = await blocked_run(s1)
    print("不切片: 计算 %.2fs, 窗口内心跳 %d 次 (循环被独占)" %
          (a1 - a0, ticks_in(s1, a0, a1)))

    s2 = []
    total2, b0, b1 = await sliced_run(s2)
    print("切片后 : 计算 %.2fs, 窗口内心跳 %d 次 (协作让步)" %
          (b1 - b0, ticks_in(s2, b0, b1)))
    assert total1 == total2, "两种切法必须同结果"
    print("结果一致:", total1, "| 切片的代价是总耗时略增的公平税")


if __name__ == "__main__":
    asyncio.run(main())
