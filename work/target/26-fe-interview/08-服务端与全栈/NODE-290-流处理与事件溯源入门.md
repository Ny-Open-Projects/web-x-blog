---
title: [NODE-290] 流处理与事件溯源入门？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-290：流处理与事件溯源入门？
**答**:
- 事件溯源：状态 = 事件序列的折叠（fold）——DB 不存当前状态只存事件，读时投影（或投影表/快照优化）。
- 收益：天然审计（每个变更都有事件）、时间旅行、天然幂等重建；代价：读模型设计成本、事件 schema 不可变约束。
- CQRS 配套：写侧事件流 → 投影器生成读模型（列表/报表）——读写分离（NODE-196 报表服务的事件驱动版）。
- Node 落地：事件存 Kafka + ES/DB 快照，投影器消费事件更新读模型——中小项目慎用（复杂度高），核心域（账务/库存）可用。

```javascript
// 事件溯源 + 投影（简化）
const events = await eventStore.load('order', orderId);   // 事件流
const state = events.reduce(fold, { status: 'created' });  // 折叠出当前状态
function fold(state, e) {
  switch (e.type) {
    case 'order.paid': return { ...state, status: 'paid', paidAt: e.at };
    case 'order.shipped': return { ...state, status: 'shipped' };
    default: return state;
  }
}
// 投影器（CQRS 读模型）
consumer.run({ eachMessage: async ({ message }) => {
  const e = JSON.parse(message.value);
  await readDb.upsert('order_view', { id: e.data.orderId, status: fold({}, e).status, ...e.data });
}});
```
