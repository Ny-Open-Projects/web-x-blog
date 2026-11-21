---
title: [WEB-471] 首页 TTFB 突然变慢的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-471：首页 TTFB 突然变慢的排查 SOP

**答**：
- 拆解 TTFB 四段：DNS → TCP/TLS → 服务端处理 → 首字节回传；用 Navigation Timing 逐段对比基线，先锁定慢在哪一段
- DNS 段变慢：DNS 服务商故障、CNAME 链新增一跳、解析 TTL 为 0；换公共 DNS 验证 + dig 看链路
- 连接段变慢：证书链不完整（客户端额外拉中间证书）、TLS 版本协商回退、机房故障导致就近调度失效
- 服务端段变慢：后端慢查/缓存穿透（配合 APM）、HTML 动态渲染变慢（发布后新增同步调用）；静态站看 CDN 是否回源（X-Cache: MISS 比例飙升）
- 拨测对比：多地域多运营商拨测 + 真实用户 RUM 分位数，排除「只在我机器上慢」

```javascript
const nav = performance.getEntriesByType('navigation')[0];
console.table({
  dns: nav.domainLookupEnd - nav.domainLookupStart,
  tcp_tls: nav.connectEnd - nav.connectStart,
  server: nav.responseStart - nav.requestStart,
});
```
