---
title: [NODE-793] 笔试题——实现灰度期数据兼容性自检（双写漂移检测）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-793：手写兼容自检

**需求与边界**：
- 需求：灰度数据兼容（SCN-OPS-331/205）——① 双写漂移检测（新旧字段一致性——SCN-OPS-331 phase1）；② 旧版本读新数据验证（降级读路径实测——SCN-OPS-277）；③ 漂移率阈值告警（>0.1% 阻断 contract 阶段——SCN-OPS-331 门禁）；④ 自动修复（可自动修的漂移——补偿任务）。
- 边界：① 抽样校验的成本（1% 抽样——SCN-OPS-331）；② 漂移原因分类（双写 bug/并发覆盖——归因不同修复不同）；③ 漂移持续时长的熔断（漂移不收敛 → 暂停迁移——SCN-OPS-348 兜底）。

**答**：
```javascript
async function dualWriteDriftCheck(table, { sampleRate = 0.01, tolerance = 0.001 } = {}) {
  const rows = await db.sampleRows(table, sampleRate);   // 抽样（SCN-OPS-331）
  const drifts = rows.filter(r => r.oldField !== transform(r.newField));   // 一致性比对
  const rate = drifts.length / rows.length;
  if (rate > tolerance) {
    alert({ type: 'DUAL_WRITE_DRIFT', rate, samples: drifts.slice(0, 5) });
    pauseContractPhase(table);                         // 漂移不收敛 → 暂停 contract（SCN-OPS-348）
    await scheduleAutoFix(drifts.filter(d => d.fixable));   // 自动补偿（可修的）
    return { drifted: true, rate, causes: classifyDrift(drifts) };   // 归因（双写bug/并发覆盖）
  }
  return { drifted: false, rate };
}
// 旧版本读新数据实测（SCN-OPS-277）
await oldVersionReadWrite(sampleRows);                 // 真实数据实测（schema 之外的逻辑兼容）
```

**评分点**:
- 抽样漂移检测 + 阈值阻断 contract（SCN-OPS-331 门禁）。
- 旧版本实测（schema 外的逻辑兼容——SCN-OPS-277）。
- 自动补偿（可修漂移——SCN-OPS-259 边界）。
- 漂移归因分类（双写 bug/并发覆盖——修复路径不同）。
