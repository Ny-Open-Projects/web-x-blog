---
title: [Q2434] WSGI 中间件的函数式组合
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2434 · WSGI 中间件的函数式组合

> 难度:★★★☆ | 标签:WSGI, 中间件, 函数式

**问**:不依赖任何框架,怎么用纯函数把 WSGI 中间件组合成一个应用?组合顺序对应什么执行模型?

**答**:WSGI 应用的本质是 callable(environ, start_response) 返回可迭代体,中间件就是"吃一个应用、吐一个应用"的高阶函数,组合只是 reduce:wrap(app, m1, m2) 等价 m1(m2(app)),m1 最先看到请求、最后看到响应,这就是洋葱模型。每个中间件在调用内层前后插自己的逻辑:前置逻辑改 environ 或提前短路返回,后置逻辑包装 start_response 往响应头里补东西,比如注入 X-Request-Id 或 Server-Timing。测试时不需要起服务器,手工构造 environ 字典、用一个收集函数扮演 start_response,就能直接断言状态码与头。这套函数式组合正是 Flask before/after 与 FastAPI 中间件栈的底层形态。

```python
# file: code/03_Web后端开发/q2434_wsgi_compose.py
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
```

**追问**:
- 中间件想改响应体怎么办?——它返回的就是内层应用的可迭代体,包一层生成器逐段改写即可,但要小心 Content-Length 需要重算。
- 短路发生在哪一层?——任何一层都可以不调用内层直接 start_response 返回,这就是认证层拒绝请求的实现位置。
