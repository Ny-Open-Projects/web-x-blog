---
title: [921] 知识库到千万 chunk 了，RAG 索引怎么做分片扩容
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 架构扩展]
type: 面试题
---

## 921：知识库到千万 chunk 了，RAG 索引怎么做分片扩容

**答**：
- 分片维度选业务路由键（租户/部门）而不是随机哈希：查询天然带租户，路由分片可以让 filter 直接命中单分片，跨分片查询只发生在全局检索场景。
- 单分片容量上限（如 500 万 chunk）触发再分裂；分裂期间双写新分片 + 追踪切换，避免搬迁窗口丢增量。
- 副本策略：检索是读多写少，副本扛读流量；写入走主分片队列削峰，embedding 批量生成是写入瓶颈，单独队列消费。
- 追问钩子：全局搜索跨 N 个分片怎么保 top-k？——每分片取 top-k 汇总再归并，k 适当放大（如本地 top-2k）减少归并误差。

```ts
async function globalSearch(q, tenant, topK = 5) {
  const shards = tenant ? [route(tenant)] : allShards();   // 租户直达单分片
  const localK = tenant ? topK : topK * 2;                 // 跨分片放大本地 k
  const parts = await Promise.all(shards.map(s => s.knn(embed(q), localK)));
  return mergeTopK(parts, topK);                           // 归并取全局 top-k
}
```

