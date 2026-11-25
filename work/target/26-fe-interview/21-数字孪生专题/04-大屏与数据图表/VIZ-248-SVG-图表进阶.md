---
title: [VIZ-248] SVG 图表进阶：大数据量 SVG 的性能边界与虚拟化
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-248：SVG 图表进阶：大数据量 SVG 的性能边界与虚拟化

**答**：
- SVG 性能边界：> 5000 元素 DOM 操作卡（每元素=节点）；策略：虚拟化（视口外不渲染）、合并 path（同系列折线合成单 path）。
- 合并 path：折线 N 点 = 1 个 path（d 属性字符串）——DOM 节点数与数据量解耦。
- 动画：SVG SMIL vs CSS transform vs JS 驱动——批量动画用 CSS transform（合成层）。

```javascript
function svgPolyline(points, scaleX, scaleY) {            // 合并 path
  const d = points.map((p, i) =>
    `${i === 0 ? 'M' : 'L'}${scaleX(p.x)},${scaleY(p.v)}`).join('');
  return `<path d="${d}" fill="none" stroke="steelblue"/>`;   // 1 节点画 N 点
}
function svgVirtualize(allPoints, viewportDomain, scaleX, scaleY) {
  const visible = allPoints.filter(p => p.x >= viewportDomain[0] && p.x <= viewportDomain[1]);
  // 只渲染视口内点——domain 变化时重算（dataZoom 联动）
  return svgPolyline(visible, scaleX, scaleY);
}
// SVG vs Canvas 选型：< 1000 点 + 强交互/无障碍 → SVG；> 5000 点 → Canvas/WebGPU
```
