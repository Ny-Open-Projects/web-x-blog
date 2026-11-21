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
