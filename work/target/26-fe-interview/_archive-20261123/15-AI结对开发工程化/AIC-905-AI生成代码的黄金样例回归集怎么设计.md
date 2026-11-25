---
title: [AIC-905] 为了让 AI 生成的代码可回归验证，「黄金样例集」应该怎么设计才不会变成摆设？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-905：为了让 AI 生成的代码可回归验证，「黄金样例集」应该怎么设计才不会变成摆设？
**答**：
- 黄金样例要「小而精、覆盖决策分支」：每个样例代表一类输入/边界，而不是把历史 bug 全堆进去——结论：样例是规格的具象化，不是 bug 博物馆。
- 每个样例必须带「预期输出 + 为什么」的注释，这样样例变更时能评审，AI 也能从注释理解意图。
- 样例要分层：核心路径（必过）、边界路径（如空数组/超限）、对抗路径（恶意输入）三层，CI 按层决定阻断还是告警。
- 要有「样例淘汰机制」：长期不再触发差异的样例归档，需求变化时及时更新，避免样例库腐化。
- 追问钩子：能说「黄金样例需要像产品代码一样被维护、有 owner、有评审」的候选人，把测试资产当成一等公民。

```typescript
// 分层黄金样例集
const golden = [
  { layer:'core', input:{ price:100, qty:2 }, expect:200, why:'常规计价' },
  { layer:'edge', input:{ price:100, qty:0 }, expect:0,   why:'数量为0边界' },
  { layer:'adversarial', input:{ price:-1, qty:2 }, expect:0, why:'负价格防御' },
];
function runGolden(impl, layer) {
  return golden.filter(g => !layer || g.layer === layer).map(g => {
    const got = impl(g.input);
    return { layer:g.layer, pass: got === g.expect, why:g.why };
  });
}
const blockingFail = runGolden(impl => impl.price * impl.qty, 'core').some(r => !r.pass);
// core 失败阻断合并；edge/adversarial 失败可告警——分层决定处置
```
