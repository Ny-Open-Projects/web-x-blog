---
title: [NODE-653] 分布式事务（Saga/TCC/最终一致）怎么选？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-653：分布式事务怎么选？
**答**：
- 优先降级：能用「单库事务 + 唯一资源」就不用分布式事务——拆分边界让强一致变成局部一致（架构解法优于协议）。
- Saga：长流程编排（每步本地事务 + 补偿动作）——编排式（中心 orchestrator）vs 协同式（事件驱动各自响应）；补偿必须幂等且可重试；适合流程长、隔离性要求低的（下单→扣库存→扣款）。
- TCC：Try-Confirm-Cancel 三段（资源预留语义）——强一致但每参与方实现三接口（复杂度高），适合资金类短事务。
- 最终一致（事务消息/本地消息表）：本地事务写业务 + 消息表 → 定时/半消息投递——最简单最常用（牺牲实时性换可靠性）；对账兜底（SCN-867 对账体系）。
- 追问钩子：为什么「本地消息表」比「事务消息中间件」更常被推荐——本地消息表用 DB 事务保证「业务写入与消息写入原子」（任何 DB 都支持），不依赖 MQ 的事务消息特性（RocketMQ 专有）；缺点是轮询投递（秒级延迟）——大多数场景「简单可靠」胜过「高级但不通用」，且对账兜底覆盖残余。

```javascript
// 本地消息表
await db.transaction(async (tx) => {
  await tx.insert('orders', order);
  await tx.insert('outbox', { topic: 'order.created', payload: order });   // 同事务写消息
});
// 定时扫描 outbox 投递（投递成功标记）
cron('*/5s', () => outboxDispatcher.flush());
```
