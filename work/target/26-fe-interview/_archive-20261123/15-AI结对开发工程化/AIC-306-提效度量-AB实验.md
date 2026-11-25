---
title: [AIC-306] 如何对「新的 AI 工作流规则」（如新评审门禁）做 AB 实验？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-306：如何对「新的 AI 工作流规则」（如新评审门禁）做 AB 实验？
**答**：
- 随机化单元：按团队/仓库随机而非按 PR（避免同组互相污染）。
- 样本量预估：周期类指标方差大，通常需要 4-8 周或 200+ PR 才有显著功效。
- 保护指标：实验同时监控守护指标（缺陷率/采纳率），恶化即提前停止。
- 持续运行护栏：实验结束保留 10% 对照组持续观测，防回归效应。

```javascript
const ab = {
  unit: 'team-level randomization',
  power: { alpha: 0.05, power: 0.8, mde: '-15% cycle time', estWeeks: 6 },
  guard: ['bugEscape', 'adoptionRate'], // 恶化 > 10% 提前终止
  after: 'keep 10% holdout for 4 weeks',
};
r
```
