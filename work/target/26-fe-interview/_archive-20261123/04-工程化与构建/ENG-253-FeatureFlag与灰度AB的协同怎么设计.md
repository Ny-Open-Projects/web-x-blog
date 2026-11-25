---
title: [ENG-253] Feature Flag 与灰度/AB 实验的协同（避免互相打架）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-253：Flag 与灰度/AB 协同怎么设计？
**答**：
- 分层正交：发布灰度（版本级，网关层）与实验分流（flag 级，应用层）分层执行——同层内互斥（一个用户同层只有一个变体），层间正交可叠加。
- 分流键统一：同一用户 ID 哈希族 + 层盐值（layer salt），保证跨实验正交且同实验内稳定。
- 组合爆炸防御：生效 flag 与实验数量看板，同时生效的「行为组合」数量告警（> 16 组合的页面不可分析）。
- 归因清晰：指标看板按「版本 × 实验」双维切片，防止 A 版本的劣化被 B 实验的成绩掩盖（辛普森悖论防御）。
- 追问钩子：为什么需要「行为组合数量告警」——每个 flag 和实验都在改变用户行为，同时生效 4 个 flag × 2 变体 = 32 种组合；组合过多时任何指标的波动都无法归因，实验体系就失效了。

```javascript
// 分层正交分流
const variant = hash(`${userId}:layer-${layer}`) % buckets;   // 层盐正交
// 组合爆炸防御
const activeCombos = activeFlags × activeExperiments;
if (activeCombos > 16) warn('该页面组合爆炸，归因失效风险');
// 双维切片看板
metrics.sliceBy(['releaseVersion', 'experimentVariant']);
```
