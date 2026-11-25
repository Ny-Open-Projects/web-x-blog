---
title: [1141] 知识库做大了之后，分层架构怎么演进
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 架构演进]
type: 面试题
---

## 1141：知识库做大了之后，分层架构怎么演进

**答**：
- 三层演进：单库 → 按领域分库（路由/联邦）→ 分层（热层：高频 FAQ 小而精的 curated 库；温层：全量文档库；冷层：历史归档按需挂载）——热点问题的延迟与成本由热层兜住。
- 热层的维护机制：从 query 日志统计高频意图，由领域 owner 维护「精选答案」（人工审校），命中热层即免全量检索——准确率与延迟双优。
- 冷层的接入策略：默认不参与检索，query 显式带时间/历史意图才挂载，防止冷层噪音稀释 top-k。
- 追问钩子：热层答案和文档库答案冲突听谁的？——热层经过人工审校且有时效标注，冲突时优先热层并展示「官方维护」标识；热层过期自动降级回温层。

```ts
async function layeredRetrieve(q) {
  const hot = await hotKb.match(q, { threshold: 0.92 });
  if (hot) return { source: 'curated', hits: [hot], stale: expired(hot) };
  const warm = await hybridSearch(warmKb, q, 10);
  if (needsHistory(q)) warm.push(...await coldKb.search(q, 5)); // 显式挂冷层
  return { source: 'warm', hits: fuse(warm) };
}
```
