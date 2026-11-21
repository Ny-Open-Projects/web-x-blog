"""并发模型实测: 单线程与线程池 HTTP 服务在慢 IO 下的差距(纯标准库)。"""
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))   # 回环直连绕过代理


class SlowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.2)                             # 模拟下游 IO 等待
        body = b"ok"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class SingleServer(HTTPServer):
    request_queue_size = 32


class PoolServer(ThreadingHTTPServer):
    request_queue_size = 32


def bench(server_cls, port, n_clients=8):
    server = server_cls(("127.0.0.1", port), SlowHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    barrier = threading.Barrier(n_clients)

    def worker():
        barrier.wait()
        opener.open("http://127.0.0.1:{}/".format(port), timeout=15).read()

    start = time.time()
    threads = [threading.Thread(target=worker) for _ in range(n_clients)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.time() - start
    server.shutdown()
    return elapsed


single = bench(SingleServer, 18701)
pooled = bench(PoolServer, 18702)
print("单线程 HTTPServer          8 并发: {:.2f}s  下限 8x0.2=1.6s 串行".format(single))
print("线程池 ThreadingHTTPServer 8 并发: {:.2f}s  等待重叠约 0.2s 量级".format(pooled))
assert pooled < single
print("要点: 同步 worker 的吞吐上限 = worker 数 / 单请求时长; 容量估算先测这两个数, 不拍脑袋")
