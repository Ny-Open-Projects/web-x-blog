---
title: [1031] 公司有多个知识库（产品文档/工单/规范），检索怎么路由
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 多库路由]
type: 面试题
---

## 1031：公司有多个知识库（产品文档/工单/规范），检索怎么路由

**答**：
- 三种架构：统一大索引（简单但权限与相关性互相干扰）、路由器分发（小模型按 query 选 1~2 个库再检索）、联邦检索（全库并行检索后融合）。
- 选型经验：库间领域差异大且权限不同 → 路由器；领域重叠多 → 统一索引 + 元数据分区；都不确定 → 先联邦（保召回）再优化路由（省成本）。
- 路由器错误代价不对称：「该查没查」（漏）比「多查一库」（浪费）严重得多，所以路由器要允许多选 + 低置信全查。
- 追问钩子：路由器怎么训练？——先用规则（query 关键词/来源历史）冷启动，线上积累「query→命中库」标注后蒸馏成小分类器。

```ts
async function federatedSearch(q, libs) {
  const route = await router(q, libs);              // 返回带置信度的候选库
  const targets = route.conf > 0.8 ? route.top2 : libs;  // 低置信全查防漏
  const rs = await Promise.all(targets.map(l => search(l, q, 10)));
  return rrfFuse(rs, targets.map(t => t.weight), 10);    // 跨库融合
}
```
