---
title: [HW-341] 手写一个 Canvas 渲染循环：脏区域检测与局部重绘
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-341：手写一个 Canvas 渲染循环：脏区域检测与局部重绘

**答**：
- 需求：实现 CanvasRenderer：全量重绘与脏区域（dirty rect）两种模式；节点标记 dirty → 收集脏包围盒（相交合并）→ 仅重绘相交节点；requestAnimationFrame 合帧（一帧最多一次重绘）。
- 边界：脏盒合并（相交或邻近合并减少 draw call）；透明节点脏盒扩大（阴影/模糊）；clearRect 精确清脏区。
- 评分点：脏区合并；仅重绘相交节点；rAF 合帧。

```javascript
class CanvasRenderer {
  constructor(canvas, nodes) { this.ctx = canvas.getContext('2d'); this.nodes = nodes;
    this.dirty = []; this.raf = null; }
  markDirty(node) {
    this.dirty.push(expandBox(bounds(node)));                // 透明效果扩盒
    if (!this.raf) this.raf = requestAnimationFrame(() => this.render());
  }
  render() {
    this.raf = null;
    if (!this.dirty.length) return this.renderAll();
    const merged = mergeBoxes(this.dirty);                   // 脏盒合并
    for (const box of merged) {
      this.ctx.clearRect(box.x, box.y, box.w, box.h);        // 精确清脏区
      for (const n of this.nodes)
        if (intersects(bounds(n), box)) this.drawNode(n);    // 仅重绘相交节点
    }
    this.dirty = [];
  }
  renderAll() { const { width, height } = this.ctx.canvas;
    this.ctx.clearRect(0, 0, width, height);
    this.nodes.forEach(n => this.drawNode(n)); }
  drawNode(n) { n.draw(this.ctx); }
}
function bounds(n) { return { x: n.x, y: n.y, w: n.w, h: n.h }; }
function expandBox(b, pad = 10) { return { x: b.x - pad, y: b.y - pad, w: b.w + 2 * pad, h: b.h + 2 * pad }; }
function intersects(a, b) { return a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h; }
function mergeBoxes(boxes) { const out = [];
  for (const b of boxes.sort((x, y) => x.x - y.x)) {
    const last = out.at(-1);
    if (last && intersects(last, b))
      Object.assign(last, { x: Math.min(last.x, b.x), y: Math.min(last.y, b.y),
        w: Math.max(last.x + last.w, b.x + b.w) - Math.min(last.x, b.x),
        h: Math.max(last.y + last.h, b.y + b.h) - Math.min(last.y, b.y) });
    else out.push({ ...b });
  }
  return out; }
```
