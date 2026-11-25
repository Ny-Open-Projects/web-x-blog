---
title: [NODE-859] 笔试题——实现发布前检查清单执行器（硬/软门禁分级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-859：手写发布门禁

**需求与边界**：
- 需求：发布门禁（SCN-OPS-229）——① 硬门禁（CI 绿/兼容矩阵/数据兼容——SCN-OPS-829）；② 软门禁（changelog/通知 ack——警告放行）；③ 豁免记录（SCN-OPS-229）；④ 门禁豁免率监控（SCN-OPS-289）。
- 边界：① 门禁项可配置（per 服务/发布类型——SCN-OPS-202 风险分级联动）；② 豁免的过期（SCN-OPS-315 有效性回看）；③ 执行记录审计（SCN-OPS-220）。

**答**：
```javascript
async function releaseGates(release, { level } = {}) {
  const gates = GATE_TEMPLATES[level];                 // 风险分级模板（SCN-OPS-202）
  const hard = gates.filter(g => g.hard), soft = gates.filter(g => !g.hard);
  const hardResults = await Promise.all(hard.map(async g =>
    ({ ...g, ok: await g.check(release) })));          // SCN-OPS-829 数据兼容等
  const hardFails = hardResults.filter(r => !r.ok);
  if (hardFails.length) {
    const waiver = release.waiver;
    if (!waiver?.valid) return { blocked: true, hardFails };   // 豁免记录（SCN-OPS-229）
    audit({ gate: 'waived', gates: hardFails.map(g => g.name), waiver });
  }
  const softWarns = await Promise.all(soft.map(async g =>
    ({ ...g, ok: await g.check(release) })));          // 软门禁警告放行
  softWarns.filter(s => !s.ok).forEach(s => warn(s.name));
  gateStats.track(level, hardResults, softWarns);      // 豁免率监控（SCN-OPS-289）
  return { blocked: false };
}
```

**评分点**:
- 硬/软分级（SCN-OPS-229）。
- 风险分级模板（SCN-OPS-202 联动）。
- 豁免记录 + 豁免率监控（SCN-OPS-289）。
- 数据兼容门禁引用（SCN-OPS-829）。
