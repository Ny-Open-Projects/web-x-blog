---
title: [PER-718] 手写一个惯性滚动列表：touch 驱动的自定义滚动（transform 位移 + 速度追踪 + 衰减动画）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-718：手写一个惯性滚动列表：touch 驱动的自定义滚动（transform 位移 + 速度追踪 + 衰减动画）

**答**：
- 自定义惯性滚动三步：move 时直接 transform 位移（跟手）；end 时用最近两帧位移算速度（速度 = Δy/Δt，采样窗口 100ms）；惯性用 rAF 衰减（每帧 v *= 0.95，位移累加，速度 < 0.1 停）。
- 要点：速度采样不能只用最后一帧（抖动大），取 100ms 窗口内样本做加权；衰减动画在到达边界时做 bounce 回弹；`will-change: transform` 仅滚动期间开启。
- 边界：滚动期间内容变化（虚拟列表填充）要防跳动；触摸打断惯性（touchstart 时取消 rAF）。
- 评分点：速度窗口采样与边界回弹。

```javascript

class InertialScroller {
  constructor(el, content) {
    this.el = el; this.content = content; this.y = 0; this.raf = null;
    this.samples = [];
    el.addEventListener('touchstart', e => this.onStart(e), { passive: true });
    el.addEventListener('touchmove', e => this.onMove(e), { passive: true });
    el.addEventListener('touchend', () => this.onEnd());
  }
  onStart(e) {
    cancelAnimationFrame(this.raf);                            // 触摸打断惯性
    this.startY = e.touches[0].clientY; this.lastY = this.y;
    this.samples = [{ t: performance.now(), y: this.y }];
    this.content.style.willChange = 'transform';               // 仅滚动期间
  }
  onMove(e) {
    const dy = e.touches[0].clientY - this.startY;
    this.y = this.lastY + dy;
    this.content.style.transform = `translateY(${this.y}px)`;  // 跟手位移
    this.samples.push({ t: performance.now(), y: this.y });
    if (this.samples.length > 6) this.samples.shift();         // 100ms 窗口
  }
  onEnd() {
    // 速度 = 窗口首尾位移 / 时间（避免单帧抖动）
    const first = this.samples[0], last = this.samples.at(-1);
    const v = (last.y - first.y) / Math.max(1, last.t - first.t); // px/ms
    let vel = v;
    const decay = () => {
      vel *= 0.95;                                             // 衰减系数
      this.y += vel * 16;
      const min = this.el.clientHeight - this.content.scrollHeight;
      if (this.y > 0 || this.y < min) {                        // 边界回弹
        this.y = Math.max(min, Math.min(0, this.y));
        this.content.style.transform = `translateY(${this.y}px)`;
        this.content.style.willChange = 'auto';
        return;
      }
      this.content.style.transform = `translateY(${this.y}px)`;
      if (Math.abs(vel) > 0.1) this.raf = requestAnimationFrame(decay);
      else this.content.style.willChange = 'auto';
    };
    this.raf = requestAnimationFrame(decay);
  }
}
```
