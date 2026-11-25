---
title: [VIZ-280] 手写玫瑰图（Nightingale Rose）：半径映射面积守恒
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-280：手写玫瑰图（Nightingale Rose）：半径映射面积守恒

**答**：
- 题目：玫瑰图——扇区角度均分（类别数），半径按值映射（区别于饼图的角度映射）。面积守恒校正（半径 = √value，否则视觉面积夸大）。
- 思路：角度 = 2π/n（均分）；半径 = sqrt(value / maxValue) × maxRadius（面积正比于值）；标签沿径向。
- 评分点：角度均分 vs 饼图值分角；√ 校正（面积守恒）；与饼图适用场景区分。

```javascript
function roseChart(values, { maxRadius = 150, innerRadius = 20 } = {}) {
  const max = Math.max(...values);
  const anglePer = 2 * Math.PI / values.length;
  return values.map((v, i) => {
    const ratio = Math.sqrt(v / max);                      // √ 校正：面积∝值
    const r = innerRadius + ratio * (maxRadius - innerRadius);
    const a0 = i * anglePer, a1 = (i + 1) * anglePer;
    return { index: i, value: v, r, a0, a1,
      path: annularSector(innerRadius, r, a0, a1),         // 环形扇区 path
      labelAngle: (a0 + a1) / 2 };
  });
}
function annularSector(r0, r1, a0, a1) {                   // 环形扇区 path
  const p = (r, a) => `${r * Math.cos(a)},${r * Math.sin(a)}`;
  const large = a1 - a0 > Math.PI ? 1 : 0;
  return `M${p(r0, a0)} L${p(r1, a0)} A${r1},${r1} 0 ${large} 1 ${p(r1, a1)} ` +
    `L${p(r0, a1)} A${r0},${r0} 0 ${large} 0 ${p(r0, a0)} Z`;
}
```
