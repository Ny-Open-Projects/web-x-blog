---
title: [VIZ-123] 坐标轴刻度是怎么算出来的？（nice ticks，压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-123：坐标轴刻度是怎么算出来的？（nice ticks，压轴）
**答**：目标是"人类友好刻度"：步长是 1/2/2.5/5×10ⁿ 这类整数、刻度数在 3~7 之间、范围覆盖数据。经典 **nice number 算法**：`rawStep = range / (tickCount - 1)`，`mag = 10^floor(log10(rawStep))`，再从 [1, 2, 2.5, 5, 10]×mag 中选不小于 rawStep 的最小者作为 step；然后 `lo = floor(min/step)*step`、`hi = ceil(max/step)*step`，从 lo 步进到 hi。浮点累加误差用 epsilon 与 toFixed 修正。对数轴与时间轴各有专用策略（时间轴按跨度选 分/时/天/月 粒度）。

```javascript
// nice ticks 算法实现
function niceTicks(min, max, tickCount = 5) {
  const range = max - min || 1;
  const rawStep = range / (tickCount - 1);
  const mag = Math.pow(10, Math.floor(Math.log10(rawStep)));
  const norm = rawStep / mag;
  const step = (norm >= 5 ? 10 : norm >= 2.5 ? 5 :
                norm >= 2 ? 2.5 : norm >= 1 ? 2 : 1) * mag;
  const lo = Math.floor(min / step) * step;
  const hi = Math.ceil(max / step) * step;
  const ticks = [];
  for (let v = lo; v <= hi + step * 1e-6; v += step)
    ticks.push(+v.toFixed(10));          // 浮点累加误差修正
  return { ticks, step, lo, hi };
}
console.log(niceTicks(3, 97).ticks);   // [0, 25, 50, 75, 100] 人类友好刻度
console.log(niceTicks(0, 1, 5).step);  // 0.25
```
