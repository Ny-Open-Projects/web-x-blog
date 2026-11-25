---
title: [NODE-504] Node 服务的聚合接口幂等（一次请求多个下游写）如何保证？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-504：聚合接口幂等
**答**:
- 场景：BFF 一个接口触发多个下游写（下单 → 创建订单 + 扣库存 + 加积分）——重试/重放时多下游要整体幂等（部分成功后重试不能重复扣）。
- 实现模式一：聚合幂等键派生（NODE-476：根键派生子调用键——每个下游调用带派生键，重放时各下游各自幂等）。
- 模式二：状态化编排（聚合操作记录状态表：各子调用状态——重放时只补未完成的子调用，已完成的跳过；类似 saga 重放 NODE-380）。
- 模式三：事务边界下沉（尽量把多写收进一个下游服务的事务——BFF 只触发一次调用；BFF 跨服务编排是不得已，能一个事务不拆）。
- 部分失败补偿：编排中途失败 → 补偿已完成的子调用（saga 逆序）或标记待补偿（对账兜底 ARC-382）——补偿本身幂等。
- 验证：重放测试（第一轮模拟第二步失败 → 重放同键 → 断言无重复扣减 + 最终一致）。
```javascript
// 状态化聚合编排
async function createOrderAgg(idemKey, cmd) {
  const rec = await steps.load(idemKey);                         // {created?, stocked?, points?}
  if (!rec.created) rec.created = await orderSvc.create(k(idemKey, 'c'), cmd);
  if (!rec.stocked) rec.stocked = await stockSvc.deduct(k(idemKey, 's'), cmd.sku);
  if (!rec.points)  rec.points  = await pointsSvc.add(k(idemKey, 'p'), cmd.uid);
  return rec;                                                    // 重放只补未完成步骤
}
```
