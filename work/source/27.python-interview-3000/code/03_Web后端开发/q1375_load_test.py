"""最小压测:标准库起被压目标并多线程发压(纯标准库)。"""
import http.server
import json
import threading
import time
from http.client import HTTPConnection


class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"                # 保持长连接

    def do_GET(self):
        body = json.dumps({"ok": True}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()

RESULTS = []
lock = threading.Lock()
N_THREADS, N_REQ = 8, 25


def worker(n_req):
    conn = HTTPConnection("127.0.0.1", port, timeout=5)
    for _ in range(n_req):
        t0 = time.perf_counter()
        conn.request("GET", "/")
        resp = conn.getresponse()
        resp.read()
        with lock:
            RESULTS.append(time.perf_counter() - t0)
    conn.close()


threads = [threading.Thread(target=worker, args=(N_REQ,)) for _ in range(N_THREADS)]
start = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
elapsed = time.perf_counter() - start
server.shutdown()
server.server_close()

RESULTS.sort()
total = N_THREADS * N_REQ


def pct(p):
    idx = min(int(len(RESULTS) * p), len(RESULTS) - 1)
    return RESULTS[idx] * 1000


print(f"requests={total} elapsed={elapsed:.2f}s rps={total / elapsed:.0f}")
print(f"p50={pct(0.5):.2f}ms p95={pct(0.95):.2f}ms p99={pct(0.99):.2f}ms")
print("提示:生产压测应在独立环境阶梯加压,避免同机互抢 CPU")
