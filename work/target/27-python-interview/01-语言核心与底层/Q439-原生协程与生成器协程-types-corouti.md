---
title: [Q439] 原生协程与生成器协程:types.coroutine 兼容层
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q439 · 原生协程与生成器协程:types.coroutine 兼容层

> 难度:★★★★ | 标签:协程, asyncio

**问**:async def 之前,生成器是怎么当协程用的?今天的原生协程和生成器协程如何互通?

**答**:老式「生成器协程」就是普通生成器 + `@types.coroutine` 装饰:装饰器在类型层面声明「这个生成器的 yield 是协程挂起语义」,让 await 可以等待它。原生协程是 async def 产生的对象,实现了 `__await__`,内部由 GET_AWAITABLE 字节码驱动;await 一个生成器协程时,挂起请求会穿透到最底层。关键差异:原生协程不是迭代器,没有 __next__,不能被 for/next 驱动,必须走 send/throw 的协程协议;而 asyncio 事件循环正是最底层的「驱动者」,接收所有穿透上来的 yield 值(如 Future)。

```python
# file: code/01_语言核心与底层/q439_native_vs_generator_coroutine.py
import types
import inspect

@types.coroutine
def generator_sleep():
    """生成器协程:yield 一个值给底层驱动者"""
    yielded = yield "SLEEP"
    return yielded

async def native_main():
    result = await generator_sleep()      # await 可以等待生成器协程
    return f"resumed with {result}"

if __name__ == "__main__":
    coro = native_main()
    print(type(coro).__name__)            # coroutine
    print("iscoroutine:", inspect.iscoroutine(coro))
    print("isgenerator:", inspect.isgenerator(coro))
    print(coro.send(None))                # 穿透到生成器协程的 yield:打印 SLEEP
    try:
        coro.send("wake")
    except StopIteration as stop:
        print("result:", stop.value)
```

**追问**:1) 为什么原生协程不能 next()?——它没有 __next__,await 在编译层生成的是协程协议字节码;硬要用生成器方式驱动可以用 types.coroutine 包一层,但正确姿势是交给事件循环。2) 挂起请求如何穿透多层协程?——await 取 __await__ 迭代器后按 yield from 语义逐层转发,内层 yield 的值穿过所有协程帧到达最底层驱动者;事件循环只见最外层 send 进来的 Future,内部结构对它透明。3) 原生协程与生成器的对象差异?——coroutine 类型有 cr_frame/cr_await、走 send/throw 协程协议、无 __next__;生成器有 gi_frame 且同时是迭代器。types.coroutine 的工作是给生成器打上 GEN_COROUTINE 标志让其可被 await。4) 生产陷阱?——混合代码里用 for/next 驱动原生协程直接 TypeError;判断「可等待」不要手写 hasattr 检查,用 inspect.isawaitable 统一口径。
