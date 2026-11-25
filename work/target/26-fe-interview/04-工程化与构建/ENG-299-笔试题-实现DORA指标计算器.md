---
title: [ENG-299] 笔试题——实现 DORA 四指标计算器（部署频率/前置时间/失败率/MTTR）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-299：手写 DORA 计算器

**需求与边界**：
- 输入：部署事件、PR 事件（创建/合并）、事故事件（发生/恢复）；输出四指标 + 分级（elite/high/medium/low）。
- 边界：① 前置时间 = PR 合并到部署的时长（不是 PR 创建到合并）；② 变更失败率 = 导致回滚/hotfix 的部署占比（部署后 24h 内出事故归属该部署）；③ MTTR 只统计有恢复事件的事故。

**答**：
```javascript
function dora(deploys, prs, incidents, { attribution = 24 * 3600_000 } = {}) {
  const sorted = [...deploys].sort((a, b) => a.ts - b.ts);
  const leadTimes = prs.filter(p => p.mergedTs && p.deployTs)
    .map(p => p.deployTs - p.mergedTs);
  const freq = sorted.length / (rangeDays(deploys) || 1);
  // 失败率：部署后 24h 内出事故归属该部署
  const failedDeploys = new Set();
  for (const inc of incidents) {
    const dep = latestBefore(sorted, inc.ts, attribution);
    if (dep) failedDeploys.add(dep.id);
  }
  const failRate = sorted.length ? failedDeploys.size / sorted.length : 0;
  const mttrs = incidents.filter(i => i.recoveredTs)
    .map(i => i.recoveredTs - i.ts);
  const leadP50 = quantile([...leadTimes].sort((a, b) => a - b), 0.5);
  return {
    deployFreq: freq, leadTime: leadP50,
    changeFailRate: failRate, mttr: quantile([...mttrs].sort((a, b) => a - b), 0.5),
    grade: gradeDORA(freq, leadP50, failRate, quantile([...mttrs].sort((a, b) => a - b), 0.5)),
  };
}
function gradeDORA(freq, lead, fail, mttr) {           // DORA 分级表
  if (freq >= 7 && lead <= 864e5 && fail <= 0.05 && mttr <= 36e5) return 'elite';
  if (freq >= 1 && lead <= 7 * 864e5 && fail <= 0.1 && mttr <= 864e5) return 'high';
  return fail <= 0.2 ? 'medium' : 'low';
}
```

**评分点**:
- 前置时间口径正确（merge→deploy 而非 PR 全程）。
- 事故归属窗口（24h 内回溯部署）。
- MTTR 只计有恢复事件的（口径诚实）。
- 分级表标准（elite/high/medium/low）。
