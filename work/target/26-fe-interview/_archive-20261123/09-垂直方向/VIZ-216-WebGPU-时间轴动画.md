---
title: [VIZ-216] WebGPU 时间轴动画：transform feedback 替代与 GPU 侧插值
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-216：WebGPU 时间轴动画：transform feedback 替代与 GPU 侧插值

**答**：
- 数据点动画（位置插值）：CPU 逐帧插值 10 万点太贵——GPU 侧插值：两帧位置 buffer（A/B），着色器按 uniform t 混合——CPU 只传 t。
- WebGPU 无 transform feedback——GPU 插值用「顶点着色器混合」或「compute pass 写目标 buffer」。
- 收益：CPU 每帧 0 传输，GPU 混合零成本。

```javascript
const mixVS = `
@group(0) @binding(0) var<storage, read> posA: array<vec2f>;
@group(0) @binding(1) var<storage, read> posB: array<vec2f>;
@group(0) @binding(2) var<uniform> params: struct { t: f32 };
@vertex fn vs(@builtin(vertex_index) vi: u32, @builtin(instance_index) ii: u32)
  -> @builtin(position) vec4f {
  let pos = mix(posA[ii], posB[ii], params.t);           // GPU 侧插值
  return vec4f(pos, 0.0, 1.0);
};`;
// CPU：数据到位后上传 A/B 两个 buffer，动画期间每帧只 writeBuffer({t})——4 字节
// 万点动画从 CPU 插值 3ms/帧 → 0（纯 GPU）
```
