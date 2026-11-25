---
title: [NODE-876] 笔试题——实现灰度决策闭环（看板→决策→执行→验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-876：手写决策闭环

**需求与边界**：
- 需求：灰度决策闭环（SCN-OPS-242/876）——① 看板 → 决策建议（SCN-OPS-858）；② 决策执行（放量/熔断/降档——SCN-OPS-292 状态机）；③ 执行验证（放行后指标复核——SCN-NODE-798）；④ 决策审计（SCN-OPS-273）。
- 边界：① 决策的自动化边界（≤25% 自动——SCN-OPS-242）；② 决策的依据留存（SCN-OPS-273 计划快照）；③ 闭环的时效（10 分钟观察窗——SCN-OPS-242）。

**答**：
```javascript
async function grayDecisionLoop(release) {
  while (release.stage < 100) {
    const board = await grayBoard(release);            // SCN-OPS-858 看板
    if (board.verdicts.fails) { await unroute(release); break; }   // 摘流（SCN-NODE-820）
    if (board.ready && release.nextStage <= 25) {      // 自动放量（SCN-OPS-242 上限）
      await grayFSM.advance({ by: 'auto', basis: board.verdicts });
    } else if (board.ready) {
      await requireHumanRamp(release, board.card);     // >25% 人工（SCN-OPS-242）
    }
    await observe(10 * 60_000);                        // 观察窗（SCN-OPS-242）
    audit({ stage: release.stage, decision: 'loop' }); // 审计（SCN-OPS-273）
  }
}
```

**评分点**:
- 看板→决策→执行→验证闭环（SCN-OPS-242/858）。
- 自动放量 ≤25% 上限（SCN-OPS-242）。
- 观察窗 + 决策审计（SCN-OPS-273）。
- 摘流联动（SCN-NODE-820）。
