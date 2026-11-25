---
title: [VIZ-279] 手写箱线图（Box Plot）：五数概括与离群点
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-279：手写箱线图（Box Plot）：五数概括与离群点

**答**：
- 题目：箱线图——五数概括（min/Q1/median/Q3/max）+ 须线（1.5 IQR）+ 离群点散标。实现计算与渲染布局。
- 思路：分位数计算（线性插值法）；IQR = Q3-Q1；须线 = [Q1-1.5IQR, Q3+1.5IQR] 内极值；离群 = 须外散点。
- 评分点：分位数插值法；IQR 须线规则；离群点分离渲染。

```javascript
function boxStats(values) {
  const sorted = [...values].sort((a, b) => a - b);
  const quantile = (p) => {                                // 线性插值分位数
    const idx = p * (sorted.length - 1);
    const lo = Math.floor(idx), frac = idx - lo;
    return sorted[lo] + (sorted[Math.min(lo + 1, sorted.length - 1)] - sorted[lo]) * frac;
  };
  const q1 = quantile(0.25), median = quantile(0.5), q3 = quantile(0.75);
  const iqr = q3 - q1;
  const lowerFence = q1 - 1.5 * iqr, upperFence = q3 + 1.5 * iqr;
  const inliers = sorted.filter(v => v >= lowerFence && v <= upperFence);
  return { min: inliers[0], q1, median, q3, max: inliers.at(-1),
    outliers: sorted.filter(v => v < lowerFence || v > upperFence),   // 离群点
    fences: [lowerFence, upperFence] };
}
// 渲染：箱体（Q1~Q3）+ 中位线 + 须线 + 离群散点（圆点）
```
