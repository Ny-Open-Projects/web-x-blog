---
title: [WEB-085] 浏览器的网络栈有哪些内部缓存？socket 复用怎么观察？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-085：浏览器的网络栈有哪些内部缓存？socket 复用怎么观察？
**答**：
- 自上而下：内存缓存（当前页面已用资源）→ 磁盘 HTTP 缓存（Cache-Control/ETag 管辖）→ DNS 缓存 → socket 池。
- socket 池按"host + 代理 + 隐私分区"分桶复用连接，HTTP/1.1 每桶并发有限，HTTP/2 一条连接多路复用。
- 观察手段：chrome://net-export 抓完整网络日志，chrome://net-internals/#sockets 看活连接与 socket 池。
- 代码侧用 Resource Timing 判断：domainLookup 与 connect 的起止时间相等，说明 DNS 与 TCP/TLS 都走了缓存复用。

```javascript
// 用 Resource Timing 判断连接是否被 socket 池复用
const entry = performance.getEntriesByType('resource')
  .find((e) => e.name.includes('api.example.com'));
if (entry) {
  const dnsReused = entry.domainLookupStart === entry.domainLookupEnd;   // true 走了 DNS 缓存
  const tcpReused = entry.connectStart === entry.connectEnd;              // true 复用已有 socket
  const tlsReused = entry.secureConnectionStart === 0;                    // 0 表示无独立 TLS 握手
  console.log({ dnsReused, tcpReused, tlsReused, ttfb: entry.responseStart - entry.requestStart });
}
// chrome://net-export 录制 + netlog-viewer 分析 socket 池全貌
```
