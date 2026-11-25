---
title: [NODE-921] 笔试题——实现灰度发布全流程控制台（端到端闭环）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-921：手写全流程控制台

**需求与边界**：
- 需求：灰度全流程（SCN-NODE-910/OPS-876）——① 准入（门禁+配置+依赖——SCN-OPS-859/886/917）；② 放行（影子→灰度→全量——SCN-OPS-236/910）；③ 观测（哨兵+看板+决策闭环——SCN-NODE-798/858/876）；④ 应急（熔断→摘流→回滚——SCN-NODE-828/820/833）；⑤ 善后（清理+验证+报告——SCN-OPS-227/913/897）。
- 边界：① 各环节复用前文实现（编号引用）；② 控制台只编排（SCN-OPS-333 原则）；③ NODE 能力地图收束（721~920 索引）。

**答**：
```javascript
async function grayReleaseConsole(release) {
  const admission = await releaseGates(release);       // ① 门禁（SCN-OPS-859/829）
  const config = await configSyncCheck(release);       // ② 配置（SCN-NODE-886）
  const deps = await canaryDepsCheck(release);         // ③ 依赖（SCN-NODE-917）
  if (admission.blocked || config.blocked || !deps.ready)
    return { blocked: true, reasons: [admission, config, deps] };   // 准入
  await shadowVerify(release);                         // 影子（SCN-OPS-236）
  await autoRamp(release);                             // 放量循环（SCN-NODE-910）
  const sentinel = canarySentinel(release);            // 哨兵（SCN-NODE-798）
  const board = grayDashboard(release);                // 看板（SCN-OPS-858）
  const emergency = { breaker: CircuitBreaker, unroute: unrouteUnhealthy, rollback: AutoRollbackExecutor };   // 应急（SCN-NODE-828/820/833）
  const aftermath = { cleanup: postReleaseCleanup, dataVerify: verifyRollbackData,
    report: releaseRegressionReport };                 // 善后（SCN-OPS-913/832/897）
  return { admission, shadow: 'passed', board, emergency, aftermath,
    map: NODE_MAP };                                   // 能力地图
}
const NODE_MAP = {   // 721~920 全链索引
  runtime: ['721-eld', '722-graceful', '723-gc', '724-worker', '725-backpressure', '726-pool', '727-cache'],
  bff: ['728-deadline', '729-aggregate', '730-als', '740-dag', '801-protocol', '813-dag'],
  release: ['776-route', '798-sentinel', '820-unroute', '833-rollback', '910-ramp', '921-console'],
};
```

**评分点**:
- 五阶段闭环（准入/放行/观测/应急/善后）全链引用编号。
- 控制台只编排（SCN-OPS-333）。
- NODE 能力地图收束（721~920）。
