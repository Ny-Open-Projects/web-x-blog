---
title: [1202] 笔试手写：实现按任务聚合的工具调用成本与轮次统计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 成本延迟]
type: 笔试题
---

## 1202：笔试手写：实现按任务聚合的工具调用成本与轮次统计

**答**：实现 taskCost(calls)：calls 为 { taskId, agent, tokens: { in, out }, priceIn, priceOut, round }[]（round 为该任务第几轮）。按任务聚合输出 { [taskId]: { rounds, totalTokens, cost } }（cost = in*priceIn + out*priceOut，2 位）；全局平均轮次 avgRounds（1 位）与最贵任务 top（taskId）。

```js
function taskCost(calls) {
  const agg = {};
  for (const c of calls) {
    const t = (agg[c.taskId] ??= { rounds: 0, totalTokens: 0, cost: 0 });
    t.rounds = Math.max(t.rounds, c.round);          // 轮次取最大值
    t.totalTokens += c.tokens.in + c.tokens.out;
    t.cost += c.tokens.in * c.priceIn + c.tokens.out * c.priceOut;
  }
  for (const t of Object.values(agg)) t.cost = +t.cost.toFixed(2);
  const list = Object.entries(agg);
  const avgRounds = list.length
    ? +(list.reduce((s, [, t]) => s + t.rounds, 0) / list.length).toFixed(1) : 0;
  const top = list.sort((a, b) => b[1].cost - a[1].cost)[0]?.[0] ?? null;
  return { tasks: agg, avgRounds, top };
}
const calls = [
  { taskId: 'T1', agent: 'coder', tokens: { in: 1000, out: 200 },
    priceIn: 0.002, priceOut: 0.006, round: 1 },
  { taskId: 'T1', agent: 'coder', tokens: { in: 800, out: 300 },
    priceIn: 0.002, priceOut: 0.006, round: 2 },
  { taskId: 'T2', agent: 'qa', tokens: { in: 500, out: 100 },
    priceIn: 0.001, priceOut: 0.003, round: 1 },
];
console.log(taskCost(calls));
// T1: rounds 2, tokens 2300, cost 5.40；T2: 1, 600, 0.80；top T1
```

**评分点**：
- rounds 取 max 而非累加（每轮一条调用记录——语义易错）
- 成本公式与精度；top 的排序取首
- 空输入 avgRounds=0、top=null 保护
- 能讨论：任务级成本与账单分摊的联动、avgRounds 的容量规划用途

