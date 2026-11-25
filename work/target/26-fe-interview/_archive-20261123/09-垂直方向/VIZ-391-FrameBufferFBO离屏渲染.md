---
title: [VIZ-391] FrameBuffer（FBO）离屏渲染的用途
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-391：FrameBuffer（FBO）离屏渲染的用途

**答**：
- 用途：后处理（先渲到纹理再处理）、阴影贴图、拾取 ID pass、反射/镜像。
- 配置：颜色 attach（RGBA8/16F HDR）+ 深度 attach；检查 FRAMEBUFFER_COMPLETE。
- 性能：FBO 切换昂贵——尽量按分辨率分组，避免每 pass 换目标；移动端 tile 架构上频繁切换伤性能。

```javascript
// FBO 创建
function createFBO(gl, w, h, { hdr = false } = {}) {
  const tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, tex);
  gl.texImage2D(gl.TEXTURE_2D, 0, hdr ? gl.RGBA16F : gl.RGBA8, w, h, 0,
    gl.RGBA, hdr ? gl.HALF_FLOAT : gl.UNSIGNED_BYTE, null);
  const fb = gl.createFramebuffer();
  gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
  gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0,
    gl.TEXTURE_2D, tex, 0);
  const ok = gl.checkFramebufferStatus(gl.FRAMEBUFFER) === gl.FRAMEBUFFER_COMPLETE;
  return { fb, tex, ok };
}
```
