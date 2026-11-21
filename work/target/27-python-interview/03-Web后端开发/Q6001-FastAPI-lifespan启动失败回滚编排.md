---
title: [Q6001] FastAPI lifespan 启动失败回滚编排
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6001 · FastAPI lifespan 启动失败回滚编排

> 难度:★★★ | 标签:FastAPI 0.95+, lifespan, 启动编排

**问**：lifespan 里依次初始化 DB 连接池、缓存、后台消费者，第 3 步失败抛异常会怎样？已建好的前两步资源谁来清？怎么把启动编排做成「失败即整体回滚」？

**答**：lifespan 是一个 asynccontextmanager：`yield` 前是启动段，`yield` 后是关停段。关键陷阱：**启动段中途抛异常，`yield` 之后的关停段永远不会执行**——前两步已成功的资源不会自动清理（进程退出可能靠 GC/OS 兜底，但连接池没优雅关闭、远端消费者没发离开心跳，都是脏状态）。正解是把启动编排写成**事务式**：用 `contextlib.AsyncExitStack` 登记每个资源，任何一步失败统一逆序 unwind；只有全部成功后才 `yield` 给应用。工程要点：1) 启动失败 → uvicorn 直接拒绝拉起服务，K8s startupProbe 不通过就不会接流量，所以 fail-fast 是对的，别吞异常硬起；2) 回滚本身也要容错（回滚中再抛异常只记日志，别掩盖原始错误）；3) 资源之间的依赖顺序要在栈里显式表达，后进先出的 unwind 顺序天然等于依赖逆序。

```python
# 基线:FastAPI 0.95+/Python 3.9+。本 demo 用标准库模拟启动编排,缺 FastAPI 也能直接运行。
import asyncio
from contextlib import AsyncExitStack

class FakeResource:
    def __init__(self, name, fail=False):
        self.name, self.fail = name, fail
    async def __aenter__(self):
        if self.fail:
            raise RuntimeError(f"{self.name} 初始化失败(如连不上依赖)")
        print(f"  acquired: {self.name}")
        return self
    async def __aexit__(self, *exc):
        print(f"  released : {self.name}")   # 逆序执行,天然等于依赖回滚
        return False                          # 不吞异常

async def startup(stack: AsyncExitStack, third_fails: bool):
    # 每步 enter 即登记,任何一步抛异常,栈自动逆序清理已成功步骤
    db = await stack.enter_async_context(FakeResource("db-pool"))
    cache = await stack.enter_async_context(FakeResource("redis-pool"))
    consumer = await stack.enter_async_context(FakeResource("bg-consumer", fail=third_fails))
    return {"db": db, "cache": cache, "consumer": consumer}

async def app_lifespan():
    """等价于 FastAPI lifespan 的启动半段:失败即整体回滚,不产出 state"""
    async with AsyncExitStack() as stack:
        state = await startup(stack, third_fails=False)
        print("lifespan yield —— 应用就绪")
        yield state
        print("lifespan 收尾")

async def main():
    agen = app_lifespan()
    await agen.__anext__()          # 执行启动段
    await agen.aclose()             # 模拟优雅关停:走关停段

    agen = app_lifespan()
    try:
        await agen.__anext__()      # 第三步抛 RuntimeError → 自动回滚前两步
    except RuntimeError as e:
        print(f"启动失败: {e}(上面已逆序 released db-pool ← redis-pool)")
    # 真实 FastAPI 写法:
    # from contextlib import asynccontextmanager
    # @asynccontextmanager
    # async def lifespan(app): ...同上,失败抛出即拒绝拉起...

asyncio.run(main())
```

**追问**：
1) 为什么不把清理逻辑写进 `except` 逐个 try？——三步就要三层嵌套 try，漏一层就是泄漏；AsyncExitStack 把「登记」和「清理」解耦，新增资源只加一行 enter，回滚顺序自动正确。手写 except 的问题在于启动步骤增多时组合爆炸。
2) 启动失败时 K8s 侧应该怎么配合？——startupProbe 只探「进程是否完成初始化」，lifespan 抛异常 uvicorn 会退出，restartPolicy 拉起重试；要配 `terminationGracePeriodSeconds` 与退避，避免失败循环打爆依赖（比如 DB 真挂了，10 个 pod 每秒重连）。探针失败时间窗要大于「重试依赖的正常抖动时长」。
3) 关停段和启动段的对称性怎么保证？——所有资源都用同一个 AsyncExitStack，启动即登记，关停自动 unwind；禁止在关停段手写清理清单，那会和启动段漂移。若关停本身可能卡死（远端 drain 慢），在 lifespan 外层再套一个总超时，超时后放弃等待让进程退出。
