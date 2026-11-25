---
title: [1175] 检索结果 5 条都来自同一文档/同一段，怎么保证多样性
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 多样性]
type: 面试题
---

## 1175：检索结果 5 条都来自同一文档/同一段，怎么保证多样性

**答**：
- 同质化的危害：top-5 全是同一文档的不同段落，信息源单一（视角缺失），生成答案覆盖面差。
- 去重多样性算法：MMR（最大边际相关）——按「相关性 - 与已选结果的相似度」贪心选下一 条，兼顾相关与多样；简单版先按「文档 id 分桶限额」（每文档最多 2 条）。
- 多样性的度：不是越多样越好，query 本身指向单一事实时多样性有害；按意图路由——事实型 query 保相关优先，比较型/综述型 query 加多样性权重。
- 追问钩子：MMR 的 λ 参数怎么定？——λ 控制相关与多样的权衡，评估集里准备「综述类」子集，扫 λ 找该子集的最优值；不同意图可用不同 λ。

```ts
function mmr(cands, q, { lambda = 0.7, k = 5 } = {}) {
  const picked = [];
  while (picked.length < k && cands.length) {
    let best = null, bestScore = -Infinity;
    for (const c of cands) {
      const div = picked.length ? Math.max(...picked.map(p => sim(p, c))) : 0;
      const s = lambda * c.score - (1 - lambda) * div;  // 相关-冗余权衡
      if (s > bestScore) { bestScore = s; best = c; }
    }
    picked.push(best);
    cands = cands.filter(c => c !== best);
  }
  return picked;
}
```
