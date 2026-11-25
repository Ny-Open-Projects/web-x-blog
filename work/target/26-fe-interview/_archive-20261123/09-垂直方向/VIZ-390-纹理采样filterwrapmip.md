---
title: [VIZ-390] 纹理采样：filter/wrap/mip 的组合选择
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-390：纹理采样：filter/wrap/mip 的组合选择

**答**：
- filter：NEAREST（像素风/数据图）/LINEAR（平滑）；mipmap + LINEAR_MIPMAP_LINEAR 消远处摩尔纹。
- wrap：CLAMP_TO_EDGE（边不重复）/REPEAT（平铺）/MIRRORED_REPEAT；NPOT 纹理 WebGL1 只支持 CLAMP+无 mip。
- 生成 mip：generateMipmap 需要 POT（WebGL1）/任意尺寸（WebGL2）；压缩纹理（KTX2/Basis）省内存与带宽。

```javascript
// 纹理参数配置
function setupTexture(gl, tex, { mipmap = true, npot = false } = {}) {
  gl.bindTexture(gl.TEXTURE_2D, tex);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER,
    mipmap && !npot ? gl.LINEAR_MIPMAP_LINEAR : gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  if (mipmap && !npot) gl.generateMipmap(gl.TEXTURE_2D);
}
// 摩尔纹验证：512px 纹理铺满 1920 宽屏幕，无 mip 时条纹明显
```
