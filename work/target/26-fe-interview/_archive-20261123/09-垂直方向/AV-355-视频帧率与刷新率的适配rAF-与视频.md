---
title: [AV-355] 视频帧率与刷新率的适配（rAF 与视频同步）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-355：视频帧率与刷新率的适配（rAF 与视频同步）

**答**：
- 视频 30fps 在 120Hz 屏渲染：rAF 每帧都跑但视频源每 4 帧才有新内容——重复帧浪费。
- 手段：requestVideoFrameCallback（每新视频帧回调）驱动 UI 动画对齐视频节奏。
- Canvas 合成：视频帧到 canvas 用 rVFC 触发而非 rAF，避免重复绘制。

```javascript
// rVFC 对齐
function syncCanvasToVideo(video, canvas) {
  const ctx = canvas.getContext('2d');
  function draw(now, metadata) {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    report({ type: 'frame', mediaTime: metadata.mediaTime,
      presented: metadata.presentationTime });
    video.requestVideoFrameCallback(draw);           // 只在新视频帧时画
  }
  video.requestVideoFrameCallback(draw);
}
```
