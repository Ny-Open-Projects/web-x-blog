---
title: [SCN-747] 笔试题——实现发布前后指标对账 diff（同口径同流量段）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-747：手写发布对账 diff

**需求与边界**：
- 需求：发布前后各 1h 的指标对比；要求同口径（calVer 一致）且排除发布瞬间抖动段（前后 5min 剔除）；输出差异与显著劣化标记。
- 边界：① 对比窗口对齐（发布前 1h vs 发布后 1h）；② 剔除 [t0-5min, t0+5min] 混合段；③ 流量差异 > 20% 时标注不可比。

**答**：
```javascript
async function deployDiff(release) {
  const t0 = release.ts;
  const cut = (range) => subtract(range, [t0 - 5 * 60_000, t0 + 5 * 60_000]);   // 剔除混合段
  const before = await metrics.query({ window: cut([t0 - 3600_000, t0]) });
  const after = await metrics.query({ window: cut([t0, t0 + 3600_000]) });
  if (before.calVer !== after.calVer) throw new Error('CAL_VER_MISMATCH');      // 口径必须一致
  const trafficDelta = (after.count - before.count) / before.count;
  return {
    trafficDelta,
    comparable: Math.abs(trafficDelta) < 0.2,
    metrics: Object.keys(before).map(k => ({
      key: k, before: before[k], after: after[k],
      delta: after[k] - before[k],
      worse: after[k] > before[k] * 1.1 && isHigherWorse(k),   // 指标方向感知
    })),
    note: Math.abs(trafficDelta) >= 0.2 ? '流量变化超 20%，差异可能由流量构成导致' : null,
  };
}
const isHigherWorse = (k) => /p95|error|duration/.test(k);   // 指标方向（成功率高是好事）
```

**评分点**:
- 剔除发布混合段（前后 5min）避免抖动污染。
- 口径版本强校验。
- 流量可比性判定（>20% 标注）。
- 指标方向感知（成功率降才是劣化）。
