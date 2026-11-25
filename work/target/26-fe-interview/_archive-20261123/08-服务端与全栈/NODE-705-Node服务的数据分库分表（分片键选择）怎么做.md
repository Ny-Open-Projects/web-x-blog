---
title: [NODE-705] 数据分库分表（分片键选择）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-705：分库分表怎么做？
**答**：
- 分片键选择：查询主维度（订单按 user_id——用户查自己的订单是主查询；按 order_id 分片则用户查询要扫全片）——「按最常用的查询维度分片」，跨维度查询走异构索引（ES/宽表）。
- 分片策略：hash 取模（均匀但扩容难）vs range（扩容易但热点）vs 一致性 hash（扩容平滑）；基因法（order_id 嵌入 user_id 后缀——跨维度也能路由）。
- 分片中间件：应用层路由（sharding proxy vs client SDK——SQL 兼容性/事务限制）；跨片查询的代价（聚合/事务跨片——设计时避免，SCN-NODE-653 单片事务原则）。
- 扩容：翻倍扩容（数据迁移双写——SCN-OPS-331 expand-contract）。
- 追问钩子：为什么「基因法」能同时满足两个维度的查询——order_id 生成时嵌入 user_id 的部分位（基因）：按 order_id 分片能路由，按 user_id 查也能从 order_id 基因定位——分片键二选一的困境用「键里携带另一个维度的路由信息」破解；代价是 ID 生成与业务耦合——设计期就要想清楚查询维度。

```javascript
// 基因法：order_id 嵌入 user_id 后 8 位
const orderId = `${snowflake()}${userGene}`;           // 同 user 的订单路由到同片
// 分片路由
const shard = hash(userGene) % N;                      // 两个维度同片
// 跨片查询走异构索引（ES 冗余一份用户维度视图）
```
