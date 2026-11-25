---
title: [VIZ-218] WebGPU 大规模文本渲染：SDF 字体图集
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-218：WebGPU 大规模文本渲染：SDF 字体图集

**答**：
- 图表文本（10 万标签）渲染：canvas fillText 逐个画会卡——SDF（Signed Distance Field）字体图集：文字渲染成图集纹理，GPU 采样放大不失真。
- 管线：字集（常用字）预烘 SDF 图集 → 每个文字 = 一个实例（uv 指向图集格子）；动态字符（用户输入）运行时补烘。
- 对比 canvas 文本：SDF 一次 draw call 画全部文本、任意缩放无锯齿；代价：图集生成与中文字符集体积。

```javascript
// SDF 文本实例
struct TextInstance { pos: vec2f, fontSize: f32, uvRect: vec4f, color: vec4f };
// 片元着色器：SDF 距离场 → 平滑边缘
const fs = `
@fragment fn fs(in: VsOut) -> @location(0) vec4f {
  let dist = textureSample(fontAtlas, sampler, in.uv).r;   // SDF 值
  let alpha = smoothstep(0.5 - fwidth(dist), 0.5 + fwidth(dist), dist);
  return vec4f(in.color.rgb, in.color.a * alpha);
};`;
// 图集生成：预烘常用 3500 汉字（64px SDF，图集 2048²）≈ 16MB——运行时按需补烘罕见字
```
