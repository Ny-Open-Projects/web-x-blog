import time
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        start = time.perf_counter()

        async def send_wrapped(message):
            if message["type"] == "http.response.start":
                ms = int((time.perf_counter() - start) * 1000)
                headers = list(message.get("headers", []))
                headers.append((b"x-process-ms", str(ms).encode()))
                message = {**message, "headers": headers}
            await send(message)

        await self.app(scope, receive, send_wrapped)

app = FastAPI()

@app.get("/hi")
def hi():
    return {"hi": True}

app.add_middleware(TimingMiddleware)

client = TestClient(app)
r = client.get("/hi")
print(r.json(), r.headers.get("x-process-ms") is not None)
