# -*- coding: utf-8 -*-
"""as_completed 超时后的漏收任务: 预算耗尽, 慢任务要显式收尸。

- as_completed(timeout) 超时抛 TimeoutError, 迭代直接终止;
- 没被迭代到的任务不会消失, 还在事件循环里默默跑着;
- 纪律: 捕获超时后, 用原 Future 列表找出未完成者, 取消并 await 收尸。
"""
import asyncio

TIMEOUT = 0.25


async def quick(name):
    await asyncio.sleep(0.05)
    return name + "-ok"


async def slow(name):
    await asyncio.sleep(5.0)
    return name + "-ok"          # 注定等不到


async def main():
    fs = [asyncio.ensure_future(quick("快1")),
          asyncio.ensure_future(slow("慢1")),
          asyncio.ensure_future(quick("快2")),
          asyncio.ensure_future(slow("慢2"))]
    got = []
    timed_out = False
    try:
        for fut in asyncio.as_completed(fs, timeout=TIMEOUT):
            got.append(await fut)
    except asyncio.TimeoutError:
        timed_out = True
    print("预算内拿到:", got)
    assert timed_out and sorted(got) == ["快1-ok", "快2-ok"]

    stragglers = [f for f in fs if not f.done()]
    print("预算外遗留:", [f.get_name() for f in stragglers])
    for f in stragglers:
        f.cancel()
    results = await asyncio.gather(*stragglers, return_exceptions=True)
    print("收尸结果:", [type(r).__name__ for r in results])
    assert all(isinstance(r, asyncio.CancelledError) for r in results), \
        "遗留任务应被取消并等到落实, 而不是放任空跑 5 秒"
    assert all(f.cancelled() for f in stragglers)


if __name__ == "__main__":
    asyncio.run(main())
