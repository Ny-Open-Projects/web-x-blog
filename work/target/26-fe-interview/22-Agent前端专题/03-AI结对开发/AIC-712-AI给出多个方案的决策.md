---
title: [AIC-712] AI 一次给出多个方案时如何做取舍决策
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-712：AI 一次给出多个方案时如何做取舍决策

**答**：
- 结论先行：不要让 AI「替你选」，而要建立可复用的决策标准——把多方案放进同一个评估矩阵（正确性、可维护性、成本、风险、团队熟悉度）逐项打分，人保留最终裁决权。
- 决策步骤：1) 先澄清方案是否真正互斥（有时只是表述不同）；2) 用同一组约束过滤掉明显不可行的；3) 对剩余方案按「最大风险点」而非「最优平均」排序；4) 记录选择理由供回溯。
- 常见陷阱：被 AI 的「推荐方案」措辞锚定；方案描述详略不一导致误判——要求 AI 用统一模板输出方案。
- 追问钩子：为什么按「最大风险点」而非「平均分」选方案？——生产中击垮项目的是最差情况，不是平均表现。

```javascript
// 方案决策矩阵：统一维度打分，按最大风险排序
function pickPlan(plans, weights) {
  const dims = ['correct', 'maintain', 'cost', 'risk', 'familiar'];
  const scored = plans.map(p => ({
    name: p.name,
    score: dims.reduce((s, d) => s + (p.scores[d] ?? 0) * weights[d], 0),
    worstRisk: Math.max(...dims.map(d => (1 - (p.scores[d] ?? 0)) * weights[d])),
  }));
  return scored.sort((a, b) => a.worstRisk - b.worstRisk || b.score - a.score)[0];
}
const w = { correct: 3, maintain: 2, cost: 1, risk: 3, familiar: 1 };
console.log(pickPlan([
  { name: 'A', scores: { correct: 1, maintain: .8, cost: .5, risk: .4, familiar: .9 } },
  { name: 'B', scores: { correct: .9, maintain: .9, cost: .9, risk: .9, familiar: .7 } },
], w).name); // B（最大风险更低）
```
