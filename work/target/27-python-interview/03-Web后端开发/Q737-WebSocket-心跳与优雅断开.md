---
title: [Q737] WebSocket 心跳与优雅断开
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q737 · WebSocket 心跳与优雅断开

> 难度:★★★★ | 标签:FastAPI, WebSocket, 可用性

**问**:TCP 连接假死怎么办?WebSocket 的心跳、超时与断开怎么设计?

**答**:对端断网或 NAT 超时后 TCP 不一定立刻感知,表现为连接"假死"。方案是应用层心跳:`asyncio.wait_for(receive, timeout)` 等消息,超时后发 ping 要求 pong,再超时就主动 close 并清理注册表。优雅断开的两件事:服务端 close 带明确 code(如 4000 表示业务下线),客户端据此决定是否重连;服务端退出前广播 close,给客户端迁移窗口。

```python
# file: code/03_Web后端开发/q737_ws_heartbeat.py
import asyncio
try:
    from fastapi import FastAPI, WebSocket, WebSocketDisconnect
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
IDLE_TIMEOUT = 0.2

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            try:
                msg = await asyncio.wait_for(ws.receive_text(), timeout=IDLE_TIMEOUT)
                await ws.send_text(f"echo:{msg}")
            except asyncio.TimeoutError:
                await ws.send_text("ping")                      # 空闲先探活
                pong = await asyncio.wait_for(ws.receive_text(), timeout=IDLE_TIMEOUT)
                if pong != "pong":
                    break                                       # 假死, 断开
    except (WebSocketDisconnect, asyncio.TimeoutError):
        pass
    finally:
        await ws.close()

client = TestClient(app)
with client.websocket_connect("/ws") as w:
    w.send_text("hi")
    print(w.receive_text())   # echo:hi
    print(w.receive_text())   # 空闲超时后收到 ping
    w.send_text("pong")
```

**追问**:
- 为什么不用 WebSocket 协议自带的 ping/pong 帧?——协议帧由库和系统代理控制,应用层心跳可控且能穿透只转发数据的中间设备。
- 客户端重连怎么避免风暴?——指数退避加抖动,服务端返回的 close code 里给出是否可重连的语义。
