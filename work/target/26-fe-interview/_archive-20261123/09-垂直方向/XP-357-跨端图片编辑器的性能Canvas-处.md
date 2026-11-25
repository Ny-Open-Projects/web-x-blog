---
title: [XP-357] 跨端图片编辑器的性能（Canvas 处理）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-357：跨端图片编辑器的性能（Canvas 处理）

**答**：
- 处理链：加载 -> 编辑（裁剪/滤镜/涂鸦）-> 导出；大图分块处理防内存爆。
- 性能：滤镜用 WebGL shader（CPU Canvas 1080p 一次 200ms -> GPU 5ms）、历史记录用命令模式（非快照堆栈）。
- 导出：分块导出 + 进度反馈。

```javascript
// 图片编辑性能
class ImageEditor {
  constructor(canvas) { this.ctx = canvas.getContext('webgl'); }
  applyFilter(glsl) {
    // GPU 滤镜：纹理上传 -> shader 处理 -> 读回
    this.program = compileFilter(glsl);
    this.render();
  }
  history: { undo() { /* 命令模式逆操作，非像素快照 */ } }
}
```
