---
title: [H5-072] Canvas 的 transform 矩阵是怎么回事？setTransform 与 translate 的关系？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-072：Canvas 的 transform 矩阵是怎么回事？setTransform 与 translate 的关系？
**答**：
- 每个绘制坐标都经过一个 2x3 仿射矩阵映射到画布：`translate/rotate/scale/skew` 都是**右乘**一个增量矩阵，效果依次叠加。
- `setTransform(a,b,c,d,e,f)` 直接**替换**整个矩阵，用于恢复坐标系或导入外部矩阵；`resetTransform()` 等价 `setTransform(1,0,0,1,0,0)`。
- 高频坑：变换叠加顺序影响结果——先 translate 再 rotate ≠ 先 rotate 再 translate；复杂场景用 `save()/restore()` 包裹局部坐标系。
- 矩阵能直接算"世界坐标 ↔ 画布坐标"互转：`DOMMatrix` 提供 `inverse().transformPoint()`，是做拾取、缩放拖拽的数学底座。
- DPR 适配、相机跟随（滚动世界）、镜像绘制本质都是改矩阵，不必手算每个点。

```html
<canvas id="c" width="400" height="400"></canvas>
<script>
  const ctx = document.getElementById('c').getContext('2d');

  // 1) 叠加语义：右乘，后写的先作用于图形
  ctx.save();
  ctx.translate(200, 200);    // 坐标系原点移到中心
  ctx.rotate(Math.PI / 4);    // 再在中心旋转 45 度
  ctx.fillStyle = 'tomato';
  ctx.fillRect(-50, -25, 100, 50);  // 画的是"自身局部坐标"
  ctx.restore();

  // 2) setTransform 直接换矩阵：常用作"相机"
  //    world(x,y) -> screen：先缩放 2 倍再平移相机偏移
  const camera = { x: 30, y: 10, zoom: 2 };
  ctx.setTransform(camera.zoom, 0, 0, camera.zoom, -camera.x * camera.zoom, -camera.y * camera.zoom);
  ctx.strokeRect(0, 0, 100, 100);   // 世界坐标下的矩形

  // 3) 屏幕点反算世界坐标：DOMMatrix 求逆，拖拽/拾取必备
  const m = new DOMMatrix([
    camera.zoom, 0, 0, camera.zoom,
    -camera.x * camera.zoom, -camera.y * camera.zoom,
  ]);
  const world = m.inverse().transformPoint(new DOMPoint(260, 60));
  console.log(world.x, world.y);    // 100, 20
</script>
```
