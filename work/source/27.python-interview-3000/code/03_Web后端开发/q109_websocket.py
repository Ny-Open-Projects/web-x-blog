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
