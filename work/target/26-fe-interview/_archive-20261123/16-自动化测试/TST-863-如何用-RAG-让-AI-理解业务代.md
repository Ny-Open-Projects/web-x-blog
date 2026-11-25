---
title: [TST-863] 如何用 RAG 让 AI 理解业务代码上下文，生成更贴合的测试？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-863：如何用 RAG 让 AI 理解业务代码上下文，生成更贴合的测试？
**答**：
- 结论：RAG 把「项目代码/领域知识/历史用例」切片向量化入库，生成测试时先检索相关上下文再交给 LLM，避免 AI 凭空臆测 API。
- 知识库内容：源码与类型定义、业务术语表、历史缺陷与对应用例、测试规范与 fixture 用法。
- 检索策略：按「被测函数名/模块路径」做混合检索（关键词 + 向量），把最相关的代码片段塞进 prompt。
- 效果：减少幻觉 API、贴合既有测试风格、生成可直接运行的用例；需控制上下文长度与相关性噪声。
- 追问钩子：RAG 检索到过时代码（旧版本 API）导致生成错误测试，你如何保证知识库「新鲜度」？

```javascript
// RAG 流程：检索相关代码上下文 -> 组装 prompt
async function ragGenerateTest(question, { embed, search, llm, codeChunks }) {
  // 1. 问题向量化
  const qVec = await embed(question);
  // 2. 检索最相关的代码片段（混合检索的简化）
  const context = search(codeChunks, qVec).slice(0, 3)
    .map(c => c.content).join('\n---\n');
  // 3. 带上下文生成
  const prompt = `基于以下代码生成 Vitest 测试，只使用出现的 API：\n${context}\n需求：${question}`;
  return llm(prompt);
}
// search 用余弦相似度；context 让 AI「看到」真实函数签名而非臆测
```
