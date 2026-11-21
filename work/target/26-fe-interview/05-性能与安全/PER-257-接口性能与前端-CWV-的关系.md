---
title: [PER-257] 后端接口慢如何传导到 CWV？前端怎么区分"网络慢"还是"服务端慢"？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-257：后端接口慢如何传导到 CWV？前端怎么区分"网络慢"还是"服务端慢"？

**答**：
- 传导路径：接口慢 → 首屏数据晚到 → LCP 元素（图/文案）晚渲染 → LCP 差；接口阻塞注水/交互初始化 → INP 差。CSR 里接口是 LCP 的前置依赖，SSR 里接口直接决定 TTFB。
- 拆解方法（Resource Timing）：一次请求的 `responseStart - requestStart` 是网络往返 + 服务端处理总和；要区分二者需服务端在响应头里回写 `Server-Timing: db;dur=120, app;dur=45`，前端从 Resource Timing 的 `serverTiming` 字段直接读出——服务端耗时与网络耗时分离。
- 前端职责边界：拿到拆解后，服务端慢推给后端（附 Server-Timing 证据），网络慢找 CDN/缓存策略；前端自己能做的是并行请求、预取、流式渲染，让"接口慢"不再串行阻塞首屏。
- 监控口径：接口维度单独出 p75（服务端耗时 + 前端可用时间），与 CWV 指标关联分析（慢接口 Top 与慢页面 Top 的交集就是元凶）。

```javascript
// 读 Server-Timing，拆分服务端与网络耗时
const res = performance.getEntriesByType('resource')
  .find(r => r.name.includes('/api/goods'));
if (res) {
  const network = Math.round(res.responseStart - res.requestStart);
  const server = res.serverTiming?.reduce((s, t) => s + t.duration, 0) ?? 0;
  report({ api: '/api/goods', network, server, total: Math.round(res.duration) });
  // server 占比 > 60% => 服务端问题；network 大且 server 小 => CDN/线路问题
}
// 服务端配合：response headers 加
// Server-Timing: db;dur=120, app;dur=45, total;dur=165
```
