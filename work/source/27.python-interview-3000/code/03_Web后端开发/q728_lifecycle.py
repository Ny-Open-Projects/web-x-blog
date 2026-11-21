try:
    from fastapi import Depends, FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

events = []
app = FastAPI()

@app.middleware("http")
async def trace_mw(request: Request, call_next):
    events.append("mw: before")
    request.state.events = events
    resp = await call_next(request)
    events.append("mw: after")
    return resp

def dep(request: Request):
    request.state.events.append("dep")

@app.get("/ping")
def ping(request: Request, _=Depends(dep)):
    request.state.events.append("handler")
    return {"ok": True}

client = TestClient(app)
client.get("/ping")
print(events)
