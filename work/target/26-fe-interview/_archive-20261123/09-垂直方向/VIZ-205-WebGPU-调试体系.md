---
title: [VIZ-205] WebGPU 调试体系：错误作用域与调试标记
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-205：WebGPU 调试体系：错误作用域与调试标记

**答**：
- WebGPU 异步报错（设备丢失/管线创建失败）——pushErrorScope / popErrorScope 捕获区间错误；对象加 label 便于定位。
- 管线创建错误：createRenderPipelineAsync 避免 catch 不到的验证错误；onuncapturederror 全局兜底。
- 调试工具：Chrome WebGPU Inspector（帧捕获/buffer 查看）、模拟降级（forceFallbackAdapter）。

```javascript
device.pushErrorScope('validation');
const pipeline = device.createRenderPipelineAsync(pipelineDesc);   // 异步创建可捕获
pipeline.then(async (p) => {
  const err = await device.popErrorScope();
  if (err) report('webgpu-error', { msg: err.message, label: pipelineDesc.label });
});
device.onuncapturederror = (e) => report('webgpu-lost', { msg: e.error.message });   // 全局兜底
device.lost.then((info) => recoverWebGL(info.reason));   // 设备丢失恢复：重建全部 GPU 资源
```
