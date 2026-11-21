---
title: [Q6062] ASGI 中间件双层结构：Stack 中间件与原生 ASGI
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6062 · ASGI 中间件双层结构：框架中间件与原生 ASGI 中间件

> 难度:★★★★★ | 标签:原理深挖, ASGI, 中间件, Starlette

**问**：FastAPI 加中间件有两种姿势：`app.add_middleware(BaseHTTPMiddleware)` 和手写 `@app.middleware("http")`，还有更底层的"纯 ASGI 中间件"。三层各自发生在协议栈哪一层？为什么 BaseHTTPMiddleware 大量使用会有任务泄漏与流式失效问题？性能敏感路径该用哪层？

**答**：ASGI 应用就是一个可调用：`async def app(scope, receive, send)`，中间件即"包住它的可调用"。三层结构：a) **纯 ASGI 中间件**：直接操作 scope/receive/send——最底层，能看到协议事件流（http.request.start / http.response.body 逐块），无额外开销，能做流式响应、Early Hints、Websocket 全协议处理；b) **Starlette BaseHTTPMiddleware**：把 ASGI 协议"翻译"成 request/response 对象模型——内部为每个请求创建 Task 运行下游 app，用队列把 send 事件桥接回来；c) **路由层依赖/DI**：根本不算中间件，是 handler 内代码。BaseHTTPMiddleware 的两个代价：a) **每请求多一个 Task + 一个内存队列**（桥接 send），中间件叠 N 层就是 N 个 Task——Task 泄漏类 bug（下游异常时桥接 Task 不结束）是 Starlette 长期 issue 源头；b) **流式语义受损**：下游的 send(body chunk) 要经过队列中转，backpressure 变形；且 `send` 事件里混合了 response.start/body，改写响应体的中间件（如压缩、签名）在 BaseHTTP 层要消费完整 body 才能工作——流式变缓冲（与 Q6011/Q6052 慢客户端问题联动）。**异常边界差异**：BaseHTTP 里可以用 try/except 拿到 handler 异常返回统一响应，纯 ASGI 层异常已包装成 response.start 之前的崩溃，要靠 exception middleware；**contextvars 差异**：BaseHTTP 的 Task 拷贝上下文，set 不回传（见 Q5561），改写请求上下文的中间件必须用纯 ASGI 层。选型：鉴权/限流/改 scope（重定向、header 注入）用纯 ASGI；需要"读完整响应再改"的用 BaseHTTP 但控制数量；每层都要实测延迟叠加（一层 BaseHTTP 约加 0.1-0.3ms）。

```python
# file: code/03_Web后端开发/q6062_asgi_middleware.py
import asyncio, time, json

# ---- 极简 ASGI 内核: 演示 scope/receive/send 协议 ----
async def send_json(send, status, obj):
    body = json.dumps(obj).encode()
    await send({"type": "http.response.start", "status": status,
                "headers": [(b"content-type", b"application/json")]})
    await send({"type": "http.response.body", "body": body})

async def endpoint(scope, receive, send):
    await send_json(send, 200, {"hello": "world", "user": scope.get("user", "?")})

# ---- 层1: 纯 ASGI 中间件: 直接改 scope, 零桥接开销 ----
def asgi_auth(app):
    async def middleware(scope, receive, send):
        if scope["type"] == "http":
            auth = dict(scope.get("headers", {})).get(b"authorization", b"")
            if auth != b"Bearer tok":            # 鉴权在协议层, 改 scope 传下去
                await send_json(send, 401, {"error": "unauthorized"})
                return
            scope["user"] = "alice"
        await app(scope, receive, send)
    return middleware

# ---- 层2: BaseHTTP 风格: Task + 队列桥接 send (演示其结构成本) ----
def http_style_middleware(app):
    async def middleware(scope, receive, send):
        queue = asyncio.Queue()                  # 每请求一个桥接队列
        async def run_downstream():
            await app(scope, receive, queue.put) # 下游 send 进队列
            await queue.put(None)                # 结束哨兵
        task = asyncio.create_task(run_downstream())   # <-- 每请求多一个 Task
        while True:
            ev = await queue.get()               # send 事件经队列中转
            if ev is None: break
            await send(ev)
        await task
    return middleware

app = http_style_middleware(asgi_auth(endpoint))

async def request(headers=(b"authorization", b"Bearer tok")):
    scope = {"type": "http", "method": "GET", "path": "/",
             "headers": {headers[0]: headers[1]}}
    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}
    out = []
    async def send(ev): out.append(ev)
    t0 = time.perf_counter()
    await app(scope, receive, send)
    return out[0]["status"], (time.perf_counter() - t0) * 1000

async def main():
    print("带 token:", await request())
    print("无 token:", await request(headers=(b"x", b"y")))   # 纯ASGI层直接 401, 未到下游
    # 洋葱顺序: http_style -> asgi_auth -> endpoint
    print("层级: BaseHTTP(Task+队列桥接) > 纯ASGI(改scope) > endpoint")
    print("选型: 改scope/header 用纯 ASGI; 读完整响应才改的控制在少数层")

asyncio.run(main())
```

**追问**：1) BaseHTTPMiddleware 的"任务泄漏"具体是什么形态？——下游 app 异常或客户端断连时，桥接 Task 可能等待永远不会来的队列事件（.receive 挂起），Starlette 用 cancel_on_collapse/shield 组合修了多轮，升级版本时要回归"客户端中断+异常路径"用例；这也是生产保持框架版本与回归中间件测试的理由。2) 为什么改写请求上下文的中间件必须在纯 ASGI 层？——BaseHTTP 在新 Task 里跑下游，Task 拷贝 contextvars 快照（见 Q5561），中间件里 `ContextVar.set` 对下游不可见；纯 ASGI 层与下游同一 Task 同一 Context，set 生效——鉴权后注入 user 就要求这个。3) 纯 ASGI 层怎么读请求体做签名校验？——循环 receive() 收 body 块聚合后再转发给下游（要自己管理 more_body 分块），这是"读 body 的中间件必须自己实现缓冲"的原因，也解释了为什么这类中间件天然和流式/大请求体（Q6051）冲突。

## 背诵要点
- ASGI 应用 = `app(scope, receive, send)`；纯 ASGI 中间件直接改 scope/操作事件流，BaseHTTPMiddleware 用 Task+队列把协议翻译成 request/response。
- BaseHTTP 两代价：每请求多一个 Task 和桥接队列（N 层 N 个 Task，泄漏 bug 源）、流式变缓冲（backpressure 变形）。
- 改 scope/上下文/鉴权用纯 ASGI（contextvars 同 Task 才可见）；读完整响应再改的层要控制数量并测延迟叠加。

## 复盘追问
- 你们的中间件栈有几层、每层在哪一级？有没有 BaseHTTP 层做"改 scope 或上下文"的隐性 bug？（提示：对照 contextvars 差异排查鉴权注入用户失效问题）
- 加一层中间件的延迟有没有实测？流式接口（SSE/大响应）经过压缩/改写层后还流吗？（提示：压测中间件叠加成本；SSE 链路逐层验证缓冲行为）
