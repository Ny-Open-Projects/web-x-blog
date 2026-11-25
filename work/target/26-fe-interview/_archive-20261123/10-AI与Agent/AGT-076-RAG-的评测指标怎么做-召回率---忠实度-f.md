---
title: [AGT-076] RAG 的评测指标怎么做（召回率 / 忠实度 faithfulness）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-076：RAG 的评测指标怎么做（召回率 / 忠实度 faithfulness）？
**答**：
- RAG 评测分两段：检索质量（recall@k——金标 chunk 是否被召回）与生成质量（忠实度——答案是否只基于检索内容）。
- 召回率要建「金标证据集」：每个问题人工标注应命中的 chunk，跑 recall@k。
- 忠实度用 LLM 拆 claim：把答案拆成原子事实，逐条判断能否由检索内容推出，未支持占比即不忠实率。
- 指标进 CI：每次改切分/embedding/提示都跑同一评测集，看趋势而不是单次感觉。

```typescript
import { z } from 'zod';

// RAG 双指标评测
interface RagCase { question: string; goldChunkIds: string[] }

export async function evalRetrievalRecall(cases: RagCase[], k = 5) {
  let totalRecall = 0;
  const details: { question: string; recall: number }[] = [];
  for (const c of cases) {
    const hits = (await hybridSearch(c.question, k)).map((h) => h.docId);
    const recall = c.goldChunkIds.filter((g) => hits.includes(g)).length / c.goldChunkIds.length;
    totalRecall += recall;
    details.push({ question: c.question, recall });
  }
  return { avgRecall: totalRecall / cases.length, details };
}

export async function evalFaithfulness(qa: { question: string; answer: string; context: string }[]) {
  let supported = 0, totalClaims = 0;
  for (const { question, answer, context } of qa) {
    const { claims } = await structuredLLM(
      [{ role: 'user', content: `把答案拆成原子化事实陈述：\n问题：${question}\n答案：${answer}` }],
      z.object({ claims: z.array(z.string()).min(1) }),
    );
    for (const claim of claims) {
      const { ok } = await structuredLLM(
        [{ role: 'user', content: `判断该陈述能否仅由资料推出。资料：${context}\n陈述：${claim}` }],
        z.object({ ok: z.boolean() }),
      );
      totalClaims += 1;
      if (ok) supported += 1;
    }
  }
  return { faithfulness: supported / totalClaims }; // 越接近 1 越忠实
}
```
