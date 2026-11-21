---
title: [HW-300] 手写一个 Tooltip 智能定位：翻转与移位策略与溢出检测
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-300：手写一个 Tooltip 智能定位：翻转与移位策略与溢出检测

**答**：
- 需求：实现 Tooltip：定位在目标元素指定方位（top/bottom/left/right）；溢出检测（tooltip 超出视口时按优先级尝试翻转方位 → 移位收缩到视口内）；箭头位置跟随；滚动/resize 重算。
- 边界：翻转顺序（首选 → 对侧 → 相邻侧 → 收缩移位）；与视口边最小间距 8px；目标元素部分在视口外时跟随可见部分。
- 评分点：翻转优先级；移位钳制；重算时机。

```javascript
class Tooltip {
  constructor(contentEl, { margin = 8 } = {}) { this.el = contentEl; this.margin = margin; }
  show(target, preferred = 'top') {
    const order = { top: ['top', 'bottom', 'right', 'left'],
      bottom: ['bottom', 'top', 'right', 'left'],
      left: ['left', 'right', 'top', 'bottom'],
      right: ['right', 'left', 'top', 'bottom'] }[preferred];
    const tr = target.getBoundingClientRect();
    const tw = this.el.offsetWidth, th = this.el.offsetHeight;
    let placed = null;
    for (const side of order) {                              // 翻转尝试
      const p = this.positionOf(side, tr, tw, th);
      if (this.fits(p, tw, th)) { placed = { side, ...p }; break; }
    }
    if (!placed) {                                           // 全溢出：移位钳制
      const p = this.positionOf(preferred, tr, tw, th);
      placed = { side: preferred,
        x: clamp(p.x, this.margin, innerWidth - tw - this.margin),
        y: clamp(p.y, this.margin, innerHeight - th - this.margin) };
    }
    this.el.style.transform = `translate(${placed.x}px, ${placed.y}px)`;
    this.arrow(placed.side, tr);                             // 箭头跟随
  }
  positionOf(side, tr, tw, th) {
    const m = this.margin;
    const map = {
      top: { x: tr.left + tr.width / 2 - tw / 2, y: tr.top - th - m },
      bottom: { x: tr.left + tr.width / 2 - tw / 2, y: tr.bottom + m },
      left: { x: tr.left - tw - m, y: tr.top + tr.height / 2 - th / 2 },
      right: { x: tr.right + m, y: tr.top + tr.height / 2 - th / 2 },
    };
    return map[side];
  }
  fits(p, tw, th) {
    return p.x >= this.margin && p.y >= this.margin
      && p.x + tw <= innerWidth - this.margin
      && p.y + th <= innerHeight - this.margin;
  }
  arrow(side, tr) { this.el.dataset.side = side; }           // CSS 按侧渲染箭头
}
const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
```
