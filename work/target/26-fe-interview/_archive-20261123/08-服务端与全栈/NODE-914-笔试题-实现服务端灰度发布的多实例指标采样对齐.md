---
title: [NODE-914] 笔试题——实现灰度指标采样对齐（canary/stable 同窗口）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-914：手写采样对齐

**需求与边界**：
- 需求：采样对齐（SCN-OPS-203/231）——① 同窗口对比（时间窗对齐——SCN-OPS-203）；② 采样率对齐（两组采样率一致——SRM 防御，SCN-OPS-293）；③ 维度分层对齐（端/地域分布一致性——SCN-OPS-203 SRM）；④ 对齐校验的报告（SCN-OPS-293）。
- 边界：① 对齐的自动化（每次对比前校验——SCN-OPS-858 看板前置）；② 维度不一致的处理（分层后对比——辛普森防御，SCN-OPS-239）；③ 对齐报告的审计（SCN-OPS-273）。

**答**：
```javascript
async function alignedCompare(canary, stable, metric) {
  const checks = {
    window: sameWindow(canary, stable),                // 时间窗对齐（SCN-OPS-203）
    sampleRate: canary.rate === stable.rate,           // 采样率对齐（SRM——SCN-OPS-293）
    dims: dimensionBalance(canary, stable, ['device', 'region']),   // 维度分层（SCN-OPS-239 辛普森）
  };
  const unaligned = Object.entries(checks).filter(([k, ok]) => !ok);
  if (unaligned.length)
    return { verdict: 'NOT_ALIGNED', unaligned,
      note: '对比暂不可信——先对齐（SCN-OPS-293 SRM）' };
  return { verdict: verdictMetric(canary, stable), aligned: true };
}
```

**评分点**:
- 三项对齐（时间窗/采样率/维度分层——SCN-OPS-203/293）。
- 未对齐拒绝对比（数据不可信声明——SCN-OPS-293）。
- 分层对比防辛普森（SCN-OPS-239）。
- 看板前置校验（SCN-OPS-858）。
