---
title: [VIZ-201] WebGPU 计算管线（Compute Pipeline）在可视化中怎么用：GPU 侧数据聚合
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-201：WebGPU 计算管线（Compute Pipeline）在可视化中怎么用：GPU 侧数据聚合

**答**：
- WebGPU 独有 Compute Shader：万点数据在 GPU 上做聚合（分桶计数/直方图），CPU 只读结果——可视化数据预处理 GPU 化。
- 管线三件套：bindGroup（buffer 绑定）、dispatch(workgroup)、storage buffer（读写共享）。
- 适用判断：数据预处理为「每元素独立计算」时可 GPU 化；带全局依赖的（排序规约）需多 pass。

```javascript
// WGSL 计算着色器：直方图分桶
const shader = `
@group(0) @binding(0) var<storage, read> data: array<f32>;
@group(0) @binding(1) var<storage, read_write> bins: array<atomic<u32>>;
@compute @workgroup_size(64)
fn main(@builtin(global_invocation_id) gid: vec3<u32>) {
  let idx = gid.x;
  if (idx >= arrayLength(&data)) { return; }
  let bin = u32(data[idx] * 100.0);                     // 归一化值 → 桶号
  atomicAdd(&bins[bin], 1u);                            // 原子累加
};`;
// JS 侧：device.createComputePipeline → setBindGroup → dispatchWorkgroups
// CPU 只读回 bins（copyBufferToBuffer），百万点直方图 < 5ms
```
