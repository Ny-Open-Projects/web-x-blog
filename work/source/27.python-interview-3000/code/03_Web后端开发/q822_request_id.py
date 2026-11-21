import logging
import uuid
from contextvars import ContextVar

request_id_var: ContextVar = ContextVar("request_id", default="-")

class ReqIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()
        return True

try:
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

log = logging.getLogger("app")
log.addFilter(ReqIdFilter())
log.addHandler(logging.StreamHandler())

app = FastAPI()

@app.middleware("http")
async def rid(request: Request, call_next):
    rid_value = request.headers.get("x-request-id") or uuid.uuid4().hex
    token = request_id_var.set(rid_value)
    resp = await call_next(request)
    request_id_var.reset(token)
    resp.headers["x-request-id"] = rid_value
    return resp

@app.get("/work")
def work():
    log.info("处理业务")
    return {"ok": True}

client = TestClient(app)
r = client.get("/work", headers={"x-request-id": "req-abc"})
print("透传的 id:", r.headers["x-request-id"])
r2 = client.get("/work")
print("自动生成 32 位:", len(r2.headers["x-request-id"]) == 32)
