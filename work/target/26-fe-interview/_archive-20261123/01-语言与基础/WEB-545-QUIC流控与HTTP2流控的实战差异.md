---
title: [WEB-545] QUIC 流控与 HTTP/2 流控的实战差异
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-545：QUIC 流控与 HTTP/2 流控的实战差异

**答**：
- h2 流控在应用层（DATA 帧的 WINDOW_UPDATE），只管请求/响应流；QUIC 流控在传输层，管所有流 + 连接两级，粒度更细也更早介入
- 两级流控的影响：一个慢流占满连接级配额会拖累其他流，服务端要平衡 per-stream 与 per-connection 窗口比例（常见 1:4~1:16）
- 对大文件下载场景：QUIC 初始流窗口偏小会限制单流吞吐，需调大 initial max_data/max_stream_data，否则 h3 下载速度反而不如 h2
- 对多请求并发场景：QUIC 流间无队头阻塞的前提是流控窗口足够，窗口太小会人为制造「应用层队头阻塞」，这是迁移后性能不升反降的常见原因
- 前端侧感知：下载类业务迁移后测速，重点对比「单流大文件」与「多流小文件」两种模式，分别定位流控参数是否合理

```text
慢流占满连接窗口 → 其他流即使空闲也被限速
调优：max_stream_data=4MB / max_data=16MB（按带宽时延积 BDP 估算）
BDP ≈ 带宽(Mbps) × RTT(ms) / 8 —— 窗口至少要 ≥ 1 个 BDP
```
