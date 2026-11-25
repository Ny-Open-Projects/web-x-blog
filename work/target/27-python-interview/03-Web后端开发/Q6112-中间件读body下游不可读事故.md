---
title: [Q6112] 中间件读 body 下游不可读事故
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6112 · 中间件消费 body 后下游不可读事故

> 难度:★★★★☆ | 标签:事故复盘, ASGI, 请求体

**问**:给 Starlette/FastAPI 加了一个签名校验中间件，在里面 `await request.body()` 读完整请求体验签，结果下游 handler 里 Pydantic 一直报"body 为空"。为什么 body 只能读一次？中间件里怎么正确地"读完再还给下游"？

**答**:结论：ASGI 里请求体是通过 `receive` 通道逐块推来的**流**，消费完就没了——`await request.body()` 会循环 `receive` 直到读完并**缓存进 `request._body`**。事故机理分两层：a) 中间件层用**裸 scope/receive 包装**（纯 ASGI 中间件，引 Q6062）自己调 `receive` 读 body 后，下游 handler 里**新建的 Request 对象**重新调 `receive`，通道已空 → body 为空；b) 如果中间件用 Starlette 的 `Request` 对象读取，body 缓存在**那个 Request 实例**上，下游 FastAPI 依赖解析又构造了**另一个 Request 实例**，缓存不共享。修复姿势：① 纯 ASGI 中间件里读完后**重放 body**：把读到的字节按 `more_body` 协议重新构造 `receive`——先发一个 `{"type": "http.request", "body": 全部字节, "more_body": False}`，再透传后续 `http.disconnect`；② Starlette 应用内中间件（BaseHTTPMiddleware 之下）用 `request.body()` 后传**同一个 request 对象**给 call_next（较新版本 Starlette 的 `_CachedRequest` 已缓解，但跨对象仍不共享）；③ 更优解：验签这类需求走**流式验签**或只对 header 验签，避免缓冲大 body（对照 Q6051 大 body OOM）。取舍：重放 body 会把整个请求体缓存在内存，等于给所有请求加了全量缓冲——大文件上传场景必须按 content-length 阈值跳过重放、改流式校验或直接拒绝。

```python
# 基线: starlette>=0.28（纯标准库 + starlette；FastAPI 0.100+ 同构）
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request

async def verify_and_replay(scope, receive, send):
    """纯 ASGI 中间件：读 body 验签后，按协议重放给下游"""
    body = b""
    while True:                                  # 读完整个流
        msg = await receive()
        if msg["type"] == "http.request":
            body += msg.get("body", b"")
            if not msg.get("more_body", False):
                break
        elif msg["type"] == "http.disconnect":
            return                                # 客户端断开，直接终止

    # 事故修复点：重建 receive 通道，把 body 重放回下游
    replayed = {"sent": False}

    async def receive_replay():
        if not replayed["sent"]:
            replayed["sent"] = True
            return {"type": "http.request", "body": body, "more_body": False}
        return await receive()                    # 透传 disconnect 等

    await app(scope, receive_replay, send)

async def handler(request: Request):
    data = await request.json()                   # 下游能拿到重放后的 body
    return JSONResponse({"echo": data, "got": bool(data)})

async def too_large_guard(scope, receive, send):
    """大 body 场景：按 content-length 拒绝重放，防内存缓冲放大（Q6051）"""
    headers = dict((k.decode().lower(), v.decode()) for k, v in scope["headers"])
    if int(headers.get("content-length", "0")) > 1_000_000:
        await JSONResponse({"error": "body too large"}, status_code=413)(scope, receive, send)
        return
    await verify_and_replay(scope, receive, send)

app = Starlette(routes=[Route("/echo", handler, methods=["POST"])])

# 自测：伪造 ASGI scope 手动跑通（无需起服务）
import asyncio, json
def run_test():
    scope = {
        "type": "http", "method": "POST", "path": "/echo",
        "headers": [(b"content-type", b"application/json"), (b"content-length", b"17")],
        "query_string": b"", "scheme": "http", "server": ("t", 80),
    }
    payload = json.dumps({"msg": "hi"}).encode()
    msgs = [{"type": "http.request", "body": payload, "more_body": False},
            {"type": "http.disconnect"}]
    it = iter(msgs)

    async def receive():
        return next(it)

    sent = []
    async def send(msg): sent.append(msg)

    asyncio.run(too_large_guard(scope, receive, send))
    body = b"".join(m.get("body", b"") for m in sent if m["type"] == "http.response.body")
    print("下游回显:", json.loads(body))

run_test()
```

**追问一层**:重放 body 时为什么要保持 `more_body` 协议、最后还要透传 `http.disconnect`？漏传会导致什么（对照 Q6089 ASGI 状态机）？
**追二层**:`BaseHTTPMiddleware` 与纯 ASGI 中间件在 body 缓存上的实现差异是什么？为什么流式验签（HMAC 分块喂入）是更工程化的终态？

**背诵要点**
- ASGI body 是 receive 通道上的流，消费即逝；缓存只属于读它的那个 Request 实例。
- 中间件读 body 后必须按 http.request/more_body 协议重放，并透传 disconnect。
- 重放=全量内存缓冲；大 body 走阈值拒绝或流式验签，防 OOM（引 Q6051）。

**复盘追问**
- 事故只在"加了验签中间件后"出现，怎么让这类问题在集成测试阶段暴露？提示：TestClient 带 body 的 POST 全量回归 + ASGI 协议断言。
- 验签中间件被多 worker 反复审计，为什么 header-only 方案（签名不覆盖 body）会被否决？提示：body 可被篡改而签名仍通过，安全边界失效。
