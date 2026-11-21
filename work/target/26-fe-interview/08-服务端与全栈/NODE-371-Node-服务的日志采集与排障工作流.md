---
title: [NODE-371] Node 服务的日志采集与排障工作流如何搭建？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-371：日志采集与排障工作流
**答**:
- 采集链路：应用 stdout JSON（pino）→ 采集器（Filebeat/vector sidecar 或 stdout 收集）→ Kafka → ES/ClickHouse → 查询界面。应用只管输出，不管落盘与轮转（容器最佳实践）。
- 排障工作流标准化：从告警/用户报障 → 拿 reqId/traceId → 日志平台查全链路（BFF → 下游每跳都有 traceId，NODE-291）→ 定位服务与接口 → 结合 trace 瀑布找慢点。目标是"一次查询定位"而不是"多台机器 grep"。
- 查询体验建设：常用查询模板（按 reqId/uid/接口）、错误日志聚合视图（指纹聚合，ARC-358）、日志与 trace 跳转互通（日志带 trace 链接，trace span 带日志链接）。
- 保留策略：错误日志 90 天、访问日志 14 天热 + 冷归档；成本与合规（ARC-356）。
- 质量守护：日志 schema 校验（坏行进死信），traceId 覆盖率监控（没 traceId 的日志=排障黑洞）。
```javascript
// 排障入口：reqId 全链路
async function debug(reqId) {
  const logs = await logQuery({ 'reqId': reqId });               // BFF 内日志
  const trace = await traceQuery({ traceId: logs[0].traceId });  // 全链路瀑布
  return { logs, waterfall: trace.spans, slowest: trace.slowestSpan() };
}
```
