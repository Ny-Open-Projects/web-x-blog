try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

trace = []
app = FastAPI()

class MarkA:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        trace.append("A-in")
        await self.app(scope, receive, send)
        trace.append("A-out")

class MarkB:
    def __init__(self, app):
        self.app = app
    async def __call__(self, scope, receive, send):
        trace.append("B-in")
        await self.app(scope, receive, send)
        trace.append("B-out")

app.add_middleware(MarkA)  # 先注册
app.add_middleware(MarkB)  # 后注册者在最外层

@app.get("/t")
def t():
    return {"ok": True}

client = TestClient(app)
client.get("/t")
print(trace)
