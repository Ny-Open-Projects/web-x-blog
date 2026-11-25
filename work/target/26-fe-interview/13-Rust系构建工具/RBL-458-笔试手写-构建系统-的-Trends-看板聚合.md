---
title: [RBL-458] 笔试：手写构建趋势看板聚合
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-458：手写构建趋势看板聚合
**答**：实现 `aggregateTrends(builds)`：1) builds：构建事件流 [{ at, durationMs, cacheHit, branch, task }]；2) 聚合维度：日/周粒度（P50/P95 时长、命中率、构建次数）、按分支过滤（main vs feature 分开看——流量差异大）；3) 环比计算（本周 vs 上周——趋势方向）；4) 异常周标记（P95 环比涨超 20% 高亮）；5) 输出 { daily: [], weekly: [], regressions: [] }；6) 数据稀疏处理（某日无构建 → null 断点而非 0——图表语义正确）。

```javascript
function pctile(sorted, p) {
  return sorted.length ? sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * p))] : null
}
const weekOf = (ts) => Math.floor(ts / (7 * 86400_000))
const dayOf = (ts) => Math.floor(ts / 86400_000)

export function aggregateTrends(builds, { branch = 'main' } = {}) {
  const filtered = builds.filter((b) => b.branch === branch)
  const daily = new Map(), weekly = new Map()

  for (const b of filtered) {
    const d = dayOf(b.at), w = weekOf(b.at)
    for (const [map, key] of [[daily, d], [weekly, w]]) {
      if (!map.has(key)) map.set(key, { durations: [], hits: 0, total: 0 })
      const bucket = map.get(key)
      bucket.durations.push(b.durationMs)
      bucket.total++
      if (b.cacheHit) bucket.hits++
    }
  }

  const toPoints = (map) => [...map.entries()]
    .map(([k, v]) => ({ key: k, count: v.total,
      p50: pctile([...v.durations].sort((a, b) => a - b), 0.5),
      p95: pctile([...v.durations].sort((a, b) => a - b), 0.95),
      hitRate: v.total ? v.hits / v.total : null }))
    .sort((a, b) => a.key - b.key)

  const weekly = toPoints(weekly)
  const regressions = []
  for (let i = 1; i < weekly.length; i++) {
    const prev = weekly[i - 1], cur = weekly[i]
    if (prev.p95 && cur.p95 && (cur.p95 - prev.p95) / prev.p95 > 0.2)
      regressions.push({ week: cur.key, from: prev.p95, to: cur.p95,
        pct: +(((cur.p95 - prev.p95) / prev.p95) * 100).toFixed(1) })
  }
  return { daily: toPoints(daily), weekly, regressions }   // 空桶自然缺失（null 断点语义）
}
```
**评分点**：
- 双粒度聚合（日/周）+ 分支过滤（main 与 feature 流量差异大）
- 分位数正确（排序 + 索引钳制）；命中率口径
- 回归检测（P95 环比 +20% 高亮——趋势看板的告警语义）
- 空桶缺失语义（null 而非 0——图表断点正确）
