---
title: [HW-206] 手写 SLO 计算器——滑动窗口达标率 + 错误预算消耗率 + 燃尽告警
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：SRE 式 SLO：目标（如 28 天窗口 CWV 达标率 ≥ 75%）→ 错误预算（25% 不达标份额）→ 消耗率（当前窗口不达标率/预算）→ 燃尽速度告警（消耗速度 > 1 = 将在窗口末前耗尽预算——需要行动）。实现为纯函数（输入桶计数，输出达标率/预算/燃尽）。

```javascript
function sloCalculator({ goodCount, totalCount, windowDays = 28, targetRatio = 0.75 }) {
  const passRatio = totalCount ? goodCount / totalCount : 1;
  const errorBudget = 1 - targetRatio;                    // 允许不达标份额
  const consumed = Math.max(0, 1 - passRatio);            // 当前不达标率
  const burnRate = errorBudget ? consumed / errorBudget : (consumed > 0 ? Infinity : 0);
  // 燃尽速度：1 = 匀速耗尽恰好用完窗口；> 1 = 提前耗尽（需行动）
  const daysToExhaust = burnRate > 0 ? windowDays / burnRate : Infinity;
  return {
    passRatio: +passRatio.toFixed(4),
    budgetLeft: Math.max(0, +(errorBudget - consumed).toFixed(4)),
    burnRate: +burnRate.toFixed(2),
    daysToExhaust: Math.round(daysToExhaust),
    verdict: burnRate > 1 ? 'action-required' : burnRate > 0.8 ? 'watch' : 'healthy',
  };
}
// sloCalculator({ goodCount: 700, totalCount: 1000 })
// => passRatio 0.70, budgetLeft 0, burnRate 1.2, daysToExhaust 23, verdict 'action-required'
// 联动：burnRate > 1 触发告警（PER-337 阈值告警的 SRE 升级版——不是"超线"而是"将超线"）
// 多窗口分级：1h 窗口快燃尽告警（急）+ 28 天窗口慢燃尽告警（慢性劣化 PER-450）
```

**评分点**：
- 错误预算与燃尽率公式（consumed/errorBudget）——本题核心。
- verdict 三级（healthy/watch/action-required）与 daysToExhaust 可解释性。
- 双窗口分级告警（急/慢性）联动 PER-337。
- 与达标率的区别：达标率是状态，燃尽率是速度（速度才能预警）。
