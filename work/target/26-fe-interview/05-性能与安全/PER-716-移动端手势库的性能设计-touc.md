---
title: [PER-716] 移动端手势库的性能设计：touch 序列状态机、手势判定与 300ms 延迟的消除
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-716：移动端手势库的性能设计：touch 序列状态机、手势判定与 300ms 延迟的消除

**答**：
- 手势库核心是一个 touch 状态机：touchstart 记录起点 -> touchmove 累计位移判定意图（tap/swipe/drag/长按）-> touchend 结算；性能要点是**判定逻辑轻**（几何计算 O(1)，不碰 DOM）与**move 节流**（每帧只处理一次）。
- 300ms 延迟的来龙去脉：历史浏览器等待双击缩放判定；现代消除条件是 `viewport` meta 设置 `width=device-width` 或 `touch-action: manipulation`——新项目直接配 meta 即可，不用 fastclick。
- 手势与滚动的冲突治理：垂直滚动容器内的横向 swipe 要 `touch-action: pan-y` 声明让合成器接管滚动，JS 只处理横移；preventDefault 尽量少用（阻断合成器滚动 = 掉帧）。
- 多点触控：双指缩放用 pinch 距离变化，注意 touchcancel 处理（来电/手势打断）——漏掉 cancel 是手势状态机卡死的主因。

```javascript

class GestureDetector {
  constructor(el, { onGesture }) {
    this.start = null; this.onGesture = onGesture;
    el.addEventListener('touchstart', e => this.onStart(e), { passive: true });
    el.addEventListener('touchmove', e => this.onMove(e), { passive: true });   // 不阻断合成滚动
    el.addEventListener('touchend', e => this.onEnd(e), { passive: true });
    el.addEventListener('touchcancel', () => this.reset());    // 来电/打断必须复位
  }
  onStart(e) {
    const t = e.touches[0];
    this.start = { x: t.clientX, y: t.clientY, t: performance.now(), moved: false };
  }
  onMove(e) {
    if (!this.start) return;
    const t = e.touches[0];
    const dx = t.clientX - this.start.x, dy = t.clientY - this.start.y;
    if (Math.abs(dx) > 10 || Math.abs(dy) > 10) this.start.moved = true;  // 超阈值即非 tap
    // 几何计算 O(1)，不碰 DOM —— 判定逻辑不产生布局开销
  }
  onEnd(e) {
    if (!this.start) return;
    const dur = performance.now() - this.start.t;
    if (!this.start.moved && dur < 250) this.onGesture('tap');
    this.reset();
  }
  reset() { this.start = null; }
}
// 300ms 延迟消除：<meta name="viewport" content="width=device-width"> 或 CSS touch-action: manipulation
```
