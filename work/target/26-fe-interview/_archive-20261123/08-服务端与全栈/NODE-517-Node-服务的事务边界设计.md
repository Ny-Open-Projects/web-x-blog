---
title: [NODE-517] Node 服务的事务边界设计（该多大才对）如何判断？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-517：事务边界设计
**答**:
- 原则：事务尽量小（锁持有短/回滚范围小）但覆盖一个完整不变量（转账两步必须同事务——拆开就不一致 NODE-412）。边界判断：一个聚合根的一致性操作 = 一个事务（DDD 聚合边界）。
- 事务内禁止：外部调用（HTTP/MQ 发送——拉长事务 + 不确定时长 NODE-412 悲观锁红线）、复杂计算（先算后写）、超长循环（分批事务）。外部副作用用"事务后动作"（本地消息表 NODE-380/事务提交后钩子——afterCommit）。
- 跨聚合事务：单服务跨聚合 → 业务上重新审视（同一事务跨聚合 = 聚合划分可能错）；跨服务 → saga/最终一致（NODE-380）。
- 隔离级别选择：默认 RC（MySQL RR 的间隙锁坑——高并发场景 RC 更稳）、需要串行语义用显式锁（select for update）而不是升隔离级别（可预测性更好）。
- 实践约束：事务超时设置（statement/transaction timeout——防悬挂 NODE-332）、重试框架（死锁/序列化失败自动重试——幂等前提下）。
```javascript
// 事务边界：聚合级 + afterCommit
await db.tx(async (t) => {
  await orderRepo.markPaid(id, payNo, t);                        // 聚合内一致
  await ledger.recordPayment(t, { id, payNo });                  // 同聚合关联账
  tx.afterCommit(() => outbox.enqueue('order.paid', { id }));     // 事务外副作用
}); // 外部调用（短信/缓存失效）全部 afterCommit——不在锁内
```
