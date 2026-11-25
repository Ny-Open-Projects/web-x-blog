---
title: "[Q5683] 跨事件循环复用 asyncio 原语：is bound to a different event loop"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5683 · 跨事件循环复用 asyncio 原语：is bound to a different event loop

难度：P6 ｜ 标签：asyncio、ClientSession、Event loop、Future、aiohttp

**问**：脚本里在模块层创建了一个 `aiohttp.ClientSession`，之后每个请求都 `asyncio.run(fetch())` 跑一次，第二、三次就报 `... is bound to a different event loop`。谁绑定了 loop？为什么有的东西跨 loop 直接报错、有的却"看起来能用"？服务里应该怎么组织才不踩？

**答**：
结论：asyncio 的 Future/Task/Event/Queue/Lock 等在**第一次需要挂起**时才绑定当时的 loop（创建等待用的 Future），之后每个会阻塞的操作都会校验 `_get_loop()`，不一致直接 `RuntimeError: ... is bound to a different event loop`。`asyncio.run` 每次都新建 loop 并在结束时关闭，所以第二次调用就是在拿"上一个 loop 的遗产"。aiohttp 的 ClientSession 内部持有 connector、连接池、以及这些原语和传输对象，天然只能活在创建它的那个 loop 里。

取舍：`asyncio.run` 是给脚本用的（一次生命周期的入口），服务里必须"一个进程一个长期 loop"——uvicorn/granian 就是这么做的。异步资源（session、连接池、redis client）要跟着 loop 走：Web 服务里放 lifespan/依赖，脚本里在 `asyncio.run` 内部创建。跨线程要用 `asyncio.run_coroutine_threadsafe` 投递，而不是在新线程里 `run`。

实战：事故形态是"本地单测每个用例 `asyncio.run` 都能过，集成到一起就随机炸"，因为单元测试天然给每个用例新 loop、天然不复用资源。下面演示三种原语跨 loop 的表现：裸 Future、Event、Queue 在 loop A 里绑定后，在 loop B 里操作全部 RuntimeError；顺带说明为什么必须在 loop 内创建资源。

```python
import asyncio


async def build():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    ev = asyncio.Event()
    q = asyncio.Queue()
    for aw in (ev.wait(), q.get()):
        try:
            await asyncio.wait_for(aw, 0.01)   # 让原语在 loop A 里绑定
        except TimeoutError:
            pass
    return fut, ev, q


fut, ev, q = asyncio.run(build())
print("Event/Queue 已绑定 loop:", ev._loop is not None, q._loop is not None)


async def probe(label, factory):
    try:
        await asyncio.wait_for(factory(), 0.3)
        print(f"{label}: 竟然复用成功")
    except RuntimeError as e:
        print(f"{label}: RuntimeError | {str(e)[:60]}...")


asyncio.run(probe("[1] 跨 loop await Future", lambda: fut))
asyncio.run(probe("[2] 跨 loop Event.wait", ev.wait))
asyncio.run(probe("[3] 跨 loop Queue.get ", q.get))
```

**追问一**：为什么 `asyncio.Lock` 有时跨 loop 不报错？—— 绑定是**惰性**的：无竞争时 `acquire()` 只是把标志位置 1，不需要建 Future，也就不校验 loop；一旦真的需要排队才绑定并校验。所以"开发环境不报、压测才炸"是常态。这也解释了为什么这类 bug 在低并发下很难复现。

**追问二**：为什么要 `await` 一个别的 loop 的 Task 时抛的是 `CancelledError` 而不是 RuntimeError？—— 原 loop 关闭时会把未完成的 Task 取消，你再 await 它拿到的就是取消结果。这说明"能 await"不等于"还能用"，而且会掩盖真正的问题（任务根本没执行完）。判断资源归属要看它内部持有的 loop/Future，而不是看能不能调用。

## 背诵要点
- asyncio 原语首次需要挂起时绑定 loop，之后跨 loop 操作直接 RuntimeError；`asyncio.run` 每次新 loop、用完即关。
- 异步资源（ClientSession/连接池/redis）必须与 loop 同生命周期：服务放 lifespan，脚本在 run 内部创建。
- Lock 的绑定是惰性的（无竞争不校验），跨 loop 问题常在并发时才暴露。

## 复盘追问
- 模块级 ClientSession + 每次 `asyncio.run` 为什么第二次就炸？如何重构？（loop 绑定、单 loop、lifespan）
- 为什么"能 await"不能证明资源可用？跨 loop Task 会抛什么？（取消语义、CancelledError 掩盖）
