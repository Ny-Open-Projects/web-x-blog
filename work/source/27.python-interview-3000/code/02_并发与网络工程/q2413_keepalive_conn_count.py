# -*- coding: utf-8 -*-
"""HTTP keep-alive 的连接计数: 用服务端视角证明连接确实被复用了。

- HTTP/1.1 默认 keep-alive, 复用与否要看服务端 accept 了几次;
- 三个请求一条连接, 服务端连接计数只涨 1, 短连接则每请求涨 1;
- 能复用的前提: 响应带 Content-Length, 服务端不主动 Connection: close。
"""
import http.client
import http.server
import socketserver
import threading
import time

COUNT = {"conn": 0, "req": 0}


class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"                # 关键: 1.1 才默认 keep-alive

    def do_GET(self):
        COUNT["req"] += 1
        body = ("req-%d" % COUNT["req"]).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):                # 静音访问日志
        pass


class CountingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

    def process_request(self, request, client_address):
        COUNT["conn"] += 1                       # accept 一次记一条
        super().process_request(request, client_address)


def main():
    srv = CountingServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.1)

    # 场景一: 一条连接上连续发三个请求
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
    seq = []
    for _ in range(3):
        c.request("GET", "/")
        resp = c.getresponse()
        seq.append(resp.read().decode())
    c.close()
    print("keep-alive 三连发: %s, 服务端连接数 %d" % (seq, COUNT["conn"]))
    assert COUNT["conn"] == 1 and COUNT["req"] == 3, "三条请求应复用同一条连接"

    # 场景二: 每个请求各建一条连接
    for _ in range(2):
        c2 = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
        c2.request("GET", "/")
        c2.getresponse().read()
        c2.close()
    print("短连接两次: 服务端连接数 %d, 请求数 %d" % (COUNT["conn"], COUNT["req"]))
    assert COUNT["conn"] == 3 and COUNT["req"] == 5, \
        "短连接每请求一条, 计数差就是连接建立开销"

    srv.shutdown()


if __name__ == "__main__":
    main()
