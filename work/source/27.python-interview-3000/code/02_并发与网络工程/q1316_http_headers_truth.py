import http.client
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class App(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"        # 打开 keep-alive

    def do_GET(self):
        if self.path == "/overload":
            self.send_response(503)
            self.send_header("Retry-After", "1")
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(b"busy")
        else:
            self.send_response(200)
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"ok")

    def log_message(self, *args):
        pass


def raw_request(port: int, path: str) -> str:
    """最原始的 HTTP 请求: 排障先看原文。"""
    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    s.sendall(f"GET {path} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n".encode())
    chunks = []
    while True:
        data = s.recv(4096)
        if not data:
            break
        chunks.append(data)
    s.close()
    return b"".join(chunks).decode(errors="replace")


def main() -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), App)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    raw = raw_request(port, "/overload")
    print("--- 原始响应报文 ---")
    print(raw.split("\r\n\r\n")[0])

    # keep-alive 复用: 同一个 TCP 连接连发两次
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
    sock_ids = []
    for _ in range(2):
        conn.request("GET", "/")
        resp = conn.getresponse()
        resp.read()
        sock_ids.append(id(conn.sock))
    assert sock_ids[0] == sock_ids[1], "keep-alive 下两次请求应复用同一连接"
    print(f"keep-alive 复用同一连接: socket id 一致 {sock_ids[0] == sock_ids[1]}")
    conn.close()

    # Retry-After 的读取
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("GET", "/overload")
    resp = conn.getresponse()
    retry_after = resp.getheader("Retry-After")
    print(f"过载响应: {resp.status}, Retry-After={retry_after} -> 客户端应等 {retry_after}s 再试")
    assert resp.status == 503 and retry_after == "1"
    resp.read()
    conn.close()
    srv.shutdown()


if __name__ == "__main__":
    main()
