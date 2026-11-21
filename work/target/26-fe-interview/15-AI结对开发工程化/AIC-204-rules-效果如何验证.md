---
title: [AIC-204] 你怎么验证一条新加的 Cursor rule 真的提升了产出质量，而不是污染上下文？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-204：你怎么验证一条新加的 Cursor rule 真的提升了产出质量，而不是污染上下文？
**答**：
- 做规则 A/B：同一批任务（固定 prompt 集）分别在带/不带该规则的会话里跑，产出做盲评或自动化校验。
- 量化指标：一次通过率、lint/类型错误数、人工修改行数（diff 与 AI 产出的比值）。
- 观察 token 消耗与响应速度，规则过多会显著稀释注意力（lost in the middle 效应）。
- 沉淀为「规则评测集」：把历史失败案例做成回归用例，规则变更时重跑。

```javascript
// 规则评测集最小实现：给定任务集，统计一次通过率
async function evalRule(tasks: string[], ruleOn: boolean) {
  let pass = 0;
  for (const t of tasks) {
    const out = await runAgent(t, { rules: ruleOn ? ['base', 'strict-ts'] : ['base'] });
    const ok = await verify(out); // 类型检查 + 测试 + lint
    if (ok) pass++;
  }
  return { ruleOn, passRate: pass / tasks.length };
}
// 期望 strict 开启后 passRate 提升 ≥ 10%，否则考虑删除或改写该规则
r
```
