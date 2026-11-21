---
title: [Q822] 请求 ID 与 contextvars 链路注入
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q822 · 请求 ID 与 contextvars 链路注入

> 难度:★★★★ | 标签:请求 ID, contextvars

**问**:怎么让一次请求里所有日志自动带上同一个 request_id?为什么用 contextvars 而不是全局变量?

**答**:中间件入口生成/透传 request_id(优先取上游头,如网关注入),**set 进 contextvar**,日志 Filter 从 contextvar 读取,业务代码零感知;响应头回传 request_id 便于用户报障。必须用 contextvars 因为它是**协程/线程安全的请求级存储**:全局变量会串请求,threading.local 在 asyncio 下同一线程跑多个协程也会串。透传规则:入口信任内网来源的 request_id,对外部请求重新生成,防止日志注入伪造。

```mermaid
flowchart LR
    A[网关生成 request id] --> B[中间件写入 contextvar]
    B --> C[业务代码与日志自动携带]
    C --> D[调用下游时透传同一 id]
    D --> E[日志系统按 id 聚合全链路]
```

```python
# file: code/03_Web后端开发/q822_request_id.py
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
```

**追问**:
- contextvar 要在 finally 里 reset 吗?——中间件场景请求结束上下文销毁可不 reset,长生命周期协程(后台任务)必须 reset 防泄漏。
- 后台任务里 request_id 丢了怎么办?——在注册任务时把 request_id 作为参数传过去,任务内重新 set。
