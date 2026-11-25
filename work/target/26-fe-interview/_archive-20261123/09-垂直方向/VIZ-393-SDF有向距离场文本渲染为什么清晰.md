---
title: [VIZ-393] SDF（有向距离场）文本渲染为什么清晰
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-393：SDF（有向距离场）文本渲染为什么清晰

**答**：
- SDF：纹理存"到字形边缘的有符号距离"，shader 里用 smoothstep 重构锐利边缘——任意缩放无锯齿。
- 对比：位图字体放大模糊/字体图集缺字；SDF 一张小图（如 64px）任意大小清晰。
- 增强：MSDF（多通道 SDF）保留彩色字形角点，字体质量更高。

```javascript
// SDF 文本 shader 核心
`float sdfAlpha(vec2 uv, sampler2D sdfTex, float pxRange, float size) {
  float d = texture(sdfTex, uv).a - 0.5;            // 距离场
  float scale = pxRange / size;                      // 每像素距离换算
  return clamp(d * scale + 0.5, 0.0, 1.0);
}`
// 生成：msdf-bmfont 工具产出图集 + 元数据（pxRange）
// 描边：alpha = smoothstep(0.5 - outlineWidth, 0.5, d + 0.5)
```
