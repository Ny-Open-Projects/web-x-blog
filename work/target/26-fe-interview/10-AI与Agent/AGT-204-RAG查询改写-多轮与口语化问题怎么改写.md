---
title: [AGT-204] RAG 查询改写——多轮对话与口语化问题怎么改写？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-204：多轮对话里用户的模糊问题怎么改写成可检索的 query？

**答**:
- 改写的三个来源问题：多轮指代（"那第二个方案呢"缺上下文）、口语化冗长（一句话里混三个意图）、术语不规范（用户词 ≠ 文档词）——不改写直接检索，召回质量断崖式下降。
- 核心手段：query 重写（结合最近 N 轮历史把指代补全成独立问题）、HyDE（让模型先生成一个假想答案再拿去检索，答案与文档的语义距离比问题更近）、同义词扩展（业务词表映射）。
- 工程取舍：改写本身是一次 LLM 调用（成本/延迟），高频场景用小模型 + 规则（首词是"那/它/这个"才触发重写）控制触发率；改写结果与原 query 双路检索取并集更稳。
- 失败兜底：改写后召回分数仍低时不硬答，走澄清反问（"您是指 A 还是 B？"）——澄清是检索失败的正确出口，不是重试。

```javascript
async function retrieveWithRewrite(query, history) {
  const needs = /^(那|它|这个|第二个|上面)/.test(query.trim());
  const rewritten = needs
    ? await smallLLM(`结合对话补全问题为独立完整的问题：
        历史:${history.slice(-4)}
        问题:${query}`)
    : query;
  const [r1, r2] = await Promise.all([
    vectorSearch(rewritten, 30),      // 改写后检索
    vectorSearch(query, 20),          // 原始 query 双路
  ]);
  return rrf([r1, r2]).slice(0, 6);
  // 召回分仍低 → 返回澄清候选而非硬答
}
```
