---
title: [Q5534] TLS 握手的容量账与 session 复用降载
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5534 · TLS 握手的容量账与 session 复用降载

> 难度:★★★★ | 标签:成本工程, TLS, session resumption, 容量规划

**问**：TLS 握手到底贵在哪？一次握手折算多少毫秒 CPU？session 复用（session ID / ticket）省掉什么、Python 客户端怎么配置？为什么"短连接 HTTPS 内网调用"是容量事故高发区？

**答**：握手贵在**非对称运算**：TLS 1.2 RSA-2048 一次完整握手服务端约 1-3ms 纯 CPU（含证书链签名验证），TLS 1.3 ECDHE 降至约 0.5-1ms，但**每次新建连接都要付**。容量账：单核 1000 QPS 的服务，若 30% 请求是新建 TLS 连接，握手就吃掉 3-10ms/请求的预算与可观 CPU 配额——这就是短连接 HTTPS 内网调用的经典事故：压测时连接池热、生产冷启动/波动时连接重建风暴，握手把 CPU 打满、RTT 翻倍。降载三板斧：1) **连接复用**是第一位的（HTTP keep-alive/Q1601，一条连接只付一次握手）；2) **session 复用**兜底重建场景——TLS 1.2 用 session ID/ticket 跳过证书与非对称部分，成本降到对称算法恢复（约 1/10）；TLS 1.3 的 PSK（0-RTT）更快但有重放面（Q5511，只配幂等 GET）；3) **握手分层超时**：connect/握手/应用读写分开设（Q5515 的超时分层），防慢握手占满 worker。Python 配置：`ssl.SSLContext` 天然带 session 缓存（客户端 per-context），跨进程共享要自己搬 `ctx.session`/`ctx.session_stats`；服务端 nginx/网关侧配 `ssl_session_cache shared` + `ssl_session_tickets`。

```python
# file: code/02_并发与网络工程/q5534_tls_handshake_cost.py
"""TLS 握手成本的可观测实验: 本地回环测握手 RTT 与复用差异."""
import socket
import ssl
import time

HOST, PORT = None, None

def find_local_tls_target() -> tuple[str, int] | None:
    """找一个本地可用的 TLS 目标做实验(无网络时降级)."""
    for host, port in (("localhost", 4443), ("127.0.0.1", 443)):
        try:
            with socket.create_connection((host, port), timeout=1):
                return host, port
        except OSError:
            continue
    return None

def handshake_once(host: str, port: int, session=None) -> tuple[float, ssl.SSLSession | None]:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE          # 实验环境; 生产必须验证
    if session is not None:
        ctx.session = session                # 客户端 session 复用
    t0 = time.perf_counter()
    with socket.create_connection((host, port), timeout=3) as raw:
        with ctx.wrap_socket(raw, server_hostname=host) as s:
            sess = s.session                 # 带回给下次复用
            was_reused = s.was_reused()      # 本次是否走了复用路径
    return (time.perf_counter() - t0) * 1000, sess, was_reused

if __name__ == "__main__":
    target = find_local_tls_target()
    if target is None:
        # 无 TLS 服务的降级: 仅演示成本模型的算术
        print("无本地 TLS 目标, 演示容量账算术:")
        print("TLS1.2 RSA-2048 全握手 ≈1-3ms CPU; TLS1.3 ECDHE ≈0.5-1ms")
        print("复用后(session/ticket/PSK) ≈ 1/10 成本")
        print("1 核 1000QPS, 30% 新建连接 -> 握手 CPU ≈ 1000*0.3*1ms = 0.3 核")
    else:
        host, port = target
        _, sess, reused = handshake_once(host, port)
        t2, _, reused2 = handshake_once(host, port, sess)
        print(f"首次握手 {t2:.1f}ms reused={reused}; 带复用 {t2:.1f}ms reused={reused2}")
    print("结论: 先连接复用, 再 session 复用兜底重建, 超时分层防慢握手占 worker")
```

**追问**：1) session ID 与 session ticket 的差异与运维要点？——ID 存服务端（要缓存共享才有跨 worker 效果），ticket 自包含加密状态（无状态但密钥要定期轮换，防 ticket 解密攻击）；Python ssl 两者都透明支持，服务端配置决定。2) 为什么 TLS 1.3 的 1-RTT/0-RTT 改变了容量公式？——1-RTT 握手省一个 RTT（RTT 60ms 的链路单此一项就省 60ms 延迟），0-RTT 在复用场景连 RTT 都省掉，但应用数据先于握手完成送达 → 重放风险（Q5511）。3) 容量账里"握手 CPU"怎么落到 k8s 配额？——用 perf/flamegraph 抽样 ssl 相关帧占比，把握手 QPS（新建连接速率）做成独立指标，与 CPU 配额线性对账。

## 背诵要点
- 握手贵在非对称运算：TLS1.2 RSA-2048 ≈1-3ms CPU/次，TLS1.3 ECDHE ≈0.5-1ms；复用降至约 1/10。
- 降载顺序：连接复用 > session 复用（ID/ticket）兜底重建 > 0-RTT（配幂等，防重放）。
- 新建连接速率是独立容量指标；压测热池掩盖握手成本是内网 HTTPS 事故高发原因。

## 复盘追问
- 生产"平时正常、发布后 5 分钟 CPU 飙高"，怎么证明是连接重建风暴而不是发布本身的慢查询？
- 你会怎么给"新建 TLS 连接速率/秒"设告警阈值？冷启动预热脚本（Q2191）里加什么动作？
