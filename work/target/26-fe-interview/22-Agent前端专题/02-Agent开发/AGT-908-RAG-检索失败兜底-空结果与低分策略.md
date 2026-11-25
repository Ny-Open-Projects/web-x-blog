---
title: [908] 检索结果为空或分数很低时，RAG 服务应该怎么兜底
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 兜底策略]
type: 面试题
---

## 908：检索结果为空或分数很低时，RAG 服务应该怎么兜底

**答**：
- 分级兜底而不是一刀切拒答：top1 分数低于硬阈值 → 直接「知识库没有相关内容」并引导人工；分数居中 → 降级为「可能相关」，答案附低置信提示；分数高 → 正常回答。
- 空结果常见根因排查顺序：query 改写后语义漂移（先拿原始 query 重试）→ 分词/向量模型与语料不匹配 → 文档根本没入库（索引监控）。
- 兜底要埋「拒答率」指标：拒答率突增通常意味着索引挂了或 embedding 服务降级，而不是用户问法变了。
- 追问钩子：能不能让模型用自身知识兜底？——可以但要显式标注「以下回答基于模型通用知识，未命中知识库」，并把该路径纳入评估，否则幻觉率统计失真。

```ts
async function answer(q: string) {
  const hits = await retrieve(q, 5);
  const top = hits[0]?.score ?? 0;
  if (!hits.length || top < HARD_CUT) {
    metrics.inc('rag_reject');
    return { text: '知识库暂无相关内容，已转人工。', level: 'reject' };
  }
  if (top < SOFT_CUT) {
    return { text: await gen(q, hits), level: 'low_confidence', hint: '仅供参考' };
  }
  return { text: await gen(q, hits), level: 'confident' };
}
```

