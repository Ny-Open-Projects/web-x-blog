---
title: [ENG-320] 笔试题——实现 AI 评审意见降噪（分级 + 采纳率闭环）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-320：手写 AI 评审降噪

**需求与边界**：
- 需求：AI 评审意见按采纳行为分级闭环——① 记录每条意见的作者响应（fixed/dismissed/waived）；② 按意见类型统计采纳率；③ 采纳率 < 20% 的意见类型自动降级（must-fix→nit→关闭）；④ 相似意见去重（同函数同问题只报一次）。
- 边界：① dismissed 带理由（可分类：误报/已另有方案/不重要）；② 降级有冷却期（7 天内不升级回）；③ 输出意见类型黑名单（完全无效类型）。

**答**：
```javascript
function reviewDenoise(feedbacks, { dropRate = 0.2, cooldown = 7 * 864e5 } = {}) {
  const byType = {};
  for (const f of feedbacks) {
    byType[f.type] ??= { total: 0, acted: 0, dismissReasons: {} };
    byType[f.type].total++;
    if (f.response === 'fixed' || f.response === 'waived-accepted') byType[f.type].acted++;
    if (f.response === 'dismissed')
      byType[f.type].dismissReasons[f.reason] = (byType[f.type].dismissReasons[f.reason] ?? 0) + 1;
  }
  const decisions = {};
  for (const [type, s] of Object.entries(byType)) {
    const rate = s.acted / s.total;
    const current = currentLevel(type);                // must-fix/nit/off
    if (rate < dropRate && current !== 'off' && !inCooldown(type, cooldown))
      decisions[type] = { from: current, to: current === 'must-fix' ? 'nit' : 'off',
        reason: `采纳率 ${(rate * 100).toFixed(0)}%` };   // 降级（ENG-259 生死线）
    if (s.dismissReasons['误报'] / s.total > 0.5)
      decisions[type] = { from: current, to: 'off', reason: '过半误报，规则需修复' };
  }
  return decisions;
}
```

**评分点**:
- 响应三分类（fixed/dismissed/waived）+ dismiss 理由聚合。
- 采纳率分级降级链（must-fix→nit→off，冷却期防震荡）。
- 过半误报直接关闭并提示修规则（不是一刀切降级）。
- 闭环语义：AI 评审不治理会退化成噪音机。
