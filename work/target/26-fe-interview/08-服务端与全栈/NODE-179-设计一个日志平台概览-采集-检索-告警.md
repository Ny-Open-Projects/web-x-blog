---
title: [NODE-179] 设计一个日志平台概览（采集/检索/告警）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-179：设计一个日志平台概览（采集/检索/告警）？
**答**：
- 架构：业务日志（pino JSON，NODE-133）→ **采集端**（tail 文件 + offset 断点 + 批量压缩，NODE-081）→ 消息队列（削峰解耦）→ 索引集群（ES/Loki）→ 检索/告警。
- 采集端可靠性：offset 落盘，上游确认后才推进——不丢不重；应用与采集解耦（写本地文件比直发远端稳）。
- 检索层：按 service+日期 分索引；traceId 做等值查询加速；Kibana/Loki 前端给排查用。
- 成本与治理：热 7 天 SSD → 温 30 天 HDD → 冷归档；字段裁剪在采集端完成；错误日志 rate 直接接告警（复用 NODE-178 规则引擎）。

```javascript
// 采集端核心：tail + checkpoint + 批量
const shipper = createShipper({
  paths: ['/var/log/bff/access.log'],
  batchSize: 500,
  flushMs: 2000,
  compress: 'zstd',
  checkpoint: '/data/offset.json',     // 断点续传：重启从 offset 继续
});
shipper.on('batch', async (batch) => {
  await mq.publish('logs.raw', batch); // 经 MQ 削峰，索引集群故障不阻塞业务
  shipper.commit(batch.lastOffset);    // 上游确认后才推进 offset → 不丢不重
});
// 检索：GET /logs?q=traceId:xxx AND level:error&from=7d
// 告警：error 日志 rate > 阈值 → NODE-178 规则引擎 → NODE-139 分级通知
```
