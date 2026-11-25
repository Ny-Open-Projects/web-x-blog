---
title: [AIC-671] AI 代码审查是赚是亏？净收益怎么算？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-671：AI 代码审查到底是赚是亏？净收益怎么算？

**答**：
- 结论先行：**净收益 = 人工审查节省的时间 − AI 误报带来的处理时间 − 漏报导致的缺陷成本 − AI 调用成本**。只算「节省多少时间」不算「误报代价」是自欺欺人（AIC-050 度量看板 / AIC-043 误报治理）。
- 拆解各项：1) **节省**：AI 发现真实问题让人工不用从头看，按「AI 发现问题数 × 平均人工发现耗时」估；2) **误报代价**：AI 报的假问题，人要逐条判断「这不是问题」，按「误报数 × 判断耗时」——误报多时这项能吃掉全部节省；3) **漏报成本**：AI 没发现、上线后出问题的修复成本（最难量化，用逃逸缺陷反推）；4) **调用成本**：API 费用 + CI 时间。
- 关键是误报率：误报率 > 50% 时工程师会开始忽略 AI 审查（「狼来了」效应），此时净收益为负——治理误报比增加检出更重要（AIC-225 误报治理）。
- 度量方式：抽检 AI 审查意见，标注「真问题/误报」，算精确率；结合缺陷逃逸率看漏报。
- 追问钩子：为什么「误报」的破坏力比「漏报」更隐蔽？——漏报导致 bug，至少有人负责修；误报导致工程师「习惯性忽略」，慢慢整个 AI 审查体系被架空——它不会立刻出事故，而是让防线悄悄失效，等真出事时已经没人看 AI 报告了。

```typescript
type ReviewStats = {
  truePositives: number; falsePositives: number;
  avgHumanDetectMin: number; avgTriageMin: number;
  escapedBugCost: number; apiCost: number;
};

function netBenefit(s: ReviewStats): { netMinutes: number; profitable: boolean; precision: number } {
  const saved = s.truePositives * s.avgHumanDetectMin;
  const fpCost = s.falsePositives * s.avgTriageMin;
  const precision = s.truePositives / Math.max(1, s.truePositives + s.falsePositives);
  const netMinutes = saved - fpCost - s.escapedBugCost - s.apiCost;
  return { netMinutes, profitable: netMinutes > 0, precision };
}

const s: ReviewStats = {
  truePositives: 20, falsePositives: 60, // 误报率75%
  avgHumanDetectMin: 5, avgTriageMin: 2, escapedBugCost: 30, apiCost: 10,
};
const r = netBenefit(s);
console.log(r.precision === 0.25);
console.log(r.netMinutes === 20*5 - 60*2 - 30 - 10); // -30 → 亏损
console.log(r.profitable === false); // 误报吃掉节省
```
