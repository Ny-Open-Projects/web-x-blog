---
title: [WEB-259] Network 面板 Timing 各阶段含义
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 排查]
type: 面试题
---

## WEB-259：Network 面板 Timing 各阶段含义

**答**：
- Queueing：请求在队列等待——并发连接上限（同域 6 个）、资源优先级低被推迟、磁盘缓存写入中。
- Stalled：等待复用连接可用/代理协商，类似 queueing 但发生在连接层。
- DNS Lookup / Initial connection / SSL：分别解析域名、TCP 三次握手、TLS 握手；复用已有连接时这三段不出现（这就是 preconnect 的价值）。
- Request sent（通常极小）→ Waiting for server response（TTFB，服务端处理时间）→ Content Download（响应体下载）。
- 优化映射：Queueing 长→减少请求数/域名分片已过时（HTTP2 不需要）；TTFB 长→服务端/CDN；Download 长→压缩/字段精简。

```bash
# 用 Resource Timing API 拿同样的分段数据
const [r] = performance.getEntriesByName('https://api.example.com/data');
console.table({
  dns: r.domainLookupEnd - r.domainLookupStart,
  tcp: r.connectEnd - r.connectStart,
  ssl: r.secureConnectionStart && r.connectEnd - r.secureConnectionStart,
  ttfb: r.responseStart - r.requestStart,
  download: r.responseEnd - r.responseStart,
});
```
