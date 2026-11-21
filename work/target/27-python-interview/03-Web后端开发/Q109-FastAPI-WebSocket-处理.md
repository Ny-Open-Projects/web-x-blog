---
title: [Q109] FastAPI WebSocket 处理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q109 · FastAPI WebSocket 处理

> 难度:★★★ | 标签:FastAPI, WebSocket

**问**:FastAPI 中如何实现 WebSocket 连接?如何在连接建立时做认证?

**答**:用 `@app.websocket('/ws')` 声明端点,通过 `await ws.accept()` 握手、`ws.receive_text()/send_text()` 收发消息,`WebSocketDisconnect` 捕获断开。WebSocket 无法标准地携带 Authorization 头,认证常通过查询参数传 token、或依赖 `Cookie`、或在 `accept()` 前校验 `ws.headers`/`ws.query_params` 后再决定 accept 还是 close。生产中还需处理心跳与连接管理器广播。

```python
# file: code/03_Web后端开发/q109_websocket.py
try:
    from fastapi import FastAPI, WebSocket, WebSocketDisconnect
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class Hub:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket, token: str):
        if token != 'abc':                 # 握手前认证
            await ws.close(code=4001)
            return
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast(self, text: str):
        for ws in list(self.active):
            await ws.send_text(text)

hub = Hub()

@app.websocket('/ws')
async def ws_endpoint(ws: WebSocket, token: str = ''):
    await hub.connect(ws, token)
    try:
        while True:
            msg = await ws.receive_text()
            await hub.broadcast(f'echo: {msg}')
    except WebSocketDisconnect:
        hub.disconnect(ws)
```

**追问**:
- WebSocket 认证的常见做法?——accept 之前校验 query token/cookie,不合法直接 `close(code=1008)`;连接建立后每条消息还可带签名校验防会话劫持。
- 断线重连怎么设计?——客户端指数退避重连,服务端用连接 ID 恢复订阅;心跳(ping/pong 帧或应用层)探测半开连接。
- WebSocket 广播怎么落地?——进程内连接注册表 + 跨进程 pub/sub(Redis channels),单进程内存表在多 worker 下只能覆盖本进程连接。
