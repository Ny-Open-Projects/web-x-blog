---
title: [PER-054] TTFB 如何分解为 DNS/TCP/TLS/服务端各段耗时？各段分别怎么优化？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-054：TTFB 如何分解为 DNS/TCP/TLS/服务端各段耗时？各段分别怎么优化？

**答**：
- TTFB = 导航发起后到收到**第一个字节**的时间，可用 `performance.getEntriesByType('navigation')[0]` 分解：`domainLookupEnd - domainLookupStart`（DNS）、`connectEnd - secureConnectionStart`（TLS）、`connectEnd - connectStart - tls`（TCP）、`responseStart - requestStart`（服务端处理）。
- DNS 慢：预热 `dns-prefetch`/`preconnect`、减少第三方域名；TLS 慢：启用 TLS 1.3、会话复用、OCSP Stapling；服务端慢：边缘缓存/CDN 回源、接口聚合、数据库索引。
- TTFB 良好阈值 800ms，其中重定向段（`redirectStart`）常被忽略，砍掉多余跳转收益最大。
- 注意 CDN 命中与否要按 `x-cache` 头区分样本，否则平均 TTFB 会被回源请求拉高误导结论。

```javascript
const nav = performance.getEntriesByType('navigation')[0];

// 把一次导航的耗时拆成五段，分别归因优化
const segments = {
  redirect: Math.round(nav.redirectEnd - nav.redirectStart),      // 重定向，尽量为 0
  dns:      Math.round(nav.domainLookupEnd - nav.domainLookupStart), // DNS 解析
  tcp:      Math.round(nav.connectEnd - nav.secureConnectionStart
              - (nav.secureConnectionStart ? 0 : 0))               // 纯 TCP 握手（无 TLS 时为 connectEnd - connectStart）
              || Math.round(nav.connectEnd - nav.connectStart),
  tls:      nav.secureConnectionStart
              ? Math.round(nav.connectEnd - nav.secureConnectionStart) // TLS 握手
              : 0,
  server:   Math.round(nav.responseStart - nav.requestStart),      // 服务端处理，边缘缓存可大幅压缩
  ttfb:     Math.round(nav.responseStart - nav.startTime),
};
console.table(segments);
// 上报时带上 x-cache 命中情况（需服务端注入），区分 CDN HIT 与 MISS 的样本
fetch('/api/ttfb-report', { method: 'POST', body: JSON.stringify({ ...segments, path: location.pathname }) });
```
