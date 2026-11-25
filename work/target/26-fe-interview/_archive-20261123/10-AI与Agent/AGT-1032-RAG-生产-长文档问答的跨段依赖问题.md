---
title: [1032] 答案需要跨章节综合（「第3章的参数在第7章怎么配置」）怎么解决
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 长文档]
type: 面试题
---

## 1032：答案需要跨章节综合（「第3章的参数在第7章怎么配置」）怎么解决

**答**：
- 独立 chunk 检索破坏跨段依赖：两个相关章节可能只召回一个；解法分层——检索时用「父子块」（子块命中召回父节），生成时给模型「文档大纲 + 相关章节全文」而不是碎片。
- 大纲注入很关键：把文档目录树放进 prompt，模型知道「第 3 章在第 7 章之前、两者属于同一主题」，跨段综合能力显著提升。
- 迭代式检索（agentic retrieval）：第一轮检索后让模型判断「还需要什么信息」发起第二轮 query，适合复杂多跳问题，代价是延迟翻倍，按问题复杂度路由。
- 追问钩子：父子块会不会让上下文爆炸？——父块设上限（如 2000 token），超限时「大纲 + 关键段落摘要」替代全文。

```ts
async function longDocQA(q, doc) {
  const hits = await search(q, { mode: 'parent_child', topK: 5 });
  const outline = doc.outline;                       // 目录树注入
  const needsMore = await judge.needsMore(q, hits);  // 多跳判断
  const extra = needsMore ? await search(await refine(q, hits), { topK: 3 }) : [];
  return llm(prompt(outline, [...hits, ...extra], q));
}
```
