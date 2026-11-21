---
title: [Q736] WebSocket 房间广播与连接管理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q736 · WebSocket 房间广播与连接管理

> 难度:★★★★ | 标签:FastAPI, WebSocket

**问**:做一个聊天室,连接管理和广播怎么设计?连接异常关闭怎么处理?

**答**:核心是一个**连接注册表**:按房间维护 WebSocket 集合,join 时 accept 并登记,broadcast 时遍历发送,发送失败就把连接踢出。异常关闭用 `WebSocketDisconnect` 捕获,finally 里保证清理。注意这是**单进程模型**:多 worker 部署时连接分散在各进程,跨进程广播必须引入外部通道(Redis pub/sub、消息队列),这是面试常考的边界意识。

```python
# file: code/03_Web后端开发/q736_ws_room.py
try:
    from fastapi import FastAPI, WebSocket, WebSocketDisconnect
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

class Room:
    def __init__(self):
        self.conns: list[WebSocket] = []

    async def join(self, ws: WebSocket):
        await ws.accept()
        self.conns.append(ws)

    def leave(self, ws: WebSocket):
        if ws in self.conns:
            self.conns.remove(ws)

    async def broadcast(self, text: str):
        for ws in list(self.conns):
            try:
                await ws.send_text(text)
            except Exception:
                self.leave(ws)

room = Room()

@app.websocket("/ws/{room_id}")
async def ws_endpoint(ws: WebSocket, room_id: str):
    await room.join(ws)
    try:
        while True:
            msg = await ws.receive_text()
            await room.broadcast(f"[{room_id}] {msg}")
    except WebSocketDisconnect:
        room.leave(ws)

client = TestClient(app)
with client.websocket_connect("/ws/1") as w1, client.websocket_connect("/ws/1") as w2:
    w1.send_text("hello")
    print(w1.receive_text())
    print(w2.receive_text())
```

**追问**:
- 多 worker 下广播怎么打通?——每个 worker 订阅 Redis 频道,收到消息后向本进程房间成员转发。
- 广播时某个客户端慢怎么办?——每连接带发送队列与水位,超水位踢掉慢消费者,避免一个客户端拖住整个房间。
