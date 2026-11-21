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
