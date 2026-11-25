---
title: [NODE-936] 笔试题——实现多服务灰度一致性巡检（跨服务版本组合）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-936：手写一致性巡检

**需求与边界**：
- 需求：多服务一致性（SCN-OPS-927/924）——① 跨服务版本组合巡检（运行时组合——SCN-OPS-927）；② 一致性约束声明（上游灰度依赖下游 canary——SCN-NODE-924）；③ 巡检报告（SCN-OPS-256）；④ 巡检的门禁（SCN-OPS-829）。
- 边界：① 巡检的频率（发布期间 1min——SCN-OPS-207）；② 约束的来源（发布计划——SCN-OPS-251）；③ 巡检的告警（SCN-OPS-256）。

**答**：
```javascript
cron('*/1m', async () => {
  const combos = await runtimeVersionCombos(activeReleases());   // 运行时组合（SCN-OPS-927）
  const violations = combos.filter(c => !compatMatrix.has(c) || !constraintSatisfied(c, plans));
  if (violations.length)
    alert({ type: 'MULTI_SERVICE_INCONSISTENT', violations,
      fix: violations.map(v => `对齐 ${v.upstream} 与 ${v.downstream} 版本（SCN-OPS-251 拓扑）`) });
  if (violations.some(v => v.blocking)) gateBlock(violations);   // 门禁（SCN-OPS-829）
});
```

**评分点**:
- 跨服务组合巡检（SCN-OPS-927）。
- 约束声明（SCN-NODE-924/OPS-251）。
- 门禁联动（SCN-OPS-829）。
- 告警修复建议（SCN-OPS-256）。
