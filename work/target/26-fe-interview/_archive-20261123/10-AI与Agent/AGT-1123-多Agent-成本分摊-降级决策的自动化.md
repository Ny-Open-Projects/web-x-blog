---
title: [1123] Agent 链路里「这个子任务值不值得跑」怎么自动决策
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 决策]
type: 面试题
---

## 1123：Agent 链路里「这个子任务值不值得跑」怎么自动决策

**答**：
- 决策输入：子任务预期收益（对最终质量的边际贡献，来自评估数据）× 成功概率（历史通过率）vs 成本（token+时间）；期望值为负就跳过或降级。
- 典型场景：校对类子任务在「低风险输出」上收益趋近零（出错概率本来就低），自动跳过；在「高风险输出」（涉及金额/对外文案）上无条件执行。
- 决策可解释：跳过/降级要在 trace 记录决策依据（收益估计、成本估计），否则「为什么这条没校对」无法回答。
- 追问钩子：收益估计从哪来？——分层统计：每类子任务在「有/无」两种状态下的端到端质量差（做消融实验），数据积累后决策越来越准。

```ts
function shouldRun(step, ctx) {
  const gain = step.marginalGain[ctx.riskTier];   // 消融实验得来的边际收益
  const p = step.passRate[ctx.intent];
  const ev = gain * p - step.cost.estimate(ctx);
  if (ev < 0 && ctx.riskTier !== 'high') {
    trace.log({ skip: step.id, ev, reason: 'negative EV' });  // 决策可解释
    return false;
  }
  return true;
}
```

