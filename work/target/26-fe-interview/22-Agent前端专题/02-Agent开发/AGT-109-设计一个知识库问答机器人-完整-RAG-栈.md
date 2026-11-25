---
title: [AGT-109] 设计一个知识库问答机器人（完整 RAG 栈）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-109：设计一个知识库问答机器人（完整 RAG 栈）？
**答**：
- 完整栈串联：文档接入（解析/清洗/父子分块）→ 增量索引 → 混合检索 + 重排 → 引用溯源回答 → 评测与反馈闭环。
- 「答不上来」的处理比答对更重要：重排分数低于阈值就明确说知识库没有相关内容并给出转人工入口，绝不编造。
- 上下文用预算制：检索块按重排分数取 top-5，超出预算从低分开始砍（复用 AGT-053 组装器）。
- 上线后持续迭代：切分粒度、embedding 模型、rerank 阈值都是可调参数，改一项跑一次回归评测（AGT-076）。

```typescript
import { z } from 'zod';

// 端到端知识库问答
export async function kbAnswer(question: string): Promise<{ answer: string; citations: string[] }> {
  const rewritten = await rewriteQuery([], question);                // 查询改写（AGT-072）
  const chunks = await hybridSearch(rewritten.queries[0], 20);       // 混合检索（AGT-071）
  const reranked = await reranker.rerank(question, chunks).slice(0, 5);
  if (!reranked.length || reranked[0].score < 0.35) {                // 相关性不足：拒答优于编造
    return { answer: '知识库中暂无相关内容，已为你转人工', citations: [] };
  }
  const numbered = reranked.map((c, i) => ({ id: i + 1, text: c.text, source: c.source }));
  const { answer } = await structuredLLM(
    [
      { role: 'system', content: '只依据资料回答，每个事实句标注 [编号]，资料不足时明确说明。' },
      { role: 'user', content: `资料：\n${numbered.map((c) => `[${c.id}] ${c.text}`).join('\n')}\n\n问题：${question}` },
    ],
    z.object({ answer: z.string() }),
  );
  const { aligned } = await answerWithCitations(question, numbered, 0); // 引用对齐（AGT-075）
  return { answer, citations: [...new Set(aligned.map((a) => a.source).filter(Boolean))] };
}
```
