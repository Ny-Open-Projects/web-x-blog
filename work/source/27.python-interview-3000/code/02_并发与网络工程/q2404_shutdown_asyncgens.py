# -*- coding: utf-8 -*-
"""shutdown_asyncgens 语义: 悬空的异步生成器, 由循环统一送终。

- break 出 async for 后, 生成器停在 yield 点, finally 不会立刻执行;
- 若还有引用兜着, GC 不来收, 资源就一直悬着, 直到循环关闭前的大扫除;
- asyncio.run 会自动调 shutdown_asyncgens, 手动管理循环时要自己补这一课。
"""
import asyncio

log = []


async def resource_gen():
    try:
        log.append("资源打开")
        yield 1
        yield 2
        yield 3
    finally:
        log.append("资源关闭")


async def use_partially(gen):
    async for x in gen:
        break                       # 只拿一个就走人, 生成器悬在 yield 点


def manual_loop_demo():
    log.clear()
    gen = resource_gen()            # 关键: 持引用, GC 不会提前收尸
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(use_partially(gen))
        before = list(log)
        loop.run_until_complete(loop.shutdown_asyncgens())
        after = list(log)
    finally:
        loop.close()
    print("run 结束时:", before)
    print("shutdown 后:", after)
    assert "资源关闭" not in before, "悬空生成器不会自己收尾"
    assert "资源关闭" in after, "shutdown_asyncgens 必须送终"
    assert after.count("资源关闭") == 1, "收尾恰好一次"


def asyncio_run_demo():
    log.clear()
    holder = {}
    gen = resource_gen()
    holder["g"] = gen               # 持引用防 GC 提前收尸

    async def main():
        async for x in gen:
            break

    asyncio.run(main())
    print("asyncio.run 返回后:", list(log))
    assert "资源关闭" in log, "run 的收尾序列自带 shutdown_asyncgens"


def main_entry():
    manual_loop_demo()
    asyncio_run_demo()


if __name__ == "__main__":
    main_entry()
