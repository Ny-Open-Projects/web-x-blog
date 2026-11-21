---
title: [H5-301] 笔试：手写 Canvas 弹幕防遮挡碰撞
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-301：笔试：手写 Canvas 弹幕防遮挡碰撞

**题目**：实现弹幕轨道分配：新弹幕进入时，从上到下找一条「尾随弹幕已驶离安全距离」的轨道；无可用轨道时排队等待；弹幕按恒定速度左移，出屏移除。

**答**：
```javascript
class Danmaku {
  constructor(canvas, speed = 120) { // px/s
    this.ctx = canvas.getContext('2d');
    this.speed = speed;
    this.lanes = Math.ceil(canvas.clientHeight / 36).fill?.() ?? [];
    this.lanes = Array(Math.ceil(canvas.clientHeight / 36)).fill(null); // 每轨道最右弹幕
    this.items = [];
    this.waiting = [];
    let last = 0;
    const loop = (t) => {
      const dt = (t - last) / 1000 || 0; last = t;
      this.update(dt); this.render();
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
  push(text) {
    const w = this.ctx.measureText(text).width + 20;
    const lane = this.pickLane(w);
    if (lane === -1) { this.waiting.push({ text, w }); return; }
    this.spawn(lane, text, w);
  }
  pickLane(w) {
    const cw = this.ctx.canvas.width;
    for (let i = 0; i < this.lanes.length; i++) {
      const prev = this.lanes[i];
      if (!prev || prev.x + prev.w < cw - 60) return i; // 前车已留出安全距离
    }
    return -1;
  }
  spawn(lane, text, w) {
    const item = { text, w, lane, x: this.ctx.canvas.width };
    this.items.push(item);
    this.lanes[lane] = item;
  }
  update(dt) {
    this.items.forEach(it => (it.x -= this.speed * dt));
    // 出屏移除并释放轨道
    this.items = this.items.filter(it => {
      if (it.x + it.w < 0) { this.lanes[it.lane] = null; return false; }
      return true;
    });
    // 队列里补位
    while (this.waiting.length && this.pickLane(this.waiting[0].w) !== -1) {
      const nxt = this.waiting.shift();
      this.spawn(this.pickLane(nxt.w), nxt.text, nxt.w);
    }
  }
  render() {
    const { ctx } = this;
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    ctx.font = '16px sans-serif';
    this.items.forEach(it => ctx.fillText(it.text, it.x, it.lane * 36 + 20));
  }
}
```

**评分点**：
- 轨道模型 + 「前车安全距离」判断（不是判断重叠，而是入场时机）
- 轨道满时入队等待，出屏时从队列补位——不丢弹幕
- dt 时间驱动的位移（帧率无关）
- 出屏释放轨道、measureText 计算弹幕宽度
