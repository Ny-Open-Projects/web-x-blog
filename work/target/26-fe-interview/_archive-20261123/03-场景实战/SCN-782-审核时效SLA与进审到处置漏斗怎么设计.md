---
title: [SCN-782] 审核时效 SLA（进审到处置）漏斗怎么设计与监控？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-782：审核时效 SLA 漏斗怎么设计？
**答**：
- 时效口径：投稿 → 进入审核队列（机审耗时）→ 领取 → 完成审核 → 处置生效，各段独立 SLA 与漏斗——机审慢和人力慢治理手段完全不同。
- 分品类 SLA：高风险品类（需人审）时效长，直放品类秒级；SLA 按品类分层设定而非一刀切。
- 漏斗监控：各段超时占比与堆积点定位（机审排队/人力不足/处置扇出慢），自动定位瓶颈段。
- 对外承诺：创作者侧展示「审核中，预计 N 分钟」用 P95 口径（不承诺平均值防止超时客诉）。
- 追问钩子：为什么对外预估用 P95——承诺 P50 会让一半用户超时客诉；P95 承诺 + 实际 P50 达成 = 超预期体验。

```javascript
const latencyFunnel = {
  stages: ['upload→queue', 'queue→claim', 'claim→verdict', 'verdict→effective'],
  sloByCategory: { direct: 30_000, human: 30 * 60_000, highRisk: 2 * 3600_000 },
  bottleneck: (stats) => argmax(stats.map(s => s.overRatio)),   // 超时占比最大段
  promise: (category) => quantile(latency(category), 0.95),     // P95 对外承诺
};
```
