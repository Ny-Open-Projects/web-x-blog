try:
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
MAX_BYTES = 1024  # 演示上限 1KB

@app.post("/upload")
async def upload(request: Request):
    size = 0
    async for chunk in request.stream():
        size += len(chunk)
        if size > MAX_BYTES:
            return {"error": "too large", "size": size}  # 超限提前拒绝
    return {"size": size}

client = TestClient(app)
print(client.post("/upload", content=b"a" * 500).json())
print(client.post("/upload", content=b"a" * 2000).json())
