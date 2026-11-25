---
title: "[Q5210] contextlib.aclosing：break 出来的异步生成器不会自己关"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5210 · contextlib.aclosing：break 出来的异步生成器不会自己关

难度：P6 ｜ 标签：aclosing、异步生成器、aclose、GeneratorExit、资源释放

**问**：异步生成器里 `finally: await conn.close()`，消费端 `async for` 中途 `break`，日志里没有 close，连接一直挂着；换成同步生成器 break 后 `finally` 很快就跑了。为什么异步生成器的清理不即时？`contextlib.aclosing` 解决什么？它和 `AsyncExitStack` 怎么配合？

**答**：
结论：同步生成器在 `break` 后引用计数归零，CPython 立即调用 `close()` 触发 `finally`；异步生成器的 `aclose()` 是协程，不能由引用计数同步调用，只能由事件循环的 asyncgen finalizer 在 GC 时调度，时机不确定（可能在 `loop.shutdown_asyncgens()` 才跑）。`async for` 的 `break` 只是停止迭代，**不会**自动 `aclose()`。`contextlib.aclosing(agen)`（3.10+）在退出 `async with` 时调用 `await agen.aclose()`，把"关闭"变成确定性的清理点。

取舍：a) 任何"消费到一半可能退出"的异步生成器，都用 `async with aclosing(gen) as g:` 包住；b) 多个异步资源用 `AsyncExitStack`，按 LIFO 关闭，`aclosing` 可作为其中一项；c) `aclose()` 会向生成器抛 `GeneratorExit`，`finally` 里不要再 `yield`，否则 `RuntimeError: async generator ignored GeneratorExit`；d) 不要在 `finally` 里做长时间网络等待，关闭路径要短；e) 框架层（StreamingResponse）会负责关闭，自己手写消费循环时别忘了。

实战：事故形态是"分页拉取上游数据，`async for` 拿到满足条件的 10 条就 `break`，生成器里的 httpx 连接池连接一直不还，跑一天后连接耗尽；用 `aclosing` 包住后，每次 break 都立刻关闭"。下面演示 break 后 `finally` 不执行、显式 `aclose` 执行、以及 `aclosing` 自动关闭。

```python
import asyncio
import contextlib

log = []


async def stream():
    try:
        for i in range(5):
            yield i
    finally:
        log.append("closed")


async def main():
    gen = stream()
    async for value in gen:
        if value == 1:
            break
    print("[1] break 之后:", log)

    await gen.aclose()
    print("[2] 显式 aclose 之后:", log)

    gen2 = stream()
    async with contextlib.aclosing(gen2) as g:
        async for value in g:
            if value == 1:
                break
    print("[3] aclosing 退出后:", log)


asyncio.run(main())
```

**追问一**：为什么 `async with aclosing(gen)` 不能直接 `async for` 外层对象？—— `aclosing` 返回的是一个异步上下文管理器，`__aenter__` 把生成器交给你，`__aexit__` 负责 `aclose`；你必须 `as g` 再用 `g` 迭代。直接 `async with aclosing(gen): async for x in gen` 也能工作，但如果 `gen` 在进入前已被消费/关闭，行为要小心；显式绑定更清晰。

**追问二**：`agen.aclose()` 和 `athrow(GeneratorExit)` 有什么区别？—— `aclose()` 是标准关闭协议：如果生成器在 `yield` 处挂起，它会在该点抛 `GeneratorExit`，执行 `finally` 后结束；`athrow(GeneratorExit)` 是手动抛同一个异常，语义接近但不走关闭状态机，可能留下"已关闭/未关闭"的边界差异。正常清理用 `aclose()`，不要手写 `athrow`。

## 背诵要点
- `async for` 的 `break` 不自动 `aclose`；异步生成器的 `finally` 要等 GC/`shutdown_asyncgens`。
- `contextlib.aclosing` 在退出时 `await agen.aclose()`，把清理变确定性。
- `aclose` 抛 `GeneratorExit`，`finally` 里不能再 `yield`；多资源用 `AsyncExitStack`。

## 复盘追问
- 异步生成器 break 后连接为什么不释放？（没有同步析构，finalizer 延迟）
- `aclosing` 与 `AsyncExitStack` 怎么配合？（一个管单个生成器，一个管多个资源 LIFO）
