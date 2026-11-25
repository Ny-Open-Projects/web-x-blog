---
title: [H5-179] 设计一个在线画板（Canvas 全技术栈整合）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-179：设计一个在线画板（Canvas 全技术栈整合）
**答**：
- 架构：**分层 canvas**（已提交笔画层 + 正在绘制层）+ 数据模型（笔画数组）+ rAF 合帧渲染；Pointer Events 统一鼠标/触摸/笔。
- 体验关键：`getCoalescedEvents()` 拿被合并的高频采样点（快速运笔不丢细节）；中点法平滑曲线；压感 `e.pressure` 决定笔宽。
- 撤销：笔画可序列化入历史栈，undo = 弹栈 + 主层重放（量大时换增量擦除或分层缓存）。
- 协作概览：WebSocket 广播**矢量笔画指令**而非位图，服务端定序；新加入者先拉快照再追增量；冲突按 clientId+seq 重放。
- 性能：`touch-action: none` 防手势冲突、dpr 适配、撤销栈上限、协作消息合并。

```html
<div class="board">
  <canvas id="main"></canvas>   <!-- 已提交笔画层 -->
  <canvas id="live"></canvas>   <!-- 正在绘制层，每帧重绘 -->
</div>
<style>
  .board { position: relative; height: 320px; }
  canvas { position: absolute; inset: 0; touch-action: none; }  /* 禁掉默认手势 */
</style>
<script>
const dpr = devicePixelRatio || 1;
function layer(sel) {
  const c = document.querySelector(sel);
  c.width = c.clientWidth * dpr; c.height = c.clientHeight * dpr;
  const ctx = c.getContext('2d');
  ctx.scale(dpr, dpr);
  return { c, ctx };
}
const main = layer('#main'), live = layer('#live');
const pt = (e) => {
  const r = e.target.getBoundingClientRect();
  return { x: e.clientX - r.left, y: e.clientY - r.top };
};
const syncBroadcast = (s) => { /* ws.send(JSON.stringify(s)) 协作同步 */ };

// 1) Pointer Events 统一鼠标/触摸/笔，压感来自 e.pressure
const history = [];
let current = null;

live.c.addEventListener('pointerdown', (e) => {
  live.c.setPointerCapture(e.pointerId);
  current = { points: [pt(e)], color: '#111', width: 3 + e.pressure * 5 };
});
live.c.addEventListener('pointermove', (e) => {
  if (!current) return;
  // getCoalescedEvents：拿到被浏览器合并的高频采样点，快速运笔不丢细节
  for (const ev of e.getCoalescedEvents?.() ?? [e]) current.points.push(pt(ev));
  dirty = true;
});
addEventListener('pointerup', () => {
  if (!current) return;
  drawStroke(main.ctx, current);            // 提交到主层
  history.push(current);
  syncBroadcast(current);                   // 协作：发矢量笔画，不是位图
  current = null;
  live.ctx.clearRect(0, 0, live.c.clientWidth, live.c.clientHeight);
});

// 2) 渲染节流：数据变更 → rAF 合帧
let dirty = false;
(function tick() {
  if (dirty && current) {
    dirty = false;
    live.ctx.clearRect(0, 0, live.c.clientWidth, live.c.clientHeight);
    drawStroke(live.ctx, current);
  }
  requestAnimationFrame(tick);
})();

// 3) 中点法平滑绘制（见 H5-128）
function drawStroke(ctx, s) {
  ctx.strokeStyle = s.color;
  ctx.lineWidth = s.width;
  ctx.lineCap = ctx.lineJoin = 'round';
  ctx.beginPath();
  const p = s.points;
  ctx.moveTo(p[0].x, p[0].y);
  for (let i = 1; i < p.length - 1; i++) {
    ctx.quadraticCurveTo(p[i].x, p[i].y,
      (p[i].x + p[i + 1].x) / 2, (p[i].y + p[i + 1].y) / 2);
  }
  ctx.stroke();
}

// 4) 撤销：重放历史（笔画可序列化；量大时换增量擦除/分层缓存）
function undo() {
  history.pop();
  main.ctx.clearRect(0, 0, main.c.clientWidth, main.c.clientHeight);
  history.forEach((s) => drawStroke(main.ctx, s));
}

// 5) 协作概览：WebSocket 广播笔画指令（矢量），服务端定序广播；
//    新加入者先拉全量快照再追增量；笔画带 clientId+seq，按服务端顺序重放
// 6) 性能清单：分层 canvas + rAF 合帧 + 撤销栈上限 + touch-action: none
</script>
```
