---
title: [H5-027] Canvas 和 SVG 怎么选型？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-027：Canvas 和 SVG 怎么选型？
**答**：
- SVG：元素级事件、CSS 控制、无限缩放，适合图标、图表、交互流程图；元素数千个后 DOM 开销大。
- Canvas：像素级绘制、成千上万对象仍流畅，适合游戏、粒子、大数据量可视化；但无 DOM、事件要自己做命中检测。
- 记忆公式：静态+交互多选 SVG，动态+对象多选 Canvas。
- 混用常见：ECharts 默认 canvas 渲染，可切 SVG 渲染器换取小数据量下的清晰导出与 a11y。

```html
<!-- 选型对比实验：1000 个方块 -->
<div id="svg-stage"></div>
<canvas id="canvas-stage" width="600" height="400"></canvas>

<script>
  // SVG：1000 个 rect 就是 1000 个 DOM 节点，增删改查都走 DOM，事件可单独绑定
  const svgNS = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(svgNS, 'svg');
  svg.setAttribute('viewBox', '0 0 600 400');
  svg.setAttribute('width', '600');
  svg.setAttribute('height', '400');
  for (let i = 0; i < 1000; i++) {
    const rect = document.createElementNS(svgNS, 'rect');
    rect.setAttribute('x', Math.random() * 580);
    rect.setAttribute('y', Math.random() * 380);
    rect.setAttribute('width', 20);
    rect.setAttribute('height', 20);
    rect.setAttribute('fill', 'steelblue');
    rect.addEventListener('click', (e) => e.target.remove()); // 每个元素有自己的事件
    svg.appendChild(rect);
  }
  document.getElementById('svg-stage').appendChild(svg);

  // Canvas：1000 个方块只是一次次 fillRect，无 DOM，快但点击要自己做命中检测
  const cvs = document.getElementById('canvas-stage');
  const ctx = cvs.getContext('2d');
  const boxes = Array.from({ length: 1000 }, () => ({
    x: Math.random() * 580,
    y: Math.random() * 380,
  }));
  boxes.forEach(({ x, y }) => ctx.fillRect(x, y, 20, 20)); // 一次遍历全部画出

  cvs.addEventListener('click', (e) => {
    const r = cvs.getBoundingClientRect();
    const mx = e.clientX - r.left;
    const my = e.clientY - r.top;
    const hit = boxes.find((b) => mx >= b.x && mx <= b.x + 20 && my >= b.y && my <= b.y + 20);
    console.log(hit ? '点中方块' : '空白'); // 交互成本自己承担
  });
</script>
```

## 六、拖放与文件二进制
