# -*- coding: utf-8 -*-
"""异步代码的单测: 不引框架, 自己驱动事件循环。

- 每个测试就是一个协程, 用 asyncio.run 驱动到完成;
- 断言写法与同步测试无异, 关键是让并发路径"跑得完、收得住";
- 覆盖三类基础: 结果正确、超时触发、取消清理。
"""
import asyncio


async def test_fifo_order():
    q = asyncio.Queue()
    out = []

    async def prod():
        for i in range(5):
            await q.put(i)

    async def cons():
        while len(out) < 5:
            out.append(await q.get())

    await asyncio.gather(prod(), cons())
    assert out == [0, 1, 2, 3, 4], out


async def test_timeout_fires():
    async def sleepy():
        await asyncio.sleep(1.0)

    try:
        await asyncio.wait_for(sleepy(), timeout=0.05)
        raise AssertionError("超时没有触发")
    except asyncio.TimeoutError:
        pass                                   # 预期路径


async def test_cancel_cleanup():
    log = []

    async def job():
        try:
            await asyncio.sleep(1.0)
        finally:
            log.append("cleanup")              # 被取消也要收尾

    t = asyncio.create_task(job())
    await asyncio.sleep(0.05)
    t.cancel()
    try:
        await t
    except asyncio.CancelledError:
        pass
    assert log == ["cleanup"], log


if __name__ == "__main__":
    for fn in (test_fifo_order, test_timeout_fires, test_cancel_cleanup):
        asyncio.run(fn())
        print("PASS", fn.__name__)
    print("要点: 协程可测的前提是它能被 asyncio.run 收敛, 别在测试里留后台任务")
