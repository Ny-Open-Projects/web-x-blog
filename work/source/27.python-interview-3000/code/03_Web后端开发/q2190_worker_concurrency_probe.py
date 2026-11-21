"""worker 并发上限探针: 慢端点加服务端在制计数, 实测有效并发(纯标准库)。"""
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))   # 回环直连绕过代理
CAP = 3
in_flight = [0]
max_seen = [0]
lock = threading.Lock()
sem = threading.BoundedSemaphore(CAP)               # 模拟 worker 池的容量上限


class CappedHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with sem:                                   # 拿到 worker 名额才真正处理
            with lock:
                in_flight[0] += 1
                max_seen[0] = max(max_seen[0], in_flight[0])
            time.sleep(0.3)
            with lock:
                in_flight[0] -= 1
        body = b"ok"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class Server(ThreadingHTTPServer):
    request_queue_size = 32


server = Server(("127.0.0.1", 18703), CappedHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def probe(n):
    barrier = threading.Barrier(n)

    def worker():
        barrier.wait()
        opener.open("http://127.0.0.1:18703/", timeout=15).read()

    start = time.time()
    threads = [threading.Thread(target=worker) for _ in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - start


elapsed = probe(8)
print("8 并发打 3 容量的服务: 总耗时 {:.2f}s, 预期约 ceil(8/3)x0.3=0.9s".format(elapsed))
print("观测到的最大同时处理数: {} (配置容量 {})".format(max_seen[0], CAP))
assert max_seen[0] == CAP
print("要点: 钉住请求时长, 服务端数在制峰值即为有效并发; 实测低于配置说明有隐藏瓶颈")
server.shutdown()
