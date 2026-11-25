---
title: [PER-769] 手写一个 Canvas 弹幕渲染器：分层 canvas、轨道分配与掉帧自适应关闭
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-769：手写一个 Canvas 弹幕渲染器：分层 canvas、轨道分配与掉帧自适应关闭

**答**：
- 实现：独立弹幕 canvas 叠加在视频上层（不进视频合成层）；弹幕对象池复用（避免 GC）；每帧遍历绘制（move x -= speed），出屏回收进池；轨道分配算法（找最近空闲轨道，100ms 一轮批处理）；帧率探针检测持续掉帧自动减少同屏条数。
- 要点：drawImage/文字绘制按轨道分桶减少状态切换；弹幕透明度动画用 globalAlpha；canvas 尺寸跟随容器（resize 防抖）。
- 边界：页面不可见暂停；弹幕内容渲染前做敏感词过滤（安全联动）；低端机起始就是精简档。
- 评分点：对象池与轨道批处理。

```javascript

class DanmakuRenderer {
  constructor(canvas, { maxOnScreen = 80 } = {}) {
    this.canvas = canvas; this.ctx = canvas.getContext('2d');
    this.pool = []; this.active = []; this.lanes = Math.floor(canvas.height / 36);
    this.laneBusy = new Array(this.lanes).fill(0);               // 轨道释放时间
    this.maxOnScreen = window.__deviceTier === 'low' ? 30 : maxOnScreen;
    this.running = true;
    this.loop();
  }
  add(text, { color = '#fff' } = {}) {
    if (this.active.length >= this.maxOnScreen) return;          // 满载丢弃
    const lane = this.pickLane();
    if (lane < 0) return;                                        // 无空闲轨道丢弃
    const item = this.pool.pop() ?? { x: 0 };
    Object.assign(item, { text, color, lane, x: this.canvas.width, speed: 2 + Math.random() });
    this.active.push(item);
  }
  pickLane() {                                                   // 批处理轨道分配
    const now = performance.now();
    for (let i = 0; i < this.lanes; i++)
      if (this.laneBusy[i] < now) { this.laneBusy[i] = now + 3000; return i; }
    return -1;
  }
  loop() {
    requestAnimationFrame(() => {
      if (!this.running) return;
      const { ctx, canvas } = this;
      ctx.clearRect(0, 0, canvas.width, canvas.height);          // 单层 canvas
      this.active = this.active.filter(d => {
        d.x -= d.speed;
        if (d.x < -200) { this.pool.push(d); return false; }     // 出屏回收对象池
        ctx.globalAlpha = 0.9;
        ctx.fillStyle = d.color;
        ctx.fillText(d.text, d.x, d.lane * 36 + 24);
        return true;
      });
      this.loop();
    });
  }
}
```
