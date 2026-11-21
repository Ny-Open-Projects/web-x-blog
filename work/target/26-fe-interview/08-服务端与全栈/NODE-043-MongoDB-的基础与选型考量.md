---
title: [NODE-043] MongoDB 的基础与选型考量？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-043：MongoDB 的基础与选型考量？
**答**：
- 文档模型（BSON）：无固定 schema、嵌套数组/对象天然匹配 JSON；适合**内容型、字段多变、读多写少**场景（CMS、商品详情、用户行为日志）。强事务场景（账务、库存扣减）仍选 MySQL（4.0+ 有多文档事务但代价高）。
- BFF 视角：API 返回 JSON，Mongo 的文档可以"少一层 ORM 映射"；聚合管道 `$lookup`/`$group` 能替代很多 SQL join/group。
- 核心概念：collection ↔ table、document ↔ row、`_id` 自动 ObjectId、索引（`explain()` 查看是否走索引）、副本集与分片。

```javascript
const { MongoClient } = require('mongodb');

const client = new MongoClient(process.env.MONGO_URL, { maxPoolSize: 20 });
await client.connect();
const col = client.db('shop').collection('goods');

// 写入：灵活 schema
await col.insertOne({
  title: '机械键盘',
  specs: { switch: '红轴', keys: 87 },     // 嵌套对象
  tags: ['外设', 'hot'],
  stock: 100,
});

// 聚合管道：分组统计 + 关联（$lookup 类似 join）
const hotByTag = await col.aggregate([
  { $match: { tags: 'hot' } },
  { $group: { _id: '$tags', avgStock: { $avg: '$stock' }, count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 10 },
]).toArray();

// 原子操作：库存扣减（findAndModify 保证条件扣减）
const result = await col.findOneAndUpdate(
  { _id: goodsId, stock: { $gte: 1 } },    // 条件更新防超卖
  { $inc: { stock: -1 } },
  { returnDocument: 'after' },
);
if (!result) throw new BizError('OUT_OF_STOCK', '库存不足', 409);

// 索引与解释
await col.createIndex({ tags: 1, stock: -1 });
console.log((await col.find({ tags: 'hot' }).explain()).queryPlanner.winningPlan);
```
