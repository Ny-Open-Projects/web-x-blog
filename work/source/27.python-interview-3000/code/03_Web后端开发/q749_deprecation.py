try:
    from fastapi import APIRouter, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
v1 = APIRouter(prefix="/v1", deprecated=True)
v2 = APIRouter(prefix="/v2")

@v1.get("/price", description="将于 2026-12-31 下线,请迁移 /v2/price")
def price_v1():
    return {"price": 100}

@v2.get("/price")
def price_v2():
    return {"price": 100.0, "currency": "CNY"}

app.include_router(v1)
app.include_router(v2)

client = TestClient(app)
print(client.get("/v1/price").json())
print(client.get("/v2/price").json())
