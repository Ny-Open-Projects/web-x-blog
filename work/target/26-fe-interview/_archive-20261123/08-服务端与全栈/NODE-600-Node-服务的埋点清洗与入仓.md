---
title: [NODE-600] Node 服务的埋点清洗与入仓（数据质量防线）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-600：埋点清洗入仓
**答**:
- 链路：端上埋点（ARC-535 协议）→ 接收网关（schema 校验——坏数据拒绝+计数，ARC-424）→ 清洗管道（去重（事件 ID/端上重发）、字段归一（时间戳统一 UTC/枚举校验）、补维度（登录态/地域/灰度标签——网关 join）、脱敏（PII 字段——NODE-396））→ 入仓（明细表分区——事件分区设计按天）。
- 质量防线：各环节质量指标（校验失败率/去重率/补维度成功率——数据健康看板）、坏数据隔离区（拒收数据暂存——修复后回补）、端版本兼容（老版本事件 schema——兼容解析窗口声明）。
- 入仓设计：事件明细宽表 vs 事件流（明细表按事件类型分域——分析友好；原始流保留——回溯重放）、分区与生命周期（TTL——存储成本 ARC-531）、幂等写入（事件 ID 主键——重复入仓防）。
- 消费质量：下游对账（上游量 vs 入仓量——断链检测 NODE-424）、schema 变更通知（事件 schema 变更 → 消费方通知——ARC-447 思想）。
```javascript
// 接收网关清洗管道
gateway.use(async (events) => {
  const valid = events.filter(e => schema.ok(e));                // 校验（失败计数+隔离区）
  return valid.map(e => enrich(dedupe(sanitize(normalize(e))))); // 清洗：去重/脱敏/归一/补维度
}).pipe(warehouse.write, { partitionBy: 'day', idempotent: 'eventId' });
```
