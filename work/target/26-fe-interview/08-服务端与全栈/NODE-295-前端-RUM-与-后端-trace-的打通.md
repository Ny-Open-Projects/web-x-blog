---
title: [NODE-295] 前端 RUM 与后端 trace 的打通？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-295：前端 RUM 与后端 trace 的打通？
**答**:
- 打通点：前端 RUM SDK 生成 traceparent（页面加载/每次请求）→ 后端 OTel 接收并续链——从"LCP 慢"直接下钻到"哪个接口哪个下游慢"。
- 页面级 trace：页面加载作为一个 trace，JS 错误/资源失败作为 span 事件——前后端一棵树。
- 实现路径：浏览器端用 OTel JS（重）或轻量自实现 W3C 头（采样率低、只传头）；CDN/网关在响应头回传 traceId 供前端上报关联。
- 收益量化：前端问题归因时间从"猜测"到"链路直查"——MTTR 显著下降。

```javascript
// 轻量前端 trace 透传
const traceId = crypto.randomUUID().replaceAll('-', '');
fetch('/api/aggregate', { headers: {
  traceparent: `00-${traceId}-${crypto.randomUUID().replaceAll('-', '').slice(0, 16)}-01`,
}});
// 响应头回传：
// res.setHeader('x-trace-id', traceId) → 前端上报 RUM 时关联：
report('webvital', { lcp, traceId });   // 平台侧：traceId 关联后端 trace 树 → 下钻
```
