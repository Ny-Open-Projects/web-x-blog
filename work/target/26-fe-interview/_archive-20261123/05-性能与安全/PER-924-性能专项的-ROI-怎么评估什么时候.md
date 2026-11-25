---
title: [PER-924] 性能专项的 ROI 怎么评估？什么时候该止损
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-924：性能专项的 ROI 怎么评估？什么时候该止损

**答**：
- 收益模型：专项收益 =（指标提升 × 业务弹性系数）- 人力成本 - 维护成本；弹性系数来自 RUM 关联分析或行业基准。
- 止损信号：连续两轮优化指标无显著变化（< 3%）、方案引入的复杂度导致故障率上升、剩余瓶颈在非前端环节（服务端/网络基建）。
- 优先级矩阵：按「影响用户数 × 可行性 × 收益」排序候选优化项，低垂果实先做，深水项立项评审。
- 止损后动作：归档结论（为什么不可行）、保留已完成的低成本改进、瓶颈移交对应团队并给出前端视角证据。

```javascript
// 优化项优先级打分
function prioritize(items) {
  return items.map(i => ({ ...i,
    score: i.users * i.feasibility * i.expectedGain / i.cost }))
    .sort((a, b) => b.score - a.score);
}
// 止损判定
function shouldStop(rounds, { minGain = 0.03, maxRounds = 3 } = {}) {
  const gains = rounds.slice(-2).map(r => r.gain);
  return rounds.length >= maxRounds || gains.every(g => g < minGain);
}
```
