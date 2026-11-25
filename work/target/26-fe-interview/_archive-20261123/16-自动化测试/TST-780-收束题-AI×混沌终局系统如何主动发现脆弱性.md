---
title: [TST-780] 收束题：AI×混沌终局——系统如何「主动」发现脆弱性
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-780：收束题：AI×混沌终局——系统如何「主动」发现脆弱性

**答**：
- 结论：终局是「持续验证闭环」——AI 从监控/事故/变更中持续生成假设与盲区，自动设计低风险实验验证，人只把关高危动作，系统逐步自我加固。
- 闭环四步：观测（找异常与盲区）→ 假设（AI 生成可证伪假设）→ 验证（受控注入 + 确定性断言）→ 固化（发现转成回归用例）。
- 关键底线：爆炸半径可控、回滚秒级、人在环审批高危、每次实验可追溯。
- 追问钩子：系统越来越「自动」，如何防止它自己把标准越调越松？

```javascript
// 持续验证闭环：观测→假设→验证→固化
function resilienceLoop(observations) {
  const blindSpots = observations.filter(o => !o.testedRecently);
  const hypothesis = blindSpots.map(o => ({
    metric: o.metric, threshold: o.slo, injectPoint: o.weakPoint,
  }));
  return {
    nextExperiments: hypothesis.slice(0, 3),
    guardrails: ['爆炸半径受限', '秒级回滚', '高危人工审批'],
  };
}
console.log(resilienceLoop([
  { metric: 'errorRate', slo: 0.01, weakPoint: 'pay-sdk', testedRecently: false },
]));
```
