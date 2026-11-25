---
title: [NODE-135] metrics 指标如何设计（RED 方法）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-135：metrics 指标如何设计（RED 方法）？
**答**：
- RED 三件套：**Rate**（每秒请求数）、**Errors**（错误率）、**Duration**（耗时分布）——服务健康的最小完备集。
- prom-client：Counter（只增）、Histogram（桶分布，算 P99）、Gauge（瞬时值）；`collectDefaultMetrics` 白送进程级指标（heap/GC/事件循环 lag）。
- 标签纪律：route 必须用**路由模板**（`/user/:id`）而非真实路径，否则标签基数爆炸打爆 TSDB。
- 告警三件套：QPS 跌 50% → 流量异常；5xx 率 > 1% → 错误告警；P99 超 SLO 持续 5 分钟 → 慢告警（NODE-139 分级）。

```javascript
const client = require('prom-client');
const register = new client.Registry();
client.collectDefaultMetrics({ register }); // 进程级：heap、eventloop lag、GC

// RED - R 与 E：Counter
const httpTotal = new client.Counter({
  name: 'http_requests_total', help: 'total requests',
  labelNames: ['method', 'route', 'status'],
  registers: [register],
});
// RED - D：Histogram 分桶
const httpDuration = new client.Histogram({
  name: 'http_request_duration_seconds', help: 'latency',
  labelNames: ['method', 'route'],
  buckets: [0.01, 0.05, 0.1, 0.3, 0.5, 1, 3],
  registers: [register],
});

app.use(async (ctx, next) => {
  const route = ctx.routerPath || 'unmatched'; // 模板而非真实路径！
  const end = httpDuration.startTimer({ method: ctx.method, route });
  try { await next(); }
  finally {
    httpTotal.inc({ method: ctx.method, route, status: ctx.status });
    end();
  }
});
// /metrics 端点供 Prometheus 抓取
```
