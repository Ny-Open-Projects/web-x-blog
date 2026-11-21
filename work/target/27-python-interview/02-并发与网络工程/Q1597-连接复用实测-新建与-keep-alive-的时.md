---
title: [Q1597] 连接复用实测:新建与 keep-alive 的时延账
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1597 · 连接复用实测:新建与 keep-alive 的时延账

> 难度:★★☆☆ | 标签:HTTP, keep-alive, 连接池

**问**:为什么高频小请求必须用连接池?复用省一次握手,到底省多少?

**答**:每次新建连接要付完整建连税:TCP 三次握手(1 个 RTT)、TLS 握手(1 到 2 个 RTT,TLS 1.3 省一个)、慢启动冷启动(初始窗口很小,头几个请求跑不满带宽)。keep-alive 复用把这笔税摊到整个会话:后续请求只剩一问一答的 1 个 RTT。本机回环上握手只要亚毫秒,账不明显;公网 RTT 50 到 200ms,10 QPS 的客户端每秒白烧 0.5 到 2 秒的握手时间。连接池的本质就是把复用管理成资源:借还、健康检查、坏连接处置、上限控制(Q1332)。

```python
# file: code/02_并发与网络工程/q1597_reuse_bench.py
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
```

**追问**:1) 服务端怎么配合?——HTTP/1.1 默认 keep-alive,但要配 Keep-Alive 超时与最大请求数;主动断开前发 Connection: close,让客户端优雅换连。2) 握手税的三个组成部分怎么拆账?——TCP 握手 1 RTT、TLS 握手 1-2 RTT(1.3 为 1)、慢启动冷启动(初始 cwnd 小,头几轮跑不满带宽,Q1602);复用后只剩 1 RTT/请求——高频小请求场景握手税占比可达 90%+。3) 连接池的容量与 keepalive 参数怎么配套?——池上限按目标并发算(不是越大越好,对端有连接上限);池内连接要配服务端 keep-alive 超时感知(服务端关了客户端要能发现,ConnectionResetError 重试幂等请求,Q627);空闲健康检查(Q1332)防「拿到死连接」。4) 生产陷阱?——每请求新建 Session/客户端对象(复用全失效);池上限过高打爆服务端 backlog;keep-alive 超时两端不一致,客户端用着被服务端掐的连接;TLS session 复用没配(每次全握手,Q630)。

---
