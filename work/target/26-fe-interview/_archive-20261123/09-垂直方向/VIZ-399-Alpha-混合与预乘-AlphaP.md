---
title: [VIZ-399] Alpha 混合与预乘 Alpha（Premultiplied）的坑
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-399：Alpha 混合与预乘 Alpha（Premultiplied）的坑

**答**：
- 预乘：RGB 已乘 alpha——混合方程 (ONE, ONE_MINUS_SRC_ALPHA)；非预乘用 (SRC_ALPHA, ONE_MINUS_SRC_ALPHA)。
- 坑：Canvas 2D 到 WebGL 上传（UNPACK_PREMULTIPLY_ALPHA_WEBGL）、mipmap 生成非预乘纹理边缘发黑。
- 规范：纹理管线统一预乘（合成正确性），导出工具链保证。

```javascript
// 混合模式对照
const BLEND_MODES = {
  straight: { src: 'SRC_ALPHA', dst: 'ONE_MINUS_SRC_ALPHA' },
  premult:  { src: 'ONE', dst: 'ONE_MINUS_SRC_ALPHA' },
};
function toPremultiplied([r, g, b, a]) {
  return [r * a, g * a, b * a, a];               // 非预乘 -> 预乘
}
// 边缘发黑根因：非预乘纹理线性过滤时 RGB 与 alpha 独立插值，
// 半透明边缘 RGB 不为 0 -> 与暗背景叠加发黑
```
