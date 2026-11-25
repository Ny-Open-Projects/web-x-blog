---
title: [NODE-991] 笔试题——实现 SLA 多维门禁（发布前 SLA 达标检查）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-991：手写 SLA 门禁

**需求与边界**：
- 需求：SLA 门禁（SCN-SLA-991/OPS-229）——① 发布前 SLA 达标检查（当前达标率——SCN-SLA-991）；② 预算检查（SCN-SLA-737）；③ 降级预案检查（SCN-SLA-975）；④ 门禁的分级（SCN-OPS-229）。
- 边界：① 达标检查的窗口（近 7 天——SCN-SLA-991）；② 预算检查（SCN-OPS-944）；③ 门禁的豁免（SCN-OPS-229）。

**答**：
```javascript
async function slaGates(release) {
  const checks = [
    { name: 'compliance-7d', run: () => recentCompliance(release.sla) >= release.sla.compliance * 0.95, level: 'block' },   // SCN-SLA-991
    { name: 'budget-remaining', run: () => errorBudget(release.slo, 30).remaining > 0, level: 'block' },   // SCN-OPS-944
    { name: 'degrade-matrix', run: () => degradeMatrixCovers(release.sla), level: 'warn' },   // SCN-SLA-975
  ];
  const fails = [];
  for (const c of checks) if (!(await c.run())) fails.push(c);
  return { pass: !fails.some(f => f.level === 'block'), fails,
    waiver: fails.length ? requireWaiver(release) : null };   // SCN-OPS-229
}
```

**评分点**:
- 达标 + 预算 + 降级三维门禁（SCN-SLA-991/944/975）。
- 分级 + 豁免（SCN-OPS-229）。
