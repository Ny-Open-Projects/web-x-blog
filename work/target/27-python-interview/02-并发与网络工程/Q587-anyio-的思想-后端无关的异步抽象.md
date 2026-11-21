---
title: [Q587] anyio 的思想:后端无关的异步抽象
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q587 · anyio 的思想:后端无关的异步抽象

> 难度:★★★☆ | 标签:anyio, asyncio, trio

**问**:anyio 解决什么问题?它和直接写 asyncio 有什么区别?

**答**:anyio 是"异步后端无关"的高层库:同一套代码可以跑在 asyncio 或 trio 上,提供统一的 TaskGroup、同步原语、流和内存对象通道。三个思想值得借鉴:一是结构化并发是原生语义(nursery 模型,任务不会逃逸出作用域);二是取消是"作用域级"的——cancel scope 进入异常即取消该作用域内全部任务,而非逐个 task.cancel;三是 Level 触发的事件语义(如 Event.set 是持久的,不依赖唤醒顺序)。面试重点是能对比:裸 asyncio 的任务可以 fire-and-forget 导致失控,anyio/trio 从类型系统上 discourages 这种写法。下面用纯 asyncio 模拟 nursery 的核心行为。注意内置 ExceptionGroup 是 3.11+ 才有,低版本直接 NameError——模拟实现要按版本分流:3.11+ 抛原生 ExceptionGroup,老版本用普通异常携带 `.exceptions` 列表聚合,捕获侧统一用 `getattr(e, "exceptions", [e])` 展开。

```python
# file: code/02_并发与网络工程/q587_nursery_sim.py
import asyncio
import sys
from contextlib import asynccontextmanager


class Nursery:
    """用纯 asyncio 模拟 trio nursery 的核心语义。"""

    def __init__(self) -> None:
        self._tasks: set = set()
        self._errors: list = []

    async def start_soon(self, coro) -> None:
        t = asyncio.create_task(self._wrap(coro))
        self._tasks.add(t)

    async def _wrap(self, coro) -> None:
        try:
            await coro
        except BaseException as e:  # 子任务异常全部收集, 不逃逸
            self._errors.append(e)

    async def join(self) -> None:
        if self._tasks:
            await asyncio.gather(*self._tasks)  # 等全部子任务退出
        if self._errors:
            if sys.version_info >= (3, 11):
                raise ExceptionGroup("nursery 子任务失败", self._errors)  # 3.11+ 原生聚合
            # 3.9/3.10 没有内置 ExceptionGroup: 用普通异常携带列表聚合
            agg = RuntimeError(f"nursery 子任务失败: 共 {len(self._errors)} 个")
            agg.exceptions = self._errors  # 模拟 ExceptionGroup.exceptions
            raise agg


@asynccontextmanager
async def open_nursery():
    n = Nursery()
    try:
        yield n
    finally:
        await n.join()


async def child(name: str, delay: float, fail: bool = False) -> None:
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"{name} 失败")
    print(f"{name} 完成")


async def main() -> None:
    try:
        async with open_nursery() as n:
            await n.start_soon(child("fast", 0.05))
            await n.start_soon(child("slow", 0.15))
            await n.start_soon(child("bad", 0.08, fail=True))
    except BaseException as eg:  # 原生 ExceptionGroup 与模拟聚合都能接住
        for e in getattr(eg, "exceptions", [eg]):
            print("nursery 收集到:", repr(e))
    print("作用域结束: 所有子任务已被等待, 无任务逃逸")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) anyio 的 cancel scope 和 asyncio.wait_for 的区别?——wait_for 只取消单个 await;cancel scope 是一个词法块,块内启动的所有任务(包括再嵌套的)都会被取消,并能区分"超时取消"与"外部取消"。2) 后端无关的价值?——同一代码跑 asyncio/trio;标准化的任务组、信号量、流抽象;框架层(anyio 作为 asyncio 高层封装)与直接 asyncio 的取舍。3) 与 TaskGroup 的关系?——asyncio.TaskGroup(3.11+)借了 trio nursery 思想;anyio 的 TaskGroup 更早且跨后端;取消树传播(Q589)是共同内核。4) 生产陷阱?——混用两套高层 API 语义;cancel scope 外捕获取消继续跑;假设 wait_for 能取消嵌套任务。

---
