---
title: [VIZ-444] WebGPU 与 WebGL 的性能差异来源
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-444：WebGPU 与 WebGL 的性能差异来源

**答**：
- WebGPU 优势：显式管线（无状态猜测）、compute（通用并行）、命令预录制、更好的多线程潜力。
- WebGL 隐式开销：驱动验证/状态猜测/隐式同步——draw 多时 CPU 驱动开销占比大。
- 现实：WebGPU 尚在普及（Safari 近期支持），生产需 WebGL fallback 双后端抽象。

```javascript
// 双后端抽象
const backend = navigator.gpu ? 'webgpu' : 'webgl2';
const RHI = {
  webgpu: { createPipeline: wgCreate, submit: wgSubmit, compute: true },
  webgl2: { createPipeline: glCreate, submit: glSubmit, compute: false },
}[backend];
// 特性探测降级矩阵：
function featureMatrix() {
  return {
    compute: backend === 'webgpu',
    msaLevels: backend === 'webgpu' ? [4, 8] : [4],
    maxTextureMB: backend === 'webgpu' ? 256 : 128,
  };
}
```
