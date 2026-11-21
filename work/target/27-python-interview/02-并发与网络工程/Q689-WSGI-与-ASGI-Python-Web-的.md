---
title: [Q689] WSGI 与 ASGI:Python Web 的两代接口
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q689 · WSGI 与 ASGI:Python Web 的两代接口

> 难度:★★★☆ | 标签:WSGI, ASGI, 网关接口

**问**:WSGI 和 ASGI 的本质区别是什么?为什么会有 ASGI?

**答**:WSGI(PEP 3333)是同步 callable 协议:`app(environ, start_response)`,一次调用阻塞直到响应完成——模型简单、生态成熟(Flask/Django),但一个请求占死一个线程,长连接/WebSocket/服务端推送无法表达(没有"请求结束后还能发数据"的通道)。ASGI 是其异步版:`async app(scope, receive, send)`,scope 携带连接生命周期(HTTP 只有一来一回,WebSocket 的 scope 存活于整个连接),receive/send 双通道支持双向消息。迁移逻辑:gunicorn+WSGI 处理传统页面,uvicorn/daphne+ASGI 处理实时;FastAPI/Starlette 全家桶即 ASGI 生态。

```python
# file: code/02_并发与网络工程/q689_wsgi.py
from wsgiref.simple_server import make_server, WSGIRequestHandler


def app(environ: dict, start_response) -> list:
    """WSGI 应用: (environ, start_response) → 可迭代字节。"""
    path = environ.get("PATH_INFO", "/")
    if path == "/":
        body = b"hello-wsgi"
        start_response("200 OK", [("Content-Type", "text/plain"),
                                  ("Content-Length", str(len(body)))])
        return [body]
    if path == "/headers":
        # environ 里就是 CGI 风格的请求元数据
        info = {k: str(v) for k, v in environ.items()
                if k.startswith("HTTP_") or k in ("REQUEST_METHOD", "PATH_INFO")}
        import json
        body = json.dumps(info).encode()
        start_response("200 OK", [("Content-Type", "application/json"),
                                  ("Content-Length", str(len(body)))])
        return [body]
    body = b"not found"
    start_response("404 Not Found", [("Content-Type", "text/plain"),
                                     ("Content-Length", str(len(body)))])
    return [body]


class QuietHandler(WSGIRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        print("[wsgi]", fmt % args)


if __name__ == "__main__":
    import socket
    import threading
    import time
    import urllib.request

    # 本机回环演示: 显式直连, 避免环境里的 http_proxy 把 urlopen 劫持到代理端口
    urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))

    def wait_port(port: int, timeout: float = 3.0) -> None:
        """等服务端端口可建立 TCP 连接再发请求, 消除服务启动竞态。"""
        deadline = time.monotonic() + timeout
        while True:
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                    return
            except OSError:
                if time.monotonic() >= deadline:
                    raise
                time.sleep(0.05)

    srv = make_server("127.0.0.1", 0, app, handler_class=QuietHandler)
    port = srv.server_address[1]

    def serve() -> None:
        srv.serve_forever(poll_interval=0.2)

    t = threading.Thread(target=serve, daemon=True)
    t.start()
    wait_port(port)

    print("GET /:     ", urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=2).read())
    print("GET /headers:", urllib.request.urlopen(f"http://127.0.0.1:{port}/headers",
                                                 timeout=2).read()[:80], b"...")
    srv.shutdown()
    print("WSGI 模型: 一次 callable 调用 = 一个完整响应, 无双向通道 → 这就是 ASGI 要解决的")
```

**追问**:1) ASGI 的 scope 为什么比 environ 多一层抽象?——environ 描述"一次请求";scope 描述"一个连接"的生命周期,HTTP 请求只是 scope 的一种消息序列,WebSocket/长轮询由此获得统一表达。2) WSGI 为什么表达不了 WebSocket?——一次 callable 调用返回即请求结束,没有「响应完成后继续发数据」的通道;WS 需要长生命周期双向消息,ASGI 的 scope+receive/send 才表达得了——接口能力由调用约定决定。3) 从 WSGI 迁 ASGI 的路径?——实时功能用 ASGI 子应用(FastAPI/Starlette)挂载、主体保留 WSGI 是低风险路径;全量迁移的收益是高并发 IO 与原生 WS/SSE,成本是同步 ORM/中间件生态重写。4) 生产陷阱?——WSGI worker 按「一请求一线程」配置,长连接把线程池耗尽;ASGI 应用里混入同步阻塞调用卡死事件循环(Q654 同源);WSGI 中间件假设套在 ASGI 外层,语义错位。

---
