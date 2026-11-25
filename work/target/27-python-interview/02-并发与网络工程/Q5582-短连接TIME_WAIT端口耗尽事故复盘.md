---
title: "[Q5582] 短连接刷出 TIME_WAIT 端口耗尽的事故复盘"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5582 · 短连接刷出 TIME_WAIT 端口耗尽的事故复盘

难度：★★★★☆ ｜ 标签：TCP / TIME_WAIT / 事故复盘 / 连接池

**问**：压测时 QPS 8000 后连接错误率飙到 100%，报错 `Cannot assign requested address`，netstat 里本机到同一个上游有 3 万个 TIME_WAIT。这是怎么形成的？主动关闭方是谁、为什么是它背锅？

**答**：
- **结论**：每条 TCP 连接由四元组标识，客户端侧的可变部分只有**临时端口**（ephemeral port，Linux 默认约 `ip_local_port_range` 3 万个）。短连接高频重建时，先发 FIN 的主动关闭方要停留 **2MSL（Linux 默认 60s×2）** 的 TIME_WAIT 状态占着四元组；客户端每次都是主动关闭（请求完就 close），端口以每秒 QPS 的速度消耗、60 秒后才回收——QPS 超过"端口数/60s"就打光临时端口，connect 直接报 `EADDRNOTAVAIL`。被动关闭方（服务端）的 TIME_WAIT 挂在服务端口上，不影响客户端端口池。
- **取舍**：修复优先级：1）**连接池/keep-alive**（根治，把 N 次握手压成 O(1) 连接）；2）`SO_LINGER` 强制 RST 关闭（避免 TIME_WAIT 但粗暴，丢尾部数据风险，仅协议确认无未发数据时可用）；3）内核参数 `tcp_tw_reuse` + 时间戳（仅出方向、需 `tcp_timestamps`，macOS 无此参数）；`tcp_tw_recycle` 在 NAT 下有灾难史已被 Linux 4.12 移除，提它只说明踩过坑。
- **实战**：容量公式先行：临时端口数 ÷ TIME_WAIT 时长 = 安全 QPS 上限（约 3 万/60s = 500 QPS 单目标）；多上游分摊端口需求，`SO_REUSEPORT`/绑定本地多 IP 也能扩池。Python 侧落实：`requests`/`httpx`/grpc 全部走 Session/Client 连接池，且连接池要设**最大空闲时长**，避免保活的连接被上游 LB 静默掐断后又重建风暴。

```python
"""演示短连接 vs keep-alive 的 fd/端口消耗差异（标准库，本机 loopback）"""
import socket, threading, time, http.server, http.client

# 起一个本地 HTTP 服务做上游
handler = http.server.BaseHTTPRequestHandler
handler.protocol_version = "HTTP/1.1"

class H(handler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write(b"ok")
    def log_message(self, *a): pass

srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()

# 客户端侧临时端口池观测
s = socket.socket()
local_range = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)  # 占位读
s.close()
print("本机临时端口池有限，每次短连接 close 都要占一个四元组 2×MSL")

def short_conn_requests(n):
    for _ in range(n):
        c = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
        c.request("GET", "/")
        c.getresponse().read()
        c.close()                     # 主动关闭 → 客户端 TIME_WAIT

def keepalive_requests(n):
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
    for _ in range(n):
        c.request("GET", "/")
        c.getresponse().read()        # 复用同一条连接
    c.close()

N = 300
t0 = time.perf_counter(); short_conn_requests(N); t1 = time.perf_counter()
print(f"短连接 ×{N}: {t1-t0:.3f}s（每次握手+关闭，端口进 TIME_WAIT）")
t0 = time.perf_counter(); keepalive_requests(N); t2 = time.perf_counter()
print(f"keep-alive ×{N}: {t2-t1-t0+t0:.3f}s 内复用单连接（对照 {t2-t1:.3f}s）")

# 工程要点：连接池要设最大空闲时长，防止 LB 静默断连后重建风暴
print("生产建议：requests.Session / httpx.Client(max_keepalive_connections, keepalive_expiry)")
srv.shutdown()
```

**追问链**
1. 为什么 TIME_WAIT 只留在主动关闭方？它的两个存在理由是什么？
   1. 理由：保证最后的 ACK 若丢失，被动方重传 FIN 时主动方还能 ACK（否则回 RST，被动方收不到干净关闭）；让旧连接的迟到报文在新四元组复用前自然消亡。
   2. 追问：服务端也堆积 TIME_WAIT 会怎样？——占的是服务端口四元组（ Accept 队列外），大量堆积影响 accept 新连接的查找表，但客户端不受端口限制；调优方向是让客户端先关或尽快复用。
2. `SO_LINGER` 与 `SO_REUSEADDR` 在这个事故里各扮演什么角色？
   1. `SO_LINGER(timeout=0)` 把关闭变成 RST，连接立刻消失、不进 TIME_WAIT——服务端重启"Address already in use"时有人拿它当救命稻草，但会截断未读完的数据，客户端必须确认收完才可用；`SO_REUSEADDR` 只解决**监听端**重启绑定旧地址的问题，不减少客户端 TIME_WAIT。
   2. 追问：为什么 `tcp_tw_recycle` 被移除？——依赖源时间戳判断"同一对端"，NAT 后多主机共享 IP 时时间戳倒跳，合法 SYN 被丢弃，排障极难。

## 背诵要点
- 客户端短连接高频主动关闭 → 临时端口（约 3 万）÷ 2×MSL(60s×2) = 安全 QPS 上限，打光后 EADDRNOTAVAIL。
- TIME_WAIT 在主动关闭方：保 ACK 重传 + 旧报文消亡；修复首选连接池 keep-alive，其次 tw_reuse，禁用 tw_recycle。
- 连接池要配最大空闲时长防 LB 静默断连；SO_LINGER(0)=RST 关闭有截断风险，SO_REUSEADDR 只管监听端。

## 复盘追问
- 事故复盘时如何从 netstat/ss 的状态分布反推"谁先关的连接"？
- keep-alive 化之后，上游 LB 的空闲超时与客户端池参数怎么对齐验证？
