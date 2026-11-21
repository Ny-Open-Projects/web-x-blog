---
title: [H5-126] 单个 canvas 卡顿，为什么"分层 canvas"能解决？怎么设计？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-126：单个 canvas 卡顿，为什么"分层 canvas"能解决？怎么设计？
**答**：
- 把"几乎不变"的背景/静态图形与"每帧变化"的动态元素画到**叠加的多个 canvas**（CSS 绝对定位叠放），动态层每帧只 clear + 重绘自己，静态层一次绘制后不再动。
- 核心收益：重绘面积从"整画布"缩小到"脏区域"，静态层不需要每帧重放几百条绘制指令。
- 配合技巧：透明背景用 `clearRect` 而不是盖色；给不需要交互的层设 `pointer-events: none`；事件层单独拆一层，拾取逻辑与渲染解耦。
- 判断标准：重绘内容 < 画布面积 30%、或静态元素指令数很大（网格、背景纹理）时收益最大；元素极少时多层反而增加合成成本。
- 极致方案：脏矩形——只 clearRect/重绘变化区域，配合分层把"整帧"变"局部帧"。

```html
<div class="stage">
  <canvas id="bg" class="layer"></canvas>   <!-- 静态层：只画一次 -->
  <canvas id="fx" class="layer"></canvas>   <!-- 动态层：每帧重绘 -->
</div>
<style>
  .stage { position: relative; width: 480px; height: 320px; }
  .layer { position: absolute; inset: 0; }
  #fx { pointer-events: none; }  /* 动态层不接事件，穿透到静态层 */
</style>
<script>
const dpr = devicePixelRatio || 1;
function setup(canvas) {
  canvas.width = 480 * dpr;
  canvas.height = 320 * dpr;
  canvas.getContext('2d').scale(dpr, dpr);
}
const bg = document.getElementById('bg'), fx = document.getElementById('fx');
setup(bg); setup(fx);

// 静态层：网格背景只在初始化/尺寸变化时画一次
{
  const c = bg.getContext('2d');
  c.strokeStyle = '#e5e7eb';
  c.beginPath();
  for (let x = 0; x <= 480; x += 24) { c.moveTo(x, 0); c.lineTo(x, 320); }
  for (let y = 0; y <= 320; y += 24) { c.moveTo(0, y); c.lineTo(480, y); }
  c.stroke();
}

// 动态层：小球动画每帧只清空自己这一层，静态层完全不受影响
const ball = { x: 40, y: 40, vx: 2.4, vy: 1.8 };
function frame() {
  const c = fx.getContext('2d');
  c.clearRect(0, 0, 480, 320);          // 透明清屏，不遮挡静态层
  ball.x += ball.vx; ball.y += ball.vy;
  if (ball.x < 8 || ball.x > 472) ball.vx *= -1;
  if (ball.y < 8 || ball.y > 312) ball.vy *= -1;
  c.beginPath(); c.arc(ball.x, ball.y, 8, 0, Math.PI * 2);
  c.fillStyle = '#2563eb'; c.fill();
  requestAnimationFrame(frame);
}
frame();
</script>
```
