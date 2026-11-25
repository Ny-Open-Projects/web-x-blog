---
title: [909] 上下文窗口越来越大，RAG 还需要做上下文压缩吗
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 上下文管理]
type: 面试题
---

## 909：上下文窗口越来越大，RAG 还需要做上下文压缩吗

**答**：
- 需要，理由有三：长上下文的「中间迷失」（模型对中部信息召回率下降）、按 token 计费的成本、以及无关内容增加幻觉概率。
- 生产组合拳：检索条数收敛（top-5 精排而非 top-50 塞入）→ 每 chunk 抽取关键句 → 无关 chunk 直接丢弃而非压缩。
- 压缩的度：QA 场景保留原文比摘要安全（数字、条款容易摘要失真）；摘要适合「概述类」问题，按 query 意图路由两种策略。
- 追问钩子：128k 窗口全塞进去行不行？——评估过，全塞成本翻 20 倍且准确率反而降，LLM-as-judge 打分从 4.2 掉到 3.6。

```ts
function buildContext(hits, queryIntent) {
  if (queryIntent === 'overview') {
    return hits.map(h => summarize(h.text, 120)).join('\n---\n'); // 概述题走摘要
  }
  // 事实/条款题保留原文，但丢掉 rerank 分数低于阈值的 chunk
  return hits.filter(h => h.score > DROP_CUT)
    .map(h => '[' + h.meta.title + ']\n' + h.text).join('\n---\n');
}
```

