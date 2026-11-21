"""连接复用实测: 新建连接与 keep-alive 复用的时延账。

每次请求新建连接都要付 TCP 三次握手 + 慢启动冷启动的税; 复用连接
把这笔税摊到整个会话里。回环上手握手便宜(亚毫秒), 公网上一次握手
就是 0.5-2 个 RTT, 高频小请求场景复用收益巨大。
本实验在本机 HTTP 服务上跑两组 5 连发, 对比总耗时。
"""
import http.client
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

N = 5


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"          # 1.1 默认 keep-alive

    def do_GET(self):
        body = b"ok"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def wait_port(port, timeout=3.0):
    import socket
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def fresh_run(port):
    """每个请求都新建连接, 用完即关。"""
    times = []
    for i in range(N):
        t0 = time.perf_counter()
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("GET", "/p%d" % i)
        resp = conn.getresponse()
        assert resp.status == 200
        resp.read()
        conn.close()
        times.append(time.perf_counter() - t0)
    return times


def reuse_run(port):
    """一条连接跑完所有请求, 只握一次手。"""
    times = []
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
    for i in range(N):
        t0 = time.perf_counter()
        conn.request("GET", "/p%d" % i)
        resp = conn.getresponse()
        assert resp.status == 200
        resp.read()
        times.append(time.perf_counter() - t0)
    conn.close()
    return times


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    wait_port(port)

    fresh = fresh_run(port)
    reuse = reuse_run(port)
    print("新建连接 5 次: 总 %.1fms  单次 %s"
          % (sum(fresh) * 1000, ["%.2f" % (t * 1000) for t in fresh]))
    print("复用连接 5 次: 总 %.1fms  单次 %s"
          % (sum(reuse) * 1000, ["%.2f" % (t * 1000) for t in reuse]))
    print("复用省下的握手次数: %d 次(公网上每次至少 1 个 RTT)"
          % (N - 1))
    assert len(fresh) == len(reuse) == N
    srv.shutdown()
    srv.server_close()
    print("结论: 复用省的是每次请求的握手与慢启动; 连接池就是把复用管理成资源")


if __name__ == "__main__":
    main()
