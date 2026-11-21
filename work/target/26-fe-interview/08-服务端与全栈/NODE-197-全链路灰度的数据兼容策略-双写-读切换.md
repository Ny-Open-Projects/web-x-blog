---
title: [NODE-197] 全链路灰度的数据兼容策略（双写/读切换）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-197：全链路灰度的数据兼容策略（双写/读切换）？
**答**：
- 演进三阶段：**双写过渡**（旧表权威 + 新表影子写，异步比对差异）→ **读灰度切换**（按规则读新表，失败回退旧表）→ **收尾**（读全量后停旧表写，观察一个周期归档）。
- schema 纪律：字段只增不删、新字段可空、枚举扩展前向兼容——保证灰度/稳定两组实例能同时读写同一份数据。
- 回退能力是底线：任何阶段出问题都能秒级切回（染色规则改回 stable 即可，NODE-176）。
- 数据校验：双写期 diff 任务全量比对，差异入库修复后再切读，不允许"带着未知差异切流量"。

```javascript
// 阶段一：双写（旧表权威，新表影子）
async function createOrderV2(order) {
  await db.$transaction([
    db.order.create({ data: toV1(order) }),      // 旧表：权威数据源
    db.orderV2.create({ data: toV2(order) }),    // 新表：影子写
  ]);
  diffJob.record(order.id, toV1(order), toV2(order)); // 异步比对，差异入库供修复
}

// 阶段二：读灰度切换（按 tint 规则，失败回退）
async function getOrder(id, { tint }) {
  if (tint === 'gray-v2') {
    const v2 = await db.orderV2.findUnique({ where: { id } }).catch(() => null);
    if (v2) return fromV2(v2);                   // 读新表
  }
  return db.order.findUnique({ where: { id } }); // 回退旧表
}
// 阶段三：diff 归零 + 观察一个周期 → 停旧表写 → 归档；全程可秒级回退
```
