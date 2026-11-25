---
title: [VIZ-212] WebGPU Buffer 布局优化：数据对齐与 packed 属性
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-212：WebGPU Buffer 布局优化：数据对齐与 packed 属性

**答**：
- 题目：10 万点实例属性（pos vec2f、color rgba8、size f32）设计 GPU buffer 布局——WGSL 对齐规则（vec2f 对齐 8、vec3f 对齐 16）下最优 packed 布局。
- 思路：WGSL struct 成员按对齐排布：pos(offset 0, 8B) + size(8, 4) + color(12, 4 packed u32) = stride 16；避免 vec3f 的 16 对齐空洞（8B 浪费/点）。
- 评分点：WGSL 对齐规则（vec3 的 16 对齐坑）；packed u32 颜色；stride 计算。

```javascript
// WGSL struct 对齐规则
const wgslStruct = `
struct Instance {
  pos: vec2f,            // offset 0, align 8
  size: f32,             // offset 8, align 4
  color: u32,            // offset 12（packed RGBA8）——若用 vec4f 会 padding 到 16
};                       // stride = 16
@group(0) @binding(0) var<storage, read> instances: array<Instance>;`;
// JS 侧 packed 打包：Float32Array 交错 + Uint32 颜色
function packInstance(pos, size, rgba) {
  const buf = new ArrayBuffer(16);
  new Float32Array(buf, 0, 2).set(pos);                  // pos 8B
  new Float32Array(buf, 8, 1)[0] = size;                 // size 4B
  new Uint32Array(buf, 12, 1)[0] = rgba;                 // color packed 4B
  return buf;
}
// 对照浪费版：color 用 vec4f → align 16 → stride 32（浪费 100%）——10 万点多耗 1.6MB
```
