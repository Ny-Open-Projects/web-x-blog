---
title: [NODE-338] Node 服务的 MongoDB 使用规范与选型边界？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-338：Node 服务的 MongoDB 使用规范与选型边界
**答**:
- 选型边界：适合文档异构、读写模式匹配聚合、快速迭代场景（CMS/用户画像/日志）；不适合强事务多集合关联（PG 事务更成熟）、复杂 JOIN 分析。
- schema 规范：无 schema ≠ 无设计——文档结构版本化（schemaVersion）、嵌入 vs 引用按读取模式定（一起读的嵌入、无限增长的引用 + 分页）、16MB 上限红线（大附件外置 OSS）。
- 索引与查询：compound index 匹配查询模式（ESR 原则：等值-排序-范围）、禁全表 aggregation 无索引支撑、explain 验证（IXSCAN vs COLLSCAN）。
- 事务与一致性：多文档事务可用但性能代价高（能单文档原子解决不建事务）；writeConcern majority + readConcern majority 保证安全级别；唯一索引兜底业务唯一性。
- Node 侧：连接池 maxPoolSize 对齐并发、游标分批（cursor.batchSize）、超时设置、Change Streams 做失效广播。
```javascript
// 按读取模式设计：评论嵌套有上限，超限引用
// post: { _id, title, recentComments: [...前10条嵌入], commentCount: 1053 }
const cursor = db.collection('comments').find({ postId }).sort({ at: -1 }).batchSize(100); // 引用分页
await db.collection('posts').updateOne({ _id }, { $inc: { commentCount: 1 } }, { writeConcern: { w: 'majority' } });
```
