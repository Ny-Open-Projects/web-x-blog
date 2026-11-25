---
title: [VIZ-278] 手写迷你图（Sparkline）：无轴微型图
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-278：手写迷你图（Sparkline）：无轴微型图

**答**：
- 题目：Sparkline——表格单元格内微型趋势线（无轴无网格，仅折线+末点标记+涨跌色）。极简渲染（一个 path）。
- 思路：数据归一到单元格内坐标；单 path；末点圆点 + 首尾值涨跌色（涨绿跌红）。
- 评分点：归一化；单 path 性能；涨跌色语义。

```javascript
function sparkline(values, { w = 80, h = 24 } = {}) {
  const min = Math.min(...values), max = Math.max(...values);
  const range = max - min || 1;
  const points = values.map((v, i) =>
    [i / (values.length - 1) * w, h - (v - min) / range * (h - 4) - 2]);
  const d = points.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join('');
  const up = values.at(-1) >= values[0];
  const last = points.at(-1);
  return { path: d, dot: { x: last[0], y: last[1] },
    color: up ? '#52c41a' : '#f5222d',                    // 涨跌色
    bg: up ? 'rgba(82,196,26,0.08)' : 'rgba(245,34,45,0.08)' };   // 背景微渐变
}
// 表格内嵌：一个 <path> + 一个 <circle>，无轴无网格——视觉噪音最小
```
