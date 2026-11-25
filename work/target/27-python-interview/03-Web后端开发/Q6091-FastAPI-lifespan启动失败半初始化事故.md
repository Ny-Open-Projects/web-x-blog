---
title: "[Q6091] FastAPI lifespan 启动失败半初始化事故复盘"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6091 · FastAPI lifespan 启动失败半初始化事故复盘

难度：P6-P7 | 标签：事故复盘 | FastAPI lifespan | 启动编排

**问**：服务启动时连了 DB、注册了定时任务，随后 Redis 连接失败抛异常。流量打进来一半组件不可用，K8s 又因探针部分通过而没重启。lifespan 抛异常后 ASGI 服务器到底处于什么状态？"启动失败要回滚"的正确编排是什么？

**答**：
结论：lifespan（`async with` 的 startup 段）抛异常时，uvicorn 会中止启动并退出进程——但**异常点之前已建立的资源不会自动回滚**，你的 finally 能做的只有你自己写的清理；更隐蔽的是：如果服务被配置成"启动失败也不退出"（如某些 supervisor 场景）或异常被吞，就会进入"部分初始化"状态——探针若只查 DB 就可能放流量进来。正确编排：① startup 段按依赖顺序初始化，任何一步失败立即抛出（fail-fast），让进程退出由编排层重启；② 把初始化产物放进一个结构化的 AppState，并注册**逆序回滚**；③ readiness 探针必须检查"全部关键依赖就绪"而不是进程活着；④ 每个启动步骤加超时与幂等（重试由编排层做，不 lifespan 里无限重试）。
取舍：在 lifespan 里做"重试到成功"会把失败变成不可观测的长时间挂起（探针超时→OOMKill 循环），不如快速失败交给 K8s 重启策略。
实战：启动清单 = 每步 try/超时 → 失败即抛 → finally 逆序清理；lifespan 的 `async with` 语义保证 startup 段异常时 shutdown 段代码（with 退出）会被执行——把回滚写在 yield 之后的 finally，而不是相信 uvicorn 帮你收尾。

```python
import asyncio, sys
from contextlib import AsyncExitStack

# 不依赖 FastAPI 安装：用 lifespan 协议同构的 async with 编排演示
class FakeLifespan:
    def __init__(self):
        self.state = {}
        self.started = False
    async def __aenter__(self):
        return self.state
    async def __aexit__(self, et, ev, tb):
        # shutdown 段：yield 之后的代码，逆序清理
        for name in reversed(self._order):
            if name in self.state:
                print(f"[rollback] close {name}")
                del self.state[name]
        self.started = False

def build_lifespan(steps):
    """steps: [(name, async_init, may_fail)]  逆序回滚 + fail-fast"""
    ls = FakeLifespan()
    async def runner():
        async with ls:
            ls._order = []
            for name, init, may_fail in steps:
                res = await asyncio.wait_for(init(), timeout=0.5)
                ls.state[name] = res
                ls._order.append(name)
                print(f"[startup] {name} ok")
            ls.started = True
            yield ls.state
    return runner

async def ok(name):
    return f"conn-{name}"

async def boom():
    raise ConnectionError("redis down")

async def main():
    steps = [("db", lambda: ok("db"), False), ("cache", boom, True)]
    # 启动失败：startup 段抛异常，with 退出执行已注册资源的回滚
    runner = build_lifespan(steps)
    agen = runner().__aiter__()
    try:
        state = await agen.__anext__()
    except (ConnectionError, asyncio.TimeoutError) as e:
        print(f"[startup] cache 失败: {e} → 进程 fail-fast，已建资源已回滚")

    # 全部成功：正常进入服务期，退出时 shutdown 段执行
    runner2 = build_lifespan([("db", lambda: ok("db"), False)])
    agen2 = runner2().__aiter__()
    state = await agen2.__anext__()
    print("[serve] ready, state keys:", list(state))
    await agen2.aclose()   # 模拟优雅停机 → shutdown 段

if __name__ == "__main__":
    asyncio.run(main())
```

**追问 1**：为什么回滚代码要写在 `yield` 之后的 finally 而不是 except？
- 追问 2 层：lifespan 协议下 startup 异常同样触发 async with 的退出路径，finally 是唯一保证两种路径（异常退出/优雅停机）都执行的位置；except 只覆盖异常路径，且拿不到"已启动到哪一步"的逆序信息。
- 追问 3 层：配合 `AsyncExitStack` 可以让每个组件注册自己的 close，栈式逆序天然正确，比手写 order 列表更稳。

**追问 2**：老写法 `@app.on_event("startup")` 与 lifespan 的差异？
- 追问 2 层：on_event 已弃用，无法用 async with 表达"失败时进入清理段"，且多个 startup handler 之间的失败传播不透明；lifespan 是 Starlette 0.26+/FastAPI 推荐形式。
- 追问 3 层：迁移时注意 lifespan 只有一个入口（yield 前后），原先分散的多个 handler 要合并，初始化顺序要显式声明。

## 背诵要点
1. lifespan startup 段异常不会自动回滚已建资源；回滚写在 yield 后的 finally，逆序清理。
2. 启动失败策略 = fail-fast + 编排层重启，不在 lifespan 里无限重试（变成不可观测挂起）。
3. readiness 探针必须覆盖全部关键依赖，防止"半初始化"放流量。

## 复盘追问
1. 为什么探针没拦住半初始化实例？——liveness 只查进程、readiness 只查了 DB；探针要按启动清单逐项映射。
2. 启动顺序里 DB 成功、Redis 失败，DB 连接泄漏到哪里？——未注册 close 的连接池；用 AsyncExitStack 统一注册可消灭这类泄漏。
