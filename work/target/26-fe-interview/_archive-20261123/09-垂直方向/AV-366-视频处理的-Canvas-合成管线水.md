---
title: [AV-366] 视频处理的 Canvas 合成管线（水印/特效叠加）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-366：视频处理的 Canvas 合成管线（水印/特效叠加）

**答**：
- 管线：video -> canvas（drawImage）叠加层（水印/字幕/特效）-> 输出（录制/推流）。
- 性能：GPU 合成（WebGL/WebCodecs + GPU 纹理）优于 CPU drawImage（1080p30 CPU 合成占 1 核）。
- 帧率：rVFC 驱动合成（355），避免重复帧处理。

```javascript
// 合成管线
function composePipeline(video, layers, { outW = 1280, outH = 720 } = {}) {
  const canvas = new OffscreenCanvas(outW, outH);
  const ctx = canvas.getContext('2d');
  function draw(now, meta) {
    ctx.drawImage(video, 0, 0, outW, outH);           // 基础帧
    for (const layer of layers) layer.render(ctx, meta);   // 叠加层
    video.requestVideoFrameCallback(draw);
  }
  video.requestVideoFrameCallback(draw);
  return canvas;                                       // captureStream()/WebCodecs 输入
}
```
