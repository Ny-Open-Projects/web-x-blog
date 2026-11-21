try:
    from fastapi import APIRouter, Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

order = []
app = FastAPI(dependencies=[Depends(lambda: order.append("app"))])
router = APIRouter(dependencies=[Depends(lambda: order.append("router"))])

def path_dep():
    order.append("path")

@router.get("/ping", dependencies=[Depends(path_dep)])
def ping():
    return {"ok": True}

app.include_router(router, dependencies=[Depends(lambda: order.append("include"))])

client = TestClient(app)
client.get("/ping")
print("依赖执行顺序:", order)
