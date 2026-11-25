---
title: [WEB-548] QUIC 握手与 TCP+TLS 握手的迁移收益测算
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-548：QUIC 握手与 TCP+TLS 握手的迁移收益测算

**答**：
- TCP+TLS1.3 首连：TCP 握手 1 RTT + TLS 1-RTT = 2 RTT 才能发请求；QUIC 把传输与加密合并，1 RTT 即发请求
- 重连场景收益更大：QUIC 0-RTT 首包即带请求数据，TCP+TLS session resumption 仍需 1 RTT；高 RTT 地区（如 100ms+）差距直接是百毫秒级
- 测算公式化：迁移首连收益 ≈ 1 × RTT，重连收益 ≈ 1 × RTT + 慢启动差异；总收益按「新建连接占比 × RTT」估
- 别只算握手：QUIC 丢包恢复不需等整条流重传排序（无 TCP 队头阻塞），弱网下吞吐收益往往大于握手收益
- 落地测法：同一页面分别在 h2-only 与 h3-enabled 的接入点采样 TTFB 分布，按 RTT 分桶（<50/50-150/>150ms）看收益曲线

```text
首连时序对比（RTT=100ms）:
TCP+TLS1.3:  SYN(1RTT) + ClientHello/ServerHello(1RTT) → 200ms 后才能发请求
QUIC:        Initial+握手(1RTT) → 100ms 后即可发请求
重连(0-RTT): QUIC 首包带请求 → ~0ms；TCP+TLS 恢复仍要 1RTT → 100ms
```
