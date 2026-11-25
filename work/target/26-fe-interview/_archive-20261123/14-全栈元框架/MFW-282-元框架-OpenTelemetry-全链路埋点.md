---
title: [MFW-282] 元框架 OTel 全链路埋点（middleware→RSC→Action→DB）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-282：OTel 全链路埋点

**答**:
- Span 树设计：request(root, route) → middleware / render(route) → fetch(db, table) / action(name) → db.stmt——每层带属性（route/user.role/缓存命中）供下钻
- 自动化优先：框架/驱动自带 instrumentation（@next/otel、pg instrumentation）注册于 MFW-281 的 register——手写只补业务 span（如「渲染报价计算」）
- 采样策略：头请求全采样 + 尾采样按错误/慢聚合（全量成本高——错误与慢样本是价值密度最高处）
- 跨层串联：W3C traceparent 从浏览器发起（客户端 SDK 生成）→ server 全程透传——前端点击到 DB 行的一条线

```javascript
// register 里注册自动 instrumentation
registerInstrumentations({
  instrumentations: [new undiciInstrumentation()/* fetch */, new pgInstrumentation()/* DB */],
})
// 业务 span
const s = tracer.startSpan('quote.calc', { attributes: { route })
try { ... } finally { s.end() }
```
