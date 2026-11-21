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
