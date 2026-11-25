---
title: "[Q5196] lru_cache 缓存 async 函数：第二次 await 直接 RuntimeError"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5196 · lru_cache 缓存 async 函数：第二次 await 直接 RuntimeError

难度：P7 ｜ 标签：lru_cache、协程对象、单飞、缓存穿透、asyncio

**问**：给 `async def load(k)` 加上 `@lru_cache(maxsize=None)`，第一次 `await load("x")` 正常，第二次 `await load("x")` 抛 `RuntimeError: cannot reuse already awaited coroutine`。为什么缓存装饰器对同步函数有效、对协程函数就坏？缓存里到底存了什么？异步缓存该怎么做才能避免并发时的缓存击穿？

**答**：
结论：`lru_cache` 缓存的是**函数调用的返回值**。对 `async def` 来说，调用函数不会执行函数体，只返回一个协程对象，所以缓存里躺着一个"已经被 await 过"的协程对象；第二次同 key 命中，直接返回同一个协程对象，再 await 就是重复驱动同一个协程帧，CPython 直接抛错。更隐蔽的是：如果某个 key 只被调用、从未被 await（比如并发限流分支），缓存里会长期挂着一个从未启动的协程，解释器关闭时冒出 `RuntimeWarning: coroutine was never awaited`。

取舍：a) 缓存"纯函数的结果"，即把 IO 拆出去：`@lru_cache` 修饰同步的 `parse(raw)`，协程里先拿数据再调用；b) 需要缓存异步结果时自己维护 `dict[key] -> value`，并用"每 key 一把锁 + 双检"实现单飞（single-flight），保证并发只打一次上游；c) 用 `cachetools`/`aiocache` 之类的异步缓存库，但要注意它们默认不防击穿。直接给协程函数套 `lru_cache` 是明确的反模式。

实战：事故形态是"本地缓存装饰器上线后，命中率看起来很高，但每隔一段时间就 500 一次；日志里是 `cannot reuse already awaited coroutine`，重启即恢复"。下面演示缓存里是协程对象、二次 await 报错，以及单飞缓存的正确实现。

```python
import asyncio
import functools

calls = 0


@functools.lru_cache(maxsize=None)
async def load_bad(key):
    global calls
    calls += 1
    await asyncio.sleep(0)
    return {"key": key}


async def main():
    print("[1] 第一次:", await load_bad("x"))
    print("[2] 缓存里的类型:", type(load_bad("x")).__name__)
    try:
        await load_bad("x")
    except RuntimeError as e:
        print("[3] 第二次同 key:", e)
    print("[4] 上游实际调用次数:", calls)


asyncio.run(main())


# 正确做法：缓存结果 + 每 key 单飞
_values = {}
_locks = {}
_upstream_calls = 0


async def fetch(key):
    global _upstream_calls
    _upstream_calls += 1
    await asyncio.sleep(0.05)
    return {"key": key, "v": _upstream_calls}


async def load(key):
    if key in _values:
        return _values[key]
    lock = _locks.setdefault(key, asyncio.Lock())
    async with lock:
        if key in _values:          # 双检：等锁期间别人可能已填好
            return _values[key]
        value = await fetch(key)
        _values[key] = value
        return value


async def main2():
    results = await asyncio.gather(*[load("x") for _ in range(5)])
    print("[5] 并发 5 次只打一次上游:", _upstream_calls)
    print("[6] 所有调用拿到同一对象:", len({id(r) for r in results}) == 1)
    print("[7] 再次命中不走上游:", (await load("x")) is results[0], _upstream_calls)


asyncio.run(main2())
```

**追问一**：`asyncio.gather` 里对同一个协程对象传两次会怎样？—— `gather(coro, coro)` 会把同一个协程包装进两个 Task，两个 Task 同时驱动同一个协程帧，第二个 await 点就会抛 `RuntimeError: cannot reuse already awaited coroutine` 或产生"协程被并发驱动"的诡异状态。正确写法是传两个**协程调用**（`load(k), load(k)`），或先建 Task 再复用 Task 对象。

**追问二**：用 `lru_cache` 缓存 Task 行不行？—— 也不行，但失败形态不同：Task 只能被 await 多次（await 同一个 Task 是合法的，返回同一结果），所以看起来能用；坑在生命周期——Task 绑定创建它的事件循环，跨请求/跨 loop 复用会抛 `got Future attached to a different loop`，而且 Task 上的异常如果无人取走会触发 "Task exception was never retrieved"。跨 loop 的缓存必须缓存**不可变的纯数据**，不能缓存任何带 loop 亲和性的对象。

## 背诵要点
- `lru_cache` 缓存返回值；`async def` 的返回值是协程对象，缓存后二次 await 必炸。
- 未 await 的缓存协程会触发 `coroutine was never awaited` 警告并泄漏帧。
- 异步缓存 = 结果字典 + 每 key 锁 + 双检单飞；不要跨 loop 缓存 Task/Future。

## 复盘追问
- 本地缓存上线后间歇性 500、报 `cannot reuse already awaited coroutine`，如何定位？（装饰器套在 async def 上）
- 高并发下缓存击穿，如何用"每 key 锁 + 双检"把上游 QPS 压到 1？（single-flight 实现与锁清理）
