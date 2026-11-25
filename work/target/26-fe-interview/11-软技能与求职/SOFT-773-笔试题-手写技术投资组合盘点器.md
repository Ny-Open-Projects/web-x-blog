---
title: [SOFT-773] 手写 techPortfolio：三层投入盘点（维护/建设/探索）、配比偏差、探索转建门槛检查？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-773：手写 techPortfolio：三层投入盘点（维护/建设/探索）、配比偏差、探索转建门槛检查

**需求与边界**：
- 实现 techPortfolio(investments, stage)。
- 边界要求：① investments 每条含 { name, layer: maintain|build|explore, hours, timeboxed? }，explore 类必须 timeboxed（无时间盒拒绝登记）；② 三层配比输出 vs 目标（按 stage：扩张期 40/35/25、稳定期 55/30/15、收缩期 70/25/5）；③ 门槛检查：explore 层超时盒（超 1 季度未决策转/弃/续——告警）；④ 输出调参建议。

**答**：
```javascript
const STAGE = { expand: { maintain: 40, build: 35, explore: 25 },
  stable: { maintain: 55, build: 30, explore: 15 },
  shrink: { maintain: 70, build: 25, explore: 5 } };
function techPortfolio(investments, stage, { today = Date.now() } = {}) {
  const target = STAGE[stage];
  if (!target) throw new Error(`未知阶段：${stage}`);
  const layers = { maintain: 0, build: 0, explore: 0 };
  let total = 0;
  const stale = [];
  for (const inv of investments) {
    if (inv.layer === 'explore' && !inv.timeboxed)
      throw new Error(`探索项「${inv.name}」必须设时间盒`);
    layers[inv.layer] += inv.hours; total += inv.hours;
    const elapsedQ = (today - inv.timeboxed?.start) / (90 * 864e5);
    if (inv.layer === 'explore' && elapsedQ > 1 && !inv.timeboxed?.resolved)
      stale.push(inv.name);                        // 超时盒未决策
  }
  const actual = Object.fromEntries(Object.entries(layers)
    .map(([k, v]) => [k, +(v / total * 100).toFixed(1)]));
  return { actual, target,
    deviate: Object.keys(target).filter(k =>
      Math.abs(actual[k] - target[k]) > 10),
    staleExplore: stale,
    advice: stale.length ? `探索项超时盒未决策（${stale}）：转建设/弃/续——必须三选一`
      : actual.explore < target.explore - 10
      ? '探索不足——未来期权在流失' : '配比OK' };
}
```

**评分点**:
- explore 强制时间盒（无盒拒绝——探索变烂尾的防线）。
- 超时盒未决策告警（转/弃/续三选一——决策纪律）。
- 按 stage 目标配比 + 10pp 偏差诊断。

