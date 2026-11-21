---
title: [Q6043] 下游 HTTP client 复用成本账
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6043 · 下游 HTTP client 的复用成本账（每请求新建 vs 池化）

> 难度:★★★☆ | 标签:httpx, 连接池, 成本工程, TCP

**问**：review 时发现 handler 里每次请求都 `with httpx.Client() as client:`。这个写法的成本账怎么算（TCP/TLS 握手、TIME_WAIT、端口耗尽）？池化 client 的正确生命周期是什么？如何用实测数据说服团队改掉？

**答**：每请求新建 client 的三笔税：1) **连接建立**：本机内网 TCP 握手 1 RTT（~1ms），跨机房 3-10ms；若走 HTTPS 再加 TLS 握手 1-2 RTT（TLS 1.2）或 1 RTT（1.3，Q5544）——每请求白付一次；2) **端口与内核态**：每请求新建连接 = 每请求消耗一个本地端口，QPS 高时 TIME_WAIT 堆积（2MSL 60s × QPS 个端口），高并发下端口耗尽（connect 报 EADDRNOTAVAIL）；3) **对象开销**：Client 构建本身（SSLContext 创建尤其贵，一次几十 ms 量级）每请求重复。池化正确姿势：**client 与进程/事件循环同生命周期**——同步代码放模块级或 app 生命周期（Q6001 的 lifespan）里，异步代码用 `httpx.AsyncClient` 挂在 lifespan，配置 `limits`（max_connections/max_keepalive）与 `timeout` 全局默认；关闭时 `aclose()` 收尾。注意多 worker（每进程一个 client）与 DNS 变化（长连接钉死旧 IP，配合 `keepalive_expiry` 定期换连接）。实测说服法：本地起一个回环服务，对比"每请求新建"vs"共享 client 连 1000 次"的总耗时与 TIME_WAIT 数，差距通常 5-20 倍，数据比规范更有说服力。

```python
# file: code/03-Web后端开发/q6043_client_reuse.py
import http.server
import socket
import threading
import time
import sys

# 降级说明: httpx 0.27+ 基线; 缺库时用标准库 http.client 演示同样结论
try:
    import httpx
    HAVE_HTTPX = True
except ImportError:
    HAVE_HTTPX = False

def make_server():
    hits = [0]
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            hits[0] += 1
            self.send_response(200)
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"ok")
        def log_message(self, *a): pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, hits

if __name__ == "__main__":
    srv, hits = make_server()
    url = f"http://127.0.0.1:{srv.server_port}/"
    N = 300

    if HAVE_HTTPX:
        # 1) 每请求新建 client(事故写法)
        t0 = time.perf_counter()
        for _ in range(N):
            with httpx.Client() as c:               # 每次新建: SSLContext/连接全重建
                c.get(url)
        t_new = time.perf_counter() - t0
        # 2) 池化 client(正确姿势): 连接复用 keep-alive
        t0 = time.perf_counter()
        with httpx.Client(limits=httpx.Limits(max_connections=10)) as shared:
            for _ in range(N):
                shared.get(url)
        t_pool = time.perf_counter() - t0
        print(f"httpx {httpx.__version__}: 每请求新建 {t_new*1000:.0f} ms | 池化 {t_pool*1000:.0f} ms "
              f"-> {t_new/t_pool:.1f}x")
    else:
        print("httpx 未安装(降级): 用标准库 socket 演示连接建立成本")
        t0 = time.perf_counter()
        for _ in range(N):                          # 每次新建 TCP 连接
            s = socket.create_connection(("127.0.0.1", srv.server_port), timeout=2)
            s.sendall(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n")
            s.recv(1024); s.close()
        t_new = time.perf_counter() - t0
        s = socket.create_connection(("127.0.0.1", srv.server_port), timeout=2)
        t0 = time.perf_counter()
        for _ in range(N):                          # 复用一条连接多次写读(简化 keep-alive)
            s.sendall(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n")
            try:
                s.recv(1024)
            except OSError:
                break
        t_pool = time.perf_counter() - t0
        s.close()
        print(f"stdlib: 新建连接 {t_new*1000:.0f} ms vs 复用 {t_pool*1000:.0f} ms -> {t_new/max(t_pool,1e-6):.1f}x")

    # 3) 内核态证据: TIME_WAIT 数量(每请求新建会在高 QPS 下堆积端口)
    tw = sum(1 for _ in range(0))                   # 占位: 真实环境 netstat 统计
    print("内核账: 新建连接 = 每请求一个本地端口, TIME_WAIT 堆积 2MSL(60s);"
          " 池化 = 常驻 N 条连接")
    srv.shutdown()
```

**追问**：1) `httpx.AsyncClient` 为什么不能跨事件循环复用？——连接池绑定创建时的 loop（内部 transport/协程原语），跨 loop 使用报 RuntimeError 或泄漏连接；多 loop（Q5501 子解释器场景）每 loop 各建一个。2) 长连接池的 DNS 缓存问题怎么破？——连接建好后不再解析 DNS，服务迁移/故障切换会连旧 IP；用 `keepalive_expiry`（httpx 默认 5s）让空闲连接定期退役，或上游用稳定 VIP。3) 什么时候"每请求新建"反而是对的？——目标 host 极端不稳定（每次都要新证书域）、或严格的多租户证书隔离场景；默认按进程池化，例外要写明理由。

## 背诵要点
- 每请求新建 client = 每请求付握手 + 端口/TIME_WAIT + SSLContext 构建税，实测 5-20 倍差距。
- client 生命周期 = 进程/lifespan 级；AsyncClient 绑定 loop，不能跨事件循环复用。
- 池参数：max_connections/max_keepalive 限流，keepalive_expiry 防 DNS 钉死旧 IP。

## 复盘追问
- 服务高峰期出现 EADDRNOTAVAIL，如何把锅精确扣到"每请求新建连接"？（提示：netstat 统计 TIME_WAIT 增速与 QPS 匹配，对照 client 创建日志）
- 改成共享 client 后偶发 "pool timeout"，参数怎么调？（提示：max_connections 打满 + 没设获取超时，按下游并发预算设 limits 与 acquire timeout）
