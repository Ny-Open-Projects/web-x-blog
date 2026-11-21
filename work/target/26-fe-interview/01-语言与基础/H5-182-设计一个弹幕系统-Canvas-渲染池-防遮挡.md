---
title: [H5-182] 设计一个弹幕系统（Canvas 渲染池/防遮挡/发送）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-182：设计一个弹幕系统（Canvas 渲染池/防遮挡/发送）
**答**：
- 渲染：Canvas 而非 DOM（同屏千条弹幕 DOM 撑不住）；时间驱动（速度 × dt）而非帧驱动；对象池复用弹幕对象，避免 GC 抖动。
- 弹道分配：每条弹幕入"通道"，新弹幕选**尾部已离开右侧最远**的通道；通道满时随机或排队丢弃。
- 可读性：描边 + 半透明降低遮挡感；防遮挡进阶是"智能防挡"——把视频主体区域（人像分割）设为禁区让弹幕绕行；产品侧配合半屏模式与密度限流。
- 发送：输入回车 → 本地立即渲染（金色标记"自己"）+ 上行服务端广播；接收端节流渲染。

```html
<div class="player">
  <video src="live.mp4" muted autoplay></video>
  <canvas id="danmu" width="480" height="180"></canvas>
</div>
<style>
  .player { position: relative; width: 480px; }
  #danmu { position: absolute; top: 0; left: 0; pointer-events: none; }
</style>
<script>
const layer = document.getElementById('danmu');
const ctx = layer.getContext('2d');
const W = layer.width, H = layer.height;
const LANES = 5, LANE_H = 36;
const pool = [], active = [];                 // 对象池复用，避免 GC 抖动
const acquire = () => pool.pop() ?? {};

// 1) 弹道分配：选"最空"通道 —— 该通道弹幕尾部离右侧最远
function pickLane(now) {
  let best = 0, bestGap = -1;
  for (let l = 0; l < LANES; l++) {
    let minTail = W;
    for (const d of active) if (d.lane === l) {
      const tail = W - (now - d.t0) * d.speed + d.text.length * d.fontSize;
      if (tail < minTail) minTail = tail;
    }
    if (minTail > bestGap) { bestGap = minTail; best = l; }
  }
  return best;
}

function send(text, { self = false } = {}) {
  const fontSize = self ? 28 : 20;
  active.push(Object.assign(acquire(), {
    text, fontSize,
    speed: 90 + Math.random() * 60,           // px/s
    lane: pickLane(performance.now()),
    t0: performance.now(),
    color: self ? '#ffd700' : '#fff',
  }));
}

// 2) 渲染循环：时间驱动（速度 x dt），出屏回收进池
let last = performance.now();
function frame(now) {
  ctx.clearRect(0, 0, W, H);
  for (let i = active.length - 1; i >= 0; i--) {
    const d = active[i];
    const x = W - (now - d.t0) * d.speed;
    if (x < -d.text.length * d.fontSize - 20) {
      pool.push(d); active.splice(i, 1); continue;       // 出屏回收
    }
    ctx.font = `${d.fontSize}px sans-serif`;
    ctx.lineWidth = 3;
    ctx.strokeStyle = 'rgba(0,0,0,.6)';                  // 描边保证可读性
    ctx.globalAlpha = 0.85;                              // 半透明降低遮挡感
    ctx.strokeText(d.text, x, d.lane * LANE_H + 26);
    ctx.fillStyle = d.color;
    ctx.fillText(d.text, x, d.lane * LANE_H + 26);
  }
  ctx.globalAlpha = 1;
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

// 3) 发送：本地立即渲染（金色标记"自己"）+ 上行服务端广播
document.getElementById('send').addEventListener('click', () => {
  const text = input.value.trim();
  if (!text) return;
  send(text, { self: true });
  ws.send(JSON.stringify({ type: 'danmu', text }));
});
// 4) 防遮挡：热门时刻降密度（发送节流）+ 半屏模式 + 智能防挡（人像分割禁区绕行）
// 5) 暂停：视频 pause 时冻结 now 基线（记录暂停时刻，恢复时平移所有 t0）
</script>
```
