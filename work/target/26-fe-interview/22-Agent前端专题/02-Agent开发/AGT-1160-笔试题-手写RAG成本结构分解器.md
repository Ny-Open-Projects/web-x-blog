---
title: [1160] 笔试手写：从调用记录分解 RAG 单次问答成本
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 成本]
type: 笔试题
---

## 1160：笔试手写：从调用记录分解 RAG 单次问答成本

**答**：实现 breakdown(calls, price)：calls 为 { stage, model, inTok, outTok, cacheHit? }[]，price 为 { [model]: { in, out, cacheDiscount? } }。计算各 stage 成本与占比（保留 3 位），cacheHit 的输入按 cacheDiscount（如 0.1）计价；总成本保留 4 位；找出占比最高的 stage。

```js
function breakdown(calls, price) {
  const rows = calls.map(c => {
    const p = price[c.model];
    const inCost = c.inTok * p.in * (c.cacheHit ? (p.cacheDiscount ?? 1) : 1);
    const outCost = c.outTok * p.out;
    return { stage: c.stage, cost: inCost + outCost };
  });
  const total = rows.reduce((s, r) => s + r.cost, 0);
  const stages = rows.map(r => ({ ...r,
    share: total ? +(r.cost / total).toFixed(3) : 0 }));
  const top = stages.reduce((m, s) => (s.cost > m.cost ? s : m), stages[0]);
  return { stages, total: +total.toFixed(4), top: top?.stage };
}
const price = { big: { in: 0.002, out: 0.006 }, small: { in: 0.0002, out: 0.0006 } };
const calls = [
  { stage: 'rewrite', model: 'small', inTok: 500, outTok: 50 },
  { stage: 'rerank', model: 'small', inTok: 8000, outTok: 0, cacheHit: true },
  { stage: 'generate', model: 'big', inTok: 4000, outTok: 600 },
];
console.log(breakdown(calls, price).top);  // 'generate'
```

**评分点**：
- cacheHit 折扣只作用于输入部分（输出无折扣概念）
- 占比与总数的精度处理；除零保护
- top 判定用成本而非 token 数（不同模型单价差数倍）
- 能讨论：分解的运营用途——找到「占比最高且可优化」的段（生成段上下文裁剪）、rerank cacheHit 模拟的合理性讨论

