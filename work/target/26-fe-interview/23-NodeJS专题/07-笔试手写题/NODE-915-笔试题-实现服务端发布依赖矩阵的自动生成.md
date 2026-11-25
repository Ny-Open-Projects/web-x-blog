---
title: [NODE-915] 笔试题——实现发布依赖矩阵自动生成（服务↔服务）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-915：手写依赖矩阵

**需求与边界**：
- 需求：依赖矩阵（SCN-NODE-824/OPS-261）——① 调用关系提取（trace 统计——SCN-NODE-645 数据源）；② 矩阵生成（服务×服务——调用方/被调方）；③ 关键路径识别（SCN-BLD-324）；④ 矩阵变更检测（新依赖出现——SCN-OPS-260）。
- 边界：① trace 数据的聚合（采样率还原——SCN-SLA-724）；② 矩阵的更新频率（周——SCN-OPS-260）；③ 矩阵的消费（评审材料/演练覆盖——SCN-OPS-881/279）。

**答**：
```javascript
async function buildDependencyMatrix() {
  const calls = await traces.aggregateCalls({ window: '7d', restore: 'sample-rate' });   // trace 聚合（SCN-NODE-645/SLA-724）
  const matrix = {};                                   // caller → callees
  for (const c of calls) (matrix[c.caller] ??= new Set()).add(c.callee);
  const critical = longestChain(matrix, weights);      // 关键路径（SCN-BLD-324）
  const newDeps = diffMatrix(matrix, lastMatrix);      // 变更检测（SCN-OPS-260）
  if (newDeps.added.length) audit({ type: 'NEW_DEPENDENCY', deps: newDeps.added });
  return { matrix, critical, newDeps,
    drillGaps: modesWithoutDrill(matrix) };            // 演练缺口（SCN-OPS-279）
}
```

**评分点**:
- trace 数据源 + 采样还原（SCN-NODE-645/SLA-724）。
- 关键路径识别（SCN-BLD-324）。
- 变更检测审计（SCN-OPS-260）。
- 消费（评审/演练——SCN-OPS-881/279）。
