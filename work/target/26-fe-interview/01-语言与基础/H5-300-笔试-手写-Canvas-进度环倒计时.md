---
title: [H5-300] 笔试：手写 Canvas 进度环倒计时
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-300：笔试：手写 Canvas 进度环倒计时

**题目**：实现倒计时进度环：剩余时间数字居中 + 外圈进度弧（随时间递减）；DPR 高清、暂停/恢复能力、结束时触发回调。

**答**：
```javascript
function countdownRing(canvas, seconds, onEnd) {
  const ctx = canvas.getContext('2d');
  const dpr = Math.min(devicePixelRatio, 2);
  const size = canvas.clientWidth;
  canvas.width = canvas.height = size * dpr;
  ctx.scale(dpr, dpr);
  const c = size / 2, r = size / 2 - 6;
  let remain = seconds * 1000, paused = false, last = performance.now(), raf;

  function draw() {
    ctx.clearRect(0, 0, size, size);
    // 底环
    ctx.lineWidth = 6; ctx.strokeStyle = '#eee';
    ctx.beginPath(); ctx.arc(c, c, r, 0, Math.PI * 2); ctx.stroke();
    // 进度弧：从顶部顺时针递减
    ctx.strokeStyle = '#4285f4'; ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.arc(c, c, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * (remain / (seconds * 1000)));
    ctx.stroke();
    // 数字
    ctx.fillStyle = '#333'; ctx.font = '20px sans-serif';
    ctx.textAlign = 'middle'; ctx.textBaseline = 'middle';
    ctx.fillText(Math.ceil(remain / 1000), c, c);
  }
  function loop(t) {
    if (!paused) {
      remain -= t - last;
      if (remain <= 0) { remain = 0; draw(); return onEnd?.(); }
      draw();
    }
    last = t;
    raf = requestAnimationFrame(loop);
  }
  raf = requestAnimationFrame(loop);
  return {
    pause() { paused = true; },
    resume() { paused = false; last = performance.now(); },
    destroy() { cancelAnimationFrame(raf); },
  };
}
```

**评分点**：
- 倒计时用「剩余毫秒数」累计而不是每秒减一（rAF 跳帧不失真）
- 弧的起始角 -PI/2（12 点方向）+ 比例映射
- DPR 缩放与 clientWidth 基准
- pause/resume 用 last 时间戳校准，destroy 清 raf
