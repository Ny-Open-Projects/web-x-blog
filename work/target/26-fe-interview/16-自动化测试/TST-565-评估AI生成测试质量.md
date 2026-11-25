---
title: [TST-565] 如何评估 AI 生成测试的质量
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-565：如何评估 AI 生成测试的质量

**答**：
- 结论：多维度评估——有效性（能抓 bug/变异分数）、正确性（自身不误报）、可维护性（可读/稳定）、覆盖率（补了多少边界），并对比人工基线。
- 做法：用变异测试衡量「AI 用例杀死突变的能力」；统计采纳率/修改率/删除率；跟踪 AI 用例的 flaky 率与存活周期；A/B 对比引入 AI 前后的逃逸缺陷。
- 追问钩子：AI 用例通过率高就说明质量好吗？——不一定，可能断言太弱；要用变异分数与断言强度交叉验证，避免「绿但无效」的测试。

```javascript
// AI 用例质量分：变异分数 + 断言强度 + 稳定性
const WEIGHTS = { mutationScore: 0.5, assertionStrength: 0.3, stability: 0.2 };
function aiQuality(m) {
  const breakdown = {
    mutationScore: m.mutationScore,
    assertionStrength: m.assertionStrength,
    stability: 1 - m.flakyRate,
  };
  const score = Object.keys(WEIGHTS).reduce((s, k) => s + breakdown[k] * WEIGHTS[k], 0);
  return { score: +score.toFixed(3), breakdown,
    trustworthy: m.mutationScore >= 0.6 && m.flakyRate <= 0.02 };
}
// 对比人工基线：AI 用例是否真的达到可用水平
function vsBaseline(aiCases, humanAvg) {
  const avg = aiCases.reduce((s, c) => s + aiQuality(c).score, 0) / aiCases.length;
  return { aiAvg: +avg.toFixed(3), humanAvg, gap: +(avg - humanAvg).toFixed(3) };
}
console.log(vsBaseline([
  { mutationScore: 0.7, assertionStrength: 0.8, flakyRate: 0.01 },
  { mutationScore: 0.5, assertionStrength: 0.6, flakyRate: 0.05 },
], 0.72));
```
