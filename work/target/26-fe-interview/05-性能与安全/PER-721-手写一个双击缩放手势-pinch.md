---
title: [PER-721] 手写一个双击缩放手势（pinch zoom）：双指距离追踪与 transform 缩放的实现要点
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-721：手写一个双击缩放手势（pinch zoom）：双指距离追踪与 transform 缩放的实现要点

**答**：
- 核心：双指时计算两触点距离，相对初始距离的比例作为 scale，中心点作为 transform-origin；单指恢复拖动语义（缩放后的平移）。
- 要点：两指事件里 touches 长度变化（一指先抬起）要做状态降级（从 pinch 平滑切到 pan）；scale 范围钳制（0.5~3）；缩放用 `transform: scale()` 合成器执行，绝不改 width/height。
- 边界：gesturestart（iOS 专有事件）可与系统缩放冲突，需要 `event.preventDefault()`（此时必须非 passive）；双击缩放与 pinch 并存时用 touch-action 控制。
- 评分点：状态降级与钳制。

```javascript

class PinchZoom {
  constructor(el, { min = 0.5, max = 3 } = {}) {
    this.el = el; this.min = min; this.max = max; this.scale = 1;
    el.addEventListener('touchmove', e => this.onMove(e), { passive: false }); // 需阻断系统缩放
    el.addEventListener('touchend', () => this.onEnd());
  }
  onMove(e) {
    if (e.touches.length !== 2) { this.twoFinger = false; return; }
    e.preventDefault();                                         // 阻断系统页面缩放
    const [a, b] = e.touches;
    const dist = Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
    if (!this.twoFinger) {                                      // 进入 pinch 状态
      this.twoFinger = true;
      this.baseDist = dist; this.baseScale = this.scale;
      this.origin = { x: (a.clientX + b.clientX) / 2, y: (a.clientY + b.clientY) / 2 };
    }
    const raw = this.baseScale * (dist / this.baseDist);
    this.scale = Math.max(this.min, Math.min(this.max, raw));   // 钳制
    this.el.style.transformOrigin = `${this.origin.x}px ${this.origin.y}px`;
    this.el.style.transform = `scale(${this.scale})`;           // 合成器执行
  }
  onEnd() {
    if (e?.touches?.length === 1) { this.twoFinger = false; }   // 一指抬起降级为 pan
    else this.twoFinger = false;
  }
}
```
