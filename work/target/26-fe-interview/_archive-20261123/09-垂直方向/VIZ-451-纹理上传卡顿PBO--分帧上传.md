---
title: [VIZ-451] 纹理上传卡顿：PBO / 分帧上传
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-451：纹理上传卡顿：PBO / 分帧上传

**答**：
- 问题：texImage2D 大纹理同步上传阻塞主线程（几十 ms）。
- 手段：WebGL2 PBO 异步上传（pixelStorei + buffer）、分帧分块（mip 逐级上传）、压缩纹理（上传量小）。
- 视频纹理：texSubImage2D 每帧上传 1080p ≈ 8MB，需与解码节奏对齐。

```javascript
// 分帧纹理上传
function uploadPerFrame(gl, tex, image, { chunkH = 256 } = {}) {
  let y = 0;
  return function step() {
    const h = Math.min(chunkH, image.height - y);
    if (h <= 0) return false;
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, y, image.width, h,
      gl.RGBA, gl.UNSIGNED_BYTE,
      image, 0, y * image.width * 4, h * image.width * 4);
    y += h;
    return true;                                     // 还有剩余
  };
}
// 每帧 step() 一次，10MB 纹理分 ~10 帧完成，无单帧尖峰
```
