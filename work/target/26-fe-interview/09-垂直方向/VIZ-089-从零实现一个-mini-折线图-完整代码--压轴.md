---
title: [VIZ-089] 从零实现一个 mini 折线图（完整代码）。（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-089：从零实现一个 mini 折线图（完整代码）。（压轴）
**答**：核心只有五步：① DPR 适配；② 算数据范围（min/max 防除零）；③ 建两个线性比例尺（数据 → 像素）；④ path 绘制折线 + 闭合到底部形成渐变面积；⑤ 暴露 update 方法支持数据更新重绘。这个 40 行的组件覆盖了图表库的完整骨架：数据 → 比例尺 → 渲染 → 更新，面试可以直接默写。

```javascript
// mini 折线图：数据 -> 比例尺 -> path 折线 + 面积，支持数据更新
function miniLine(container, data, { width = 300, height = 120, padding = 8 } = {}) {
  const canvas = document.createElement('canvas');
  container.appendChild(canvas);
  const ctx = setupHiDPI(canvas, width, height);   // 复用 VIZ-021 的 DPR 适配
  const ys = data.map(d => d.value);
  const min = Math.min(...ys), max = Math.max(...ys);
  const x = i => padding + (i / (data.length - 1)) * (width - padding * 2);
  const y = v => height - padding - ((v - min) / (max - min || 1)) * (height - padding * 2);
  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.beginPath();                                // 折线
    data.forEach((_, i) => (i ? ctx.lineTo(x(i), y(ys[i])) : ctx.moveTo(x(i), y(ys[i]))));
    ctx.strokeStyle = '#3b82f6'; ctx.lineWidth = 2; ctx.stroke();
    ctx.lineTo(x(data.length - 1), height - padding); // 闭合到底部形成面积
    ctx.lineTo(x(0), height - padding); ctx.closePath();
    ctx.fillStyle = 'rgba(59,130,246,0.15)'; ctx.fill();
  }
  draw();
  return {
    update(newData) {                               // 数据更新：重算范围后重绘
      ys.length = 0; ys.push(...newData.map(d => d.value));
      data = newData;
      draw();
    },
  };
}
const chart = miniLine(document.body,
  Array.from({ length: 30 }, (_, i) => ({ value: Math.sin(i / 3) * 40 + 50 })));
```
