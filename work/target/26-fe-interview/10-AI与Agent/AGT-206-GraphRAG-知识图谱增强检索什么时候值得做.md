---
title: [AGT-206] GraphRAG——知识图谱增强检索什么时候值得做？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-206：GraphRAG 是什么——什么业务场景值得引入知识图谱？

**答**:
- 核心思路：向量化解决"语义相似"，图解决"关系结构"——把文档中的实体与关系预抽取成图（实体节点+关系边），检索时既走向量又走图遍历，能回答"关系型/全局型"问题。
- 适合的信号：问题高频出现"A 和 B 什么关系""涉及 X 的所有相关方"、文档间引用密集（法规/组织架构/故障树/供应链）——全局总结类问题（"这批文档的主线是什么"）向量检索天然弱，GraphRAG 的社区摘要有效。
- 不适合的信号：问答多为单点事实、文档更新极频繁（图重建成本高）、团队没有图谱维护能力——为图而图会把 RAG 工程拖入无底洞。
- 混合架构：向量检索为主、图为辅助（命中实体后沿边扩展 1~2 度补充上下文），图的构建用 LLM 抽取 + 人工抽检关键实体，更新走增量 pipeline。

```javascript
// GraphRAG 混合检索示意
async function graphRAG(query) {
  const vec = await vectorSearch(query, 30);
  const ents = await extractEntities(query);          // query 抽实体
  const graph = await graphExpand(ents, DEPTH = 2);   // 沿边扩展 2 度
  const docs = await docsByEntities(graph.nodes);     // 实体回查文档
  return rrf([vec, docs]).slice(0, 6);
  // 全局总结类 → 走预生成的社区摘要而非逐文档
}
```
