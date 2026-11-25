---
title: "[Q6089] ASGI 请求生命周期的 receive/send 状态机原理"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6089 · ASGI 请求生命周期的 receive/send 状态机原理

难度：★★★★☆ ｜ 标签：原理深挖 / ASGI / Starlette / 事件消息

**问**：一个 ASGI 应用收到的三个参数（scope、receive、send）背后的消息协议是什么？"一次请求"在协议层是哪些事件的序列？为什么手动 send 两个 `http.response.body` 会报错？

**答**：
- **结论**：ASGI 是**事件消息协议**：应用是 `async def app(scope, receive, send)`。HTTP 请求的生命周期事件序列：`receive` 依次给出 `http.request`（body 分块，`more_body` 标记是否还有）→ `http.disconnect`；`send` 必须**按协议序**发出：`http.response.start`（status+headers，且只能一次）→ 一个或多个 `http.response.body`（最后一个 `more_body: False` 收尾）。violations：send 两次 start、在 start 前发 body、`more_body` 不收 False → uvicorn 直接抛异常或断连（Q6078 的 StreamingResponse 就是合法的多次 body）。scope 是请求级只读字典（type/http_version/path/headers...）， lifespan 场景 scope.type="lifespan" 走另一套 startup/shutdown 消息。
- **取舍**：为什么协议设计成消息流而非函数调用：同一协议覆盖 HTTP/WebSocket/lifespan 三种形态（ws 的 connect/accept/receive/send/disconnect），服务器与应用解耦——uvicorn/granian/hypercorn 可互换（Q6065）。中间件（Q6062）就是"包一层 app，转发或改写消息"。理解消息序才能解释：为什么必须在收到完整请求体前**不能**先发响应（可以！`http.response.start` 后服务器会停止读 body——这是"提前拒绝大文件上传"的实现原理）、为什么 SSE 断开要靠 `http.disconnect` 事件感知（Q6071）。
- **实战**：调试手段：自己写裸 ASGI 应用（不经过 FastAPI）测试消息序；`uvicorn --log-level trace` 级别看消息；TestClient 是模拟服务器，它按协议喂消息但**行为与真实服务器有差**（如 disconnect 时机），消息序 bug 要用真服务器复现。

```python
"""裸 ASGI 应用：亲手操作 receive/send 消息序（标准库 + 手写驱动）"""
import json

async def raw_app(scope, receive, send):
    assert scope["type"] == "http"
    # 1) 读请求体：http.request 消息分块到达，more_body 标记续传
    body = b""
    while True:
        msg = await receive()
        if msg["type"] == "http.request":
            body += msg.get("body", b"")
            if not msg.get("more_body"):
                break
        elif msg["type"] == "http.disconnect":
            return                              # 客户端断开：直接退出，不再 send
    # 2) 响应必须先 start 再 body，且 start 只能一次
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"application/json")]})
    payload = json.dumps({"echo": body.decode() or "<empty>", "path": scope["path"]}).encode()
    await send({"type": "http.response.body", "body": payload, "more_body": False})

# --- 手写迷你驱动：扮演服务器按协议喂消息（学习用；生产用 uvicorn）---
class FakeServer:
    def __init__(self, body=b"hello asgi"):
        self.body, self.pos, self.sent, self.done = body, 0, [], False
    async def receive(self):                     # 服务器 → 应用
        if self.pos < len(self.body):
            chunk = self.body[self.pos:self.pos + 3]
            self.pos += 3
            return {"type": "http.request", "body": chunk, "more_body": self.pos < len(self.body)}
        return {"type": "http.disconnect"}
    async def send(self, msg):                   # 应用 → 服务器（校验协议序）
        if msg["type"] == "http.response.start":
            assert "status" in msg and not self.sent, "response.start 只能一次"
        elif msg["type"] == "http.response.body":
            assert self.sent or "必须先发 response.start", "body 前必须先 start"
            if not msg.get("more_body"):
                self.done = True
        self.sent.append(msg["type"])

async def main():
    srv = FakeServer(b"hi")
    await raw_app({"type": "http", "method": "GET", "path": "/demo", "headers": []},
                  srv.receive, srv.send)
    print("消息序:", srv.sent)
    print("收尾正确:", srv.done)

import asyncio
asyncio.run(main())

# 3) 提前拒绝大上传的原理：先发 response.start，服务器停止读 body
async def guard_app(scope, receive, send):
    msg = await receive()                        # 第一块
    if msg.get("more_body"):                     # 声明还有后续 → 拒绝
        await send({"type": "http.response.start", "status": 413, "headers": []})
        await send({"type": "http.response.body", "body": b"payload too large", "more_body": False})
        return                                    # 不再 receive：服务器侧停止接收
    await send({"type": "http.response.start", "status": 200, "headers": []})
    await send({"type": "http.response.body", "body": b"ok", "more_body": False})
print("提前 413 的机制：start 后服务器停止读请求体（Q6051 大请求体 OOM 的根治路径之一）")
```

**追问链**
1. WebSocket 在同一协议下的消息序是什么？和 HTTP 差在哪？
   1. ws 生命周期：应用收到 `websocket.connect` → 应用可选 `websocket.accept`/`websocket.close` → 双向 `websocket.send/receive`（text/bytes）→ 任一侧 `websocket.disconnect`；区别是 accept 前应用有"拒绝权"，且连接是长期双向流——所以断开检测、背压（send 不 await drain 会堆内存）都比 HTTP 更关键。
   2. 追问：为什么 `websocket.accept` 之前就能 receive 到数据？——协议允许在 accept 前客户端消息排队，应用可以"先看第一帧再决定收不收"，实现按首帧路由的网关。
2. lifespan 协议解决什么问题？和 3.0 之前的 on_event 有什么本质差？
   1. lifespan 用独立 scope（type="lifespan"）的消息对（`lifespan.startup` → 应用 `lifespan.startup.complete`，shutdown 同理）把"应用级启动/清理"从模块导入期搬到协议里——多 worker/多实例下每个进程都有明确的初始化与排空点，且失败能显式上报（Q6001 的启动失败回滚就靠 complete/error 消息）。
   2. 追问：TestClient 的 lifespan 行为差在哪？——TestClient 用 with 块进入/退出 lifespan，真实 uvicorn 在 worker 启动时跑；依赖 lifespan 打日志验证顺序的测试可能与生产时序不一致，关键路径要用真服务器冒烟。

## 背诵要点
- ASGI = scope + receive/send 消息流；HTTP 序：http.request(more_body 分块) → http.disconnect；响应序：response.start(仅一次) → response.body(more_body=False 收尾)。
- response.start 发出后服务器停止读请求体——"提前 413 拒绝大上传"的协议级实现。
- 同一协议覆盖 http/ws/lifespan 三形态，服务器可替换；TestClient 与真实服务器的 disconnect/lifespan 时序有差，消息序 bug 用真服务器复现。

## 复盘追问
- 线上偶发 "Response content longer than Content-Length" 类 uvicorn 报错，按消息序怎么排查？
- 要实现"请求体超 100MB 且已收 1MB 就断开"，用裸 ASGI 还是框架中间件？各自的坑？
