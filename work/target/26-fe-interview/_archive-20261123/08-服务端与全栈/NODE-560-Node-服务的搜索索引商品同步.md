---
title: [NODE-560] Node 服务的商品搜索索引同步（CDC/重建/对账）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-560：商品索引同步
**答**:
- 同步链路：商品变更 → CDC（binlog）→ MQ → 索引消费者（NODE-387 链路商品特化）——字段映射（DB 字段 → ES 文档：类目路径/价格/销量聚合字段——投影计算）。
- 一致性保障：顺序问题（同商品乱序更新——按版本号/updateTs 丢弃旧事件）、删除同步（下架/删除 → 索引删除或状态过滤——搜索结果过滤下架）、重建兜底（全量重建任务——夜间低峰：新索引 bulk → 别名切换；重建后对账抽检）。
- 索引设计：分词（商品标题分词 + 品牌词权重）、聚合字段预计算（销量/评分——搜索排序因子预写入，查询时不 join）、过滤字段（类目/状态/价格区间——filter 缓存友好）。
- 延迟管理：同步延迟监控（变更到可搜的时长 P99——秒级目标）、延迟超标降级（索引挂 → 降级 DB 简单搜索 NODE-387）。
- 对账：抽样比对（随机商品：DB 状态 vs ES 文档——一致性抽检任务每日跑）。
```javascript
// 索引消费者（顺序 + 幂等）
consumer.on('goods.change', async (e) => {
  const cur = await es.get(e.id).catch(() => null);
  if (cur && cur._source.version >= e.version) return skip();    // 旧事件丢弃
  await es.index({ id: e.id, document: project(e.row) });        // 投影写入
});
// 每日对账：sample(1000) → compare(db, es) → diffRate > 0.1% → 重建评估
```
