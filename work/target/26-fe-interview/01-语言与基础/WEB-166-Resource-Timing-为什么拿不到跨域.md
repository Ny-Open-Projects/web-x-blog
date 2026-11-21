---
title: [WEB-166] Resource Timing 为什么拿不到跨域资源的耗时细节？TAO 怎么解决？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-166：Resource Timing 为什么拿不到跨域资源的耗时细节？TAO 怎么解决？
**答**：
- 出于隐私（时序侧信道可推测资源内容），跨域资源的 Resource Timing 敏感字段被置 0（transferSize、requestStart、responseStart 等）。
- Timing-Allow-Origin（TAO）响应头授权指定来源读取完整时序，等价于 CORS 的"时序版"。
- 同源资源天然全量可读；上报要拿到细粒度数据，就要让 CDN 与静态资源都带上 TAO。
- entry 里还有 nextHopProtocol（h2/h3）与 serverTiming（需服务端配合）可一起上报。

```javascript
// 跨域资源未授权 TAO 时，敏感字段全是 0
const entry = performance.getEntriesByType('resource').find((e) => e.name.includes('cdn.example.com'));
console.log(entry.requestStart); // 0，未配置 Timing-Allow-Origin
// CDN 配置 Timing-Allow-Origin: https://app.example.com 后即可读取
console.log({
  protocol: entry.nextHopProtocol,     // h2 / h3
  dns: entry.domainLookupEnd - entry.domainLookupStart,
  tcp: entry.connectEnd - entry.connectStart,
  ttfb: entry.responseStart - entry.startTime,
  size: entry.transferSize,            // 未授权时也是 0
});
```
