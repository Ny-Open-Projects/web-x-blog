---
title: [AGT-212] RAG 上下文压缩——召回内容太多塞不下上下文怎么办？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-212：召回的文档超过上下文预算时怎么压缩？

**答**:
- 压缩四阶梯（成本从低到高）：截断（按 rerank 分数取 top-n，最便宜）、抽取（LLM/规则只抽与 query 相关的句子，即 LLMLingua 式压缩或知识 strip）、摘要（每块先压缩成要点再拼接）、分治（内容确实都重要时 map-reduce 分块作答再合并）。
- 选择依据：问题类型决定——事实型问题用抽取（细节不能丢），总结型问题用摘要（细节可牺牲），对比型/全量型问题用分治（必须全覆盖）。
- 必守红线：压缩不得改变数字、实体、否定词——摘要模型改写数字是幻觉重灾区，数值类内容原样保留或引用原文块。
- 工程实现：压缩与生成解耦为独立服务，压缩率可配置（按模型窗口动态调整），并对压缩前后做忠实性抽检（数值/实体比对）。

```javascript
async function compress(docs, query, budgetTokens) {
  const total = sumTokens(docs);
  if (total <= budgetTokens) return docs;                       // 不压
  if (isFactQuery(query))  return extractRelevant(docs, query); // 事实：抽取
  if (isSummaryQuery(query)) return summarizeEach(docs);        // 总结：摘要
  return mapReduce(docs, query);                                // 全量：分治
}
// 忠实性抽检：压缩前后比对数字与实体集合，
// 出现原文没有的数字 → 告警并回退用原文块。
```
