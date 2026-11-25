---
title: [VIZ-400] Gamma/Linear 工作流在 shader 内的正确顺序
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-400：Gamma/Linear 工作流在 shader 内的正确顺序

**答**：
- 纹理（sRGB）进 shader 前转线性 → 光照计算 → tone mapping → gamma 输出。
- WebGL1 无 sRGB 纹理格式：shader 里 pow(tex, 2.2) 手动转；WebGL2 用 SRGB8_ALPHA8 自动。
- 混合发生在 framebuffer（sRGB 输出）——混合前输出的已是 gamma 空间，混合有轻微误差（业界普遍接受）。

```javascript
// gamma 工作流
const GAMMA = 2.2;
function fragPipeline(srgbTex, light) {
  const albedo = Math.pow(srgbTex, GAMMA);       // sRGB -> linear
  const hdr = albedo * light;                     // 光照（linear HDR）
  const mapped = aces(hdr);                       // 1257 tone map
  return Math.pow(mapped, 1 / GAMMA);             // gamma 输出
}
// WebGL2 捷径：internalFormat = gl.SRGB8_ALPHA8（自动转线性）
```
