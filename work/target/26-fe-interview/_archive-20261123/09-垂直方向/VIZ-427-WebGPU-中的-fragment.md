---
title: [VIZ-427] WebGPU 中的 fragment 插值控制（flat/perspective）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-427：WebGPU 中的 fragment 插值控制（flat/perspective）

**答**：
- 默认透视校正插值；@interpolate(flat) 不插值（每图元常量，如实例 ID）；linear 为屏幕空间线性。
- 用途：flat 用于 ID/材质索引；noperspective 类似 linear（WGSL 用 linear 显式声明）。
- 坑：ID 被默认插值会得到错误值——必须 flat，这是拾取错误的最常见原因。

```javascript
// WGSL 插值声明
`struct VSOut {
  @builtin(position) pos: vec4<f32>,
  @location(0) @interpolate(perspective) uv: vec2<f32>,
  @location(1) @interpolate(flat) instanceId: u32,
}`
// GLSL 对应：flat out int vId;（WebGL2）
```
