---
title: [NODE-931] 笔试题——实现多服务演练覆盖（跨服务故障场景）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-931：手写跨服务演练

**需求与边界**：
- 需求：跨服务演练（SCN-OPS-279/915）——① 跨服务故障场景生成（依赖矩阵——SCN-NODE-915）；② 联动演练（A 挂 → B 降级验证——SCN-NODE-828）；③ 覆盖度统计（SCN-OPS-279）；④ 演练债务（SCN-OPS-279）。
- 边界：① 场景的生成来源（依赖矩阵——SCN-NODE-915）；② 演练的并行（多服务同时——SCN-OPS-281 范围）；③ 报告的聚合（SCN-OPS-279）。

**答**：
```javascript
async function crossServiceDrill(matrix) {
  const scenarios = dependencyFailureScenarios(matrix);   // 依赖矩阵 → 场景（SCN-NODE-915）
  const results = [];
  for (const s of scenarios) {
    injector.inject(s.inject);                         // 注入（SCN-OPS-281）
    const ok = await verifyDownstreamDegrades(s.dependents);   // 联动降级验证（SCN-NODE-828）
    results.push({ scenario: s, ok });
    injector.emergencyStop();                          // 清理
  }
  return { results, coverage: coverageCalc(results, matrix),   // 覆盖度（SCN-OPS-279）
    debt: uncoveredModes(matrix) };
}
```

**评分点**:
- 依赖矩阵 → 跨服务场景（SCN-NODE-915）。
- 联动降级验证（SCN-NODE-828）。
- 覆盖度 + 债务（SCN-OPS-279）。
- 注入器联动（SCN-OPS-281）。
