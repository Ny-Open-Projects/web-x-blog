---
title: [PER-1062] HTTP/2 与 HTTP/3 的服务器端配置要点（前端要知道什么）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1062：HTTP/2 与 HTTP/3 的服务器端配置要点（前端要知道什么）

**答**：
- H2：开启头部压缩（HPACK 动态表足够大）、并发流上限合理（>100）、禁用响应头部冗余（每请求省字节）；避免过小 SETTINGS 帧窗口导致吞吐受限。
- H3：UDP 缓冲区调大、拥塞控制算法选择（BBR 优于 CUBIC 弱网）、连接迁移与 0-RTT 策略配置。
- 前端联动点：知道服务端参数才能解释"为什么 H3 弱网收益没达到预期"（可能是拥塞算法没换）。
- 协作：前端提供真实分布数据（协议占比、弱网占比）帮助服务端定参。

```javascript
// 服务端 Nginx H2/H3 配置要点
// listen 443 quic reuseport;                 # H3
// listen 443 ssl http2;
// ssl_early_data on;                          # 0-RTT（配合幂等白名单）
// quic_retry on;
// http2_max_concurrent_streams 256;
// ssl_buffer_size 8k;                         # TLS 记录大小影响流式
// 前端验证：protocolMix() 观察 h3 占比是否健康（>60% 为佳）
```
