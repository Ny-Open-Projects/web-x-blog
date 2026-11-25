---
title: "[Q5703] httpx 与 requests：连接复用和 TLS 握手的账不一样"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5703 · httpx 与 requests：连接复用和 TLS 握手的账不一样

难度：P7 ｜ 标签：httpx、requests、keep-alive、TLS、连接池、性能

**问**：把 `requests.get()` 换成 `httpx.Client()` 长连接，QPS 没涨反而更慢；抓包发现每几秒就有一次新的 TLS 握手。`requests.Session` 和 `httpx.Client` 都复用了连接，为什么复用率差这么多？`keepalive_expiry`、`pool_maxsize`、HTTP/2 多路复用分别影响什么？

**答**：
结论：两者都靠连接池复用 TCP 连接，但**空闲连接的保留策略**不同：`requests` 底层 urllib3 默认不主动过期空闲连接（`pool_connections`/`pool_maxsize` 控数量，连接一直留着直到服务端关或池淘汰），所以低频请求也容易命中旧连接；`httpx` 默认 `keepalive_expiry=5.0` 秒，空闲超过 5 秒就关闭，下一次请求重新 TCP + TLS 握手。TLS 握手（尤其 TLS 1.2 的 2-RTT）是主要成本，复用连接就跳过了它；`httpx` 的短过期在"每隔几秒一次"的流量下会显著降低复用率。

取舍：a) 高频调用用 `httpx.Client(limits=Limits(max_keepalive_connections=..., keepalive_expiry=...))`，把过期调到大于典型请求间隔；b) `requests.Session` 复用久但容易拿到服务端已关闭的 stale 连接，需要重试策略或 `pool_maxsize` 配合健康检查；c) HTTP/2（`http2=True`）在单连接上多路复用，能减少连接数，但对端不支持时退回 1.1，别把它当万能加速；d) 客户端实例要**进程级复用**，别每次请求 `with httpx.Client()`，那等于每次新建池；e) 注意 TLS session ticket/会话缓存由 OpenSSL 管，Python 层不保证跨连接复用，别把"连接复用"和"TLS 会话复用"混为一谈。

实战：事故形态是"定时任务每 3 秒调一次风控接口，从 requests 迁到 httpx 后 P99 从 20ms 涨到 90ms，抓包看到每条请求都重新握手；把 `keepalive_expiry` 从默认 5 秒调到 30 秒，并复用全局 Client，P99 回落"。下面用连接池模型对比两种过期策略下的握手次数。

```python
class Pool:
    def __init__(self, keepalive=None, max_conns=10):
        self.keepalive = keepalive      # None 表示不主动过期
        self.max_conns = max_conns
        self.conns = []                 # [(host, last_used)]
        self.handshakes = 0

    def acquire(self, host, now):
        if self.keepalive is not None:
            self.conns = [
                (h, t) for h, t in self.conns
                if now - t < self.keepalive
            ]
        for i, (h, _) in enumerate(self.conns):
            if h == host:
                self.conns[i] = (host, now)
                return "reuse"
        self.handshakes += 1
        if len(self.conns) >= self.max_conns:
            self.conns.pop(0)
        self.conns.append((host, now))
        return "new"


def run(pool, gaps):
    now = 0.0
    for gap in gaps:
        now += gap
        pool.acquire("api.example.com", now)
    return pool.handshakes


gaps = [0, 0.1, 10, 0.1, 60, 0.1]
print("[1] requests.Session 不主动过期，握手次数:", run(Pool(), gaps))
print("[2] httpx 默认 keepalive_expiry=5s，握手次数:", run(Pool(keepalive=5.0), gaps))
print("[3] httpx 调到 30s，握手次数:", run(Pool(keepalive=30.0), gaps))
print("[4] 复用省掉的是 TCP+TLS 握手，不是请求本身的 RTT")
```

**追问一**：为什么 `requests` 复用了连接还会偶发 `ConnectionResetError`？—— 服务端或中间设备（LB/NAT）有 idle timeout，空闲连接被单方面关闭，客户端池里仍认为是活的，下次写入才收到 RST。`requests` 默认没有重试，需要 `HTTPAdapter(max_retries=Retry(...))`；`httpx` 有 `keepalive_expiry` 主动淘汰，但过期时间必须小于链路的 idle timeout，否则同样踩。生产上把 keepalive 设为"小于最短板 idle timeout"，并加幂等重试。

**追问二**：HTTP/2 多路复用能否替代连接池？—— 不能完全替代。HTTP/2 在**一个连接**上并发多个 stream，减少了连接数，但仍受 `max_concurrent_streams`、TCP 队头阻塞、单连接带宽限制；而且每个请求仍要经过池的 stream 配额。对高并发，连接池 + HTTP/2 多流要一起调；对低延迟小请求，单连接多流收益明显，但对大响应/丢包场景，多连接反而更稳。

## 背诵要点
- requests（urllib3）不主动过期空闲连接；httpx 默认 `keepalive_expiry=5s`，低频流量下会反复握手。
- 连接复用跳过 TCP+TLS 握手；客户端要进程级复用，别每请求新建 Client。
- keepalive 必须小于链路 idle timeout，否则 stale 连接导致 RST；HTTP/2 多流不替代池。

## 复盘追问
- 迁到 httpx 后 P99 变差，抓包看到重复握手，怎么调？（keepalive_expiry + 全局 Client）
- 连接复用了还偶发 ConnectionReset，根因是什么？（服务端/LB 先关空闲连接）
