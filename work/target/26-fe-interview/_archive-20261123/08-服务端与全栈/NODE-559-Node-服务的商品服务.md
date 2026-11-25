---
title: [NODE-559] Node 服务的商品服务（SPU/SKU/上下架）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-559：商品服务
**答**:
- 模型：SPU（商品）× SKU（规格实例——价格/库存/条码挂 SKU）、类目/属性（类目属性驱动筛选 ARC-650——属性 schema 版本化）、多语言商品（跨国——内容多语言字段）。
- 上下架与状态：商品状态机（草稿/在售/下架/冻结——下架联动：搜索索引/缓存/前端可见性）、定时上下架（预约任务 NODE-379）、违规下架（风控/合规——下架原因与申诉）。
- 变更传播：商品变更事件（改名/改图/下架——下游失效：缓存 NODE-507/搜索索引 NODE-387/购物车价格重算）——事件契约（NODE-487）。
- 查询性能：详情缓存（ARC-617 静态骨架）、列表检索（ES——商品索引同步 CDC）、批量接口（购物车/订单回填——batch get + 缓存）。
- 一致性：SKU 级操作幂等（改价幂等——版本号条件更新）、商品与订单快照解耦（订单存快照——商品后续变更不影响历史订单）。
```javascript
// 商品状态机 + 变更事件
async function offShelf(spuId, reason) {
  await db.tx(async (t) => {
    const r = await t.query(`update spu set state='off' where id=$1 and state='on'`, [spuId]);
    if (!r.rowCount) throw new StateConflict();
    await outbox(t, 'goods.offshelved', { spuId, reason });      // 同事务事件：缓存/索引失效
  });
}
```
