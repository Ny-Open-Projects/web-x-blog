---
title: [AGT-211] CRAG 与自纠错检索——召回质量差时系统怎么自救？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-211：CRAG（纠错型 RAG）的核心机制是什么？

**答**:
- 动机：固定管线把"低质量召回"也直接喂给模型，垃圾进垃圾出——CRAG 在检索与生成之间加"评估门"：先判断召回质量，再决定走哪条路。
- 三分支：正确（召回与问题相关）→ 精炼后生成；模糊（部分相关）→ 精炼+补充检索；错误（不相关）→ 丢弃，回退到 Web 搜索或改写重检或拒答——不让低质量证据污染答案。
- 精炼动作：对召回块做"知识 strip"——只保留与问题相关的句子，去掉无关内容，降低噪声对生成的干扰。
- 实现要点：评估器可用小模型打分（快）或规则（召回分数阈值）；回退链要有上限（重试 ≤2 次），全部失败走"未找到相关信息"的诚实拒答——拒答是兜底不是失败。

```javascript
async function crag(query) {
  let docs = await retrieve(query);
  let verdict = await judge(query, docs);    // correct / ambiguous / incorrect
  for (let i = 0; i < 2 && verdict !== 'correct'; i++) {
    if (verdict === 'ambiguous') docs = refine(docs, query);   // 精炼
    else docs = [ ...(await webSearch(query)), ...(await rewriteAndRetrieve(query)) ];
    verdict = await judge(query, docs);
  }
  if (verdict !== 'correct') return '知识库中未找到可靠依据，无法作答'; // 诚实拒答
  return generate(query, refine(docs, query));
}
```
