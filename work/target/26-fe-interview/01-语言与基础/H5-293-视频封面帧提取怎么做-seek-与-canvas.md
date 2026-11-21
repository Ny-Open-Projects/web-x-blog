---
title: [H5-293] 视频封面帧提取怎么做：seek 与 canvas
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-293：视频封面帧提取怎么做：seek 与 canvas

**答**：
- 纯前端方案：隐藏 video + `currentTime = t` + seeked 事件 + drawImage 到 canvas + toDataURL——不依赖服务端
- 时序要点：必须等 seeked（seek 完成回调）再画，否则画到旧帧；跨域视频需 CORS 否则画布污染
- 快速取多帧：按时间点批量 seek 逐帧画；关键帧（I 帧）附近 seek 最快——选 GOP 边界时间点
- 性能与内存：大视频 seek 慢，批量抽帧建议放 Worker（createImageBitmap + OffscreenCanvas）或走服务端 ffmpeg 预生成
- 用途：视频列表封面、进度条缩略图（雪碧图预生成）、剪辑预览

```javascript
async function grabFrame(videoUrl, t = 0.5) {
  const v = document.createElement('video');
  v.crossOrigin = 'anonymous'; v.src = videoUrl; v.muted = true;
  await new Promise(r => v.onloadedmetadata = r);
  v.currentTime = t;
  await new Promise(r => v.onseeked = r);
  const c = document.createElement('canvas');
  c.width = v.videoWidth; c.height = v.videoHeight;
  c.getContext('2d').drawImage(v, 0, 0);
  return c.toDataURL('image/jpeg', 0.8);
}
```
