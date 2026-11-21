---
title: [Q2711] 错误响应的 trace-id 兜底注入
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2711 · 错误响应的 trace-id 兜底注入

> 难度:★★★☆ | 标签:可观测性, 错误处理, contextvars

**问**:用户报障只发一张截图,怎么保证任何错误响应都能让他报出一个可查的编号?

**答**:trace-id 兜底注入中间件:入口生成或透传(上游网关注入的合法头优先),存进 contextvar,所有错误出口——业务异常、框架 4xx、未捕获 500——统一从 contextvar 取值写进错误体与 X-Trace-Id 响应头,连 500 都带号,这是用户报障的凭据。兜底链设计:透传头先过格式校验(长度、字符集白名单)才采信,防日志注入;没透传就现场生成 uuid4;异常处理器不能假设中间件已 set,要独立兜底。FastAPI 两层都要配:middleware 设值,exception_handler(Exception) 兜未捕获异常,测试时 TestClient 要 raise_server_exceptions=False 才能看到 500 响应体。错误体的 trace_id 与响应头的 X-Trace-Id 必须同值,否则工单对不上。

```python
# file: code/03_Web后端开发/q2711_trace_id_inject.py
"""错误响应的 trace-id 兜底注入: 连 500 都要能被用户报障(缺库降级)。"""
import sys
import uuid
from contextvars import ContextVar

trace_var = ContextVar("trace_id", default=None)

try:
    from fastapi import FastAPI, Request
    from fastapi.responses import JSONResponse
    from fastapi.testclient import TestClient
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("未安装 fastapi/httpx, 框架部分跳过, 标准库演示兜底链核心")


def resolve_trace(request_headers):
    """兜底链: 上游透传头 > contextvar 既有值 > 现场生成。

    透传头只信网关, 对外请求要重生成, 防止日志被伪造的 id 污染。
    """
    upstream = request_headers.get("x-trace-id")
    if upstream and 8 <= len(upstream) <= 64 and all(c.isalnum() or c == "-" for c in upstream):
        return upstream
    return trace_var.get() or uuid.uuid4().hex


def error_body(status, message, trace_id):
    """所有错误出口共用一个构造器, trace_id 同时进 body 和响应头。"""
    return {"error": {"code": "HTTP_%d" % status, "message": message, "trace_id": trace_id}}


if HAS_FASTAPI:
    app = FastAPI()

    @app.middleware("http")
    async def trace_middleware(request: Request, call_next):
        trace_var.set(resolve_trace(request.headers))
        response = await call_next(request)
        response.headers["X-Trace-Id"] = trace_var.get()
        return response

    @app.exception_handler(Exception)
    async def unhandled(request: Request, exc: Exception):
        """未捕获异常的兜底: 500 也必须带 trace_id, 这是用户报障的凭据。"""
        trace_id = resolve_trace(request.headers)
        return JSONResponse(status_code=500, content=error_body(500, "internal error", trace_id),
                            headers={"X-Trace-Id": trace_id})

    @app.get("/boom")
    async def boom():
        raise RuntimeError("oops")

    client = TestClient(app, raise_server_exceptions=False)
    r = client.get("/boom", headers={"X-Trace-Id": "gw-abc-123"})
    assert r.status_code == 500
    assert r.headers["X-Trace-Id"] == "gw-abc-123", r.headers
    assert r.json()["error"]["trace_id"] == "gw-abc-123"
    r2 = client.get("/boom")
    assert len(r2.json()["error"]["trace_id"]) == 32
    print("透传 trace 回显:", r.headers["X-Trace-Id"])
    print("无透传时现场生成:", r2.json()["error"]["trace_id"][:8], "...")
else:
    assert resolve_trace({"x-trace-id": "gw-abc-123"}) == "gw-abc-123"
    assert resolve_trace({}) is not None and len(resolve_trace({})) == 32
    assert resolve_trace({"x-trace-id": "bad id!!"}) != "bad id!!", "非法字符的透传头不采信"
    print("标准库兜底链: 合法透传 > 生成, 非法透传拒绝")
```

**追问**:
- trace-id 和 W3C traceparent 什么关系?——traceparent 是标准化 trace 上下文含采样位,trace-id 是简化版;内部系统可以直接以 traceparent 为源提取 trace-id。
- 500 的错误体里能放堆栈吗?——不能,堆栈只进日志;错误体放 trace_id 与人话描述,详情靠 trace_id 到日志系统查。
