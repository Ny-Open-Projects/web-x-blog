---
title: [VIZ-020] Canvas 的命中检测有哪几种方案？各自适用场景？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-020：Canvas 的命中检测有哪几种方案？各自适用场景？
**答**：三种：① **几何法**——自己按图元形状做点在圆/矩形/多边形内判断，最快、可配合空间索引（quadtree/grid）支撑百万图元，需要自己维护图元几何表；② **isPointInPath / isPointInStroke**——把命中交给上下文，对复杂贝塞尔形状省心，但每次调用都要重建 path，量大时慢；③ **像素法**——`getImageData` 读该像素 alpha（或专属拾色色板 hit-map），对任意渲染结果通用，但读回 GPU 位图慢且需维护离屏拾取层。实践：常规图元用几何法 + 索引，异形元素用像素拾取层兜底。

```javascript
// 命中检测：几何法为主（倒序遍历，后画的在上层），复杂异形再考虑像素法
const shapes = [
  { type: 'circle', x: 100, y: 100, r: 30, id: 'a' },
  { type: 'rect', x: 200, y: 50, w: 80, h: 40, id: 'b' },
];
function hitTest(px, py) {
  for (let i = shapes.length - 1; i >= 0; i--) {
    const s = shapes[i];
    if (s.type === 'circle' && (px - s.x) ** 2 + (py - s.y) ** 2 <= s.r ** 2) return s.id;
    if (s.type === 'rect' && px >= s.x && px <= s.x + s.w && py >= s.y && py <= s.y + s.h) return s.id;
  }
  return null;
}
canvas.addEventListener('mousemove', e => {
  // 高频事件里只做几何判断；isPointInPath 需重建 path，getImageData 需读回位图，均更贵
  hoverShape = hitTest(e.offsetX, e.offsetY);
});
// 像素拾取法示意：离屏 hit-map 给每个图元分配唯一颜色，读 alpha/RGB 反查 id
function pickByPixel(hitCtx, x, y) {
  const [r, g, b] = hitCtx.getImageData(x, y, 1, 1).data;
  return r || g || b ? (r << 16) | (g << 8) | b : null; // 颜色即图元 id
}
```
