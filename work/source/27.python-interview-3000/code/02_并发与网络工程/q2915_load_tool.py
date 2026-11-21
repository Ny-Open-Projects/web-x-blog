# -*- coding: utf-8 -*-
"""压测小工具: 并发压测 + 分位数统计。

- workers 个线程各发 n_req 个请求, 记录每次时延与错误;
- 汇总口径: QPS、p50/p90/p99/max、错误数, 全部来自同一次运行;
- 对照并发 1 与并发 6: 服务端每请求固定思考时间, 吞吐差异立现。
"""
import json
import random
import socket
import statistics
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))
random.seed(42)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.03)                        # 服务端思考时间 30ms
        body = json.dumps({"ok": True}).encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def run_load(url, workers, n_req, timeout=3.0):
    """返回 (成功数, 失败数, 时延列表, 墙钟秒)。"""
    lat = []
    errs = [0]
    lock = threading.Lock()

    def hit():
        for _ in range(n_req):
            t1 = time.perf_counter()
            try:
                with OPENER.open(url, timeout=timeout) as resp:
                    resp.read()
            except (urllib.error.URLError, OSError):
                with lock:
                    errs[0] += 1
            dt = time.perf_counter() - t1
            with lock:
                lat.append(dt)

    ts = [threading.Thread(target=hit) for _ in range(workers)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    wall = time.perf_counter() - t0
    return len(lat) - errs[0], errs[0], lat, wall


def pct(sorted_lat, p):
    """分位数: 最近秩取法, 样本少时也稳定。"""
    n = len(sorted_lat)
    return sorted_lat[min(n - 1, int(round(p * (n - 1))))]


def report(tag, workers, n_req, url):
    ok, bad, lat, wall = run_load(url, workers, n_req)
    lat.sort()
    print("%s 并发=%d: QPS=%.0f ok=%d err=%d | p50=%.1fms p90=%.1fms "
          "p99=%.1fms max=%.1fms"
          % (tag, workers, ok / wall, ok, bad,
             pct(lat, 0.50) * 1000, pct(lat, 0.90) * 1000,
             pct(lat, 0.99) * 1000, lat[-1] * 1000))
    return ok / wall, pct(lat, 0.99) * 1000


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    srv.daemon_threads = True
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    assert wait_port(port)
    url = "http://127.0.0.1:%d/work" % port

    run_load(url, 2, 3)                         # 预热: 连接与解释器热身
    qps1, p99_1 = report("A", 1, 30, url)
    qps6, p99_6 = report("B", 6, 30, url)

    assert qps6 > qps1 * 2, "并发 6 应显著快于并发 1"
    # 断言采用确定性设计: 思考时间取 30ms 主导连接与调度开销, p99 上界按思考时间倍数
    # (10 倍/20 倍)设定, 不与机器绝对速度比较; report 返回的 p99 单位是 ms
    assert p99_1 < 300 and p99_6 < 600
    srv.shutdown()
    print("要点: 压测三件套 = 并发施压 + 分位数统计 + 错误计数,"
          " 并发抬吞吐也抬排队延迟, 两面都要看")
