import json
import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 本机回环演示: 显式直连, 避免环境里的 http_proxy 把 urlopen 劫持到代理端口
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))

START = time.monotonic()
state = {"db_ok": True, "draining": False}


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


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _respond(self, code: int, obj: dict) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/livez":
            # liveness: 只回答进程自身活着, 绝不碰外部依赖
            self._respond(200, {"status": "alive",
                                "uptime": round(time.monotonic() - START, 1)})
        elif self.path == "/readyz":
            if state["draining"]:
                self._respond(503, {"status": "draining", "ready": False})
            elif not state["db_ok"]:
                self._respond(503, {"status": "dependency-down", "ready": False})
            else:
                self._respond(200, {"status": "ready", "checks": {"db": "ok"}})
        else:
            self._respond(404, {"error": "not found"})

    def log_message(self, fmt: str, *args) -> None:
        pass


def server(stop: threading.Event, port_box: list) -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port_box.append(srv.server_address[1])
    srv.timeout = 0.2
    while not stop.is_set():
        srv.handle_request()
    srv.server_close()


def probe(base: str, path: str) -> None:
    try:
        r = urllib.request.urlopen(base + path, timeout=2)
        print(f"  {path}: {r.status} {r.read().decode()}")
    except urllib.error.HTTPError as e:
        print(f"  {path}: {e.code} {e.read().decode()}")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    wait_port(box[0])
    base = f"http://127.0.0.1:{box[0]}"

    print("正常状态:")
    probe(base, "/livez")
    probe(base, "/readyz")

    print("依赖故障 (db_ok=False) → liveness 仍 200, readiness 503:")
    state["db_ok"] = False
    probe(base, "/livez")
    probe(base, "/readyz")

    print("优雅排水 (draining=True) → readiness 503 摘流, 进程不重启:")
    state["db_ok"] = True
    state["draining"] = True
    probe(base, "/livez")
    probe(base, "/readyz")
    stop.set()
