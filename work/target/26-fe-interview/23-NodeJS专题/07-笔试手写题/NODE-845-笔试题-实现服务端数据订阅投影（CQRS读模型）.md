---
title: [NODE-845] 笔试题——实现 CQRS 读模型投影（事件→查询视图）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-845：手写读模型投影

**需求与边界**：
- 需求：CQRS 投影（SCN-NODE-713）——① 事件消费建投影（事件 → 查询视图——读模型）；② 重放重建（投影损坏 → 全量重建——SCN-NODE-713 自愈）；③ 投影延迟标注（查询带 freshness——SCN-联想-675）；④ 投影版本（schema 变更——SCN-OPS-646 迁移）。
- 边界：① 投影与主库的一致性（最终一致——SCN-NODE-654 BASE）；② 重放的成本（全量重放耗时——后台任务，SCN-NODE-667）；③ 投影查询的路由（读模型查询入口——SCN-NODE-706 读写分离联动）。

**答**：
```javascript
// 事件消费 → 投影（SCN-NODE-713）
consumer.on('order.paid', async (e) => {
  await projection.upsert('sales_by_day', { day: dayOf(e.ts), amount: e.amount }, { incr: e.amount });
  await projection.upsert('user_orders', { userId: e.userId }, { push: e.orderId });
});
// 重放重建（自愈——SCN-NODE-713）
async function rebuildProjection(name) {
  await projection.clear(name);
  await db.streamEvents(name, async (events) => {      // 全量重放（后台任务——SCN-NODE-667）
    events.forEach(applyToProjection);
  }, { progress: (p) => report(p) });
  markProjectionFresh(name);
}
// 查询带 freshness（SCN-联想-675）
app.get('/stats/sales', async (req, res) => {
  const data = await projection.query('sales_by_day', req.query);
  res.json({ ...data, freshness: projection.lag(name) });   // 延迟标注
});
```

**评分点**:
- 事件消费建投影（SCN-NODE-713 CQRS 轻量版）。
- 重放重建自愈（SCN-NODE-713）。
- freshness 延迟标注（SCN-联想-675 陈旧可见）。
- 投影版本迁移（SCN-OPS-646）。
