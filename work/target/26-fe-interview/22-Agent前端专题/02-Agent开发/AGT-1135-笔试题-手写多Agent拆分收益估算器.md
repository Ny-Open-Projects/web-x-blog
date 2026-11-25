---
title: [1135] 笔试手写：实现拆分收益估算（质量/延迟/协调成本）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 决策]
type: 笔试题
---

## 1135：笔试手写：实现拆分收益估算（质量/延迟/协调成本）

**答**：实现 splitScore(single, plan)：single = { latencyMs, cost, acc }；plan = { agents: [{ latencyMs, cost, acc }], msgOverheadMs, msgCost }（串行链路假设：延迟相加、质量取 min（木桶）、成本相加）。返回 { latencyGain, costDelta, accDelta, verdict }（accDelta ≥ 0.02 且 costDelta < 0.3 判 'split'，否则 'keep'），数值保留 3 位。

```js
function splitScore(single, plan) {
  const latency = plan.agents.reduce((s, a) => s + a.latencyMs, 0) + plan.msgOverheadMs;
  const cost = plan.agents.reduce((s, a) => s + a.cost, 0) + plan.msgCost;
  const acc = Math.min(...plan.agents.map(a => a.acc));   // 木桶效应
  return {
    latencyGain: +(single.latencyMs - latency).toFixed(3),
    costDelta: +((cost - single.cost) / single.cost).toFixed(3),
    accDelta: +(acc - single.acc).toFixed(3),
    verdict: (acc - single.acc) >= 0.02 && (cost - single.cost) / single.cost < 0.3
      ? 'split' : 'keep',
  };
}
const s = { latencyMs: 3000, cost: 1, acc: 0.80 };
const p = { agents: [{ latencyMs: 800, cost: 0.4, acc: 0.9 },
  { latencyMs: 1000, cost: 0.5, acc: 0.95 }], msgOverheadMs: 200, msgCost: 0.1 };
console.log(splitScore(s, p));
// { latencyGain: 1000, costDelta: 0, accDelta: 0.1, verdict: 'split' }
```

**评分点**：
- 串行延迟相加 + 消息开销计入；质量取 min（短板决定链路质量）
- costDelta 是相对比例、accDelta 是绝对差，两种口径不混
- 判定条件双门槛（质量必须提升 + 成本增幅受限）
- 能讨论：并行拓扑时延迟取 max 而非相加；min(accuracy) 假设的适用边界（有重试/补偿时可放宽）

