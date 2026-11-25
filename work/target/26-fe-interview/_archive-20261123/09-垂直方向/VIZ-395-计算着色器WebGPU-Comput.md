---
title: [VIZ-395] 计算着色器（WebGPU Compute）能解决什么
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-395：计算着色器（WebGPU Compute）能解决什么

**答**：
- 通用并行：粒子物理、GPU 拾取（与场景求交）、蒙皮计算、数据聚合（直方图）。
- 结构：workgroup 划分（如 64 线程/组），storage buffer 读写共享；barrier 同步组内。
- Web 端适用：CPU 瓶颈在大量同质计算时下沉 GPU（粒子 10 万级 CPU 8ms -> GPU 0.5ms）。

```javascript
// WebGPU compute 最小例
const MODULE = `
@group(0) @binding(0) var<storage, read> input: array<f32>;
@group(0) @binding(1) var<storage, read_write> output: array<f32>;
@compute @workgroup_size(64)
fn main(@builtin(global_invocation_id) gid: vec3<u32>) {
  let i = gid.x;
  if (i < arrayLength(&input)) { output[i] = input[i] * 2.0; }
}`;
// dispatch: pass.dispatchWorkgroups(Math.ceil(n / 64));
```
