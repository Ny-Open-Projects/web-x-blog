---
title: [NODE-923] 笔试题——实现灰度指标异常自动归因（异常→候选原因）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-923：手写异常归因

**需求与边界**：
- 需求：灰度异常归因（SCN-SLA-716/OPS-234）——① 异常检测（SCN-OPS-723 三类检测）；② 候选原因排序（变更集关联——SCN-OPS-716）；③ 排除项列出（SCN-OPS-716 候选语义）；④ 归因报告（人工确认前——SCN-OPS-716）。
- 边界：① 候选的置信度（SCN-OPS-716）；② 变更集来源（发版/配置/依赖——SCN-OPS-260）；③ 归因与决策树联动（SCN-OPS-234）。

**答**：
```javascript
async function anomalyAttribution(anomaly, release) {
  const changes = await changesets.in(anomaly.window);   // 变更集（SCN-OPS-716）
  const candidates = changes.map(c => ({
    change: c, confidence: correlate(c, anomaly.series),   // 置信度（SCN-OPS-716）
  })).sort((a, b) => b.confidence - a.confidence);
  const excluded = await exclusions(anomaly);          // 排除项（SCN-OPS-716 语义）
  return {
    candidates, excluded,
    summary: autoSummary(anomaly, candidates),         // 「疑似」措辞（SCN-OPS-716）
    decisionTree: candidates.length ? routeToOps234(anomaly, candidates[0]) : 'MANUAL',   // 决策树（SCN-OPS-234）
    humanConfirmed: false,                             // 人工确认前（SCN-OPS-716）
  };
}
```

**评分点**:
- 候选原因 + 置信度（SCN-OPS-716）。
- 排除项列出（SCN-OPS-716 语义）。
- 决策树联动（SCN-OPS-234）。
- 人工确认前标记（SCN-OPS-716）。
