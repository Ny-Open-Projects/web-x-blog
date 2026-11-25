---
title: [CSS-345] 渲染管线全阶段：从 JS 改样式到屏幕点亮的 commit 机制
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-345：渲染管线全阶段：从 JS 改样式到屏幕点亮的 commit 机制

**答**：
- 一帧管线：JS/task → style recalc → layout → paint(记录绘制命令) → composite layers commit（主线程把图层树提交给合成器）→ raster（合成器线程/光栅线程）→ draw（GPU 合成上屏）
- commit 是关键边界：主线程产出「图层树快照」一次性交给合成器线程，之后主线程卡死也不影响已提交帧的动画/滚动——这就是合成器动画流畅的架构原因
- 管线裁剪：只改合成属性（transform/opacity）→ 跳过 layout/paint，直接 raster+draw；只改不影响布局的属性（color）→ 跳过 layout——「跳过哪几段」就是性能优化的本质
- 强制同步与帧丢失：JS 中读布局触发提前 sync layout，一帧内反复「读-写」造成多次管线执行；16.7ms 预算内完不成 → 掉帧
- 验证工具：Performance 面板帧条（每一帧的管线段耗时）、FPS meter、Layers 面板（合成层拓扑）

```text
改 transform 动画: JS → style → (skip layout/paint) → commit → raster → draw   [最便宜]
改 color:          JS → style → layout? → paint → commit → raster → draw      [中]
改 width:          JS → style → layout → paint → commit → raster → draw       [最贵]
目标: 让高频路径落在最便宜那条
```
