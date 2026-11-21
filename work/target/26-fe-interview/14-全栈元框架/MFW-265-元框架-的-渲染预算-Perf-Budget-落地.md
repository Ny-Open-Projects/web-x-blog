---
title: [MFW-265] 元框架的渲染预算落地（TTFB/Payload/DB 时间分账）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-265：渲染预算分账

**答**:
- 分账模型：TTFB = 路由决策+middleware(≤10ms) + RSC 渲染 DB 时间（P95 预算按路由）+ 序列化与网络——每段独立埋点才能归因（全塞一个 number 无法优化）
- 采集：renderSpan 包 RSC 树（开始/结束/attrs: 路由/dbMs/payloadBytes）→ OTel——与构建遥测同一后端（RBL-437 复用）
- 预算执行：P95 超路由预算 → 门禁级告警（不是看板看看——回归阻塞合流，接 CI 性能快照）
- 分层预算示例：营销页 TTFB≤300ms（全静态命中）｜列表页 ≤600ms（DB ≤200）｜搜索 ≤900ms——预算表进代码（常量+测试断言）

```javascript
// 渲染 span 与预算断言
const { stop } = startRenderSpan(route)            // attrs: dbMs/payload
const r = await renderApp()
stop()
expect(r.dbP95).toBeLessThan(BUD[rowte].dbMs)      // CI 性能快照断言（RBL-469 同款）
```
