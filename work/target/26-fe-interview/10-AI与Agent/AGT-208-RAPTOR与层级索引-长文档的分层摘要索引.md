---
title: [AGT-208] RAPTOR 与层级索引——长文档的分层摘要索引怎么做？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-208：几百页的长文档怎么建索引——RAPTOR 层级摘要索引是什么？

**答**:
- 长文档的两难：细粒度块适合具体问题但丢全局，全文摘要适合总结类问题但定位差——RAPTOR 的解法是分层：叶子层是原文块，向上每层对相邻块聚类并生成摘要，形成"金字塔"索引。
- 检索策略：具体问题命中叶子层（细节准），总结类问题命中高层摘要（全局全），查询路由或全层检索+rerank 决定用哪层——一套索引同时服务两类问题。
- 层级设计：叶子块 300~500 token，聚类阈值控制每层合并比例（每层约缩 3~5 倍），顶层摘要覆盖全文；摘要节点带"覆盖范围"元数据便于引用溯源。
- 成本考量：摘要生成是一次性索引成本（用便宜模型批量跑），换来的是总结类问题的可用性——没有分层索引时，"这文档讲了什么"这类问题基本不可答。

```javascript
// RAPTOR 建索引示意
async function buildRaptor(doc) {
  let level = chunk(doc, 400);                 // L0 原文块
  const tree = [level];
  while (level.length > 1) {
    const clusters = await cluster(level, SIM_THRESHOLD);
    level = await Promise.all(clusters.map(c =>
      summarize(c.map(n => n.text))));         // 上层摘要节点
    tree.push(level);
  }
  return tree.flat();                          // 全层入库，节点带 level 元数据
}
// 检索：query 向量在全部层召回 → rerank
// 总结类问题自然命中高层摘要节点
```
