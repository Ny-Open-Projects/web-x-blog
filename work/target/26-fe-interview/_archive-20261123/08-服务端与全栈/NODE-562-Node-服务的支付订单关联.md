---
title: [NODE-562] Node 服务的支付-订单关联（多订单合并支付/部分支付）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-562：支付订单关联
**答**:
- 支付单模型：支付单（payNo）与订单多对一（购物车合并支付——一个支付单关联 N 订单）或一对一；支付单金额 = 订单合计（分摊回各订单——分摊记录可追溯）。
- 状态协调：支付成功 → 所有关联订单联动（批量状态更新——事务内 + 事件分发）、部分失败处理（合并支付成功但某订单库存失效——退款该子单差额或整单处理——业务规则显式）。
- 多次支付：部分支付场景（定金+尾款——支付计划：多次支付节点，各节点独立支付单——尾款超时处理规则）、补差价（价格变动补差——追加支付单关联原单）。
- 幂等与查单：支付回调幂等（渠道单号唯一）、查单对齐（渠道状态 vs 本地状态机——对账修复任务 ARC-382）、关单联动（订单关闭 → 未支付支付单关单——防漏关被"碰巧支付"）。
- 边界：支付单金额与订单金额不一致的校验（回调金额校验——金额不符告警人工——防"0.01 元支付成功"漏洞）。
```javascript
// 支付成功联动
bus.on('pay.succeeded', async (pay) => {
  const orders = await payRepo.linkedOrders(pay.payNo);
  verifyAmount(pay, orders);                                     // 金额校验
  await db.tx(t => orders.forEach(o => orderRepo.markPaid(o.id, pay.payNo, t))); // 批量状态同事务
  orders.forEach(o => outbox('order.paid', o));                  // 事件分发
});
```
