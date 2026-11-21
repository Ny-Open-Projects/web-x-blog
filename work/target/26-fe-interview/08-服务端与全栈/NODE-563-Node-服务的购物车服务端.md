---
title: [NODE-563] Node 服务的购物车服务端（多端/合并/失效）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-563：购物车服务端
**答**:
- 模型：服务端购物车（用户维度——多端同步 ARC-647 合并）、条目（sku/qty/选中/加入时间）、匿名车（临时 ID——登录合并）。
- 操作协议：增删改（幂等——同 SKU 加购数量累加的原子 RMW：Lua/条件更新防并发数量错乱）、选中状态（UI 态服务端存储——跨端一致）、批量操作（批量勾选/删除）。
- 失效处理：价格/库存失效重算（读时实时校验——购物车展示价 = 实时价格服务（短缓存），失效商品标记不可结算）、商品下架联动（事件——失效标记）。
- 性能：购物车条目数限制（百条——上限与分页策略）、Redis 缓存热车（写后读一致性——写操作失效缓存 ARC-507）、结算预检（结算时全量重算价格库存——ARC-599）。
- 一致性：并发加购（同 SKU 双端同时 +1——服务端 RMW 原子）、合并幂等（合并请求幂等键）。
```javascript
// 加购 RMW
async function addItem(uid, sku, qty) {
  const r = await redis.eval(`local c = redis.call('hget',K1,ARGV1) or 0
    if c + tonumber(ARGV2) > tonumber(ARGV3) then return 0 end   -- 上限校验
    redis.call('hincrby',K1,ARGV1,ARGV2) return 1`, cartKey(uid), sku, qty, MAX_QTY);
  if (r) await db.tx(t => upsertCartItem(t, uid, sku, qty));     // 落库（最终持久）
  await invalidate(cartCache(uid));                              // 失效展示缓存
}
```
