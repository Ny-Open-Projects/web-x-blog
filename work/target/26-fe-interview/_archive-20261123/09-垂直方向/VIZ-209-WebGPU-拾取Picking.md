---
title: [VIZ-209] WebGPU 拾取（Picking）：CPU 射线与 GPU ID 缓冲两方案
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-209：WebGPU 拾取（Picking）：CPU 射线与 GPU ID 缓冲两方案

**答**：
- 题目：WebGPU 场景点选交互（点击选中数据点），两种实现：CPU 射线相交（数学计算）与 GPU ID 缓冲（渲染时写 ID，读取点击像素）。对比并实现 ID 方案。
- 思路：ID pass——单独 render pass，片元输出「实例 ID」颜色（ вместо颜色），点击时 readTexture 该像素。CPU 方案：屏幕坐标反投影 → 射线 → 与点/三角形求交。
- 评分点：两方案取舍（CPU 精确可调试 / GPU 一次搞定复杂场景）；ID 编码（RGBA 打包）；readback 成本控制。

```javascript
// GPU ID 缓冲方案
function pick(device, idTexture, x, y) {
  // 1. 独立 ID pass：片元着色器输出 vec4u(instanceId)
  // 2. 点击时 readTexture 单像素（1×1 区域）
  const encoder = device.createCommandEncoder();
  const buf = device.createBuffer({ size: 16, usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ });
  encoder.copyTextureToBuffer(
    { texture: idTexture, origin: { x, y } },
    { buffer: buf, bytesPerRow: 256 }, [1, 1]);          // 只读 1 像素
  device.queue.submit([encoder.finish()]);
  return buf.mapAsync(GPUMapMode.READ).then(() => {
    const id = new Uint32Array(buf.getMappedRange())[0];
    buf.unmap();
    return id;                                           // 命中的实例 ID
  });
}
// CPU 方案：射线求交适合少量对象/需要精确深度排序；ID 方案适合百万级实例（GPU 一次算完）
```
