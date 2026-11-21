try:
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

class BodyPeekMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        chunks = []
        while True:
            msg = await receive()
            chunks.append(msg.get("body", b""))
            if not msg.get("more_body"):
                break
        seen = b"".join(chunks)
        replayed = [{"type": "http.request", "body": seen, "more_body": False}]

        async def receive_replay():
            if replayed:
                return replayed.pop(0)
            return {"type": "http.disconnect"}

        scope = dict(scope, body_size=len(seen))
        await self.app(scope, receive_replay, send)

app.add_middleware(BodyPeekMiddleware)

@app.post("/echo")
async def echo(request: Request):
    raw = await request.body()
    return {"len": len(raw), "size_seen": request.scope.get("body_size")}

client = TestClient(app)
print(client.post("/echo", content=b"hello").json())
