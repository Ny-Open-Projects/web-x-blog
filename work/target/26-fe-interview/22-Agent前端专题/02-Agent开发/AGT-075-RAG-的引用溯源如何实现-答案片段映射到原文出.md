---
title: [AGT-075] RAG 的引用溯源如何实现（答案片段映射到原文出处）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-075：RAG 的引用溯源如何实现（答案片段映射到原文出处）？
**答**：
- 让答案可信的关键是引用可验证：检索块带编号进 prompt，要求模型每个事实句用 `[1]` `[2]` 标注。
- 服务端校验：解析引用标记，剔除编造编号（超出提供范围）与零引用答案，必要时重试。
- 更强的溯源是句子级对齐：把答案每句与检索块做相似度匹配，模型没标也能自动补出处，同时发现无出处句子（幻觉信号）。
- 前端呈现：引用标记渲染成角标/超链，hover 或点击展示原文块与来源定位。

```typescript
import { z } from 'zod';

// 引用注入 + 编号校验 + 句子级自动对齐
interface Chunk { id: number; text: string; source: string }

export async function answerWithCitations(query: string, chunks: Chunk[], retry = 1): Promise<ReturnType<typeof align>> {
  const context = chunks.map((c) => `[${c.id}] ${c.text}（来源：${c.source}）`).join('\n');
  const answer = await chatOnce([
    { role: 'system', content: '只依据提供的资料回答。每个事实性陈述末尾用 [编号] 标注来源，资料无法回答时明确说明。' },
    { role: 'user', content: `资料：\n${context}\n\n问题：${query}` },
  ]);
  // 校验：引用编号必须都在提供范围内，编造则重试
  const cited = [...answer.matchAll(/\[(\d+)\]/g)].map((m) => Number(m[1]));
  if (!cited.every((id) => chunks.some((c) => c.id === id)) && retry > 0) {
    return answerWithCitations(query, chunks, retry - 1);
  }
  return align(answer, chunks);
}

// 句子级对齐：未标注的句子自动补出处，无出处即疑似幻觉
async function align(answer: string, chunks: Chunk[]) {
  const sentences = answer.split(/(?<=[。！？])/).filter(Boolean);
  const aligned = await Promise.all(sentences.map(async (s) => {
    const inline = s.match(/\[(\d+)\]/);
    if (inline) return { sentence: s, source: chunks.find((c) => c.id === Number(inline[1]))!.source };
    const sv = await embed(s);
    const scores = await Promise.all(chunks.map(async (c) => ({ c, score: cosine(sv, await embed(c.text)) })));
    const best = scores.sort((a, b) => b.score - a.score)[0];
    return { sentence: s, source: best.score > 0.7 ? best.c.source : null }; // null = 无出处
  }));
  return { answer, aligned };
}
```
