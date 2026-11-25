---
title: [SCN-742] 笔试题——实现异常检测标注（周期基线 + 3σ + 排除事件时段）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-742：手写异常检测标注

**需求与边界**：
- 需求：按周周期（同时刻历史）计算基线与残差；残差 > 3σ 标 anomaly；已知事件时段（大促/故障）不学习进基线也不标异常。
- 边界：① 基线 = 同 weekday 同 hour 历史中位数（抗离群）；② σ 用 MAD（中位绝对偏差）替代标准差（更稳）；③ 历史不足 3 周输出 insufficient。

**答**：
```javascript
function anomalyMark(series, { period = 7 * 24, events = new Set(), minWeeks = 3 } = {}) {
  // series: 按小时排列 [{t, v}]
  const buckets = new Map();                          // (weekday,hour) -> values
  for (const p of series) {
    const key = phaseKey(p.t);                        // weekday*24+hour
    if (events.has(p.t)) continue;                    // 事件时段不学习
    (buckets.get(key) ?? buckets.set(key, []).get(key)).push(p.v);
  }
  const weeks = Math.max(...[...buckets.values()].map(v => v.length));
  if (weeks < minWeeks) return { insufficient: true };
  const stdOf = (arr) => {
    const med = median(arr);
    return 1.4826 * median(arr.map(v => Math.abs(v - med)));   // MAD→σ 等价
  };
  const result = series.map(p => {
    const base = buckets.get(phaseKey(p.t)) || [];
    if (!base.length) return { ...p, anomaly: false, skip: true };   // 首周无基线
    const med = median(base), sigma = stdOf(base);
    const residual = p.v - med;
    return { ...p, baseline: med,
      anomaly: !events.has(p.t) && Math.abs(residual) > 3 * sigma,
      kind: residual > 3 * sigma ? 'spike' : 'drop' };
  });
  return { result };
}
const phaseKey = (ts) => { const d = new Date(ts); return `${d.getDay()}:${d.getHours()}`; };
const median = (a) => { const s = [...a].sort((x, y) => x - y);
  return s.length % 2 ? s[(s.length - 1) / 2] : (s[s.length / 2 - 1] + s[s.length / 2]) / 2; };
```

**评分点**:
- 周期基线（同 weekday+hour 中位数，抗离群）。
- MAD 估计 σ（对异常值稳健）。
- 事件时段双排除（不学习也不标注）。
- 历史不足降级 insufficient + 首周 skip。
