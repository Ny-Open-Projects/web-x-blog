---
title: [VIZ-013] SVG 的性能边界在哪？节点多了如何优化？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-013：SVG 的性能边界在哪？节点多了如何优化？
**答**：经验阈值：500 节点内随意交互，1k~3k 需要优化，上万节点基本不可用（样式重算 + 合成开销线性爆炸）。优化手段按优先级：**视窗裁剪/虚拟化**——只渲染可视区节点，总数恒定；**减少属性变更**——用 `transform` 而不是 x/y 逐个改，批量改样式用 class；**合并重绘**——DocumentFragment 或 `replaceChildren` 批量插入；**降级**——超阈值自动切 Canvas 渲染器；**文本与滤镜减负**——text 换 canvas 贴图、滤镜只用于静态元素。

```javascript
// 视窗虚拟化：无论数据多少，DOM 节点数恒定在可视窗口量级
const svgRoot = document.querySelector('#root');
function renderVisibleSvg(allData, viewport, rowH = 24) {
  const start = Math.max(0, Math.floor(viewport.scrollTop / rowH) - 5); // 上下各留 5 行缓冲
  const count = Math.ceil(viewport.clientHeight / rowH) + 10;
  const slice = allData.slice(start, start + count); // 视窗裁剪
  const frag = document.createDocumentFragment();
  for (const d of slice) {
    const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    g.setAttribute('transform', `translate(0, ${d.i * rowH})`);
    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    rect.setAttribute('width', d.value); rect.setAttribute('height', rowH - 2);
    g.appendChild(rect); frag.appendChild(g);
  }
  svgRoot.replaceChildren(frag); // 整体替换，节点数不随数据量增长
}
// 超过阈值自动降级：if (data.length > 3000) useCanvasRenderer()
```
