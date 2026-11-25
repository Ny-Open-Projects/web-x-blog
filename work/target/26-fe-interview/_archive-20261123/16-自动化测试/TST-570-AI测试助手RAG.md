---
title: [TST-570] AI 测试助手如何与企业知识库结合（RAG）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-570：AI 测试助手如何与企业知识库结合（RAG）

**答**：
- 结论：RAG = 把企业文档（需求/接口/历史缺陷/测试规范）切片向量化入库，提问时先检索相关片段再喂给 LLM，让回答基于企业事实而非通用知识。
- 做法：按语义切片 + 元数据（模块/版本）标注；检索用混合检索（关键词+向量）提升召回；Prompt 要求引用来源片段；对过期文档设版本与失效机制。
- 追问钩子：RAG 检索到过时文档给出错误答案怎么办？——给文档打版本/生效时间，检索时过滤旧版；回答附来源链接便于核验；定期清理与更新知识库。

```javascript
// RAG 简化流程：检索相关片段 → 拼装带引用的 Prompt
function buildRagPrompt(query, chunks, topK = 3) {
  const picked = chunks
    .map(c => ({ ...c, score: c.text.includes(query) ? 1 : 0.3 }))
    .sort((a, b) => b.score - a.score).slice(0, topK);
  const context = picked.map((c, i) => `[${i+1}](${c.source}) ${c.text}`).join('\n');
  return `基于以下资料回答，引用来源编号：\n${context}\n问题：${query}`;
}
console.log(buildRagPrompt('如何测弱网?', [{ source: 'A.md', text: '弱网用 CDP 模拟' }]));
console.log(buildRagPrompt('支付超时?', [
  { source: 'A.md', text: '弱网用 CDP 模拟' },
  { source: 'B.md', text: '支付超时重试 3 次' },
], 2).includes('[2](B.md)')); // true
```
