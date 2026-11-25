---
title: [VIZ-416] 抗锯齿方案对比：MSAA/FXAA/TAA 在 Web 的可用性
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-416：抗锯齿方案对比：MSAA/FXAA/TAA 在 Web 的可用性

**答**：
- MSAA：WebGL antialias: true 上下文开（对几何边缘有效，alpha tested 材质需 sample shading）；WebGPU 4x 常用。
- FXAA：后处理单 pass，便宜但糊文本；TAA 需 motion vector（前端少用）。
- 组合：MSAA 4x + HDR 后处理（WebGL2 多采样 FBO resolve）是 Web 3D 标配。

```javascript
// MSAA FBO（WebGL2）
function createMSAAFBO(gl, w, h, samples = 4) {
  const rbColor = gl.createRenderbuffer();
  gl.bindRenderbuffer(gl.RENDERBUFFER, rbColor);
  gl.renderbufferStorageMultisample(gl.RENDERBUFFER, samples,
    gl.RGBA8, w, h);
  const fb = gl.createFramebuffer();
  gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
  gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0,
    gl.RENDERBUFFER, rbColor);
  return fb;    // resolve: blitFramebuffer 到普通纹理 FBO
}
```
