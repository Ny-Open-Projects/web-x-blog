---
title: "[Q6177] 上游 keep-alive 与 LB 空闲超时错配导致偶发 502"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6177 · 上游 keep-alive 与 LB 空闲超时错配导致偶发 502

难度：P6-P7 ｜ 标签：keep-alive、502、反向代理、超时、连接池

**问**：服务上 K8s 后，低峰期每隔几分钟出现几个 502，高并发时反而没有；重启 Pod/扩缩容时更明显。抓包看到 LB 把请求复用到一条连接上，upstream 刚回了 FIN/RST。为什么"连接看着是好的"却发不出去？uvicorn 的 `--timeout-keep-alive`（默认 5 秒）和 Nginx/ALB 的 `keepalive_timeout`（常见 60 秒）谁该大？本题与 Q617（TCP keepalive 探活）的边界在哪？三端超时到底该怎么排？

**答**：
结论：keep-alive 连接有**两端各自的空闲超时**。上游（uvicorn）默认 5 秒没有新请求就主动关连接；LB 却认为这条连接还能复用 60 秒，于是把下一个请求塞进一条"上游已经关了、LB 还没感知"的连接——写请求可能成功（进入内核缓冲），读响应时收到 FIN/RST，LB 返回 502。高并发时连接一直有流量、不会触发空闲超时，所以"低峰才出问题"是典型指纹。修复原则：**上游空闲超时必须大于下游（LB/客户端）的空闲超时**，让关闭动作由下游先发起，或者至少给下游留出感知窗口（常见配置：upstream 75s、LB 60s）。

取舍：把 uvicorn `--timeout-keep-alive` 调到 75s，连接复用率高、握手少，但空闲连接占 fd/内存更久；LB 侧也可以把 `keepalive_timeout` 调小到 5s 以下，代价是上游连接频繁重建。更稳的是让 LB 对"连接被上游关闭"做**幂等请求重试**（GET/HEAD/PUT/DELETE，Q6170 的幂等前提），但 POST 不能盲目重试。客户端连接池的 `keepalive_expiry` 要小于服务端/LB 的最小空闲超时，否则同样会复用死连接。

实战：事故形态是"监控上 502 占比 0.1%，只在凌晨低峰出现；重启发布窗口放大"。下面用时间线模拟：客户端认为连接可复用 60s、上游 5s 就关，请求间隔 0.1s 时大量请求撞上已关闭连接；把上游调到大于客户端后，撞死连接降为 0。这不是真实网络，但精确复现"谁先关"的因果。

```python
def simulate(client_keepalive, server_idle, lb_idle, interval, total=100):
    stale = 0
    reuse = 0
    horizon = min(client_keepalive, lb_idle)   # 三端里最早到期的那个决定上限
    for i in range(total):
        age = i * interval
        if age <= horizon:
            reuse += 1
            if age > server_idle:
                stale += 1
    return stale, reuse


for label, ck, si, lb in [
    ("默认 Uvicorn 5s / LB 60s", 60, 5, 60),
    ("对齐后 4s / 5s / 60s", 4, 5, 60),
]:
    stale, reuse = simulate(ck, si, lb, interval=0.1)
    print(f"{label:24} 复用 {reuse} 次，其中撞到已关闭连接 {stale} 次")


def request(pool, now, server_idle, retried=False):
    age = now - pool["last_used"]
    if age > server_idle:
        return "502: 上游已关闭 keep-alive 连接" + ("（重试成功）" if retried else "")
    return "200"


pool = {"last_used": 0.0}
print("30 秒后复用:", request(pool, now=30, server_idle=5))
print("幂等请求重试:", request(pool, now=30, server_idle=5, retried=True))
```

**追问一**：为什么高并发时不出现、低峰才出现？——keep-alive 超时是"空闲计时"：连接一直在传请求就不会到 5 秒；低峰时请求间隔可能几十秒，连接早被上游关了，LB 的连接池里却还留着它。扩缩容/发布时更明显，因为 Pod 被终止会主动关连接，LB 还没来得及摘除。排查时看 502 的时间分布（是否集中在低峰/发布窗口）、抓包看 FIN 的方向和时序。

**追问二**：让 LB 重试不就行了吗？——只有**幂等**请求能安全重试（GET/HEAD/PUT/DELETE，且 PUT 要保证语义幂等，Q6170）；POST 重试可能重复下单/扣款。而且重试只能掩盖"死连接复用"，不能解决根因：每次都要多一次 RTT，POST 仍然 502。正确顺序是先把超时关系配对（upstream > LB > client），再把重试作为兜底，并监控"stale connection"计数。

## 背诵要点
- keep-alive 空闲超时两端独立；上游先关、LB 后知 → 复用死连接 → 偶发 502，低峰/发布窗口最明显。
- 配置原则：upstream idle > LB idle > client pool expiry（如 75s/60s/50s），让下游先关。
- 重试只救幂等请求；POST 不能盲目重试，根因是超时关系配反。

## 复盘追问
- 低峰每几分钟几个 502、高并发正常，如何用 keep-alive 空闲超时解释并修？（两端计时、upstream > LB、抓包 FIN）
- 为什么"给 LB 加重试"不能作为唯一修复？POST 怎么办？（幂等前提、重复副作用、超时关系才是根因）
