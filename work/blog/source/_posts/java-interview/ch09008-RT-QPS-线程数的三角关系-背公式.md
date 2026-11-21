---
title: "RT/QPS/线程数的三角关系（背公式）"
date: 2026-11-18
categories: [Java面试, 系统设计]
tags: [Java面试, 讲义, 33]
type: 讲义
disableNunjucks: true
---

### RT/QPS/线程数的三角关系（背公式）
- QPS = 线程数 / 平均 RT（同步阻塞模型）；
- 线程数 = QPS × RT；QPS 固定 RT 上升 → 线程数需求上升 → 线程切换开销上升 → RT 更高（死亡螺旋，故障的经典机理）；
- 排查口诀：**RT 涨了先看下游与 GC，别急着加机器**。
