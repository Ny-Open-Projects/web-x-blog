---
title: [NODE-379] Node 服务的延迟任务（定时触发/超时取消）实现方案有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-379：延迟任务的实现方案
**答**:
- 场景：订单 30 分钟未支付取消、预约提醒、冷却期解锁。方案谱系：BullMQ delayed job（毫秒级精度、Node 生态首选）、Redis ZSET 轮询（score=执行时间，扫描到期任务，精度秒级、实现简单）、MQ 延迟消息（RocketMQ 延迟等级）、DB 轮询（定时扫表，量大时效率低但可靠）。
- 关键设计：延迟任务必须是"可验证的"——到期执行前检查前置条件（订单已支付则跳过取消）；执行幂等（重复触发不双扣）；取消支持（支付成功删掉延迟任务或靠状态检查短路）。
- 精度与规模权衡：万级任务 BullMQ 足够；亿级用时间轮/分桶 ZSET（按小时分桶，桶内秒级扫描）。
- 补偿：调度器宕机漏触发——对账兜底（每日扫"应取消未取消"订单，ARC-324）；延迟任务的可靠性靠"最终对账"而不是"绝对准点"。
- 可观测：到期未执行数（积压）、延迟误差分布告警。
```javascript
// BullMQ 延迟取消
await queue.add('cancel-order', { orderId }, {
  delay: 30 * 60e3, jobId: `cancel:${orderId}` });             // 30 分钟后执行
// 支付成功：const job = await queue.getJob(`cancel:${orderId}`); await job?.remove();
// worker 内短路：if (await order.isPaid(orderId)) return;     // 状态检查幂等
```
