---
title: [920] 笔试手写：实现 MRR 与 NDCG@k 评估指标
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 评估指标]
type: 笔试题
---

## 920：笔试手写：实现 MRR 与 NDCG@k 评估指标

**答**：输入 results（每次查询的返回 docId 有序列表）与 golds（每次查询的相关 docId 到等级的 Map，2=高度相关 1=相关）。实现 mrr(results, golds) 与 ndcg(results, golds, k)（gain = 2^rel - 1），保留 4 位小数；空结果/无命中按 0 处理。

```js
function mrr(results, golds) {
  let sum = 0;
  results.forEach((docs, i) => {
    const first = docs.findIndex(d => golds[i].has(d));   // 第一个相关文档的排名
    sum += first === -1 ? 0 : 1 / (first + 1);
  });
  return (sum / results.length).toFixed(4);
}
function ndcg(results, golds, k = 5) {
  let sum = 0;
  results.forEach((docs, i) => {
    const rel = id => golds[i].get(id) || 0;              // docId -> 等级
    const dcg = docs.slice(0, k)
      .reduce((s, d, r) => s + (2 ** rel(d) - 1) / Math.log2(r + 2), 0); // r 从 0 起
    const ideal = [...golds[i].entries()]
      .sort((a, b) => b[1] - a[1]).slice(0, k)
      .reduce((s, [, g], r) => s + (2 ** g - 1) / Math.log2(r + 2), 0);
    sum += ideal ? dcg / ideal : 0;
  });
  return (sum / results.length).toFixed(4);
}
const res = [['a','b','c']];
console.log(mrr(res, [new Map([['b',2]])]));           // '0.5000'
console.log(ndcg(res, [new Map([['b',2],['c',1]])], 3)); // dcg=1+3/log2(3)≈2.893
```

**评分点**：
- MRR 首个相关位次倒数、无命中记 0 的边界
- NDCG 的折损公式 log2(rank+2)（rank 从 0 起），最容易写错的一步
- IDCG 必须按等级降序截取前 k，不能拿 DCG 分子瞎除
- 空结果、k 大于列表长度、等级全 0 时返回 0 而不抛错

