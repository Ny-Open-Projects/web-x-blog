---
title: [TST-867] 如何评估「AI 测试 Agent」的效果（准确率/召回率/人工采纳率）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-867：如何评估「AI 测试 Agent」的效果（准确率/召回率/人工采纳率）？
**答**：
- 结论：AI 测试 Agent 不能只看「生成了多少用例」，要用「有效率（生成的用例中真正有用且被采纳的比例）+ 缺陷发现率 + 误报率」组合度量。
- 核心指标：采纳率（人接受/生成的用例）、有效率（采纳后发现真实问题或长期保留）、幻觉率（引用不存在 API）。
- 召回视角：在已知缺陷集合上，Agent 生成的测试能覆盖多少比例（发现 bug 的召回）。
- 对照实验：与人工基线对比「单位时间发现的有效缺陷数」，证明 AI 是否真的提效而非增加评审负担。
- 追问钩子：AI 生成 100 个用例人采纳了 90 个，但线上缺陷没减少，说明指标哪里出了问题？

```javascript
// AI 测试 Agent 效果评估
function evaluateAgent({ generated, adopted, keptLongTerm, bugsCaught, knownBugs }) {
  return {
    采纳率: Number((adopted / generated).toFixed(3)),
    有效率: Number((keptLongTerm / generated).toFixed(3)),
    幻觉率: Number(((generated - adopted) / generated).toFixed(3)),
    缺陷召回: Number((bugsCaught / knownBugs).toFixed(3)),
  };
}
console.log(evaluateAgent({ generated: 100, adopted: 90,
  keptLongTerm: 30, bugsCaught: 5, knownBugs: 20 }));
// 采纳率高但有效率仅 0.3 -> 说明很多用例被采纳却没长期价值
```
