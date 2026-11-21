---
title: [NODE-387] Node 服务的搜索服务（ES）集成与索引同步如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-387：Node 服务的搜索服务集成
**答**:
- 职责边界：ES 负责检索（全文/筛选/排序/聚合），DB 仍是事实源；业务写不改 ES 数据语义，只同步。
- 同步方案：双写（写 DB 后写 ES——简单但有双写不一致风险，失败重试 + 对账兜底）、CDC 监听 binlog（Debezium → MQ → 索引，解耦可靠，主流）、定时全量重建（兜底纠偏，夜间全量 + 白天增量）。
- 索引工程：mapping 显式定义（禁动态 mapping 失控）、分词器选型（中文 ik，业务词典自定义）、别名机制（reindex 无缝切换：索引版本 → 别名原子切换 → 删旧索引）。
- 一致性窗口：同步延迟秒级，业务要接受"搜到旧数据"或对强一致场景做 DB 复核（点开详情以 DB 为准）。
- Node 侧：查询 DSL 封装（防注入：用户输入走参数化 query，禁脚本注入）、超时与降级（ES 挂时降级 DB 简单查询，ARC-447）。
```javascript
// CDC 同步消费（binlog → ES）
consumer.subscribe('db.goods');
consumer.on('data', async (msg) => {
  const { op, after } = msg;
  if (op === 'delete') await es.delete({ index: 'goods', id: after.id });
  else await es.index({ index: 'goods', id: after.id, document: toEsDoc(after) }); // upsert
});
// 重建：新索引 goods_v2 → bulk 全量 → 别名 goods 切换 → 删 goods_v1
```
