"""WSGI 应用的函数式组合: 中间件即高阶函数(纯标准库)。"""
import itertools

_counter = itertools.count(1)


def wrap(app, *middlewares):
    """把中间件按从外到内的顺序包裹应用: wrap(app, a, b) 等价 a(b(app))。"""
    for mw in reversed(middlewares):
        app = mw(app)
    return app


def request_id_middleware(app):
    """最外层: 给每个请求注入 x-request-id 并写进响应头。"""
    def handler(environ, start_response):
        rid = "req-{}".format(next(_counter))
        environ["x-request-id"] = rid

        def sr(status, headers):
            start_response(status, headers + [("X-Request-Id", rid)])
        return app(environ, sr)
    return handler


def timing_middleware(app):
    """内层: 记录处理耗时, 演示用固定刻度代替真实时钟。"""
    def handler(environ, start_response):
        ticks = [3]

        def sr(status, headers):
            start_response(status, headers + [("X-Server-Timing", "app;dur={}".format(ticks[0]))])
        body = app(environ, sr)
        return body
    return handler


def router_app(environ, start_response):
    """最小应用: 根据路径返回文本。"""
    path = environ.get("PATH_INFO", "/")
    if path == "/hello":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return ["hello, {}".format(environ.get("x-request-id", "anon")).encode()]
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"not found"]


def call_wsgi(app, path):
    """不启服务器, 直接构造 environ 调用应用并收集响应。"""
    captured = {}
    environ = {"PATH_INFO": path, "REQUEST_METHOD": "GET"}

    def start_response(status, headers):
        captured["status"], captured["headers"] = status, headers
    body = b"".join(app(environ, start_response))
    return captured["status"], captured["headers"], body


app = wrap(router_app, request_id_middleware, timing_middleware)
status, headers, body = call_wsgi(app, "/hello")
print("GET /hello -> {} body={}".format(status, body.decode()))
for k, v in headers:
    print("  响应头: {}: {}".format(k, v))
assert status == "200 OK"
assert body == b"hello, req-1"
names = [k.lower() for k, _ in headers]
assert "x-request-id" in names and "x-server-timing" in names

status404, _, body404 = call_wsgi(app, "/nope")
print("GET /nope  -> {} body={}".format(status404, body404.decode()))
assert status404 == "404 Not Found"
print("要点: WSGI 应用就是 callable(environ, start_response) -> iterable, "
      "中间件是吃应用吐应用的高阶函数, 组合顺序即洋葱层次")
