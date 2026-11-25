---
title: [AV-361] 录制（MediaRecorder）的格式与质量控制
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-361：录制（MediaRecorder）的格式与质量控制

**答**：
- MediaRecorder：WebM（VP8/VP9+Opus）原生；MP4 支持参差——Safari 走 MP4。
- 参数：videoBitsPerSecond/audioBitsPerSecond/timeslice（分段产出 Blob）。
- 限制：不能录制 DRM 内容（EME 保护）；长录内存涨（分段+IndexedDB 落盘）。

```javascript
// 分段录制落盘
async function recordWithPersistence(stream, { timeslice = 10000 } = {}) {
  const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp9')
    ? 'video/webm;codecs=vp9' : 'video/webm';
  const rec = new MediaRecorder(stream, { mimeType: mime,
    videoBitsPerSecond: 4_000_000 });
  rec.ondataavailable = async e => {
    if (e.data.size === 0) return;
    await saveChunkToIDB(e.data);                     // 每 10s 落盘防内存
  };
  rec.start(timeslice);
  return { stop: () => new Promise(r => {
    rec.onstop = r; rec.stop();
  }) };
}
```
