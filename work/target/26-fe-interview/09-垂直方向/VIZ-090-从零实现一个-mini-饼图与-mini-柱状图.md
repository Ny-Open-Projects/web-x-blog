---
title: [VIZ-090] 从零实现一个 mini 饼图与 mini 柱状图。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-090：从零实现一个 mini 饼图与 mini 柱状图。
**答**：饼图核心是极坐标转 path：逐扇区累计角度，`M 圆心 L 弧起点 A 弧终点 Z`，角度过半要设 large-arc 标志，最后一段直接收在 2π 防缝隙。柱状图核心是 max 归一：值/最大值 × 绘图高即柱高，均分带宽防挤。两者都刻意用 SVG 实现——几十个图元的场景 SVG 代码最短、可直接导出。

```javascript
// mini 饼图：极坐标逐扇区生成 path，最后一段收在 2PI 防缝隙
function miniPie(container, data, { size = 120 } = {}) {
  const total = data.reduce((s, d) => s + d.value, 0);
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', `0 0 ${size} ${size}`);
  const R = size / 2 - 4, cx = size / 2, cy = size / 2;
  let angle = -Math.PI / 2;
  data.forEach((d, i) => {
    const a1 = angle;
    const a2 = i === data.length - 1 ? Math.PI * 1.5 : angle + (d.value / total) * Math.PI * 2;
    angle = a2;
    const [x1, y1] = [cx + Math.cos(a1) * R, cy + Math.sin(a1) * R];
    const [x2, y2] = [cx + Math.cos(a2) * R, cy + Math.sin(a2) * R];
    const large = a2 - a1 > Math.PI ? 1 : 0;   // 角度过半需要 large-arc 标志
    svg.insertAdjacentHTML('beforeend',
      `<path d="M${cx},${cy} L${x1},${y1} A${R},${R} 0 ${large} 1 ${x2},${y2} Z"
        fill="hsl(${i * 60},70%,55%)"></path>`);
  });
  container.appendChild(svg);
}
// mini 柱状图：max 归一 -> rect 高度，均分带宽
function miniBar(container, values, { width = 120, height = 40 } = {}) {
  const max = Math.max(...values, 1);
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
  const bw = width / values.length;
  values.forEach((v, i) => svg.insertAdjacentHTML('beforeend',
    `<rect x="${(i * bw + 1).toFixed(1)}" y="${(height - (v / max) * height).toFixed(1)}"
      width="${(bw - 2).toFixed(1)}" height="${((v / max) * height).toFixed(1)}"
      fill="#3b82f6"></rect>`));
  container.appendChild(svg);
}
```
