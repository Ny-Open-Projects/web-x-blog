---
title: "[Q6178] HTTP/2 Rapid Reset：流并发上限挡不住创建速率"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6178 · HTTP/2 Rapid Reset：流并发上限挡不住创建速率

难度：P7 ｜ 标签：HTTP/2、Rapid Reset、CVE-2023-44487、流控、限流

**问**：2023 年的 HTTP/2 Rapid Reset（CVE-2023-44487）为什么能让一条连接打满 8 核？攻击者只是不停发 `HEADERS` 再立刻 `RST_STREAM`，服务端的 `MAX_CONCURRENT_STREAMS=100` 明明没被突破，为什么还是被打穿？"并发流数"和"流创建速率"差在哪？Python 的 uvicorn/hypercorn/h2 栈要怎么防？这和 Q6052（slowloris/慢客户端）、Q5667（HTTP/2 流控窗口）是同一类问题吗？

**答**：
结论：`SETTINGS_MAX_CONCURRENT_STREAMS` 限制的是**同时在途**的流数；`RST_STREAM` 会立刻释放一个流配额，所以攻击者可以"建流 → 重置 → 再建流"高速循环，**并发数永远是 1~N，但创建速率可以是每秒数万**。服务端的成本不对称：客户端发两个很小的帧，服务端要解析 HPACK/HEADERS、分配流状态、创建 Task/调用 handler、再处理取消与清理（日志、指标、连接池归还）；即使 handler 立刻被取消，这些工作已经发生。Rapid Reset 利用的就是"创建/销毁成本 >> 攻击成本"，把单连接变成放大器。防御要限**速率**而不只是并发：连接级流创建 token bucket、重置率阈值、单连接/单 IP 连接数上限、边缘（LB/Envoy/云 WAF）的 HTTP/2 防护、必要时 `GOAWAY` 关闭滥用连接；应用层还要保证取消是协作式、清理不阻塞。

取舍：限速太严会误伤正常客户端（移动网络切换、用户主动取消、长轮询重连都会产生 RST）；放在应用层做只能保底，最好在边缘做（更早丢弃、成本更低），应用层保留"每连接创建速率/重置率"指标与熔断。`max_concurrent_streams` 仍然要设（防慢流占用），但它不是 Rapid Reset 的解。和 Q6052 的区别：slowloris 是"连接/请求慢慢发、占住 worker"，Rapid Reset 是"流快速建删、烧 CPU/调度"；和 Q5667 的区别：那张卡讲流控窗口导致的跨流阻塞，本题讲流生命周期的创建/销毁成本。

实战：事故形态是"单 IP 一条 h2 连接，HEADERS/RST 循环 10 万次/秒，CPU 打满、正常请求 P99 飙升；`max_concurrent_streams=100` 的指标一直很低，所以告警没触发"。下面用流表模拟：并发上限 100、RST 立即释放配额，攻击循环 1 万个流时并发峰值始终 ≤100，但创建数 10000；加一个 200 流/秒的 token bucket 后，创建数被压到几百、其余直接拒绝。

```python
class StreamTable:
    def __init__(self, max_concurrent, rate_per_sec):
        self.max_concurrent = max_concurrent
        self.rate_per_sec = rate_per_sec
        self.active = 0
        self.created = 0
        self.rejected = 0
        self.handlers_started = 0
        self.tokens = rate_per_sec
        self.last = 0.0

    def _refill(self, now):
        elapsed = now - self.last
        self.last = now
        self.tokens = min(self.rate_per_sec, self.tokens + elapsed * self.rate_per_sec)

    def open_stream(self, now):
        self._refill(now)
        if self.active >= self.max_concurrent or self.tokens < 1:
            self.rejected += 1
            return False
        self.tokens -= 1
        self.active += 1
        self.created += 1
        self.handlers_started += 1       # 服务端已开始处理
        return True

    def reset_stream(self):
        if self.active:
            self.active -= 1             # 配额立刻释放，但 handler 清理仍在跑


def attack(limit_rate):
    table = StreamTable(max_concurrent=100, rate_per_sec=limit_rate or 10**9)
    now = 0.0
    for _ in range(10000):
        now += 0.0001                     # 每 0.1ms 一个流
        if table.open_stream(now):
            table.reset_stream()
    return table


for rate in (None, 200):
    t = attack(rate)
    label = "无限速" if rate is None else f"限速 {rate}/s"
    print(f"{label:10} 创建={t.created:5} 拒绝={t.rejected:5} "
          f"峰值并发<={t.max_concurrent} 实际 active={t.active}")
```

**追问一**：为什么 RST 之后服务端不能"立刻停止工作"？——流被重置只表示对端不再要响应，服务端的 handler 可能已经启动（读 body、查 DB、调用下游），取消是**协作式**的：要等协程在下一个 await 点检查取消、要执行 `finally` 归还连接/释放锁/写日志。ASGI 服务器通常会给应用发 `http.disconnect`，但应用不检查就继续跑；即使检查，清理本身也要花 CPU。Rapid Reset 的放大效应就来自"每个流都要走一遍创建 + 取消 + 清理"。

**追问二**：为什么"每 IP 连接数限制"不够？——NAT/移动网络后大量正常用户共享 IP，严格 per-IP 会误伤；攻击者也可以用大量源 IP/代理池。更有效的是**每连接**的流创建速率 + 全局/每 worker 的总流速率 + 边缘的连接数上限，多层配合；同时对"高重置率、低完成率"的连接打标并 `GOAWAY`。监控上要区分 `streams_created`、`rst_stream_received`、`active_streams` 三条曲线：并发低但创建/重置高，就是 Rapid Reset 的指纹。

## 背诵要点
- `MAX_CONCURRENT_STREAMS` 限的是同时在途流；RST 立即释放配额，挡不住"建-重置-再建"的创建速率。
- Rapid Reset 利用创建/销毁成本不对称（客户端两个小帧 vs 服务端完整请求生命周期 + 取消清理）。
- 防御：连接级流创建速率 + 重置率阈值 + 边缘防护 + `GOAWAY`；监控 created/rst/active 三条曲线，别只看并发。

## 复盘追问
- 单连接打满 CPU、但 `max_concurrent_streams` 指标很低，如何用 Rapid Reset 解释？（并发 vs 速率、RST 释放配额、成本不对称）
- 为什么 per-IP 限流不够？应用层限速和边缘限速各自的价值是什么？（NAT/代理池、成本位置、全局/每连接速率）
