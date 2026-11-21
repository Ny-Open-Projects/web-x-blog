try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

inner = FastAPI(title="inner")

@inner.get("/health")
def inner_health():
    return {"app": "inner"}

outer = FastAPI(title="outer")

@outer.get("/health")
def outer_health():
    return {"app": "outer"}

outer.mount("/sub", inner)

client = TestClient(outer)
print(client.get("/health").json())      # 命中 outer 自己的路由
print(client.get("/sub/health").json())  # 前缀转发给子应用
