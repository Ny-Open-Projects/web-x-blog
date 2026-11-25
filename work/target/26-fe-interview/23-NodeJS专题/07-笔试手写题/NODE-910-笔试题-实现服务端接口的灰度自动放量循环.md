---
title: [NODE-910] 笔试题——实现灰度自动放量循环（分档+观察+判定）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-910：手写放量循环

**需求与边界**：
- 需求：自动放量（SCN-OPS-242/876）——① 分档推进（1→5→25→50→100——SCN-OPS-204）；② 每档观察窗（SCN-OPS-242）；③ 判定（硬指标自动——SCN-OPS-239）；④ 中断条件（熔断/告警——SCN-OPS-222）。
- 边界：① 自动上限 25%（SCN-OPS-242）；② 观察窗的业务周期（SCN-OPS-268 周期覆盖）；③ 循环的事件审计（SCN-OPS-273）。

**答**：
```javascript
const STAGES = [1, 5, 25, 50, 100];
async function autoRamp(release) {
  for (const stage of STAGES) {
    if (stage > 25) await requireHuman(stage);         // 上限（SCN-OPS-242）
    await setGray(stage);                              // 推进（SCN-OPS-292）
    const ok = await observeWindow(release, { window: dwell(stage),   // 观察窗（SCN-OPS-242）
      coverCycle: stage >= 25 });                      // 周期覆盖（SCN-OPS-268）
    if (!ok) { await circuitBreak(release); break; }   // 中断（SCN-OPS-222）
    audit({ stage, verdict: ok });                     // 审计（SCN-OPS-273）
  }
}
```

**评分点**:
- 分档推进 + 观察窗（SCN-OPS-242）。
- 自动上限 25%（SCN-OPS-242）。
- 周期覆盖（SCN-OPS-268）。
- 中断（熔断——SCN-OPS-222）+ 审计（SCN-OPS-273）。
