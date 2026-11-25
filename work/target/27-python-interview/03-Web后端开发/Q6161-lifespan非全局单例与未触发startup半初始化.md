---
title: "[Q6161] lifespan 非全局单例与未触发 startup 的半初始化"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6161 · lifespan 非全局单例与未触发 startup 的半初始化

难度：P7 ｜ 标签：ASGI、lifespan、多 worker、启动时序、半初始化

**问**：`lifespan` 里创建的连接池/后台消费者是"进程级单例"还是"全局单例"？多个 uvicorn worker 各自跑一遍 lifespan 意味着什么？为什么 `TestClient` 不用 `with` 包起来时 lifespan 不会触发、应用状态停在半初始化？探针（readiness）在 startup 完成前就通过为什么会造成"流量打进半初始化服务"？这和 Q6001/Q6091 讲的启动失败回滚是同一问题吗？

**答**：
结论：`lifespan` 是 **ASGI 服务器与单个应用实例**之间的生命周期协议，不是跨进程全局钩子——每个 worker 进程各自持有自己的 app 实例、各自执行一遍 `lifespan.startup`/`shutdown`，所以"连接池"是**每 worker 一份**（N worker = N 个池、N 份后台任务），不要把全局资源当"整个服务只有一个"。`TestClient(app)` 若不进 `with TestClient(app) as c:` 上下文，很多版本**不会发 `lifespan.startup`**，依赖 lifespan 注入的状态（如 `app.state.db`）仍是 `None`，请求进来就拿到半初始化对象——这是"测试里能跑、上线正常、某个测试单独跑却空指针"的常见原因。K8s readiness 探针若在 startup 未完成时返回 200，流量会打进资源未就绪的实例；正确姿势是让 readiness 依赖"lifespan 完成标志"。

取舍：区分三个层次——① **进程内共享**：lifespan 注入 `app.state`，同 worker 内所有请求共享；② **跨 worker 共享**：必须外置（数据库、Redis），不能在 lifespan 里搞"全局单例"；③ **跨进程协调**：需要选主/分布式锁时另行设计，不要指望 lifespan。测试里统一用 `with TestClient(app)` 或显式 `app.router.lifespan_context`；探针对齐 `app.state.ready` 标志而不是"端口通了"。与 Q6001/Q6091 的关系是互补：那两题讲"启动失败如何整体回滚"，本题讲"启动的作用域与触发时机"——一个管失败路径，一个管正常路径的边界。

实战：事故形态是"4 个 worker 各自起了 4 个后台消费任务，消息被重复消费 4 次"——根因是把 lifespan 当全局单例。排查用 `print(os.getpid())` 在 startup 里确认每 worker 都执行。下面用最小 ASGI 模拟跑出：两个 worker 各触发一次 startup、`state` 是每实例独立的、以及未触发 startup 时请求看到半初始化状态。

```python
import asyncio

class App:
    def __init__(self):
        self.state = {"db": None, "ready": False, "starts": 0}
    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            while True:
                msg = await receive()
                if msg["type"] == "lifespan.startup":
                    self.state["db"] = object()   # 每 worker 一份连接
                    self.state["starts"] += 1
                    self.state["ready"] = True
                    await send({"type": "lifespan.startup.complete"})
                elif msg["type"] == "lifespan.shutdown":
                    self.state["db"] = None
                    self.state["ready"] = False
                    await send({"type": "lifespan.shutdown.complete"})
                    return
        elif scope["type"] == "http":
            body = b"ok" if self.state["ready"] else b"NOT-READY"
            await send({"type": "http.response.start", "status": 200, "headers": []})
            await send({"type": "http.response.body", "body": body})

async def run_lifespan(app):
    msgs = iter([{"type": "lifespan.startup"}, {"type": "lifespan.shutdown"}])
    async def receive(): return next(msgs, {"type": "lifespan.shutdown"})
    sent = []
    async def send(m): sent.append(m["type"])
    await app({"type": "lifespan"}, receive, send)
    return sent

async def main():
    app = App()
    for _ in range(2):                       # 两个 worker 各跑一遍
        print("lifespan events:", await run_lifespan(app))
    print("startup count:", app.state["starts"], "(每 worker 一次，非全局)")

    untouched = App()                        # 模拟 TestClient 未进 with
    sent = []
    async def send(m): sent.append(m)
    await untouched({"type": "http"}, None, send)
    print("http without startup:", sent[-1]["body"])

asyncio.run(main())
```

**追问一**：为什么应用代码里写 `@app.on_event("startup")` 里的全局变量仍可能"跨 worker 不一致"？——`@app.on_event` 修饰的函数在每个 worker 进程里都执行一遍，但修改的是**本进程**的全局变量；worker 之间内存不共享，所以 A worker 的全局变量改了、B worker 看不到。看起来"同一个全局变量名"，实则 N 份独立副本。要跨 worker 一致必须用外部存储或 IPC，这也是"配置热更新"类功能必须用 Redis 广播而非全局变量的原因。

**追问二**：readiness 探针只检查"进程能响应 HTTP 200"为什么不等于"lifespan 已完成"？——因为 ASGI 服务器可能先开监听 socket、再跑 lifespan；也可能 lifespan 失败但进程还活着（尤其配合多线程/多 worker 时部分实例失败）。此时端口通、但 `app.state.db` 还是 `None`，探针误判为就绪。正确做法是把 `app.state.ready`（由 lifespan 最后一步置位）作为探针的数据源，并对"ready 后资源又失效"的情况做持续健康检查——探针反映的是"应用逻辑就绪"，不是"OS 层端口打开"。

## 背诵要点
- lifespan 是每 worker/每 app 实例一次，非全局；N worker = N 份连接池与后台任务。
- `TestClient` 不用 `with` 可能不触发 startup → `app.state` 半初始化；测试统一用上下文管理器。
- readiness 探针应依赖 `app.state.ready` 而非端口通；与 Q6001/Q6091 的"失败回滚"互补，本题管正常路径边界。

## 复盘追问
- 4 个 worker 各起一个后台消费任务导致消息重复消费 4 次，如何用 lifespan 作用域解释并给出选主方案？（每 worker 一次 + 外部协调，讨论进程内共享 vs 跨 worker 共享）
- 为什么"端口能响应 200"不等于"应用已就绪"？（lifespan 与监听 socket 的时序、部分 worker 失败，讨论 ready 标志驱动的探针）
