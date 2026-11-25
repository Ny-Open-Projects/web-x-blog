---
title: [1216] 笔试手写：实现 MMR 多样性选择（相关-冗余权衡）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1216：笔试手写：实现 MMR 多样性选择（相关-冗余权衡）

**答**：实现 mmr(cands, simFn, { lambda=0.7, k=5 })：cands 为 { id, score }[]（score 为相关性），simFn(a, b) 返回两候选相似度 0~1。贪心选 k 条：每步选「lambda×score - (1-lambda)×与已选最大相似度」最大者；已选过的跳过。返回选中 id 序列。

```js
function mmr(cands, simFn, { lambda = 0.7, k = 5 } = {}) {
  const pool = [...cands];
  const picked = [];
  while (picked.length < k && pool.length) {
    let best = null, bestScore = -Infinity;
    for (const c of pool) {
      const div = picked.length
        ? Math.max(...picked.map(id => simFn(id, c.id)))
        : 0;                                  // 与已选的最大相似度 = 冗余度
      const s = lambda * c.score - (1 - lambda) * div;
      if (s > bestScore) { bestScore = s; best = c; }
    }
    picked.push(best.id);
    pool.splice(pool.indexOf(best), 1);
  }
  return picked;
}
const cands = [
  { id: 'a', score: 0.9 }, { id: 'a2', score: 0.85 }, { id: 'b', score: 0.8 },
];
const simFn = (x, y) => (x[0] === y[0] ? 0.9 : 0.1);  // 同前缀=同文档近似
console.log(mmr(cands, simFn, { lambda: 0.7, k: 3 }));
// ['a', 'b', 'a2'] —— 同源 a2 被多样性惩罚后移
```

**评分点**：
- MMR 公式正确（lambda×相关 - (1-lambda)×最大冗余）
- 冗余度取「与已选的最大相似度」（不是均值——语义易错）
- 空池/不足 k 的自然终止
- 能讨论：lambda 按意图路由（事实题 lambda→1、综述题→0.5）、相似度函数来源（嵌入向量余弦）

