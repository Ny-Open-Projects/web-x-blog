---
title: [SOFT-659] 手写 careerQuadrant：绩效与环境机会输入、象限判定、行动建议、复评日期？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-659：手写 careerQuadrant：绩效与环境机会输入、象限判定、行动建议、复评日期

**需求与边界**：
- 实现 careerQuadrant({ rating, trend, envOpportunity, fixable })。
- 边界要求：① rating ∈ {high, low}，trend ∈ {up, flat, down}；② 四象限判定（高+好机会=加码/高+差机会=试水/低+可修复=改进周期/低+不可修复=外部为主）；③ 趋势修正：down 趋势时"高绩效+试水"升级为"优先试水"；④ 每个建议带复评日期（3 个月后）；⑤ 输入缺字段抛错。

**答**：
```javascript
function careerQuadrant({ rating, trend, envOpportunity, fixable }) {
  for (const k of ['rating', 'trend', 'envOpportunity', 'fixable'])
    if (arguments[0][k] === undefined)
      throw new Error(`缺字段：${k}`);
  const map = {
    'high-good': { action: '加码投入（晋升窗口全力冲）',
      recheck: '+3mo' },
    'high-poor': { action: rating === 'high' && trend === 'down'
        ? '优先试水外部（下滑趋势下环境机会差=强信号）'
        : '内部转岗评估+外部试水（市场定价检验）',
      recheck: '+3mo' },
    'low-good': fixable
      ? { action: '一个周期改进（差距清单+领导支持）',
          recheck: '+1季度' }
      : { action: '改进+外部并行（可修复存疑）', recheck: '+2mo' },
    'low-bad': { action: '外部机会为主，内部自救为辅',
      recheck: '+1mo' },
  };
  const key = `${rating}-${envOpportunity}`;
  const out = map[key];
  return { ...out,
    recheckAt: new Date(Date.now() +
      parseInt(out.recheck.slice(1)) * 30 * 864e5).toISOString().slice(0, 10),
    note: '以3个月为单位评估，不因单次评级冲动决策' };
}
```

**评分点**:
- 四象限判定完整；趋势修正逻辑（down 时升级行动紧迫度）。
- fixable 不可修复时行动组合调整；复评日期强制（决策纪律）。
- 缺字段抛错（输入完整性）。

