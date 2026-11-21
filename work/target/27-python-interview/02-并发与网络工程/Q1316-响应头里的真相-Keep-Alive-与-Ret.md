---
title: [Q1316] 响应头里的真相:Keep-Alive 与 Retry-After 排障
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1316 · 响应头里的真相:Keep-Alive 与 Retry-After 排障

> 难度:★★☆☆ | 标签:HTTP, 响应头, 排障

**问**:接口偶发变慢,你会先看响应头里的哪几个字段?为什么?

**答**:响应头是服务端自述的"体检单"。Connection: keep-alive/Close 决定你要不要为每次请求重新握手——大量短连接的慢,一半是握手造成的;Date 与客户端时钟差暴露 NTP 漂移;Retry-After 是过载时服务端给你的合法等待时长,无视它硬重试等于顶风作案;Server/X-Powered-By 只能当弱指纹,别拿来做安全判断;Content-Length 与实际字节数不符,说明链路上有代理在截断。排障第一步永远是"看原始报文":用 socket 发一个最小请求,把响应头原文打出来,再决定用 http.client 还是浏览器视角复测。下面的演示在回环上检查 keep-alive 复用与 Retry-After 的读取。

```python
# file: code/02_并发与网络工程/q1316_http_headers_truth.py
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
```

**追问**:1) 为什么 Server 头不能作为安全判断依据?——它可被任意伪造或被代理改写,只能当弱指纹;真正的指纹要看 TLS 证书、行为特征与时序。2) Retry-After 缺失时怎么办?——按服务端惯例退避(指数+抖动,Q1335),或直接放弃该次重试;硬顶重试等于把过载变成雪崩;客户端实现要把「有/无 Retry-After」两条路径都写明。3) keep-alive 与性能的关系怎么量化?——对比 Connection 头与请求耗时分布:短连接的耗时里握手(TLS 更甚)占大头;复用连接后 P50 显著下降;中间代理可能强制 Connection: close(排查「明明配了 keep-alive 还抖」先看响应头)。4) 生产陷阱?——忽略 Retry-After(服务端给的合法等待被浪费);把 Server 头当安全指纹;Date 头与本地时钟的差值没人看(NTP 漂移漏检);Content-Length 与实际不符当偶发丢包(其实是代理截断,要查链路)。

---
