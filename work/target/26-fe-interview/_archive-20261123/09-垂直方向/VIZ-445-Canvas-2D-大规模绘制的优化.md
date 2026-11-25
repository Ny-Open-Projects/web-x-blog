---
title: [VIZ-445] Canvas 2D 大规模绘制的优化（非 WebGL 场景）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-445：Canvas 2D 大规模绘制的优化（非 WebGL 场景）

**答**：
- 手段：离屏缓存静态层（背景一次绘制）、绘制区域裁剪（只重绘脏区）、requestAnimationFrame 合帧。
- 测量：DrawCall 数（Canvas 无 API，用代码统计）与帧时间；10 万矩形直接绘必卡。
- 升级路径：Canvas 2D 瓶颈时切 WebGL（同一场景双实现成本高，抽象层先建）。

```javascript
// Canvas 脏区重绘
class DirtyCanvas {
  constructor(canvas) { this.ctx = canvas.getContext('2d');
    this.dirty = new Set(); }
  mark(x, y, w, h) { this.dirty.add([x, y, w, h]); }
  flush(drawScene) {
    if (!this.dirty.size) return;
    for (const [x, y, w, h] of this.dirty)
      this.ctx.clearRect(x, y, w, h), drawScene(this.ctx, x, y, w, h);
    this.dirty.clear();
  }
}
```
