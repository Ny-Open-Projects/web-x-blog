---
title: [Q2673] 异步资源的确定性收尾:手写 aclosing,把 aclose 绑进 with 块
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2673 · 异步资源的确定性收尾:手写 aclosing,把 aclose 绑进 with 块

> 难度:★★★ | 标签:异步生成器, aclosing, 资源清理

**问**:async for 中途 break 之后,异步生成器的清理代码什么时候执行?

**答**:不立刻执行:生成器悬在 yield 点,finally 缺席,靠 GC 钩子或循环关闭时的大扫除兜底,时机随缘。确定性方案是 aclosing 模式——把 aclose 绑进 async with 的块边界:实测离开 with 块立即输出 close,裸 break 则只有 open,手动补 aclose 才收尾。3.9 还没有 contextlib.aclosing,二十行就能自己造。

- 块边界是唯一可靠的清理时机:break、return、异常都汇聚到 __aexit__;

- 悬空的异步生成器占着连接与句柄,泄漏到进程退出才释放;

- aclosing 与 async with open 的语义对仗:资源的开与关写在同一个作用域;

- 3.10+ 升级时直接换成 contextlib.aclosing,语义一致。

```python
# file: code/02_并发与网络工程/q2673_aclosing.py
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
```

**追问**:1) aclose 内部做了什么?——向生成器注入 GeneratorExit,协程在 yield 点恢复并走 finally,之后再迭代会抛 StopAsyncIteration。2) finally 里还能 await 吗?——可以,这正是异步生成器清理的价值,但要保证清理本身不被取消干扰。3) 底层机制:GeneratorExit 注入的纪律是什么?——aclose 在 yield 点抛入 GeneratorExit,协程恢复后不得再 yield,否则抛 RuntimeError: async generator ignored GeneratorExit;finally 里的 await 会真实挂起在事件循环里,所以 aclose 本身可等待,清理动作也不能无限阻塞。4) 生产陷阱?——裸 break 靠 GC 兜底,长进程下连接与句柄泄漏放大;清理协程抛出的异常覆盖原始异常;清理写成无限等待,aclose 挂死整个收尾。

---
