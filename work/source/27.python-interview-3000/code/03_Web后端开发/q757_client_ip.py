try:
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

TRUSTED_PROXIES = 1  # 信任的代理层数

def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for", "")
    if forwarded:
        parts = [p.strip() for p in forwarded.split(",")]
        return parts[-TRUSTED_PROXIES]   # 取右侧可信层写入的地址
    return request.client.host if request.client else "unknown"

app = FastAPI()

@app.get("/ip")
def ip(request: Request):
    return {"ip": client_ip(request)}

client = TestClient(app)
r = client.get("/ip", headers={"X-Forwarded-For": "1.2.3.4, 10.0.0.9"})
print(r.json())  # 不取被伪造的 1.2.3.4
