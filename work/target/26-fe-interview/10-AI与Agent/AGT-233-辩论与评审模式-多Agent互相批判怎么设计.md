---
title: [AGT-233] 辩论与评审模式——多 Agent 互相批判提升输出质量怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-233：生成-批判（debate/critic）模式怎么设计才有效而不是互相客气？

**答**:
- 有效批判的三个条件：批判者角色独立（不同系统提示，甚至不同模型——同源模型容易互相认同）、批判维度明确（按清单批：事实性/逻辑/边界/成本，不是"整体不错"）、有迭代上限与收敛判据（两轮后无新意见即收敛，防止无限拉扯）。
- 流程设计：Generator 产出 → Critic 逐维度批（必须给出可执行的修改意见与依据）→ Generator 修订并逐条回应（采纳/不采纳+理由）→ 终审（Judge 或人）裁决——修订回应制防止敷衍。
- 成本控制：辩论模式成本是单模型的 3~5 倍——只对高风险输出启用（发布文案/方案决策/安全相关），低风险任务走单模型+规则校验；批判者用便宜模型是常见降本。
- 反模式识别：批判一轮就"完美了"（批判者敷衍）、越改越平庸（多轮平均化）——前者换更强批判者，后者限制修订轮数并保留原始版本对比。

```javascript
async function generateWithCritique(task) {
  let draft = await generator(task);
  for (let i = 0; i < 2; i++) {            // 迭代上限
    const critiques = await critic(`
      按维度批：事实性/逻辑/边界/成本。
      每条给修改意见+依据。`, draft);
    if (critiques.every(c => c.severity === 'minor')) break; // 收敛
    draft = await generator(`修订并逐条回应：
      ${critiques}`, draft);                // 修订+回应制
  }
  return judge(task, draft);               // 终审裁决
}
```
