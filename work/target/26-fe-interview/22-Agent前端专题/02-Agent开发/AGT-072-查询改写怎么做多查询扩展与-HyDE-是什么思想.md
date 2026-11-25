---
title: [AGT-072] 查询改写怎么做？多查询扩展与 HyDE 是什么思想？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-072：查询改写怎么做？多查询扩展与 HyDE 是什么思想？
**答**：
- 用户问句常常短、口语化、带指代（「它怎么部署」），直接检索召回差：改写是性价比最高的检索优化。
- 多查询扩展：让模型改写出 3-5 个不同角度的独立查询，并行检索后合并去重，覆盖面显著提升。
- HyDE 思想：先让模型生成一个「假设答案」，拿假设答案做向量检索——答案与文档的语义距离比问题与文档更近。
- 成本控制：改写用小模型、限制条数；首轮召回充分的场景可跳过改写。

```typescript
import { z } from 'zod';

// 查询改写：多查询扩展 + HyDE 双策略
export async function rewriteQuery(history: ChatMessage[], question: string) {
  const { queries, hypotheticalAnswer } = await structuredLLM(
    [{
      role: 'user',
      content: `结合对话历史完成两项改写：
1. 把问题改写成 3 个独立、无指代的检索查询（换同义词与角度）
2. 写一段约 100 字的假设性答案（HyDE，用于向量检索，不需要正确）
对话历史：${JSON.stringify(history.slice(-4))}
问题：${question}`,
    }],
    z.object({ queries: z.array(z.string()).length(3), hypotheticalAnswer: z.string() }),
  );
  return { queries, hypotheticalAnswer };
}

export async function searchWithRewrite(history: ChatMessage[], question: string) {
  const { queries, hypotheticalAnswer } = await rewriteQuery(history, question);
  const all = await Promise.all([
    ...queries.map((q) => vectorStore.search(await embed(q), 10)),
    vectorStore.search(await embed(hypotheticalAnswer), 10), // HyDE 通道
  ]);
  const seen = new Set<string>();
  const merged: { id: string; score: number }[] = [];
  for (const list of all) {
    for (const h of list) {
      if (!seen.has(h.id)) { seen.add(h.id); merged.push(h); } // 合并去重
    }
  }
  return merged.sort((a, b) => b.score - a.score).slice(0, 8);
}
```
