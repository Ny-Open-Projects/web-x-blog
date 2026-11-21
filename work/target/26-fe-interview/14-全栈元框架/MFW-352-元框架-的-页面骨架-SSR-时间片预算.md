---
title: [MFW-352] SSR 时间片预算（每路由的渲染 CPU 约束）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-352：SSR 时间片预算

**答**:
- 模型：给每路由声明 CPU 预算（营销 5ms/列表 20ms/报表 200ms——超预算路由属「批处理」应出 SSR 池）——预算表驱动容量计算（MFW-284 公式的输入）与告警分母
- 执行：renderSpan 实测 CPU（process.cpuUsage 差分——挂路由属性）→ 超限路由两级处置（dev 警告+profile 建议链 / prod 自动降级到轻量变体或排入异步段）
- 与 DB 预算解耦：CPU 预算≠DB 预算（IO 等待不占 CPU）——两张表分开治理（N+1 是 DB 病，深组件树是 CPU 病，归因别混）
- 用途闭环：预算表同时是「容量公式输入」「告警阈值」「新路由评审单字段」——一表三用

```javascript
const CPU_BUDGET = { '/': 5, '/list': 20, '/report': null }   // null=禁入 SSR 池
const span = startRouteSpan(route)                            // cpuUsage 差分入 attrs
// 超限：dev=warn+profile 链接；prod=轻量变体或移异步段（SUSPENSE 后台化）
```
