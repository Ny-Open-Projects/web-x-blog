---
title: [VIZ-420] 视口缩放与 DPI 在 shader 侧的注意事项
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-420：视口缩放与 DPI 在 shader 侧的注意事项

**答**：
- gl_FragCoord 与像素对应——物理像素（DPR 缩放后）；逻辑坐标换算在 uniform 传 viewport 尺寸。
- DPR 变化（浏览器缩放/换屏）需重建 FBO 与 viewport——监听 resize + matchMedia。
- 糊 vs 锯齿：DPR 1.5 时用 1x + FXAA 或 2x FBO（显存换清晰度），按设备档位决策。

```javascript
// DPI 适配
function setupViewport(gl, canvas, dprCap = 2) {
  const dpr = Math.min(window.devicePixelRatio || 1, dprCap);
  const w = Math.round(canvas.clientWidth * dpr);
  const h = Math.round(canvas.clientHeight * dpr);
  if (canvas.width !== w || canvas.height !== h) {
    canvas.width = w; canvas.height = h;
  }
  gl.viewport(0, 0, w, h);
  return { w, h, dpr };       // FBO 尺寸同步重建
}
```
