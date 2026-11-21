---
title: [H5-078] Canvas 动画循环与帧率如何控制？rAF 有哪些陷阱？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-078：Canvas 动画循环与帧率如何控制？rAF 有哪些陷阱？
**答**：
- `requestAnimationFrame` 回调拿到的 `timestamp` 才是帧时钟基准；用 `performance.now()` 反而可能与渲染帧错位。
- 逻辑更新要与帧率解耦：按 `dt = (ts - last) / 1000` 做增量（`x += v * dt`），144Hz 与 60Hz 屏行为一致。
- 帧率钳制：不是每帧都画时，用"距上次绘制间隔 >= 1000/fps 才 render"实现，rAF 仍按屏幕节拍跑。
- 陷阱：切后台 rAF 自动暂停，回来时 dt 巨大——需 clamp（如 dt 最大 0.05s）；页面隐藏用 `visibilitychange` 停表；组件卸载记得 `cancelAnimationFrame`。
- 长任务掉帧排查：控制台 Performance 面板看长帧；优先减少每帧绘制量（脏矩形/分层）而非"优化循环写法"。

```html
<canvas id="anim" width="480" height="240"></canvas>
<script>
  const cv = document.getElementById('anim');
  const ctx = cv.getContext('2d');
  const state = { x: 0, v: 120 };       // 速度：120 逻辑像素/秒
  let last = null;
  let acc = 0;
  const FPS = 30;                        // 目标帧率：动画 30fps 足够且省电
  const MIN_DT = 1 / FPS;

  function loop(ts) {
    if (last === null) last = ts;
    let dt = (ts - last) / 1000;
    last = ts;
    dt = Math.min(dt, 0.05);             // 切后台回来的巨大 dt 钳掉

    state.x += state.v * dt;             // 逻辑按 dt 增量，帧率无关
    if (state.x > cv.width) state.x = -40;

    acc += dt;
    if (acc >= MIN_DT) {                 // 帧率钳制：间隔不足就跳过绘制
      acc = 0;
      ctx.clearRect(0, 0, cv.width, cv.height);
      ctx.fillStyle = 'seagreen';
      ctx.fillRect(state.x, 100, 40, 40);
    }
    raf = requestAnimationFrame(loop);
  }

  let raf = requestAnimationFrame(loop);

  // 页面隐藏即停，恢复时重置时钟防跳变
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      cancelAnimationFrame(raf);
      last = null;
    } else {
      raf = requestAnimationFrame(loop);
    }
  });
</script>
```

## 十五、SVG 进阶
