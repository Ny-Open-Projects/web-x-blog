---
title: [NODE-948] 笔试题——实现发布质量趋势看板（发布模式分析）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-948：手写质量趋势

**需求与边界**：
- 需求：发布质量趋势（SCN-OPS-948/ENG-323）——① 发布模式分析（星期/时段/变更大小——SCN-OPS-948）；② 高危模式识别（SCN-OPS-948）；③ 趋势与基线（SCN-OPS-948）；④ 模式→规则回灌（SCN-OPS-322）。
- 边界：① 样本下限（SCN-OPS-948）；② 相关非因果（SCN-OPS-948）；③ 报告的消费（发布日历回灌——SCN-OPS-258）。

**答**：
```javascript
async function releaseQualityTrend(releases) {
  const patterns = analyzePatterns(releases, { dims: ['weekday', 'hour', 'size'],
    minSamples: 5, baseline: 'overall' });             // SCN-OPS-948 三维
  const highRisk = patterns.filter(p => p.rate > p.base * 2);   // 2× 基线
  return {
    patterns, highRisk,
    rules: highRisk.map(p => p.ruleSuggest),           // 规则回灌（SCN-OPS-322）
    trend: qualityTrend(releases),                     // 趋势（SCN-OPS-948）
    note: '模式相关性，非因果（SCN-OPS-948）',
  };
}
```

**评分点**:
- 三维模式分析（SCN-OPS-948）。
- 高危模式 → 规则回灌（SCN-OPS-322）。
- 样本下限 + 相关非因果（SCN-OPS-948）。
- 趋势（SCN-OPS-948）。
