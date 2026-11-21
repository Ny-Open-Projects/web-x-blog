---
title: [NODE-065] 生产环境如何监控 Node 进程（指标与慢查询定位）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-065：生产环境如何监控 Node 进程（指标与慢查询定位）？
**答**：
- 核心指标：**事件循环延迟**（`perf_hooks.monitorEventLoopDelay`，>100ms 说明主线程被阻塞）、CPU 使用率、堆内存（`process.memoryUsage()` 的 heapUsed/rss，接近 `--max-old-space-size` 预警）、GC 暂停（`perf_hooks` PerformanceObserver gc）、句柄数（`process._getActiveHandles`）。
- 采集方案：`prom-client` 暴露 `/metrics`（Prometheus 格式）+ Grafana 看板 + 告警规则；APM（阿里 ARMS、Datadog、SkyWalking）看接口级 trace。
- 慢查询定位：接口内部打点（`server-timing` 响应头 + 日志耗时字段）→ 区分"下游慢"还是"自身计算慢"→ 事件循环延迟高则查同步大计算/大 JSON 序列化。

```javascript
const { monitorEventLoopDelay, performance, PerformanceObserver } = require('node:perf_hooks');
const client = require('prom-client');
const register = new client.Registry();
client.collectDefaultMetrics({ register });

// 1. 事件循环延迟采样
const loopDelay = monitorEventLoopDelay({ resolution: 10 });
loopDelay.enable();
setInterval(() => {
  const p99 = loopDelay.percentile(99) / 1e6; // ns → ms
  if (p99 > 100) {
    console.warn(JSON.stringify({ event: 'loop_blocked', p99_ms: p99,
      heap: process.memoryUsage().heapUsed / 1e6 }));
  }
  loopDelay.reset();
}, 10000).unref();

// 2. GC 观察
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 50) {
      console.warn(JSON.stringify({ event: 'long_gc', kind: entry.kind, ms: entry.duration }));
    }
  }
}).observe({ entryTypes: ['gc'] });

// 3. Prometheus 指标
const httpDuration = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: '请求耗时分布',
  labelNames: ['method', 'route', 'status'],
  buckets: [0.01, 0.05, 0.1, 0.3, 0.5, 1, 3],
});
register.registerMetric(httpDuration);

app.use(async (ctx, next) => {
  const end = httpDuration.startTimer();
  try { await next(); }
  finally { end({ method: ctx.method, route: ctx._matchedRoute || 'unknown', status: ctx.status }); }
});
app.get('/metrics', async (ctx) => { ctx.body = await register.metrics(); });
```
