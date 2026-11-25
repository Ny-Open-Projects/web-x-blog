---
title: [H5-423] 笔试：手写双指缩放手势 Pinch
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## H5-423：笔试：手写双指缩放手势

**答**：实现 `PinchZoom`：① 双指按下记录初始两指间距与初始 scale；② 双指移动按「当前间距/初始间距」计算新 scale，围绕两指中心点缩放（transform-origin 或矩阵补偿）；③ scale 限制 [min, max]，超界回弹（松手后动画回界值）；④ 双指变单指时锁定当前 scale 转为平移；⑤ 双击切换 1x/2x（tap 间隔 <300ms 判定双击）。写出核心实现（rAF 节流渲染）。

```javascript
class PinchZoom {
  constructor(el, { min = 1, max = 4 } = {}) {
    this.el = el; this.min = min; this.max = max;
    this.scale = 1; this.tx = 0; this.ty = 0;
    let startDist = 0, startScale = 1, cx = 0, cy = 0, lastTap = 0;
    const dist = (t) => Math.hypot(t[0].clientX - t[1].clientX, t[0].clientY - t[1].clientY);
    el.addEventListener('touchstart', (e) => {
      if (e.touches.length === 2) {
        startDist = dist(e.touches); startScale = this.scale;
        cx = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        cy = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      } else if (e.touches.length === 1) {                    // 双击判定
        const now = Date.now();
        if (now - lastTap < 300) this._animate(this.scale > 1.5 ? this.min : 2);
        lastTap = now;
      }
    }, { passive: true });
    el.addEventListener('touchmove', (e) => {
      if (e.touches.length !== 2 || !startDist) return;
      e.preventDefault();
      const s = startScale * dist(e.touches) / startDist;
      this.scale = Math.min(this.max, Math.max(this.min, s));
      const ncx = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      const ncy = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      this.tx += ncx - cx; this.ty += ncy - cy;               // 中心点跟随平移
      cx = ncx; cy = ncy;
      requestAnimationFrame(() => this._render());
    }, { passive: false });
    el.addEventListener('touchend', () => {
      startDist = 0;
      if (this.scale < this.min) this._animate(this.min);     // 回弹
    });
  }
  _render() { this.el.style.transform = `translate(${this.tx}px,${this.ty}px) scale(${this.scale})`; }
  _animate(target) {
    const from = this.scale, t0 = performance.now();
    const step = (t) => {
      const p = Math.min(1, (t - t0) / 200);
      this.scale = from + (target - from) * (1 - Math.pow(1 - p, 3));
      this._render();
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }
}
```

**评分点**：
- 双指间距比值缩放 + 中心点平移补偿，缩放围绕手指
- scale 边界 + 松手回弹动画
- 双指→单指状态切换（startDist 清零）不崩
- 双击 1x/2x 切换与 touchmove preventDefault 阻止页面缩放
