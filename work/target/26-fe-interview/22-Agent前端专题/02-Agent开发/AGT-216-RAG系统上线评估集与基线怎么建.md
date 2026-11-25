---
title: [AGT-216] RAG 上线前评估——评测集与指标基线怎么建？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-216：RAG 系统上线前怎么建立评估——评测集与指标怎么定？

**答**:
- 评测集三层：检索评测（query→金标文档，指标 recall@k/MRR，150~300 条）、生成评测（query→金标答案，指标忠实性/相关性/完整性，用 LLM-as-judge + 人工抽检）、端到端业务评测（真实 badcase 回放 + 用户反馈率基线）。
- 评测集来源：真实用户问题（最重要，覆盖各意图分布）+ 边界集（该拒答的问题/时效问题/权限边界）+ 回归集（每次改动必须重跑的 50~100 条核心集）。
- 分层定位问题：端到端差 → 先看检索指标，检索差修检索，检索好但答案差修生成（prompt/模型/压缩）——分层指标让优化有的放矢。
- 基线纪律：任何索引/prompt/模型变更都必须过回归集，指标回退超阈值即拦截上线——没有基线的 RAG 迭代全是玄学。

```javascript
async function evalRAG(dataset) {
  const retrieval = { hit: 0, mrr: 0 };
  for (const { query, goldIds } of dataset.retrieval) {
    const docs = await retrieve(query, { k: 10 });
    const rank = docs.findIndex(d => goldIds.includes(d.id));
    if (rank !== -1) { retrieval.hit++; retrieval.mrr += 1 / (rank + 1); }
  }
  const gen = await judgeAnswers(dataset.generation); // 忠实性/相关性 1-5
  return { recall10: retrieval.hit / dataset.retrieval.length,
           mrr: retrieval.mrr / dataset.retrieval.length, ...gen };
  // 上线门槛示例：recall10 ≥ 0.85，忠实性均分 ≥ 4.2
}
```
