---
title: [1258] 笔试手写：实现 rerank 预算裁剪器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 检索]
type: 笔试题
---

## 1258：笔试手写：实现 rerank 预算裁剪器

**答**：实现 rerankBudget(candidates, budget)：candidates 为 { id, vecScore, ms }[]（精排单条耗时 ms）。在总耗时预算 budget 内选送精排的子集：按 vecScore 降序依次装入，直到预算耗尽；但至少送 1 条，且分数差距 < 0.01 的候选必须整组同送或同舍（防相近结果被腰斩）。返回 { picked, cost }。

```js
function rerankBudget(candidates, budget) {
  const sorted = [...candidates].sort((a, b) => b.vecScore - a.vecScore);
  const picked = [];
  let i = 0, cost = 0;
  while (i < sorted.length) {
    // 同分组：分数差 < 0.01 的连续段
    let j = i;
    while (j + 1 < sorted.length && sorted[j].vecScore - sorted[j + 1].vecScore < 0.01) j++;
    const group = sorted.slice(i, j + 1);
    const gCost = group.reduce((s, c) => s + c.ms, 0);
    if (picked.length === 0 || cost + gCost <= budget) { // 首组强制送
      picked.push(...group); cost += gCost;
    } else break;
    i = j + 1;
  }
  return { picked: picked.map(c => c.id), cost };
}
```

**评分点**：
- 分数相近整组同送（避免语义等价候选被预算腰斩）
- 至少送一组的首组保底
- 预算判断在累加前
- 能讨论：预算耗尽后未精排候选的降级呈现方式（标注未精排）
