---
title: [Q583] 异步生成器底层:asend / athrow / aclose
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q583 · 异步生成器底层:asend / athrow / aclose

> 难度:★★★☆ | 标签:异步生成器, 协议, async for

**问**:async for 在底层是怎么驱动异步生成器的?手动控制它有哪些原语?

**答**:三个原语对应同步生成器的 send/throw/close:`asend(None)` 启动或恢复生成器拿到下一个值(本身是 awaitable,可能涉及 IO);`athrow(exc)` 在挂起点注入异常,常用于提前中断;`aclose()` 注入 GeneratorExit 让生成器执行清理。async for 语句编译后就是循环调 `__anext__`(= asend(None)),捕获 StopAsyncIteration 结束。理解这点就能解释"异步生成器必须在 with/事件循环存活期间关闭",否则关闭时的 await 没有循环可跑会报警告。

```python
# file: code/02_并发与网络工程/q583_async_gen_protocol.py
import asyncio


async def numbers(n: int):
    for i in range(n):
        await asyncio.sleep(0.01)  # 异步生成器: 产出前可能做 IO
        yield i


async def manual_drive() -> None:
    gen = numbers(3)
    print("手动 asend:", await gen.asend(None))  # 启动
    print("手动 asend:", await gen.asend(None))
    try:
        await gen.asend(None)
        await gen.asend(None)
    except StopAsyncIteration:
        print("耗尽: StopAsyncIteration")

    gen2 = numbers(10)
    await gen2.asend(None)
    try:
        await gen2.athrow(ValueError("提前中止"))
    except ValueError as e:
        print("athrow 注入并透出:", e)
    await gen2.aclose()  # 触发 GeneratorExit 执行清理


async def for_loop() -> None:
    async for i in numbers(3):  # 语法糖: 循环调用 __anext__
        print("async for:", i)


async def main() -> None:
    await manual_drive()
    await for_loop()


asyncio.run(main())
```

**追问**:1) 异步生成器和异步迭代器什么关系?——异步生成器是实现异步迭代器的便捷方式(带 yield 的 async def 自动获得 __anext__/aclose),任何实现 `__aiter__/__anext__` 的类都是异步迭代器,不一定要生成器。2) 三方法的协作?——asend 驱动产出、athrow 注入异常、aclose 触发清理;清理本身是协程,靠 loop.shutdown_asyncgens 兜底(Q441);StopAsyncIteration 是结束信号(独立于同步版)。3) 与 asend(None) 的关系?——首次驱动用 asend(None) 或 __anext__;非 None 注入是「值进入 yield 表达式」(Q431 的异步版)。4) 生产陷阱?——事件循环外丢弃未 aclose 的异步生成器;清理代码做同步 IO 阻塞循环;把同步 for 用在异步生成器(Q441)。

---
