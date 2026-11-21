---
title: [Q2190] worker 并发上限的实测探针
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2190 · worker 并发上限的实测探针

> 难度:★★★☆ | 标签:部署, 性能

**问**:上线前怎么实测一个实例"同时能处理几个请求"?探针怎么设计?

**答**:探针的思路是"钉住处理时长,数同时处理的个数":准备一个 handler 固定 sleep 的慢端点,用超过预期并发的客户端(如 8 个)同时打,服务端自己统计在处理中的请求数峰值(max in-flight)。这个峰值就是实例的有效并发上限——如果测出来 3 而配置的 worker×线程是 20,说明连接池、锁或下游限流里有额外的瓶颈,配置是纸面数字。探针要点:请求时长要足够长(几百毫秒)让并发充分重叠;客户端用 Barrier 对齐起点;统计在服务端做(客户端只知道总耗时);对照配置值输出偏差,偏差就是排障线索。这个探针应进发布前的例行检查,部署拓扑或参数变更后重测。

```python
# file: code/03_Web后端开发/q2190_worker_concurrency_probe.py
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
```

**追问**:
- 探针会不会影响线上?——在预发或灰度实例上跑,打流时间控制在秒级,并从负载均衡摘除探针实例。
- 测出并发是 20 但压测吞吐上不去,为什么?——并发上限只是能力,吞吐还受下游 RT 与错误率约束,两个指标要分开看。
