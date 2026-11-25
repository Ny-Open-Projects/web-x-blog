---
title: [VIZ-151] Canvas 与 WebGL 的性能边界如何决策？（数据量 × 交互复杂度矩阵）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-151：Canvas 与 WebGL 的性能边界如何决策？（数据量 × 交互复杂度矩阵）
**答**：决策维度：① **数据量**——静态渲染 < 1 万点 Canvas 足够；每帧重绘 > 1 万或总量 > 10 万选 WebGL；② **交互复杂度**——高频动画（实时曲线/粒子）偏 WebGL，重文本标注/鼠标拾取偏 Canvas/SVG；③ **开发成本**——Canvas 调试直观，WebGL 心智成本高（状态机/着色器）；④ **文本质量**——大量文字标注 SVG/Canvas 排版好，WebGL 文本（SDF）实现复杂。实践准则：优先用现成封装（ECharts 大数据系列/deck.gl），确认瓶颈后再自研 WebGL；混合策略（WebGL 底层 + Canvas 标注层）常是最优解。

```javascript
// 决策矩阵：数据量 × 交互 -> 渲染后端
function pickRenderer({ pointCount, fpsInteraction, textHeavy, needGLFeatures }) {
  if (needGLFeatures) return 'WebGL';                       // 3D/着色器效果硬需求
  if (pointCount > 100_000 || (fpsInteraction && pointCount > 10_000))
    return 'WebGL';                                         // 大数据或高频动画
  if (textHeavy || pointCount < 5_000) return 'SVG 或 Canvas2D'; // 文本排版/小数据
  return 'Canvas2D';                                        // 中等规模默认
}
// 混合策略：静态大数据 WebGL 层 + 交互标注 Canvas2D 层叠加
// 例：deck.gl 画百万点，上层透明 canvas 画选中标注与 tooltip 引线
```
