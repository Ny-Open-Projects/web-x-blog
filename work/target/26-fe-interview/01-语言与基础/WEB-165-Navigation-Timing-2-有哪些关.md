---
title: [WEB-165] Navigation Timing 2 有哪些关键字段？怎么用它们拆解加载耗时？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-165：Navigation Timing 2 有哪些关键字段？怎么用它们拆解加载耗时？
**答**：
- 时间轴主干：startTime → redirect → fetchStart → DNS（domainLookup）→ TCP（connect，secureConnectionStart 拆 TLS）→ requestStart → responseStart（TTFB）→ responseEnd → domInteractive/DCL/load 等里程碑。
- 常用派生：DNS = domainLookupEnd - domainLookupStart；TTFB = responseStart - startTime；TLS = connectEnd - secureConnectionStart。
- type 字段区分 navigate/reload/back_forward，预渲染会影响口径。
- 上报注意：时间统一从 startTime 起算，避免与 timeOrigin 混用带来的偏差。

```javascript
const nav = performance.getEntriesByType('navigation')[0];
const timing = {
  type: nav.type,                                   // navigate / reload / back_forward
  redirect: nav.redirectEnd - nav.redirectStart,    // 重定向开销
  dns: nav.domainLookupEnd - nav.domainLookupStart, // DNS 解析
  tcp: nav.secureConnectionStart > 0
    ? nav.secureConnectionStart - nav.connectStart  // 纯 TCP 段
    : nav.connectEnd - nav.connectStart,            // 无 TLS 时整段都是 TCP
  tls: nav.secureConnectionStart > 0 ? nav.connectEnd - nav.secureConnectionStart : 0,
  ttfb: nav.responseStart - nav.startTime,          // 首字节
  download: nav.responseEnd - nav.responseStart,    // 响应下载
  domReady: nav.domContentLoadedEventEnd - nav.startTime,
  load: nav.loadEventEnd - nav.startTime,
};
report('navigation-timing', timing); // 逐段定位慢在哪一层
```
