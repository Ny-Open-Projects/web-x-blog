---
title: [Q441] async 迭代器与 async 生成器协议
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q441 · async 迭代器与 async 生成器协议

> 难度:★★★★ | 标签:异步, 迭代器

**问**:async for 背后的协议是什么?async def 里出现 yield 后,这个函数变成了什么?

**答**:async for 要求对象实现 `__aiter__`(返回异步迭代器)和 `__anext__`(返回协程,结束时抛 StopAsyncIteration)。async def 函数体内出现 yield,它就是「异步生成器」:同时具备 `__aiter__/__anext__/athrow/aclose`,每次产出之间可以 await。与同步迭代器的关键差异是每一步都可能在挂起点让出控制权,所以驱动它的事件循环必须在场;清理(aclose)也是协程,需要事件循环执行,这就是 asyncio.run 里 `loop.shutdown_asyncgens()` 存在的原因。

```python
# file: code/01_语言核心与底层/q441_async_iterator_protocol.py
import asyncio

class AsyncCounter:
    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        self.cur = 0
        return self

    async def __anext__(self):
        if self.cur >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0)        # 每步之间都可以挂起
        self.cur += 1
        return self.cur

async def async_gen():
    for i in range(3):
        await asyncio.sleep(0)
        yield f"item-{i}"

async def main():
    async for v in AsyncCounter(2):
        print("counter:", v)
    async for v in async_gen():
        print("gen:", v)

if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 直接 async for 一个普通迭代器会怎样?——TypeError: async for 要求 __anext__ 返回协程;反之普通 for 遍历异步生成器也会报错,两套协议互不兼容。2) 为什么需要独立的 StopAsyncIteration?——异步迭代的每步都可能在 await 挂起,结束信号走协程协议传播;复用同步 StopIteration 会与协程自身的结束信号混淆,协议层必须区分。3) 异步生成器的清理为什么是协程?——aclose 本身要在事件循环里执行(清理代码可能有 await);asyncio.run 退出时 loop.shutdown_asyncgens 统一驱动所有未关闭的异步生成器,这是资源不泄漏的兜底。4) 生产陷阱?——在事件循环外丢弃未 aclose 的异步生成器,清理协程无人驱动导致连接泄漏;以及用 try/finally 包 async for 却在 finally 里做同步 IO,阻塞循环。
