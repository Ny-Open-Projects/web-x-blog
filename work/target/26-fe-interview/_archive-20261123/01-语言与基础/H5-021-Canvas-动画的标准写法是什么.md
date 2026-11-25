---
title: [H5-021] Canvas 动画的标准写法是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-021：Canvas 动画的标准写法是什么？
**答**：
- 套路是"清屏 → 更新状态 → 重绘"，循环用 requestAnimationFrame 驱动，帧间隔用 delta time 校准速度。
- 不要在循环里 new 对象或频繁扩容，状态用闭包/类字段保存。
- 动画结束或元素离屏时要 cancelAnimationFrame，防止空转耗电。
- 简单缓动可手写插值函数，不必引库。

```html
<canvas id="anim" width="400" height="200" style="width:400px;height:200px;"></canvas>

<script>
  const ctx = document.getElementById('anim').getContext('2d');
  const ball = { x: 0, y: 100, vx: 120 }; // vx 单位：像素/秒

  let rafId = null;
  let last = performance.now();

  function frame(now) {
    const dt = (now - last) / 1000; // delta time 秒
    last = now;

    ball.x += ball.vx * dt; // 帧率无关的位移
    if (ball.x > 420) ball.x = -20; // 循环

    ctx.clearRect(0, 0, 400, 200); // 1. 清屏
    ctx.fillStyle = '#3367d6'; //    2. 更新后的状态绘制
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, 12, 0, Math.PI * 2);
    ctx.fill();

    rafId = requestAnimationFrame(frame); // 3. 排下一帧
  }
  rafId = requestAnimationFrame(frame);

  // 页面不可见或组件卸载时停止，避免后台空转
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) cancelAnimationFrame(rafId);
    else {
      last = performance.now(); // 恢复时校准 last，防止 dt 巨大跳变
      rafId = requestAnimationFrame(frame);
    }
  });
</script>
```
