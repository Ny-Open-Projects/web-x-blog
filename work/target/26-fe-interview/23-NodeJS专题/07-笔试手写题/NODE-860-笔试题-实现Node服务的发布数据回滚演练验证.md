---
title: [NODE-860] 笔试题——实现发布回滚演练验证（盲演 + 计时）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-860：手写回滚演练

**需求与边界**：
- 需求：回滚演练（SCN-OPS-215）——① 盲演（值班不知情——SCN-OPS-215 真实性）；② 计时硬指标（决策/执行/验证分段——SCN-OPS-215 < 5min）；③ runbook 执行完整性（步骤全走——SCN-OPS-851 联动）；④ 演练报告与改进（卡点——SCN-OPS-215 复盘）。
- 边界：① 演练环境真实性（预发+真实数据——SCN-OPS-215）；② 盲演的调度（值班表随机——SCN-OPS-215）；③ 演练覆盖度统计（SCN-OPS-279 联动）。

**答**：
```javascript
async function rollbackDrill({ blind = true } = {}) {
  const oncall = pickRandomOncall();                   // 盲演：随机值班（不知情——SCN-OPS-215）
  const t0 = Date.now();
  const result = await runRunbook(rollbackRunbook, {   // SCN-OPS-851 runbook 即代码
    by: oncall, blind });
  const segments = {
    decision: result.decisionTs - t0,
    exec: result.switchTs - result.decisionTs,
    verify: result.verifyTs - result.switchTs,
    total: result.verifyTs - t0,                       // 分段计时（SCN-OPS-215）
  };
  const pass = segments.total < 5 * 60_000;            // 硬指标
  reportDrill({ pass, segments, runbookCoverage: result.stepsCovered,
    coverageDebt: uncoveredSteps() });                 // 覆盖度（SCN-OPS-279）
  return { pass, segments, improvements: result.blockers };
}
```

**评分点**:
- 盲演调度（值班不知情——SCN-OPS-215 真实性）。
- 分段计时硬指标（决策/执行/验证——< 5min）。
- runbook 即代码执行（SCN-OPS-851）。
- 覆盖度联动（SCN-OPS-279）。
