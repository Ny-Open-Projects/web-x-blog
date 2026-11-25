---
title: [910] 笔试手写：实现 RRF 倒数排名融合并支持来源权重
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 检索融合]
type: 笔试题
---

## 910：笔试手写：实现 RRF 倒数排名融合并支持来源权重

**答**：输入多路检索结果 lists（每路为 docId 数组，按相关性降序）与每路权重 weights。输出融合后的 docId 排序列表（去重，取前 limit 个）。公式：score = Σ w_i / (k + rank_i + 1)，k 默认 60，rank 从 0 开始。并列分数按 docId 字典序稳定排序。

```js
/**
 * @param {string[][]} lists
 * @param {number[]} weights 与 lists 等长
 * @param {number} limit
 * @returns {string[]}
 */
function rrfFuse(lists, weights, limit, k = 60) {
  const score = new Map();
  lists.forEach((list, li) => {
    list.forEach((id, rank) => {
      score.set(id, (score.get(id) || 0) + weights[li] / (k + rank + 1));
    });
  });
  return [...score.entries()]
    .sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1)) // 并列稳定排序
    .slice(0, limit)
    .map(([id]) => id);
}
const bm25 = ['d1', 'd2', 'd3'], vec = ['d2', 'd4', 'd1'];
console.log(rrfFuse([bm25, vec], [1, 1], 3)); // ['d2','d1','d3']
console.log(rrfFuse([bm25, vec], [3, 1], 3)); // BM25 权重高 -> ['d1','d2','d3']
```

**评分点**：
- 公式正确：rank 从 0 起、分母 k + rank + 1，很多候选人写成 rank+1 漏掉偏移
- 并列分数的稳定排序处理（评估可复现的前提）
- 边界：空列表、某 doc 只出现在一路、limit 大于去重总数
- 能说明 k 的作用：k 越大各排名差距越平缓，对「哪一路」越不敏感

