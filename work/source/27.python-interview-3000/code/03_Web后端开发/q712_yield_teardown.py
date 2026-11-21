try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

log = []
app = FastAPI()

def dep_outer():
    log.append("outer: enter")
    try:
        yield "outer"
    finally:
        log.append("outer: exit")

def dep_inner():
    log.append("inner: enter")
    try:
        yield "inner"
        log.append("inner: after-yield-正常")
    except Exception:
        log.append("inner: 捕获到 handler 异常")
        raise
    finally:
        log.append("inner: finally")

@app.get("/ok")
def ok(a: str = Depends(dep_outer), b: str = Depends(dep_inner)):
    return {"a": a, "b": b}

@app.get("/boom")
def boom(a: str = Depends(dep_outer), b: str = Depends(dep_inner)):
    raise RuntimeError("业务异常")

client = TestClient(app, raise_server_exceptions=False)
print(client.get("/ok").json())
print(client.get("/boom").status_code)
print("\n".join(log))
