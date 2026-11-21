# -*- coding: utf-8 -*-
"""异步资源的确定性收尾: 手写 aclosing, 把 aclose 绑进 with 块。

- async for 中途 break, 生成器悬在 yield 点, finally 不会立刻执行;
- 3.9 还没有 contextlib.aclosing, 二十行就能自己造一个;
- with 块退出(含 break 与异常)必然触发 aclose, 清理时机从"随缘"变"确定"。
"""
import asyncio


class aclosing:
    """让异步生成器可以用 async with 管生命周期。"""

    def __init__(self, agen):
        self.agen = agen

    async def __aenter__(self):
        return self.agen

    async def __aexit__(self, *exc):
        await self.agen.aclose()


async def stream(log):
    log.append("open")
    try:
        for i in range(100):
            yield i
    finally:
        log.append("close")                  # 清理只该发生一次


async def main():
    log1 = []
    async with aclosing(stream(log1)) as s:
        async for v in s:
            if v == 2:
                break                        # 提前离场
    print("aclosing 模式日志:", log1, "(离开 with 即收尾)")

    log2 = []
    s2 = stream(log2)
    async for v in s2:
        if v == 2:
            break
    print("裸 break 日志:   ", log2, "(清理悬着)")
    await s2.aclose()                        # 手动补课
    print("手动 aclose 后:  ", log2)
    print("要点: 不确定收尾会泄漏连接与句柄, aclosing 把时机钉死在块边界")


if __name__ == "__main__":
    asyncio.run(main())
