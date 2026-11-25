---
title: [914] 线上 RAG badcase 怎么回流成改进，闭环怎么搭
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, badcase]
type: 面试题
---

## 914：线上 RAG badcase 怎么回流成改进，闭环怎么搭

**答**：
- 采集：用户负反馈（点踩/重问/转人工）+ 自动哨兵（答案引用编号越界、答案与来源相似度低），两类信号进同一 badcase 队列并去重。
- 归因四分法：检索没召回 / 召回但排序错 / 排序对但生成丢信息 / 知识库本身缺失。四类改法完全不同（改分块、改融合、改 prompt、补文档），归因错了改动就是白费。
- 回流节奏：每周把已归因 badcase 转成评估集条目（带证据出处），改动跑全量评估 + 回归集，通过才上线。
- 追问钩子：怎么证明这周的改动有效？——固定回归集 + 留出集双指标，同时看拒答率和幻觉率没恶化，防止按下葫芦浮起瓢。

```ts
function triage(case_: BadCase) {
  const hits = await retrieve(case_.query, 10);
  if (!hits.length || hits[0].score < CUT) return 'retrieval_miss';     // 改分块/索引
  if (hits.some(h => h.meta.evidence === case_.evidence)) return 'rank_miss'; // 改融合权重
  if (answerSim(case_.answer, case_.evidenceText) < 0.6) return 'gen_miss';   // 改 prompt
  return 'knowledge_gap';                                               // 补文档
}
```

