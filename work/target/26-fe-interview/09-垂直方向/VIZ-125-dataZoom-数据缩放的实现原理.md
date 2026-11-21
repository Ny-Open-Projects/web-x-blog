---
title: [VIZ-125] dataZoom 数据缩放的实现原理？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-125：dataZoom 数据缩放的实现原理？
**答**：dataZoom 本质是**数据窗口过滤器**：① inside 型监听滚轮/拖拽，slider 型是独立组件画窗口把手；② 窗口模型——`start/end`（百分比）与 `startValue/endValue`（绝对值）双表示互转；`filterMode: 'filter' | 'weakFilter' | 'empty' | 'none'` 决定物理过滤数据还是只裁剪显示；③ 联动——窗口变化后重走"数据 → 视觉映射 → View"管线，轴刻度按新窗口重新 niceTicks；④ 性能——大数据配 `sampling: 'lttb'`、`throttle: 50` 拖动节流、`filterMode: 'none'` 避免频繁重建数据。

```javascript
// dataZoom 配置要点 + 手写迷你缩放原理
chart.setOption({
  dataZoom: [
    { type: 'inside', throttle: 50, filterMode: 'none' },  // 滚轮缩放，节流 50ms
    { type: 'slider', start: 0, end: 100 },
  ],
  series: [{ type: 'line', sampling: 'lttb', data: bigData }],
});
// 手写核心：归一化窗口 -> 切片 -> 重渲染
let win = { lo: 0, hi: 1 };
onZoom(k => { win.hi = Math.max(0.01, win.hi * k); render(); }); // 滚轮改窗口
function render() {
  const n = data.length, a = Math.floor(win.lo * n), b = Math.ceil(win.hi * n);
  drawSeries(data.slice(a, b));   // 只渲染窗口内数据
  drawSlider(a / n, b / n);       // 缩略图上的窗口把手
}
```

---

## 十五、大数据可视化（VIZ-126 ~ VIZ-131）
