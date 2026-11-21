---
title: [NODE-614] Node 服务的领域事件落地（进程内事件 vs 跨进程事件）如何选择？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-614：领域事件落地选择
**答**:
- 两种事件：进程内事件（EventEmitter/内存总线——同进程模块解耦）、跨进程事件（MQ 领域事件——跨服务集成 ARC-080/487）。选择：消费方在别进程 → MQ；同进程 → 进程内（简单，无序列化成本）。
- 进程内事件语义：同步 vs 异步（同步监听器：调用方等待——事务内副作用；异步（setImmediate）：不阻塞主流程——失败不回滚业务，需补偿语义）、事务边界（事务内发的事件——afterCommit 才分发，防"事件先于提交"NODE-380/517）。
- 跨进程事件一致性：本地消息表保证发布可靠（NODE-380）、消费幂等（NODE-488）。
- 防滥用：事件不是万能解耦（隐式依赖难追踪——事件链可视化需求）、监听器错误隔离（一个监听器炸不炸其他——错误收集）、监听器泄漏（重复注册——生命周期管理 NODE-466）。
- 演进：进程内事件迁移跨进程（同一事件模型——平滑升级：先进程内聚合，规模大了拆 MQ）。
```javascript
// 事务内事件（afterCommit 语义）
bus.onTransactional('order.paid', (o) => grantPoints(o));        // 事务提交后分发
async function markPaid(order) {
  await db.tx(t => { update; bus.deferEmit('order.paid', order, t); }); // defer：提交后才发
}
// 进程内异步监听器错误隔离：Promise.allSettled(handlers.map(h => h(e)))
```
