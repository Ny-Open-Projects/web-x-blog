---
title: [VIZ-154] 超大 SVG（几万个节点）如何降维救场？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-154：超大 SVG（几万个节点）如何降维救场？
**答**：SVG 节点多后 DOM 重排与事件委托都会崩，降维方案：① **栅格化**——整幅 SVG 转 Canvas 位图（serialize → Image → drawImage），交互缩放改用瓦片金字塔像地图一样按视口重绘；② **按需矢量**——只保留视口内元素虚拟化，其余走图片；③ **结构简化**——同样式路径合并 d、去 filter/clip-path（GPU 慢源）、CSS 分层；④ **事件**——SVG 容器 pointer-events: none，命中改用几何索引（R-tree/quadtree）反查 DOM；⑤ **混合渲染**——图形层 Canvas + 文字层 SVG（清晰可选中）。能换渲染引擎就别死磕 SVG。

```javascript
// SVG 栅格化 + 几何索引命中：把 N 万节点 SVG 变成地图体验
async function svgToCanvas(svgEl, scale = 2) {
  const { width, height } = svgEl.viewBox.baseVal;
  const blob = new Blob([new XMLSerializer().serializeToString(svgEl)], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(blob);
  const img = new Image();
  await new Promise(res => { img.onload = res; img.src = url; });
  const canvas = document.createElement('canvas');
  canvas.width = width * scale; canvas.height = height * scale;
  canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
  URL.revokeObjectURL(url);
  return canvas;   // 交互层：缩放平移画这张位图
}
// 命中索引：元素几何信息建 quadtree，鼠标事件查树反查 DOM
qt.add({ x, y, w, h, elRef });
container.addEventListener('pointermove', e =>
  highlight(qt.collides(hitBox(e))[0]?.elRef));
```
