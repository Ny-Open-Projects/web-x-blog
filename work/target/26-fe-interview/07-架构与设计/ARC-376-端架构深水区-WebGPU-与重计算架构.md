---
title: [ARC-376] WebGPU/重图形计算的架构如何设计？可视化平台的算力分层
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-376：WebGPU/重图形计算的架构如何设计？
**答**:
- 算力分层：Canvas 2D（轻量图表）→ WebGL（十万级点/特效）→ WebGPU（百万级实例、compute shader 通用计算）；架构上定义"渲染引擎适配层"，业务声明数据规模与特效需求，引擎层选路。
- WebGPU 相比 WebGL 的架构意义：compute pipeline 让 GPGPU 成为一等公民（粒子模拟/物理计算/图像处理可全 GPU 化）；API 更贴近现代图形管线，抽象层（如 three.js 的 WebGPURenderer）屏蔽差异。
- 降级矩阵：WebGPU → WebGL2 → WebGL1 → Canvas；能力探测 + 性能档位（devicePixelRatio 降采样、特效开关）组合。
- 大数据传输：GPU 上传用大 buffer 批量提交，实例数据用 instanced draw；CPU-GPU 往返是最大陷阱，尽量一次上传常驻。
- 架构治理：shader 与材质资产纳入资产管线（编译产物缓存、版本管理），shader 编译耗时在首帧预算内预留。
```javascript
const adapter = await navigator.gpu?.requestAdapter();
const device = adapter && await adapter.requestDevice();
const tier = device ? 'webgpu' : hasWebGL2() ? 'webgl2' : 'canvas';
const engine = EngineFactory.create(tier, { maxInstances: tier === 'webgpu' ? 1e6 : 5e4 });
// 数据常驻：一次写入 storage buffer，帧间只更新脏区间
```
