---
title: [AIC-050] AI Review 的度量看板应该看哪些指标？怎么判断「AI 审查是赚是亏」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-050：AI Review 的度量看板应该看哪些指标？怎么判断「AI 审查是赚是亏」？
**答**：
- 效果指标：意见采纳率（核心）、blocker 抓出数、线上缺陷回溯中「AI 曾提示但被忽略」的比例（漏报成本）。
- 成本指标：每次 review 的 token 费用 × PR 数、AI 意见导致的人类 review 延迟变化。
- 健康指标：误报率趋势、豁免率、意见分布（如果 90% 是 nit，说明清单该改了）。
- 算账方法：抓出一个 blocker 的平均成本 vs 这些缺陷流到线上的平均修复成本，前者低一个量级就是赚。
- 追问钩子：看板要按「清单项」下钻——哪类检查贡献了最多采纳率，哪类纯噪音，这是 prompt 迭代的依据。

```javascript
// 看板指标聚合
function reviewMetrics(prs) {
  const all = prs.flatMap(p => p.findings);
  return {
    adoptionRate: count(all, f => f.accepted) / all.length,
    blockerCaught: count(all, f => f.level === 'blocker' && f.accepted),
    falsePositiveRate: count(all, f => f.markedFalse) / all.length,
    costPerPr: avg(prs.map(p => p.reviewCost)),
    byChecklist: groupBy(all, f => f.checklistItem).map(kv => ({ item: kv.key, rate: adoption(kv.values) })),
  };
}
```
