---
title: [VIZ-182] 实现 DOM 与 Canvas 混合渲染。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-182：实现 DOM 与 Canvas 混合渲染。
**答**：原则：**文本/可访问/富交互用 DOM，图形/海量用 Canvas**。① 分层结构——canvas 底层画图形，DOM 上层透明叠加文本标签/tooltip/按钮，绝对定位对齐；② **同步**——平移缩放时两层共用同一容器 transform 一起动，避免逐元素重排；坐标转换收敛为统一函数 dataToPixel；③ **事件**——DOM 层元素自己接事件，canvas 层自绘命中（quadtree）；④ 典型应用——知识图谱（边 canvas + 节点 DOM 卡片）、地图富标注；⑤ 代价——两层坐标同步、遮挡裁剪、z 序要自己维护。

```javascript
// 混合渲染：Canvas 画边 + DOM 画节点卡片，统一坐标函数
const dataToPixel = p => ({ x: (p.x - view.x) * view.k, y: (p.y - view.y) * view.k });
function render() {
  ctx.clearRect(0, 0, w, h);
  for (const e of edges) {                       // 边走 canvas，量大
    const a = dataToPixel(nodes[e.s]), b = dataToPixel(nodes[e.t]);
    ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
  }
  for (const n of visibleNodes()) {              // 节点走 DOM，支持富文本与交互
    const p = dataToPixel(n);
    n.el.style.transform = `translate(${p.x}px, ${p.y}px)`;  // transform 定位不触发重排
  }
}
zoomLayer.style.transform = `translate(${view.x * view.k}px,${view.y * view.k}px) scale(${view.k})`;
```
