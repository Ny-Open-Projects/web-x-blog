import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 本机回环演示: 代理自身与客户端都显式直连, 避免环境 http_proxy 劫持 urlopen
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


HOP_BY_HOP = {"connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
              "te", "trailers", "transfer-encoding", "upgrade", "proxy-connection"}


class BackendHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:
        body = f"backend-response for {self.path}".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("X-Backend", "origin-1")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args) -> None:
        print("[backend]", fmt % args)


class ProxyHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    upstream: str = ""

    def do_GET(self) -> None:
        url = self.upstream + self.path
        req = urllib.request.Request(url)
        # 透传除逐跳头以外的头
        for key, value in self.headers.items():
            if key.lower() not in HOP_BY_HOP:
                req.add_header(key, value)
        req.add_header("X-Forwarded-For", self.client_address[0])
        try:
            with urllib.request.urlopen(req, timeout=2) as resp:
                body = resp.read()
                self.send_response(resp.status)
                for key, value in resp.headers.items():
                    if key.lower() not in HOP_BY_HOP and key.lower() != "server":
                        self.send_header(key, value)
        except urllib.error.URLError as e:
            body = b"upstream unavailable"
            self.send_response(502)
            print("[proxy] 上游失败:", e)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args) -> None:
        print("[proxy]", fmt % args)


def run(srv: ThreadingHTTPServer) -> None:
    srv.timeout = 0.2
    while srv_keeping[0]:
        srv.handle_request()


srv_keeping = [True]

if __name__ == "__main__":
    backend = ThreadingHTTPServer(("127.0.0.1", 0), BackendHandler)
    proxy = ThreadingHTTPServer(("127.0.0.1", 0), ProxyHandler)
    ProxyHandler.upstream = f"http://127.0.0.1:{backend.server_address[1]}"

    threading.Thread(target=run, args=(backend,), daemon=True).start()
    threading.Thread(target=run, args=(proxy,), daemon=True).start()
    wait_port(backend.server_address[1])
    wait_port(proxy.server_address[1])

    proxy_port = proxy.server_address[1]
    r = urllib.request.urlopen(f"http://127.0.0.1:{proxy_port}/api/data", timeout=2)
    print("客户端经代理收到:", r.read().decode())
    print("响应头 X-Backend:", r.headers.get("X-Backend"), "(上游标记被透传)")
    srv_keeping[0] = False
