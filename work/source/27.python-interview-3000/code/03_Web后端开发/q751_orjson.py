try:
    from fastapi import FastAPI
    from fastapi.responses import ORJSONResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install orjson fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI(default_response_class=ORJSONResponse)

@app.get("/big")
def big():
    return {"items": [{"id": i, "name": f"item-{i}"} for i in range(1000)]}

client = TestClient(app)
r = client.get("/big")
print(r.status_code, len(r.content))
