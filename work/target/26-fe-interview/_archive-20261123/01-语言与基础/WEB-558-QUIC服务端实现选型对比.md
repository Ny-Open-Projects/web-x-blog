---
title: [WEB-558] QUIC 服务端实现选型：ngtcp2/quiche/msquic/envoy 怎么选
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-558：QUIC 服务端实现选型：ngtcp2/quiche/msquic/envoy 怎么选

**答**：
- 自建网关/代理：envoy（quiche 后端）适合已有 envoy 栈的团队；ngtcp2+nghttp3 性能好但偏库不是成品；quiche（Cloudflare）工程化成熟、文档全
- 语言栈匹配优先：Go 服务可用 quic-go（生态最顺）、Rust 用 quiche/quinn、C/C++ 用 ngtcp2/msquic——选型第一原则是团队维护语言
- 生产成熟度要验证：看有没有大厂生产案例、HTTP/3 语义（h3 ALPN、QPACK）实现完整度、Datagram/WebTransport 支持进度
- 大多数业务其实不该自建：CDN/云厂商网关自带 h3 能力，自建只在你需要协议级定制（私有信令、拥塞策略）时才值得
- 评估清单：0-RTT/Retry/连接迁移/QPACK 动态表/GSO 支持/内存占用 per connection——逐项打分再定

```text
选型速查:
  CDN 覆盖为主        → 不自建, 配置 CDN h3
  Go 微服务直出 h3    → quic-go + 反代
  高定制网关          → envoy + quiche
  Windows 生态        → msquic
  极致性能/库形态     → ngtcp2
```
