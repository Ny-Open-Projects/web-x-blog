---
title: [NODE-289] 事件驱动架构的领域事件设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-289：事件驱动架构的领域事件设计？
**答**:
- 事件设计三原则：自包含（payload 带齐消费所需数据，或带 id 让消费方回查）、可版本化（schema 版本字段，向后兼容演进）、可追溯（eventId/traceId/correlationId）。
- 事件命名：过去时领域事实（order.paid / user.registered）——事件是"已发生的事实"不是命令。
- schema 治理：事件 schema 注册表（JSON Schema）+ 兼容性检查（新增可选字段 OK，删字段/改语义需大版本）。
- 消费耦合控制：消费者只依赖 schema 不依赖生产者代码——契约测试（ARC-214 同款思想）。

```typescript
// 领域事件契约
interface OrderPaidEvent {
  eventId: string;            // 幂等键
  traceId: string;            // 链路（NODE-36x）
  type: 'order.paid';
  version: 2;                 // schema 版本
  occurredAt: string;
  data: { orderId: string; userId: string; amount: number; payMethod: string };
}
// 兼容演进：v2 加 payMethod（可选）；消费端按 version 分支处理
// 发布：outbox → Kafka topic: order-events（key=orderId 保序）
```
