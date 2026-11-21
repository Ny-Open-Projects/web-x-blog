"""中间件链的可组合实现: 函数式洋葱模型、执行顺序与短路(纯标准库)。"""
import time


def build_chain(middlewares, handler):
    """把中间件从左到右叠成洋葱: 最左在最外层。每个中间件形如 fn(ctx, next)。"""
    def dispatch(ctx, i):
        if i == len(middlewares):
            return handler(ctx)

        def nxt():
            return dispatch(ctx, i + 1)

        return middlewares[i](ctx, nxt)

    def entry(ctx):
        return dispatch(ctx, 0)

    return entry


def auth_mw(ctx, nxt):
    """短路型中间件: 未登录直接返回 401, 内层完全不会执行。"""
    if ctx["headers"].get("authorization") != "Bearer ok":
        ctx["trace"].append("auth:401")
        return {"status": 401, "body": "unauthorized"}
    ctx["trace"].append("auth:pass")
    return nxt()


def logging_mw(ctx, nxt):
    ctx["trace"].append("log:enter")
    resp = nxt()
    ctx["trace"].append("log:leave status=%s" % resp["status"])
    return resp


def timing_mw(ctx, nxt):
    start = time.monotonic()
    resp = nxt()
    resp = dict(resp, duration_ms=int((time.monotonic() - start) * 1000))
    ctx["trace"].append("timing:done")
    return resp


def handler(ctx):
    ctx["trace"].append("handler")
    return {"status": 200, "body": "fine"}


app = build_chain([auth_mw, logging_mw, timing_mw], handler)

ctx_ok = {"headers": {"authorization": "Bearer ok"}, "trace": []}
resp = app(ctx_ok)
print("放行路径 trace:", ctx_ok["trace"])
assert resp["status"] == 200 and "duration_ms" in resp
assert ctx_ok["trace"] == ["auth:pass", "log:enter", "handler", "timing:done", "log:leave status=200"], "洋葱回程: 内层收尾先于外层"

ctx_bad = {"headers": {}, "trace": []}
resp = app(ctx_bad)
print("短路路径 trace:", ctx_bad["trace"])
assert resp["status"] == 401
assert ctx_bad["trace"] == ["auth:401"], "短路时日志与计时层都不应执行"

# 顺序即语义: 日志放最外层后, 401 也会留下 enter/leave 两条记录
app2 = build_chain([logging_mw, auth_mw, timing_mw], handler)
ctx3 = {"headers": {}, "trace": []}
resp2 = app2(ctx3)
print("日志外置时 trace:", ctx3["trace"])
assert ctx3["trace"] == ["log:enter", "auth:401", "log:leave status=401"]

# 组合可复用: 同一批中间件换 handler 即换业务
def other_handler(ctx):
    ctx["trace"].append("other")
    return {"status": 201, "body": "created"}

app3 = build_chain([auth_mw, logging_mw], other_handler)
ctx4 = {"headers": {"authorization": "Bearer ok"}, "trace": []}
assert app3(ctx4)["status"] == 201
print("换 handler 复用同一链:", ctx4["trace"])
print("中间件链演示通过")
