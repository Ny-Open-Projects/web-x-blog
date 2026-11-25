---
title: [NODE-178] 设计一个监控告警服务端（时序存储/规则/通知）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-178：设计一个监控告警服务端（时序存储/规则/通知）？
**答**：
- 组成：采集端（push 行协议）→ TSDB（Prometheus/VictoriaMetrics，含降采样）→ **规则引擎**（周期求值 + 防抖状态机）→ 通知路由（NODE-139 分级）。
- 规则状态机：inactive → pending（首次满足）→ firing（持续满足）→ resolved（恢复必须通知，闭环）。
- 告警治理：同服务同规则去重聚合（1 条通知）、静默窗口（发布期间）、恢复通知与触发通知同一链路。
- 采集协议：行协议 `metric{labels} value timestamp`，支持批量压缩上报（NODE-081 思想）。

```javascript
app.post('/api/v1/metrics', async (ctx) => {
  for (const s of ctx.request.body.samples) {       // 批量写入
    await tsdb.insert({ metric: s.name, labels: s.labels, value: s.value, ts: s.ts });
  }
  ctx.status = 204;
});

// 规则引擎：每 30s 求值，pending → firing → resolved 状态机
setInterval(async () => {
  for (const rule of rules) {
    const series = await tsdb.query(rule.expr);     // 如 sum(rate(http_5xx[5m]))
    const active = series.some((s) => s.value > 0);
    const state = await updateAlertState(rule, active); // 防抖：for 持续时长内保持 pending
    if (state === 'firing') {
      await notifier.route(rule.severity, renderAlert(rule, series)); // 去重聚合后通知
    } else if (state === 'resolved') {
      await notifier.route(rule.severity, renderResolved(rule));      // 恢复必须通知
    }
  }
}, 30_000);
// TSDB 分层：10s 原始保留 7 天 → 1min 预聚合 30 天 → 10min 长期归档
```
