---
title: [VIZ-091] 实现双 Y 轴刻度对齐。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-091：实现双 Y 轴刻度对齐。
**答**：双轴不对齐的根因是两轴各自取整后网格线数量/位置不一致。解法：两轴用**相同的 tick 数**，各自做 nice 取整（把 min/max 调整到"好看"的步长倍数上），这样两轴的刻度线共享同一组像素位置。进阶要求：让两轴 0 线也对齐——以两轴 span 的比例做映射换算，避免两序列在 0 线上下交叉产生视觉误导。校验手段：截图检查网格线是否一一重合。

```javascript
// 双 Y 轴对齐：两轴同 tick 数 + 各自 nice 取整 -> 刻度线共享同一组像素位置
function alignedDualAxis(leftData, rightData, ticks = 5) {
  const nice = (min, max) => {
    const span = max - min || 1;
    const rough = span / (ticks - 1);
    const mag = 10 ** Math.floor(Math.log10(rough));
    const norm = rough / mag;                        // 归到 1~10
    const step = mag * (norm >= 7.5 ? 10 : norm >= 3 ? 5 : norm >= 1.5 ? 2 : 1);
    return {
      min: Math.floor(min / step) * step,
      max: Math.ceil(max / step) * step,
      interval: step,
    };
  };
  const L = nice(Math.min(...leftData), Math.max(...leftData));
  const R = nice(Math.min(...rightData), Math.max(...rightData));
  return { // 两轴 tick 数相同 -> 网格线天然对齐，0 线是否重合取决于区间
    left: { min: L.min, max: L.max, interval: L.interval },
    right: { min: R.min, max: R.max, interval: R.interval },
  };
}
```
