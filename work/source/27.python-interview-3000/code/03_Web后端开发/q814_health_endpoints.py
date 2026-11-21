try:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

db_ok = True
app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"ok": True}                       # 进程活着就 200, 不查依赖

@app.get("/readyz")
def readyz():
    if not db_ok:                             # 依赖不可用就摘流
        return JSONResponse(status_code=503, content={"ok": False})
    return {"ok": True}

client = TestClient(app)
print("healthz:", client.get("/healthz").status_code)
print("readyz(依赖正常):", client.get("/readyz").status_code)
db_ok = False
print("readyz(依赖故障):", client.get("/readyz").status_code)
