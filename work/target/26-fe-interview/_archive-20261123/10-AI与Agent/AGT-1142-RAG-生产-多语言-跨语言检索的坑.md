---
title: [1142] 中英混合知识库的跨语言检索怎么处理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 多语言]
type: 面试题
---

## 1142：中英混合知识库的跨语言检索怎么处理

**答**：
- 核心问题：中文 query 检索英文文档（或反向），跨语言向量模型的召回显著低于同语言；解法三选一——多语言 embedding 模型（对齐跨语言空间）、查询翻译（query 先译成文档语言再检索，双路并跑取融合）、文档双写（关键文档两语言各存一份）。
- 生产常见组合：多语言模型为底 + 高价值文档双写（对精度敏感的规范类）；查询翻译要保留实体不译（产品名/错误码翻译反而破坏检索）。
- 语言识别是前置件：query 语言识别错（混杂中英）会导致翻译链路全错，识别置信度低时直接走多语言模型原样检索。
- 追问钩子：跨语言的引用溯源有什么坑？——命中文档语言与用户语言不同，回答需要「检索语言理解 + 回答语言生成」两个阶段，且引用高亮定位要按文档原语言偏移计算。

```ts
async function crossLingual(q) {
  const lang = detect(q, { confidence: 0.9 });
  if (!lang.confident) return hybridSearch(q, 10);       // 混杂语言原样检索
  const translated = await translate(q, { keep: ['实体'] }); // 实体不译
  return rrfFuse([hybridSearch(q, 10), hybridSearch(translated, 10)], [1, 1], 8);
}
```
