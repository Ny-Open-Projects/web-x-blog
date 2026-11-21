"""中间件洋葱: 执行序、短路响应与异常边界(纯标准库, 附 fastapi 降级对照)。"""

try:
    from fastapi import FastAPI
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi, 以下用手写洋葱模拟同一执行语义")


class Onion:
    """中间件按注册顺序形成洋葱: 请求段正序执行, 响应段倒序执行。

    中间件返回非 None 即短路: 跳过更内层与其响应段, 只保留外层响应段。
    """

    def __init__(self, handler):
        self.handler = handler
        self.layers = []

    def add(self, name, on_request=None, on_response=None):
        self.layers.append((name, on_request, on_response))

    def run(self, request):
        trace = []
        for name, on_req, _ in self.layers:          # 请求段: 外层到内层
            out = on_req(request) if on_req else None
            trace.append(("req", name, out))
            if out is not None:                       # 短路: 不再进入内层
                short = out
                for rname, _, on_resp in reversed(self.layers[:len(trace)]):
                    short = on_resp(short, request) if on_resp else short
                    trace.append(("resp(short)", rname))
                return short, trace
        try:
            response = self.handler(request)
        except ValueError as e:                       # 内层异常由业务兜底层转 500
            response = {"status": 500, "error": str(e)}
            trace.append(("handler", "raised", str(e)))
        for name, _, on_resp in reversed(self.layers):  # 响应段: 内层到外层
            response = on_resp(response, request) if on_resp else response
            trace.append(("resp", name))
        return response, trace


def handler(request):
    if request.get("crash"):
        raise ValueError("boom")
    return {"status": 200, "user": request.get("user")}


app = Onion(handler)
app.add("logging",
        on_request=lambda r: print(r) or None,
        on_response=lambda resp, r: resp if resp["status"] != 500 else resp)
app.add("auth", on_request=lambda r: {"status": 401} if "user" not in r else None)
app.add("compress", on_response=lambda resp, r: dict(resp, gzipped=True))

ok, trace = app.run({"user": "alice"})
print("正常链 trace:", [(t[0], t[1]) for t in trace], "->", ok)
blocked, trace2 = app.run({})
print("短路链 trace:", [(t[0], t[1]) for t in trace2], "->", blocked)
bad, trace3 = app.run({"user": "bob", "crash": True})
print("异常链 ->", bad, "被最外层兜底, 内层异常不打穿响应链")
assert ok["status"] == 200 and ok.get("gzipped")
assert blocked["status"] == 401
assert bad["status"] == 500
if HAS_FASTAPI:
    print("fastapi 可用: add_middleware 注册序即请求序, 与手写洋葱一致")
print("要点: 短路只跳过更内层, 外层响应段仍要收尾; 异常在内层兜底转 500 才不打穿洋葱")
