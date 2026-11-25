---
title: [NODE-898] 笔试题——实现数据修复任务编排器（修复链 + 幂等 + 审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-898：手写数据修复

**需求与边界**：
- 需求：数据修复编排（SCN-OPS-227/868）——① 修复链声明（依赖顺序——SCN-NODE-740 DAG）；② 修复幂等（idemKey——SCN-NODE-655）；③ 修复的审计与回滚（down 脚本——SCN-NODE-766）；④ 修复的风险分级（金额大走人工——SCN-联想-868）。
- 边界：① 修复的前置校验（修复前的状态确认——SCN-OPS-259）；② 修复的 dry-run（先试后跑——SCN-联想-898）；③ 修复任务的超时与孤儿（SCN-NODE-787）。

**答**：
```javascript
class RepairOrchestrator {
  async run(repair) {
    await assertPrecondition(repair);                  // 前置校验（SCN-OPS-259）
    const dryRun = await dryRunRepair(repair);         // dry-run（SCN-联想-898）
    if (!dryRun.ok) return { blocked: dryRun.issues };
    for (const step of repair.steps) {                 // 修复链（SCN-NODE-740 DAG）
      const claimed = await claimStep(repair.id, step.name);   // 幂等 claim（SCN-NODE-787）
      if (!claimed) continue;
      try { await step.exec({ dryRunResult: dryRun }); await markDone(repair.id, step.name); }
      catch (e) { await repair.down?.(repair); throw e; }   // down 脚本（SCN-NODE-766）
    }
    audit({ repair: repair.id, steps: repair.steps.length });   // 审计
  }
}
```

**评分点**:
- dry-run 先行（SCN-联想-898）。
- 修复链 claim 幂等（SCN-NODE-787/655）。
- down 脚本（SCN-NODE-766 回滚）。
- 风险分级 + 审计（SCN-联想-868/OPS-220）。
