---
title: [WEB-426] QUIC 包头为什么加密，对中间设备意味着什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-426：QUIC 包头为什么加密，对中间设备意味着什么

**答**：
- QUIC 除少量固定字段外连包头都加密，中间设备（防火墙、运营商设备）看不到流号、ACK 内容
- 动机：避免 TCP 时代「中间盒看懂协议后擅自干预」导致协议僵化（如对 HTTP/2 的干扰），让协议只能靠版本升级演进
- 代价：丢包定位、网络诊断变难——抓包看不到流细节，只能靠 QUIC 跟踪头和客户端打点
- 前端关联：线上 HTTP/3 的问题排查更多依赖 RUM（真实用户监控）与浏览器内部指标，而不是 tcpdump
- 钩子：部分运营商对 UDP 限速/拦截，QUIC 有 Retry/Version Negotiation 与回退 H2 的兜底

```javascript
// HTTP/3 下排查要靠 RUM 打点：上报协议版本
performance.getEntriesByType('navigation').forEach(n => {
  if (n.nextHopProtocol) {
    navigator.sendBeacon('/log', JSON.stringify({ proto: n.nextHopProtocol, dns: n.domainLookupEnd - n.domainLookupStart }));
  }
});
```
