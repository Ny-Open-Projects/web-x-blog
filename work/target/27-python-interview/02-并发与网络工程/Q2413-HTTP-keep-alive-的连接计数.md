---
title: [Q2413] HTTP keep-alive 的连接计数
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2413 · HTTP keep-alive 的连接计数

> 难度:★★★ | 标签:HTTP keep-alive, 连接复用, http.client

**问**:怎么用服务端视角证明客户端确实在复用连接?

**答**:在服务端 accept 处计数:HTTP/1.1 默认 keep-alive,同一条连接上连续发请求,连接计数只涨一次;短连接每个请求都新建,计数逐次上涨。

- 实测:一条 HTTPConnection 连发三个 GET,服务端连接数 1、请求数 3,响应逐条递增,复用实锤;

- 实测短连接两次:连接数涨到 3、请求数 5,计数差就是连接建立的开销;

- 复用的前提:响应带 Content-Length(或 chunked),服务端不主动发 Connection: close,否则连接用一次就断;

- 连接数是容量指标:每连接一线程的服务模型下,连接数直接对应线程数与内存。

```python
# file: code/02_并发与网络工程/q2413_keepalive_conn_count.py
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
```

**追问**:1) keep-alive 什么时候该主动关?——服务端设 Keep-Alive 超时与最大请求数,防止僵尸连接长期占坑。2) 管线化 pipelining 为什么没人用?——响应必须按序返回,队头阻塞无解,HTTP/2 的多路复用才是正解。3) 复用成立的三前提与失效路径?——响应带 Content-Length(或 chunked)、服务端不发 Connection: close、客户端连接池持有——任一破坏=退化为短连接;「连接数是容量指标」:每连接一线程模型下连接数=线程数=内存账(Q654)。4) Keep-Alive 的服务端治理参数?——超时(空闲连接回收)+最大请求数(单连接上限,防单连接独占);主动关时先发 Connection: close 让客户端优雅换连(Q1597)——「服务端主动限」与「客户端复用」是配合关系。5) 生产陷阱?——响应缺 Content-Length(复用失效,客户端挂等,Q627);僵尸连接占坑(无超时回收);连接数指标缺失(容量问题隐形);管线化误用(队头阻塞,见原问);keep-alive 超时两端不一致(客户端用着被掐的连接)。

---
