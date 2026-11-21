---
title: [NODE-414] Node 服务的跨服务分页与聚合（BFF 组合分页）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-414：跨服务分页与聚合
**答**:
- 问题：BFF 聚合多个下游的列表（订单 + 商品信息），各自分页如何组合？深分页跨服务是成本放大器（每页都要全量联合）。
- 方案选择：主从分页（一个服务是分页主源，另一个按主源 ID 批量补数据——90% 场景的正确做法，避免跨服务真分页）、搜索引擎统一索引（跨服务检索需求 → 异构宽表/ES，NODE-387）、数据冗余（下单时快照商品信息进订单——查询免跨服务）。
- 主从分页实现：主服务 cursor 分页取 ID 列表 → 从服务批量 get（DataLoader，NODE-365）→ 组装排序保持主源顺序；从服务数据缺失的兜底（已删除 → 占位符或过滤）。
- 组合分页的坑：各源排序键不一致（时间精度）→ 主源排序权威；过滤条件跨服务（按商品类目筛订单）→ 必须异构索引，硬组合不现实。
- 性能预算：组合分页 P95 < 500ms（主源 + 从源批量并行）；从源慢/挂降级（缺图占位，ARC-447）。
```javascript
async function listOrdersWithGoods(query) {
  const orders = await orderSvc.list(cursorPage(query));         // 主源分页
  const ids = orders.items.map(o => o.skuId);
  const goods = await goodsSvc.batchGet(ids).catch(() => ({}));  // 从源批量补
  return { ...orders, items: orders.items.map(o =>
    ({ ...o, goods: goods[o.skuId] ?? { placeholder: true } })) };
}
```
