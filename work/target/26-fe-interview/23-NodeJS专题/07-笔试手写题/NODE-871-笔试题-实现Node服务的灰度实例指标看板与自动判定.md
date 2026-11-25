---
title: [NODE-871] 笔试题——实现灰度实例看板与自动判定（指标+门槛+IM）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-871：手写灰度看板

**需求与边界**：
- 需求：灰度看板与判定（SCN-OPS-239/NODE-798）——① 实例维度指标（per 实例——SCN-OPS-850 版本切片）；② 门槛判定（SCN-OPS-242）；③ IM 卡片推送（SCN-OPS-325）；④ 摘流联动（SCN-NODE-820）。
- 边界：① 动态基线（SCN-OPS-304）；② 样本下限（SCN-OPS-203）；③ 门槛判定与放量建议（SCN-OPS-242 自动上限）。

**答**：
```javascript
async function grayBoard(release) {
  const canary = await instanceMetrics(release.canaryInstances);   // per 实例（SCN-OPS-850）
  const stable = await instanceMetrics(release.stableInstances);
  const verdicts = hardVerdict(canary, stable, dynamicBaseline());   // 动态基线（SCN-OPS-304）
  const ready = allOk(verdicts) && canary.samples >= 100;   // 门槛（SCN-OPS-242/203）
  if (ready && release.autoRamp) await rampTo(next(release));   // 自动放量（≤25% 上限——SCN-OPS-242）
  if (fails(verdicts)) await unrouteUnhealthy(release);   // 摘流联动（SCN-NODE-820）
  await imCard({ verdicts, ready });                   // IM 卡片（SCN-OPS-325）
  return { verdicts, ready };
}
```

**评分点**:
- per 实例指标（SCN-OPS-850 版本切片）。
- 动态基线 + 样本下限（SCN-OPS-304/203）。
- 自动放量上限（≤25%——SCN-OPS-242）。
- 摘流联动 + IM 卡片（SCN-NODE-820/OPS-325）。
