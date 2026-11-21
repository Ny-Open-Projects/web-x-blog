---
title: [VIZ-110] WebGPU 计算着色器能做什么？对可视化的价值在哪里？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-110：WebGPU 计算着色器能做什么？对可视化的价值在哪里？
**答**：Compute Pass 让 GPU 做通用并行计算：workgroup 内多线程，通过 `workgroupBarrier` 同步、storage buffer 读写数据。对可视化的价值：① **布局计算**——力导向图迭代、大规模分桶/排序搬到 GPU，主线程不卡；② **数据聚合**——百万点的直方图/热力格一次 pass 完成；③ **粒子模拟**——模拟与渲染共享同一份显存，零拷贝。入门经典是 GPU 直方图：每线程原子加分桶（atomicAdd）。注意 storage buffer 在顶点阶段读取的能力与设备相关，需要 feature 检测。

```javascript
// Compute：直方图分桶——百万数据一次 pass 聚合，替代主线程 for 循环
const shader = device.createShaderModule({ code: `
  @group(0) @binding(0) var<storage, read> data: array<f32>;
  @group(0) @binding(1) var<storage, read_write> bins: array<atomic<u32>>;
  @compute @workgroup_size(64)
  fn main(@builtin(global_invocation_id) gid: vec3u) {
    let n = arrayLength(&bins);
    let idx = u32(clamp(data[gid.x] * f32(n), 0.0, f32(n - 1u)));
    atomicAdd(&bins[idx], 1u);   // 原子加，多线程安全分桶
  }`});
const encoder = device.createCommandEncoder();
const pass = encoder.beginComputePass();
pass.setPipeline(computePipeline);
pass.setBindGroup(0, bindGroup);
pass.dispatchWorkgroups(Math.ceil(N / 64));  // 派发足够覆盖全部数据的线程组
pass.end();
device.queue.submit([encoder.finish()]);
// 之后渲染 pass 直接用 bins 作为柱高，模拟与渲染共享显存零拷贝
```
