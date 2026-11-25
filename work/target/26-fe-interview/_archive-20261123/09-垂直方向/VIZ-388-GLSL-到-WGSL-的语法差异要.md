---
title: [VIZ-388] GLSL 到 WGSL 的语法差异要点（WebGPU 迁移）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-388：GLSL 到 WGSL 的语法差异要点（WebGPU 迁移）

**答**：
- 声明式绑定：WGSL 用 @group @binding 注解替代 uniform location；变量类型强制（vec3<f32>）。
- 语法：WGSL 无隐式转换（f32(i) 显式）、数组访问 [] 一致、循环更严格。
- 入口：@vertex @fragment 函数注解 + @builtin(position) 等内建；与 GLSL 的 gl_Position/gl_FragColor 对应。

```javascript
// 同一效果的 GLSL vs WGSL
// GLSL:
// out vec4 color; color = texture(tex, uv) * tint;
// WGSL:
`@group(0) @binding(0) var samp: sampler;
@group(0) @binding(1) var tex: texture_2d<f32>;
@group(0) @binding(2) var<uniform> tint: vec4<f32>;
@fragment
fn fs(@location(0) uv: vec2<f32>) -> @location(0) vec4<f32> {
  return textureSample(tex, samp, uv) * tint;
}`
```
