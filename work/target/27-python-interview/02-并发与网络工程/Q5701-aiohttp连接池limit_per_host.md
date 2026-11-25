---
title: "[Q5701] aiohttp 连接池：limit_per_host 与超时分层"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5701 · aiohttp 连接池：limit_per_host 与超时分层

难度：P6 ｜ 标签：aiohttp、TCPConnector、连接池、limit_per_host、ClientTimeout

**问**：爬虫/网关用 `aiohttp.ClientSession` 并发 200 个请求打同一个上游，上游直接 429；把 `TCPConnector(limit=100)` 调小也没用，因为瓶颈在单个域名。`limit` 和 `limit_per_host` 分别管什么？连接池排队的时间算在哪个超时里？为什么 `ClientTimeout(total=5)` 有时 5 秒才失败，有时 1 秒就 `ConnectionTimeoutError`？

**答**：
结论：`limit` 是整个 connector 的**总连接数**上限，`limit_per_host` 是**单个 (scheme, host, port) 组合**的上限；默认 `limit=100`、`limit_per_host=0`（不限），所以只调 `limit` 挡不住"一个域名打满"。请求拿不到空闲连接时会在 connector 的等待队列里排队，这段等待计入 `ClientTimeout.total`，而 `connect` 只覆盖 TCP/TLS 建连、`sock_connect` 覆盖单次 connect 系统调用、`sock_read` 覆盖两次读之间的空闲。因此"池排队 + 建连"超过 total 时，先触发 `total`；建连本身超过 connect 时，抛 `ConnectionTimeoutError`（`ServerTimeoutError` 是 sock_read 超时）。

取舍：a) 对单上游限流，`limit_per_host` 才是正确旋钮，配合 `limit` 防全局打满；b) 池大小要 ≥ 并发度，否则请求在池里排队，表面超时、实际没发出去；c) 给"获取连接"单独留预算：`total` 要大于 `connect + 业务读`，别把 total 设得和 sock_read 一样；d) 长连接复用依赖 keep-alive，服务端 `Connection: close` 会让连接池反复建连，需观察 `connector` 的 `acquired`/`free` 指标；e) DNS 缓存 `ttl_dns_cache` 默认 10 秒，解析慢也会占 connect 预算。

实战：事故形态是"聚合接口对同一家汇率 API 并发 300，`limit=100` 只限制了总连接，单域名仍然 300 并发，对方按 IP 限流直接 429；把 `limit_per_host=20` 后排队变多，又把 `total` 从 3 秒提到 8 秒，才既不 429 也不误超时"。下面用信号量模拟连接池，观察每主机并发峰值与全局上限。

```python
import asyncio


class FakeConnector:
    def __init__(self, limit=100, limit_per_host=0):
        self.total = asyncio.Semaphore(limit)
        self.limit_per_host = limit_per_host
        self.per_host = {}
        self.active = {}
        self.peak = {}

    def host_sem(self, host):
        if self.limit_per_host == 0:
            return None
        return self.per_host.setdefault(
            host, asyncio.Semaphore(self.limit_per_host)
        )

    async def request(self, host, delay=0.01):
        async with self.total:
            sem = self.host_sem(host)
            if sem is None:
                await self._run(host, delay)
            else:
                async with sem:
                    await self._run(host, delay)

    async def _run(self, host, delay):
        self.active[host] = self.active.get(host, 0) + 1
        self.peak[host] = max(self.peak.get(host, 0), self.active[host])
        try:
            await asyncio.sleep(delay)
        finally:
            self.active[host] -= 1


async def main():
    connector = FakeConnector(limit=8, limit_per_host=2)
    await asyncio.gather(
        *[connector.request("api.a.com") for _ in range(10)],
        *[connector.request("api.b.com") for _ in range(10)],
    )
    print("[1] 每主机并发峰值:", connector.peak)
    print("[2] limit_per_host=2 生效:",
          all(v <= 2 for v in connector.peak.values()))
    print("[3] 全局 limit=8 仍是上限，池排队时间计入 total")


asyncio.run(main())
```

**追问一**：`limit_per_host` 的 key 包含哪些部分？—— 是 `(scheme, host, port)`，不是裸 hostname。`https://api.a.com:443` 与 `http://api.a.com:80` 是两个池；同一域名换端口也会另算。想按"业务上游"聚合限流，连接池做不到，得在应用层用信号量/令牌桶按上游 ID 控制。

**追问二**：为什么调大连接池反而更慢/更容易 429？—— 连接池只控制"同时打开多少连接"，不控制"上游能承受多少 QPS"。池越大，瞬时并发越高，上游限流/排队/超时越严重；正确顺序是先按上游容量定 `limit_per_host`，再用 `total` 控制本进程总量，最后用应用层限流做全局限速。连接池是资源上限，不是限流器。

## 背诵要点
- `limit` 是 connector 总连接数，`limit_per_host` 按 `(scheme, host, port)` 限单上游；默认 `limit=100`、per_host=0。
- 池排队计入 `ClientTimeout.total`；`connect` 只管建连，`sock_read` 管读空闲。
- 连接池不是限流器；按上游容量设 per_host，再配合应用层令牌桶。

## 复盘追问
- 只调 `limit` 为什么挡不住单域名打满？（per_host 默认 0 不限）
- 请求 1 秒就 `ConnectionTimeoutError` 而 total 是 5 秒，怎么解释？（connect 子超时先触发）
