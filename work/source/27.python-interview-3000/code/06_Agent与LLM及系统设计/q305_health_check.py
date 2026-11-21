from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HealthState:
    """模拟依赖健康状态,生产中来自连接池 ping。"""
    def __init__(self):
        self.db_ok = True
        self.cache_ok = True

    def liveness(self) -> tuple[int, dict]:
        return 200, {"status": "alive"}  # 不碰外部依赖

    def readiness(self) -> tuple[int, dict]:
        deps = {"db": self.db_ok, "cache": self.cache_ok}
        ok = all(deps.values())
        return (200 if ok else 503), {"status": "ready" if ok else "not ready",
                                      "checks": deps}


state = HealthState()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            code, body = state.liveness()
        elif self.path == "/readyz":
            code, body = state.readiness()
        else:
            code, body = 404, {"error": "not found"}
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def log_message(self, *a):  # 静音默认日志
        pass


if __name__ == "__main__":
    import threading
    import time
    from urllib.request import build_opener, ProxyHandler

    server = HTTPServer(("127.0.0.1", 0), Handler)  # 随机空闲端口
    port = server.server_address[1]
    th = threading.Thread(target=server.serve_forever, daemon=True)
    th.start()

    opener = build_opener(ProxyHandler({}))  # 本机回环直连,不走环境代理
    def probe(path: str) -> tuple[int, dict]:
        from urllib.error import HTTPError, URLError
        for _ in range(50):  # 端口就绪等待
            try:
                with opener.open(f"http://127.0.0.1:{port}{path}", timeout=2) as r:
                    return r.status, json.loads(r.read())
            except HTTPError as e:  # 503 也是合法探针结果,直接读 body
                return e.code, json.loads(e.read())
            except URLError:
                time.sleep(0.05)  # 连接不上=服务未就绪,重试
        raise RuntimeError("server not ready")

    print("liveness:", probe("/healthz"))
    print("readiness(依赖正常):", probe("/readyz"))
    state.db_ok = False  # 模拟依赖故障
    print("readiness(db 挂了):", probe("/readyz"))
    server.shutdown()
    print("结论:存活探针不碰依赖,依赖故障只影响 readiness(503)")
