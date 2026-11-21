---
title: [H5-206] Canvas 缩放拖拽的坐标系变换怎么做
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-206：Canvas 缩放拖拽的坐标系变换怎么做

**答**：
- 核心是两套坐标：屏幕坐标（鼠标事件值）与世界坐标（画布逻辑值）；变换 = 世界→屏幕 `screen = (world - offset) * scale`
- 缩放锚点：以鼠标位置为中心缩放，缩放后要调整 offset 使鼠标下的世界点保持在原屏幕位置（公式 `offset = mouse - mouse/scale' ... `按推导写）
- 实现顺序：`ctx.setTransform(scale, 0, 0, scale, -offset.x*scale, -offset.y*scale)` 后按世界坐标绘制
- 拾取反向变换：`world = screen/scale + offset`，点击检测用世界坐标比较
- 钩子：滚轮缩放 + 拖拽平移的「手势冲突」用 pointer capture 解决

```javascript
let scale = 1, offset = { x: 0, y: 0 };
function zoomAt(sx, sy, factor) {
  const wx = sx / scale + offset.x, wy = sy / scale + offset.y; // 鼠标下的世界点
  scale *= factor;
  offset.x = wx - sx / scale;  // 让该世界点回到鼠标位置
  offset.y = wy - sy / scale;
}
function render() {
  ctx.setTransform(scale, 0, 0, scale, -offset.x * scale, -offset.y * scale);
  drawWorld();
}
```
