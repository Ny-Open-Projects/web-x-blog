---
title: [NODE-561] Node 服务的订单服务（创建/状态机/超时关单）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-561：订单服务
**答**:
- 订单模型：订单主单（金额构成/地址/支付信息快照）+ 明细行（SKU 快照——商品变更不影响历史）+ 拆单规则（多商家拆子单——ARC-645）。
- 创建链路：下单（库存预扣 NODE-557 + 价格计算 NODE-558 + 优惠核销——多服务编排，聚合幂等 NODE-504）→ 订单创建（幂等键——前端重试安全）、超时关单（15min 未支付 → 关单 + 回补——延迟任务 NODE-379）。
- 状态机：待支付 → 已支付 → 发货 → 签收 → 完成；分支：取消/关闭/售后——状态流转条件更新（NODE-412 条件更新防并发跳态：不可从未支付直接完成）。
- 事件驱动：订单状态事件（order.paid/shipped——下游消费：积分/通知/结算 NODE-487 契约）、事件与状态同事务（本地消息表 NODE-380）。
- 查询性能：订单列表（用户维度索引 + cursor 分页）、商家维度（商家订单索引——双维度冗余或异构索引）、订单详情聚合（订单服务单源——不依赖商品实时数据，用快照）。
```javascript
// 下单编排（幂等）
async function createOrder(idemKey, cmd) {
  const hold = await stock.hold(cmd.sku, cmd.qty, idemKey);      // 预扣（幂等）
  const price = await price.calc(cmd, { coupons: cmd.coupons }); // 价格快照
  const order = await orderRepo.create({ ...cmd, price, idemKey }); // 幂等创建
  scheduleClose(order.id, 15 * 60e3);                            // 超时关单
  await outbox('order.created', order);                          // 事件
  return order;
}
// 关单：sm transition pending→closed + stock.release + coupon.return —— 全幂等
```
