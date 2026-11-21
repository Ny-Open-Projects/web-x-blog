---
title: [H5-202] Canvas 大量文本渲染怎么优化
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-202：Canvas 大量文本渲染怎么优化

**答**：
- fillText 是 Canvas 里最贵的操作之一（字形排版），千级文本逐条画必卡
- 优化一：静态文本预渲染成离屏 canvas（位图），每帧 drawImage 一张位图代替几百次 fillText
- 优化二：同一 style 的文本批量绘制（减少 fillStyle/font 切换，状态切换有成本）
- 优化三：measureText 结果缓存（同字号同内容的宽度不变），避免每帧重排
- 优化四：视口裁剪，只画可见区域文本（配合滚动偏移计算可见索引区间）

```javascript
// 离屏缓存静态文本层
const layer = document.createElement('canvas');
function renderTextLayer(texts) {
  layer.width = canvas.width; layer.height = canvas.height;
  const c = layer.getContext('2d');
  c.font = '14px sans-serif';
  texts.forEach(t => c.fillText(t.text, t.x, t.y)); // 只画一次
}
function frame() {
  ctx.clearRect(0, 0, w, h);
  ctx.drawImage(layer, 0, 0);        // 位图拷贝，极快
  drawDynamic();                      // 动态元素单独画
  requestAnimationFrame(frame);
}
```
