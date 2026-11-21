import json
import socket
import threading
import time
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import urllib.request

# 本机回环演示: 显式直连, 避免环境里的 http_proxy 把 urlopen 劫持到代理端口
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))

START = time.monotonic()


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
    protocol_version = "HTTP/1.1"  # 显式开启 keep-alive

    def _json(self, code: int, obj: dict) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/hello":
            self._json(200, {"msg": "hello", "uptime": round(time.monotonic() - START, 2)})
        elif self.path == "/healthz":
            self._json(200, {"status": "ok"})
        else:
            self._json(404, {"error": "not found", "path": self.path})

    def do_POST(self) -> None:
        if self.path == "/echo":
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            self._json(200, {"you_sent": json.loads(data) if data else None})
        else:
            self._json(405, {"error": "method/path not allowed"})

    def log_message(self, fmt: str, *args) -> None:  # 自定义访问日志
        print(f"[http] {self.address_string()} {fmt % args}")


def server(stop: threading.Event, port_box: list) -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port_box.append(srv.server_address[1])
    srv.timeout = 0.2
    while not stop.is_set():
        srv.handle_request()  # 单步循环以便响应停止信号
    srv.server_close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    wait_port(box[0])
    base = f"http://127.0.0.1:{box[0]}"

    print("GET /hello:", urllib.request.urlopen(base + "/hello", timeout=2).read().decode())
    try:
        print("GET /none: ", urllib.request.urlopen(base + "/none", timeout=2).read().decode())
    except urllib.error.HTTPError as e:  # 4xx/5xx 也是响应: urllib 以 HTTPError 呈现, 错误体照样可读
        print("GET /none: ", e.code, e.read().decode())
    req = urllib.request.Request(base + "/echo", data=json.dumps({"x": 1}).encode(),
                                 headers={"Content-Type": "application/json"})
    print("POST /echo:", urllib.request.urlopen(req, timeout=2).read().decode())
    stop.set()
