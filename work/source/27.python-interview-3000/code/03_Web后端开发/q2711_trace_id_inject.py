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
