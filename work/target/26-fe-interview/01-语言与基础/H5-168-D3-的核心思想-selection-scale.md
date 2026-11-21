---
title: [H5-168] D3 的核心思想（selection/scale/axis）是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-168：D3 的核心思想（selection/scale/axis）是什么？
**答**：
- **数据驱动文档**：`selection.data(join)` 把数据数组绑到 DOM 集合，enter/update/exit 三态分别处理新增/更新/删除——这是 D3 一切图表的骨架。
- **scale** 是"数据域 → 视觉域"的映射函数（linear/band/time/log），图表里所有坐标都应该是 scale 的输出而不是手算。
- **axis/shape 生成器**：基于 scale 生成刻度、path、arc、line——D3 不封装图表，只提供这些原语，与 ECharts（开箱即用）定位相反。
- 现代姿势：与框架配合时"D3 算坐标、React/Vue 管 DOM"；完整接管 DOM 的 select 方式与 vdom 会打架。

```html
<svg id="chart" width="320" height="200"></svg>
<script>
// D3 三大原语：selection（数据绑定）、scale（映射）、axis（坐标轴）
const data = [30, 80, 45, 95, 60, 20];
const W = 320, H = 200, M = { top: 10, right: 10, bottom: 24, left: 24 };
const NS = 'http://www.w3.org/2000/svg';

// scale：数据域 [0, max] → 值域（屏幕 y 向下，所以反向）
const yMax = Math.max(...data);
const scaleY = (v) => (H - M.top - M.bottom) * (1 - v / yMax) + M.top;
// band scale：类别 → x 位置（手写演示，D3 里是 d3.scaleBand）
const step = (W - M.left - M.right) / data.length;
const scaleX = (i) => M.left + i * step + step * 0.15;

// selection.data join 思想：enter 新增 / update 更新 / exit 删除
const svg = document.getElementById('chart');
// enter：缺多少补多少
for (let i = svg.querySelectorAll('rect').length; i < data.length; i++) {
  svg.append(document.createElementNS(NS, 'rect'));
}
// update：绑数据 + 写属性
[...svg.querySelectorAll('rect')].forEach((r, i) => {
  r.setAttribute('x', scaleX(i));
  r.setAttribute('y', scaleY(data[i]));
  r.setAttribute('width', step * 0.7);
  r.setAttribute('height', H - M.bottom - scaleY(data[i]));
  r.setAttribute('fill', '#2563eb');
});
// exit：多了就删
[...svg.querySelectorAll('rect')].slice(data.length).forEach((r) => r.remove());

// axis 本质：基于 scale 生成"刻度线 + 文本"的 g（D3 里一行 d3.axisBottom(scale)）
// 面试口径：
// 1) D3 不出图表只出原语：join 模型 + 映射函数 + 形状生成器（path/arc/line）
// 2) 与框架配合：D3 负责"算"（scale/layout），React/Vue 负责"画"（渲染）
// 3) 标准统计图优先 ECharts/Recharts，需要深度定制交互/布局再上 D3
</script>
```

## 二十八、Web Components 实战
