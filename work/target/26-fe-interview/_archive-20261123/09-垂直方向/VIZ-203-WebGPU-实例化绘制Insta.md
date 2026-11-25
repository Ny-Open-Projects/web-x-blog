---
title: [VIZ-203] WebGPU 实例化绘制（Instanced Draw）：万点散点图
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-203：WebGPU 实例化绘制（Instanced Draw）：万点散点图

**答**：
- 题目：WebGPU 绘制 10 万点散点图，要求每帧更新位置（动画）且 60fps。用实例化：一个点的几何 × 10 万实例属性（位置/颜色/大小）。
- 思路：顶点着色器读 instance_index 取实例属性；数据放 storage buffer，每帧 writeBuffer 更新（或 transform feedback/GPU 计算）。
- 评分点：实例化 vs 逐点 draw call；buffer 更新策略（部分更新 offset）；drawCount 控制。

```javascript
// 顶点着色器（WGSL）读取实例属性
const vs = `
struct Instance { pos: vec2f, color: vec4f, size: f32 };
@group(0) @binding(0) var<storage, read> instances: array<Instance>;
@vertex fn vs(@builtin(vertex_index) vi: u32, @builtin(instance_index) ii: u32)
  -> @builtin(position) vec4f {
  let corner = vec2f(f32(vi & 1u) * 2.0 - 1.0, f32(vi >> 1u) * 2.0 - 1.0);   // 点单位三角形
  let inst = instances[ii];
  return vec4f(inst.pos + corner * inst.size, 0.0, 1.0);
};`;
// 绘制：pass.draw(6, 100000)—— 6 顶点 × 10 万实例 = 一次 draw call
// 帧更新：device.queue.writeBuffer(instBuf, 0, positions, changedCount * stride)——只写变化段
```
