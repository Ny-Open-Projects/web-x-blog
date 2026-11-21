# -*- coding: utf-8 -*-
"""loop.time 时钟源与 call_at 绝对时刻重调度。

- loop.time() 与 time.monotonic() 同源, 不受系统改表影响;
- call_at 用"绝对时刻"调度: 周期任务按 next = base + n*period 排, 不累积漂移;
- 实测 5 拍 50ms 周期: 绝对时刻调度的漂移远小于 sleep 链式的累积漂移。
"""
import asyncio
import time

PERIOD = 0.05


async def sleep_chain(n=5):
    """相对延迟链: 每拍延迟 = 上拍结束 + PERIOD, 误差会累积。"""
    stamps = []
    for i in range(n):
        await asyncio.sleep(PERIOD)
        stamps.append(time.monotonic())
    return stamps


def call_at_chain(loop, n=5):
    """绝对时刻调度: 第 i 拍固定在 base + i*PERIOD, 不看上拍何时结束。"""
    stamps = []
    base = loop.time() + PERIOD

    def fire(i):
        stamps.append(loop.time())
        if i + 1 < n:
            loop.call_at(base + (i + 1) * PERIOD, fire, i + 1)

    loop.call_at(base, fire, 0)
    return stamps, base


async def main():
    loop = asyncio.get_event_loop()
    print("loop.time = %.6f, time.monotonic = %.6f, 差值 %.6f" %
          (loop.time(), time.monotonic(),
           abs(loop.time() - time.monotonic())))

    s1 = await sleep_chain()
    drift1 = [s - s1[0] - i * PERIOD for i, s in enumerate(s1)]
    print("sleep 链各拍相对漂移: %s" %
          ["%+.1fms" % (d * 1000) for d in drift1])

    fut = asyncio.Future()
    s2, base = call_at_chain(loop)

    def done():
        if not fut.done():
            fut.set_result(None)
    loop.call_later(PERIOD * 7, done)
    await fut
    drift2 = [s - base - i * PERIOD for i, s in enumerate(s2)]
    print("call_at 各拍相对漂移: %s" %
          ["%+.1fms" % (d * 1000) for d in drift2])
    print("call_at 以绝对时刻为锚, 回调晚点不影响下一拍的锚点")


if __name__ == "__main__":
    asyncio.run(main())
