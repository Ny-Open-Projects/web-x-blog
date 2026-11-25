---
title: [H5-073] 离屏 canvas 与双缓冲如何消除闪烁和撕裂？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-073：离屏 canvas 与双缓冲如何消除闪烁和撕裂？
**答**：
- 双缓冲 = 在**离屏 canvas** 上完成整帧绘制，再用 `drawImage` 一次性搬上屏；屏幕永远只看到"完整帧"，避免逐个绘制造成的中间态闪烁。
- 离屏创建两条路：`document.createElement('canvas')` 或 `new OffscreenCanvas(w, h)`（Worker 可用，不进 DOM）。
- 相比逐对象绘制，`drawImage` 是位块拷贝，性能远高于重绘大量矢量指令，这是 H5-023 缓存思路的帧级版本。
- 与脏矩形（下一题）可以叠加：缓存层整帧更新 + 屏层只拷贝变化区域，兼得两者。
- 注意内存：离屏尺寸 = 显示尺寸 x DPR，别按物理像素翻倍再翻倍。

```html
<canvas id="stage" width="800" height="450"></canvas>
<script>
  const stage = document.getElementById('stage');
  const sctx = stage.getContext('2d');

  // 后缓冲：与舞台同尺寸的离屏画布
  const off = new OffscreenCanvas(stage.width, stage.height);
  const octx = off.getContext('2d');

  let t = 0;
  function drawScene(g, t) {
    g.clearRect(0, 0, stage.width, stage.height);
    // 复杂场景：背景、网格、上百个元素全部画在后缓冲
    for (let i = 0; i < 200; i++) {
      const x = (i * 37 + t) % stage.width;
      const y = 80 + Math.sin((t + i * 13) / 40) * 60;
      g.fillStyle = `hsl(${(i * 7 + t) % 360} 70% 60%)`;
      g.beginPath();
      g.arc(x, y, 10, 0, Math.PI * 2);
      g.fill();
    }
  }

  function frame() {
    t += 1;
    drawScene(octx, t);            // 1. 整帧绘制到离屏
    sctx.clearRect(0, 0, stage.width, stage.height);
    sctx.drawImage(off, 0, 0);     // 2. 一次位块拷贝上屏：无中间态
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
</script>
```
