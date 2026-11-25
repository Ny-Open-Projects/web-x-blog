---
title: [VIZ-008] SVG 的渲染模型是什么？DOM 开销瓶颈在哪？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-008：SVG 的渲染模型是什么？DOM 开销瓶颈在哪？
**答**：SVG 是 retained mode（保留模式）：每个图形都是一个活的 DOM 节点，浏览器维护完整文档树，修改任意节点都可能触发样式重算、layout 与重绘，且可直接用 CSS/事件/DOM API。代价是节点数增长时内存、样式匹配与渲染树开销线性爆炸——几千节点就开始卡。所以 SVG 适合节点少、强交互、需要无级缩放与导出的场景；节点一多就应换 Canvas。

```html
<svg id="chart" width="600" height="400"></svg>
<script>
  // retained mode：每个 rect 都是活 DOM，创建上万个会拖垮 style/layout
  const svg = document.getElementById('chart');
  const N = 500;
  const frag = document.createDocumentFragment(); // 批量插入避免多次 reflow
  const t0 = performance.now();
  for (let i = 0; i < N; i++) {
    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    rect.setAttribute('x', (i % 50) * 12);
    rect.setAttribute('y', Math.floor(i / 50) * 12);
    rect.setAttribute('width', 10); rect.setAttribute('height', 10);
    rect.setAttribute('fill', `hsl(${i % 360},70%,60%)`);
    frag.appendChild(rect);
  }
  svg.appendChild(frag);
  console.log(`创建 ${svg.childNodes.length} 个节点耗时 ${(performance.now() - t0).toFixed(1)}ms`);
</script>
```
