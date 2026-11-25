---
title: [NODE-372] Node 服务的指标体系（RED/USE）与 SLO 如何建立？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-372：Node 服务的指标体系与 SLO
**答**:
- RED（面向用户）：Rate（QPS 按路由）、Errors（错误率分类型：业务错/系统错分开）、Duration（P50/P95/P99 直方图）；USE（面向资源）：Utilization/Saturation/Errors（CPU、内存、事件循环延迟、连接池占用、GC 停顿）。
- 指标采集：prom-client（histogram 按路由打标注意基数爆炸——路由参数归一化 /goods/:id 而非具体 id）；/metrics 暴露 + Pull 模式；运行时指标（Node 默认 GC/heap 指标）。
- SLO 定义（ARC-354 服务端版）：可用性（非 5xx 占比 99.9%）、延迟（P99 < 500ms）、新鲜度（MQ lag < 30s）；错误预算驱动发布冻结决策。
- 关键联动：指标带版本与灰度标签（NODE-370）、与前端 RUM 指标对齐（接口 P95 与前端等待体感一致）。
- 告警基于 SLO 燃烧率而非绝对阈值（快速燃烧告警，慢速燃烧进日报）。
```javascript
const client = require('prom-client');
const hist = new client.Histogram({ name: 'http_duration_seconds', help: 'req dur',
  buckets: [0.05, 0.1, 0.3, 0.5, 1, 3],
  labelNames: ['route', 'method', 'status', 'gray'] });          // route 归一化防基数爆炸
app.use(async (ctx, next) => {
  const t = Date.now();
  await next();
  hist.observe({ route: normalize(ctx.path), method: ctx.method,
    status: ctx.status, gray: ctx.state.gray ?? 'stable' }, (Date.now() - t) / 1000);
});
```
