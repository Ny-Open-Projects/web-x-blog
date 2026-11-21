---
title: [H5-217] WebGPU 和 WebGL 的区别，要不要现在学
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-217：WebGPU 和 WebGL 的区别，要不要现在学

**答**：
- 架构差异：WebGL 映射 OpenGL ES（为嵌入式设计的老 API），WebGPU 直接对齐 Vulkan/Metal/DX12，开销更低、控制更细
- 编程模型：WebGPU 用管线对象（pipeline）一次性固化状态，避免 WebGL 状态机的隐性切换；计算着色器（compute shader）让通用 GPU 计算成为可能（物理/AI 推理）
- 显式内存管理：buffer/texture 需显式 map/unmap，性能可预测
- 现状（2026）：Chrome/Edge 全量、Safari/Firefox 就绪，仍建议「学 WebGL 概念迁移到 WebGPU」，原生 WebGL 项目短期不必重写
- 学习建议：three.js/WebGPU.js 等库先行，关注 compute shader 与 AI 推理场景

```javascript
if (navigator.gpu) {
  const adapter = await navigator.gpu.requestAdapter();
  const device = await adapter.requestDevice();
  // WebGPU：显式 pipeline + command encoder
  const pipeline = device.createRenderPipeline({ /* 一次性描述全部状态 */ });
} else {
  // WebGL 降级
}
```
