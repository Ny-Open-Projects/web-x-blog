---
title: [VIZ-214] WebGPU 与 Web Workers：OffscreenCanvas + Worker 渲染架构
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-214：WebGPU 与 Web Workers：OffscreenCanvas + Worker 渲染架构

**答**：
- 把 WebGPU 渲染搬到 Worker：canvas.transferControlToOffscreen() 传给 Worker，Worker 内 getContext webgpu 渲染——主线程零卡顿。
- 架构：主线程只做交互与数据，Worker 持 GPU device 渲染循环，postMessage 传控制指令（相机/数据更新）。
- 注意：GPUDevice 不能跨线程转移——device 与所有资源都在 Worker 创建。

```javascript
// main.js
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker('gpu-worker.js');
worker.postMessage({ canvas: offscreen, type: 'init' }, [offscreen]);   // 转移所有权
worker.postMessage({ type: 'update-data', points: packedBuffer });
// gpu-worker.js
self.onmessage = async (e) => {
  if (e.data.type === 'init') {
    const adapter = await navigator.gpu.requestAdapter();
    const device = await adapter.requestDevice();         // device 在 Worker 创建
    startRenderLoop(e.data.canvas, device);               // 渲染循环全在 Worker
  }
  if (e.data.type === 'update-data') updateInstances(e.data.points);
};
// 收益：主线程 JS 长任务不阻塞渲染（数据解析/计算下沉）——大盘/编辑器大场景标配
```
