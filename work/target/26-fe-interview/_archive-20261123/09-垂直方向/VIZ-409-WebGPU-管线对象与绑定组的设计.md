---
title: [VIZ-409] WebGPU 管线对象与绑定组的设计
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-409：WebGPU 管线对象与绑定组的设计

**答**：
- 管线：vertex/fragment 模块 + 状态（混合/深度/格式）编译为 immutable pipeline；切换即换 bindGroup。
- bindGroupLayout：显式声明每 binding 类型（uniform/storage/sampler/texture），驱动可预优化。
- 最佳实践：按更新频率分 group（0=每帧相机，1=每材质，2=每实例）。

```javascript
// WebGPU 管线骨架
const pipeline = device.createRenderPipeline({
  vertex: { module, entryPoint: 'vs', buffers: [vertexLayout] },
  fragment: { module, entryPoint: 'fs', targets: [{ format: 'bgra8unorm' }] },
  primitive: { topology: 'triangle-list' },
  depthStencil: { format: 'depth24plus', depthWriteEnabled: true,
    depthCompare: 'less' },
});
// 分组：
// group0: camera (uniform, 每帧) | group1: material (每材质) | group2: instance
```
