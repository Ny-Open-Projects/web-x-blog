---
title: [Q2670] 手写异步迭代器:__aiter__ 与 __anext__ 协议
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2670 · 手写异步迭代器:__aiter__ 与 __anext__ 协议

> 难度:★★ | 标签:异步迭代器, 协议, async for

**问**:async for 背后的协议是什么?和异步生成器什么关系?

**答**:协议有两个方法:__aiter__ 返回异步迭代器本身,__anext__ 返回可等待对象,结束时抛 StopAsyncIteration。类实现的迭代器把状态放在 self 上,显式控制每一拍;async def 里用 yield 的异步生成器只是这套协议的语法糖。实测两者在 async for 下行为一致,还可以绕过 async for 手动 await it.__anext__() 驱动。

- StopAsyncIteration 是异步世界的 StopIteration,对仗但不可混用;

- 类实现适合状态复杂、需要复用与多实例的场景,生成器适合线性流水;

- __aiter__ 里可以有 await,允许迭代器的构造本身异步;

- 第三方 aiter()/anext() 内建函数是 3.10 才有的,3.9 直接调方法即可。

```python
# file: code/02_并发与网络工程/q2670_aiter_protocol.py
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
```

**追问**:1) 异步生成器的 __anext__ 是哪来的?——生成器对象自带,agen.asend(None) 就是它的协议层真身。2) __anext__ 忘了抛 StopAsyncIteration 会怎样?——async for 永远等下去,迭代器成为无限流,这是设计而非错误。3) 底层机制:为什么异步协议不复用 StopIteration?——Task.__step 把协程内冒出的 StopIteration 当作正常完成的信号,若 __anext__ 也用它表结束就会被误解释;PEP 492 因此规定异步世界用独立的 StopAsyncIteration,而 async def 函数体内抛 StopIteration 会被机制转成 RuntimeError。4) 生产陷阱?——给类只实现了 __iter__/__next__,async for 报 'async for' requires an object with __aiter__/__anext__;无限流没有退出条件,下游 gather 挂死;内建 anext() 是 3.10 才有的,3.9 兼容代码要直接调方法。

---
