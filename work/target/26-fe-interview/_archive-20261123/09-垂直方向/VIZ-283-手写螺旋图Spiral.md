---
title: [VIZ-283] 手写螺旋图（Spiral）：周期数据可视化
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-283：手写螺旋图（Spiral）：周期数据可视化

**答**：
- 螺旋图：时间序列按周期（周/年）螺旋排列——径向=周期序号，角向=周期内位置，适合长时序趋势+周期模式展示。
- 实现：阿基米德螺旋半径 = 内径 + 周期序号 × 层距；角度 = 周期内位置比例 × 2π；值映射到点色/大小。
- 适用：年度节假日模式、周内流量模式——一眼看出「周期 + 趋势」。

```javascript
function spiralChart(data, { period = 7, innerR = 30, layerGap = 12 } = {}) {
  const points = data.map((d, i) => {
    const cycle = Math.floor(i / period);                  // 周期序号（径向）
    const phase = (i % period) / period;                   // 周期内相位（角向）
    const r = innerR + cycle * layerGap;
    const a = phase * 2 * Math.PI - Math.PI / 2;
    return { x: r * Math.cos(a), y: r * Math.sin(a), r, a, value: d.value, cycle, phase };
  });
  return points;
}
// 渲染：点按 value 上色（连续色标），同相位点连线可见周期模式
// 对比热力日历：螺旋图对长周期（年）更紧凑
```
