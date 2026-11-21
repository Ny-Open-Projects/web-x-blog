---
title: [Q419] shutdown_asyncgens 与异步上下文的收尾
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q419 · shutdown_asyncgens 与异步上下文的收尾

> 难度:★★★★☆ | 标签:asyncio, async generator, 资源管理

**问**:为什么 `loop.run_until_complete` 之外要显式 `shutdown_asyncgens`?异步生成器的 `aclose` 什么时候不被调用?文件/连接在 async gen 里怎么保证关闭?

**答**:异步生成器的资源释放发生在 `aclose()` 把 `GeneratorExit` 投进挂起点之后;但 async gen 实例可能悬在半空(没人消费完),事件循环关闭前需要遍历 `loop.shutdown_asyncgens()` 对所有"挂起中的 async gen"逐一 aclose——`asyncio.run` 内部已自动做这件事,自己管理 loop 的代码容易漏。风险场景:客户端 `break` 跳出 `async for`,生成器挂起在 yield,若再无引用,要等 GC 才有系统机会 finalize(时序不定);连接类资源必须用 `async with` 或在 finally 里 `aclose`。3.10+ 还要区分 `shutdown_asyncgens` 与 `shutdown_default_executor`;此外 `GeneratorExit` 里不允许再次 yield,否则 `RuntimeError: async generator ignored GeneratorExit`。

```python
# file: code/01_语言核心与底层/q419_shutdown_asyncgens.py
import asyncio

opened = []

async def stream():
    conn = f"conn-{id(stream):x}"
    opened.append(conn)
    try:
        for i in range(10):
            await asyncio.sleep(0)
            yield f"{conn}:{i}"
    finally:
        opened.remove(conn)         # 只有 aclose 被驱动才会执行
        print("closed:", conn)

async def main():
    agen = stream()
    async for v in agen:
        if v.endswith("1"):         # 提前 break,生成器悬挂在 yield
            break
    print("still open:", opened)
    await agen.aclose()             # 显式收尾
    print("after aclose:", opened)

asyncio.run(main())                 # run 内部最后调用 loop.shutdown_asyncgens
```

**追问**:1) 不手动 aclose 会怎样?——`asyncio.run` 退出时 `shutdown_asyncgens` 兜底;自己管理 loop 则资源可能在 loop 已关闭后才被 finalize,抛 "Event loop is closed"。2) `aclose` 与 `asend(None)` 的关系?——`aclose()` 等价于在挂起点注入 GeneratorExit,`asend(None)` 是更底层的同一机制。

```mermaid
sequenceDiagram
    participant User as async for 循环
    participant Agen as async generator 帧
    participant Loop as 事件循环
    User->>Agen: anext
    Agen->>Loop: await IO
    Loop-->>Agen: 就绪 yield 值
    User->>User: break 提前退出
    Note over Agen: 帧悬挂在 yield 引用未释放
    User->>Agen: aclose 或 loop.shutdown_asyncgens
    Agen->>Agen: finally 执行 释放连接
```
