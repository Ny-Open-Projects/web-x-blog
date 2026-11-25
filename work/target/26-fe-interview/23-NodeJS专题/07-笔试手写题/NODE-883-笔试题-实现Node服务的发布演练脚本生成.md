---
title: [NODE-883] 笔试题——实现发布演练脚本生成（故障模式→演练场景）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-883：手写演练脚本

**需求与边界**：
- 需求：演练脚本生成（SCN-OPS-281/269）——① 故障模式枚举（SCN-OPS-281 注入库）；② 场景生成（故障 → 注入参数 → 断言——SCN-OPS-269 runbook）；③ 演练覆盖度（SCN-OPS-279）；④ 脚本与预案一致性（SCN-OPS-311）。
- 边界：① 注入参数的边界（影响范围限定——预发/灰度小流量）；② 演练的自动执行（CI 定时——SCN-OPS-269）；③ 生成脚本的人工审核（演练安全——不自动执行未审核脚本）。

**答**：
```javascript
function generateDrillScripts(failureModes,预案) {
  return failureModes.map(mode => ({
    name: `drill-${mode.id}`,
    inject: injectionFor(mode),                        // 注入参数（SCN-OPS-281）
    steps: fromPlaybook(预案[mode.id]),                // 预案同源（SCN-OPS-311）
    assert: { fallbackWithin: '5min', notifyFired: true },
    scope: { env: 'staging', pct: 10 },                // 范围限定
    reviewed: false,                                   // 人工审核标记（不自动执行）
  }));
}
// CI 定时执行（审核过的脚本）
cron('0 3 * * 6', () => drills.filter(d => d.reviewed).forEach(runDrill));   // SCN-OPS-269
```

**评分点**:
- 故障模式 → 演练场景（SCN-OPS-281 注入库）。
- 预案同源 + 一致性（SCN-OPS-311）。
- 范围限定（预发/小流量——安全边界）。
- 人工审核 + CI 定时（SCN-OPS-269）。
