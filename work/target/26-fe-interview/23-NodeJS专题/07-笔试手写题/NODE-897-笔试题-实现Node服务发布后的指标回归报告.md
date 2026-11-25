---
title: [NODE-897] 笔试题——实现发布后指标回归报告（自动生成）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-897：手写回归报告

**需求与边界**：
- 需求：发布回归报告（SCN-OPS-708/298）——① 多指标回归（错误率/延迟/资源 vs 前版本——SCN-OPS-239）；② 自动叙述（结论模板——SCN-SLA-708）；③ 标注（发版/活动——SCN-SLA-708）；④ 报告归档（发布档案——SCN-OPS-248）。
- 边界：① 对比窗口（发布后 1h——SCN-OPS-246 混合段剔除）；② 最差三件事（SCN-SLA-708 强制）；③ 报告的分发（团队/管理层——SCN-OPS-868 两版）。

**答**：
```javascript
async function releaseRegressionReport(release) {
  const after = await metrics.slice({ version: release.version, window: cut(release, 3600_000) });   // 混合段剔除（SCN-OPS-747）
  const before = await metrics.slice({ version: release.stableVer });
  const rows = metricCompare(after, before);           // SCN-OPS-239 对比
  const worst = rows.sort(byRegression).slice(0, 3);   // 最差三件（SCN-SLA-708 强制）
  const annotations = eventsIn(release.window);        // 标注（SCN-SLA-708）
  return {
    narrative: autoNarrative(rows, worst),             // 结论模板
    rows, worst, annotations,
    archive: releaseArchive(release, rows),            // 发布档案（SCN-OPS-248）
  };
}
```

**评分点**:
- 多指标对比 + 混合段剔除（SCN-OPS-239/747）。
- 最差三件强制 + 自动叙述（SCN-SLA-708）。
- 标注（发版/活动）+ 档案归档（SCN-OPS-248）。
- 两版分发（SCN-OPS-868）。
