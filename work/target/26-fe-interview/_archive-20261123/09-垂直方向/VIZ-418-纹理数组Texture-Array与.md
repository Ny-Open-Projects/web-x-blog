---
title: [VIZ-418] 纹理数组（Texture Array）与图集的取舍
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-418：纹理数组（Texture Array）与图集的取舍

**答**：
- 图集：单纹理多子图，mipmap 跨子图渗色（bleeding）需 padding；采样 UV 计算在 CPU/顶点。
- 数组：WebGL2 TEXTURE_2D_ARRAY 独立 mip 不渗色，layer 切换零成本；一致尺寸限制。
- 选择：Sprite 大小一致用数组；尺寸悬殊用图集+padding。

```javascript
// 纹理数组使用
function createTexArray(gl, layers, w, h) {
  const tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D_ARRAY, tex);
  gl.texImage3D(gl.TEXTURE_2D_ARRAY, 0, gl.RGBA8, w, h, layers, 0,
    gl.RGBA, gl.UNSIGNED_BYTE, null);
  // 逐层上传 texSubImage3D(..., layer, ...)
  return tex;
}
// shader: texture(uArray, vec3(uv, layer))
```
