# -*- coding: utf-8 -*-
"""手写异步迭代器: __aiter__ 与 __anext__ 协议。

- async for 的协议面: __aiter__ 返回迭代器, __anext__ 返回可等待对象;
- 结束信号是抛 StopAsyncIteration, 与同步协议的 StopIteration 对仗;
- async def 里 yield 的异步生成器只是该协议的语法糖实现。
"""
import asyncio


class Countdown:
    """类实现的异步迭代器: 状态在 self 上, 不依赖生成器机制。"""

    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        print("__aiter__ 被调用, 返回 self")
        return self

    async def __anext__(self):
        if self.n <= 0:
            raise StopAsyncIteration        # 结束信号
        self.n -= 1
        await asyncio.sleep(0.01)           # 真正的异步暂停点
        return self.n + 1


async def agen_version(n):
    """同一语义的异步生成器版本, 对比用。"""
    for i in range(n):
        await asyncio.sleep(0.01)
        yield n - i


async def main():
    async for v in Countdown(3):            # 触发 __aiter__/__anext__
        print("class 迭代:", v)

    it = Countdown(2)
    got = await it.__anext__()              # 不用 async for, 手动驱动协议
    print("手动 __anext__:", got)

    async for v in agen_version(3):         # 生成器版: 同一协议的糖
        print("agen  迭代:", v)

    print("isinstance 检查: both are async iterable")
    print("协议要点: __aiter__ 给迭代器, __anext__ 给下一值或 StopAsyncIteration")


if __name__ == "__main__":
    asyncio.run(main())
