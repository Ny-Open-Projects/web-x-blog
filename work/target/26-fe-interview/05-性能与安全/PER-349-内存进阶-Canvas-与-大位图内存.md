---
title: [PER-349] Canvas 应用（白板/修图）的内存治理：位图快照、离屏画布与历史记录的内存预算？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-349：Canvas 应用（白板/修图）的内存治理：位图快照、离屏画布与历史记录的内存预算？

**答**:
- 位图内存账：4K 画布 4096×4096×4 ≈ 64MB/张。undo 历史若每步存全量位图快照，50 步历史 = 3.2GB——这是 Canvas 应用第一杀手。
- 治理四招：① 历史存**操作指令**（矢量重放）而不是位图快照——撤销时重放指令链，内存几乎为零；② 必须存快照的场景（如滤镜后的像素）用低分辨率快照 + 局部快照（只存变更区域 dirty rect）；③ 快照池化复用 ArrayBuffer，Transferable 传给 Worker 处理（PER-270 回压）；④ 历史上限（如 30 步）+ 超限丢最旧。
- 离屏画布：OffscreenCanvas 在 Worker 里做重滤镜/缩放（PER-290），主线程零成本；中间位图用完 `canvas.width = 0` 显式释放。
- 检测手段：Chrome 任务管理器看 GPU 内存列；Performance 面板录制滚动/绘制时内存曲线；Allocation timeline 找大块位图分配点。

```javascript
class UndoStack {
  constructor(max = 30) { this.ops = []; this.max = max; }
  push(op) {                       // op = 指令对象（矢量），不是位图
    this.ops.push(op);
    if (this.ops.length > this.max) this.ops.shift();   // 上限：丢最旧
  }
  redraw(ctx) {                    // 撤销 = 从头重放指令
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    for (const op of this.ops) drawOp(ctx, op);
  }
}
// 必须存像素的场景（滤镜）：低分辨率快照 + dirty rect
function snapshotRegion(canvas, rect, scale = 0.25) {    // 1/4 分辨率局部快照
  const c = document.createElement('canvas');
  c.width = rect.w * scale; c.height = rect.h * scale;
  c.getContext('2d').drawImage(canvas, rect.x, rect.y, rect.w, rect.h, 0, 0, c.width, c.height);
  return c;   // 64MB 全图 → 4MB 局部
}
```
