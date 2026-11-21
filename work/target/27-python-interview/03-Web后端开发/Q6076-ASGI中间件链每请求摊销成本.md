---
title: [Q6076] ASGI 中间件链的每请求摊销成本
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6076 · ASGI 中间件链的每请求摊销成本

> 难度:★★★★ | 标签:成本工程, ASGI, 中间件

**问**：中间件链上挂了 8 层（CORS、认证、限流、日志、tracing、压缩、异常兜底、租户注入），每层的"每请求固定成本"是多少、怎么量？哪些中间件必须放在链路哪个位置，位置错了除了 bug 还有什么成本后果？装饰器式中间件（`@app.middleware`）与 BaseHTTPMiddleware 的隐藏开销在哪？

**答**：结论：中间件链每请求成本 = Σ(每层调用开销 + 每层实际工作)。纯 ASGI 转发层很便宜（每层 1-5μs），但 Starlette 的 **BaseHTTPMiddleware 每层都要把下游 app 包成 task + 建 anyio 内存消息流**来模拟"请求/响应对象"，单层 50-200μs——8 层就是每请求毫秒级纯税，这正是"什么都没做也慢"的解释。量化方法：空请求（`/healthz` 无业务）压测，其 P50/QPS 就是链路总税基；再逐层摘除（feature flag）看每层增量，或 py-spy 看 anyio 调度栈（Q6010 手法）。位置即成本：a) **越早短路越省钱**——限流、认证放最外层，被拒绝的请求后面 N 层零成本（顺序错误除了 bug 还有"每请求白做 N 层"的税，功能性问题见 Q6045）；b) 日志/tracing 放认证之后（未认证流量不刷日志），异常兜底放最外层兜住全部；c) 压缩放出口，但它缓冲响应体、与 SSE/流式冲突（Q6071 同源）。装饰器式 `@app.middleware("http")` 就是 BaseHTTPMiddleware 的语法糖，糖纸下面同一个 task 流开销；高性能路径用**纯 ASGI 函数中间件**（直接操作 scope/receive/send 消息），只适合转发/打点类简单逻辑，要读响应 body 的复杂处理不建议手写。实战：每季度对中间件做一次减法审计——合并（日志+tracing 并一层）、降级为配置项、下放到边缘网关。

```python
# file: code/03-Web后端开发/q6076_middleware_cost.py
import asyncio, time, sys

# 1) 纯 ASGI 转发层 vs BaseHTTP 式(task+消息流) 的成本结构对比
def pure_asgi_mw(app):
    async def mw(scope, receive, send):
        await app(scope, receive, send)          # 纯转发, 不造对象流
    return mw

class FakeBaseHTTPMiddleware:
    """模拟 Starlette BaseHTTPMiddleware 结构: 下游包成 task + 队列消息流"""
    def __init__(self, app): self.app = app
    async def __call__(self, scope, receive, send):
        q = asyncio.Queue(maxsize=4)             # 每请求建队列(开销来源之一)
        async def downstream():
            await self.app(scope, receive, lambda m: q.put(m) or asyncio.sleep(0))
        t = asyncio.create_task(downstream())    # 每层一个 task
        while True:
            msg = await q.get()
            if msg == "end": break
        await t

async def downstream_app(scope, receive, send):
    await send("end")

async def bench(mw, n=300):
    scope = {"type": "http"}
    async def receive(): return {"type": "http.request", "body": b""}
    async def send(msg): await asyncio.sleep(0)
    app = mw(downstream_app)
    t0 = time.perf_counter()
    for _ in range(n):
        await app(scope, receive, send)
    return (time.perf_counter() - t0) / n * 1e6

async def main():
    t_pure = await bench(pure_asgi_mw)
    t_bhm  = await bench(lambda a: (lambda s, r, sd: FakeBaseHTTPMiddleware(a)(s, r, sd)))
    print(f"纯 ASGI 转发: {t_pure:.1f}us/请求 | BaseHTTP 式(模拟): {t_bhm:.1f}us/请求 "
          f"(每层 task+队列开销 {t_bhm - t_pure:.1f}us, 真实 Starlette 50-200us/层)")

    # 2) 位置即成本: 第 1 层短路 vs 第 8 层才拒绝
    async def heavy_chain(scope, receive, send):
        _ = sum(i * i for i in range(500))       # 模拟前几层白做的计算
        await downstream_app(scope, receive, send)
    async def early_reject(scope, receive, send):
        if scope.get("blocked"): return          # 第 1 层短路: 后面全免
        await heavy_chain(scope, receive, send)
    async def late_reject(scope, receive, send):
        await heavy_chain(scope, receive, send)
        if scope.get("blocked"): return          # 第 8 层才拒绝: 税已交完
    for tag, app, scope in [("早短路", early_reject, {}),
                            ("晚拒绝", late_reject, {"blocked": True})]:
        t0 = time.perf_counter()
        for _ in range(200):
            await app(scope, lambda: asyncio.sleep(0), lambda m: asyncio.sleep(0))
        print(f"{tag}: {(time.perf_counter()-t0)/200*1e6:.1f}us/请求")

    # 3) 审计口径
    print("审计法: /healthz 空请求 P50+QPS = 链路税基; 逐层摘除(feature flag)看增量")

asyncio.run(main())
print("python:", sys.version.split()[0])
```

**追问**：1) 为什么 BaseHTTPMiddleware 必须用 task + 消息流实现？——它要给用户暴露 `Request`/`Response` 的"对象视图"，而 ASGI 底层是消息对；把 receive/send 桥接成对象流需要缓冲与调度，anyio memory object stream 就是载体；这个抽象的代价无法在库内消除，只能绕开（纯 ASGI）或换框架层实现（FastAPI 曾多次优化该路径）。2) 中间件顺序的"正确序"模板？——外→内：异常兜底（最外，兜全局）→ 限流 → 认证/租户注入 → tracing/日志 → 业务 → 压缩（内/出口）；原则是"廉价的、能短路的在外，贵依赖上下文的在内，改响应出口的在最内"。3) 怎么说服团队做减法？——用税基数据说话：空请求 QPS 与全链 QPS 的差值 × QPS = 白烧 CPU，换算成实例数/月成本；再把"摘除某层后 P50 下降"做成 A/B 报告，减法就有了预算依据。

## 背诵要点
- 链路成本=Σ(层开销+层工作)：纯 ASGI 层 1-5μs，BaseHTTPMiddleware 每层 50-200μs（task+消息流），8 层即毫秒级税。
- 位置即成本：限流/认证最外层早短路，日志/tracing 在认证后，异常兜底最外，压缩最内（且与流式冲突）。
- 量化靠空请求税基 + 逐层摘除；`@app.middleware` 是 BaseHTTPMiddleware 语法糖，性能敏感用纯 ASGI 中间件。

## 复盘追问
- 你们的 /healthz P50 是多少、有几层中间件？税基换算成每月多少实例成本？（提示：空请求压测 + 逐层摘除出报告，用"可省实例数"推动减法审计）
- 有没有压缩/日志中间件与流式响应冲突的隐患？（提示：grep 流式接口路径上的 buffering/压缩中间件，见 Q6071/Q6052，给流式路径单独的中间件白名单）
