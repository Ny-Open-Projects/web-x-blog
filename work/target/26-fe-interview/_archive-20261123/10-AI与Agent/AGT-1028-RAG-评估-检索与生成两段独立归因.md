---
title: [1028] 回答错了，怎么快速判断是检索的锅还是生成的锅
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 归因]
type: 面试题
---

## 1028：回答错了，怎么快速判断是检索的锅还是生成的锅

**答**：
- 两段独立评估是 RAG 评测的地基：检索段只评「证据是否进 top-k」（命中率/MRR），生成段固定输入理想证据只评「答案质量」——两段分数合起来才能定位短板。
- 快速归因四象限：证据在且答对 / 证据在答错（生成的锅：prompt/模型）/ 证据不在答对（模型在用自身知识，幻觉隐患）/ 证据不在答错（检索的锅）。
- 「证据不在却答对」是隐性炸弹：上线后知识库换了，这类题全变幻觉——评估集要标注每题的「证据依赖」属性，无证据依赖的题单独统计。
- 追问钩子：检索和生成谁先优化？——看四象限占比：证据不在占多数先修检索；证据在答错占多数修生成。经验上检索问题占 60% 以上。

```ts
function attribution(case_, topK) {
  const hits = retrieve(case_.query, topK);
  const hasEvidence = hits.some(h => case_.evidence.includes(h.id));
  const correct = grade(answer(case_.query, hits), case_.goldAnswer);
  if (hasEvidence && correct) return 'ok';
  if (hasEvidence) return 'gen_fail';        // 生成的锅
  return correct ? 'hidden_risk' : 'retrieval_fail'; // 检索的锅/幻觉隐患
}
```
