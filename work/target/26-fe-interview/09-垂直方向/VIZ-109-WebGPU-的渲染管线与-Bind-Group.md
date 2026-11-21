---
title: [VIZ-109] WebGPU 的渲染管线与 Bind Group 是什么？怎么组织资源？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-109：WebGPU 的渲染管线与 Bind Group 是什么？怎么组织资源？
**答**：GPURenderPipeline 在初始化时一次性声明：顶点/片元着色器、顶点缓冲布局、图元拓扑、深度模板、输出颜色格式——创建昂贵但之后切换零成本。资源（uniform buffer、纹理、采样器）通过 **BindGroupLayout → BindGroup** 声明式绑定到编号组与槽位；同一布局的多个 BindGroup 提前创建好按帧切换。易错点：bufferUsage 必须与声明一致、纹理格式必须与 pipeline 的 targets 格式匹配、每帧渲染前要拿 `context.getCurrentTexture().createView()`。

```javascript
// 管线 + BindGroup：声明一次，按帧复用
const pipeline = device.createRenderPipeline({
  layout: 'auto',
  vertex: {
    module, entryPoint: 'vs',
    buffers: [{ arrayStride: 20, attributes: [
      { shaderLocation: 0, offset: 0,  format: 'float32x3' },  // position
      { shaderLocation: 1, offset: 12, format: 'float32x2' },  // uv
    ]}],
  },
  fragment: { module, entryPoint: 'fs', targets: [{ format: canvasFormat }] },
  primitive: { topology: 'triangle-list' },
});
const bindGroup = device.createBindGroup({
  layout: pipeline.getBindGroupLayout(0),
  entries: [
    { binding: 0, resource: { buffer: uniformBuffer } },  // MVP 矩阵等
    { binding: 1, resource: texture.createView() },        // 采样纹理
    { binding: 2, resource: sampler },                     // 采样器
  ],
});
```
