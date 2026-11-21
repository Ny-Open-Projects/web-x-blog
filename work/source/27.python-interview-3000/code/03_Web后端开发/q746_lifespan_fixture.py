from contextlib import asynccontextmanager
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    state["pool"] = "connection-pool"
    yield
    state.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/pool")
def pool():
    return {"pool": state.get("pool")}

with TestClient(app) as client:   # with 才触发 lifespan
    print(client.get("/pool").json())
print("退出后资源已清理:", state)
