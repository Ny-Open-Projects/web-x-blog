---
title: [NODE-713] 事件驱动架构（事件溯源轻量版）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-713：事件驱动怎么做？
**答**：
- 事件模型：领域事件（业务语义命名——OrderPaid 而非 update_order）、事件不可变（append-only——审计天然满足，SCN-OPS-271 事件溯源）、事件 schema 版本化（消费者按版本兼容）。
- 轻量事件溯源：事件表（append-only）+ 投影（读模型从事件推导——报表/查询视图独立重建）；完整溯源（重放历史）按需——不是所有系统都要全量溯源。
- 消费模型：订阅投影（各自消费事件建读模型——读写分离的 CQRS 轻量版）+ 重放能力（读模型坏了从事件重建——自愈数据）。
- 一致性：写路径事件表与业务同事务（SCN-NODE-653 outbox）、投影最终一致（延迟标注——SCN-OPS-675 健康度）。
- 追问钩子：为什么事件驱动里「事件 schema 版本化」最容易漏——事件被多消费者订阅（v1 消费者解析 v2 事件——字段缺失崩溃）；事件 schema 加字段向后兼容（消费者忽略未知字段）+ breaking 变更发新事件类型（OrderPaidV2）——事件是不可变的，schema 演进靠「新增类型」而非「修改旧事件」。

```javascript
// 事件表（append-only）
await tx.insert('events', { type: 'OrderPaid.v2', payload, occurredAt });
// 投影重建（读模型自愈）
function rebuildProjection() {
  events.forEach(applyToProjection);                   // 全量重放（SCN-OPS-271 时间旅行）
}
// 消费者兼容（v2 事件新字段可选）
const { couponId, couponIdV2 = couponId } = payload;   // 向后兼容
```
