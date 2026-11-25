---
title: [1248] 笔试手写：实现 Agent 步数预算分配器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## 1248：笔试手写：实现 Agent 步数预算分配器

**需求**：实现 allocateSteps(tasks)：tasks 为 { id, complexity: 1|2|3 }[]，总预算 budget 步。按复杂度加权分配（权重 1:2:4），每任务保底 2 步；保底总额超过 budget 时按复杂度降序砍掉末位任务并返回 trimmed 列表；分配后剩余余量按权重再分配（整除余数给高复杂度）。返回 { alloc: Map, trimmed }。

```js
function allocateSteps(tasks, budget) {
  const W = { 1: 1, 2: 2, 3: 4 };
  let list = [...tasks].sort((a, b) => b.complexity - a.complexity);
  const trimmed = [];
  while (list.length * 2 > budget) trimmed.push(list.pop()); // 保底 2 步放不下
  const totalW = list.reduce((s, t) => s + W[t.complexity], 0);
  const alloc = new Map();
  let used = 0;
  for (const t of list) {
    const n = Math.floor(budget * W[t.complexity] / totalW);
    alloc.set(t.id, Math.max(2, n)); used += Math.max(2, n);
  }
  let rest = budget - used; // 余量按权重回填
  for (const t of list) {
    if (rest <= 0) break;
    alloc.set(t.id, alloc.get(t.id) + 1); rest--;
  }
  return { alloc, trimmed: trimmed.map(t => t.id) };
}
```

**评分点**：
- 保底优先于按比例分配（先保障后加权）
- 砍任务按复杂度降序保高优
- 余量回填规则明确且不超预算
- 能讨论：预算与最大步数熔断（AGT-136）的配合
