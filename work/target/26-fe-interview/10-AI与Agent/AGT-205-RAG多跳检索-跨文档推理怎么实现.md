---
title: [AGT-205] RAG 多跳检索——跨文档推理问题怎么实现？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-205："A 的作者所在的公司"这类多跳问题怎么检索？

**答**:
- 多跳的本质：答案需要串联多份文档（文档 A 给出中间结论，文档 B 给出最终答案），单次检索只命中一跳——直查只会召回不完整的证据链。
- 实现路径：迭代检索（每跳用上跳结论改写新 query，循环直到证据齐或达到跳数上限）、分解检索（把多跳问题先拆成子问题列表，分别检索再汇总，Agentic RAG 的基础形态）、GraphRAG（把实体关系预抽取成图，沿图边跳转）。
- 闭环判据：每跳记录"已确认的中间事实"，全部子问题有证据才合成答案；子问题缺证时降级为部分回答并声明缺口，不编造连接。
- 成本控制：跳数上限（通常 ≤3）+ 子问题缓存 + 中间结论复用——多跳检索的成本是线性跳数，必须有预算护栏。

```javascript
async function multiHop(question, maxHops = 3) {
  let subQs = await decompose(question);       // 拆子问题
  const facts = [];
  for (const q of subQs) {
    let evidence = await retrieve(q);
    // 若子问题本身是多跳，用已确认事实改写再检索
    for (let hop = 0; hop < maxHops && !evidence.length; hop++) {
      q = await rewriteWith(facts, q);
      evidence = await retrieve(q);
    }
    if (!evidence.length) return { partial: true, missing: q }; // 缺口声明
    facts.push(...evidence);
  }
  return synthesize(question, facts);          // 证据齐才合成
}
```
