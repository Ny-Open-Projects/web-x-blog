---
title: [AV-216] WebRTC 录制：MediaRecorder 与服务端录制选型
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-216：WebRTC 录制：MediaRecorder 与服务端录制选型

**答**：
- 客户端录制：MediaRecorder（本地合成 webm）——优点无服务器成本，缺点依赖端性能、页面关闭即断。
- 服务端录制：SFU 转发流在服务端录制（稳定、可多路混流）——生产首选。
- MediaRecorder 细节：mimeType 选择（video/webm;codecs=vp8,opus）、timeslice 分片、paused 状态处理。

```javascript
class LocalRecorder {
  constructor(stream, { timeslice = 5000 } = {}) {
    const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp9,opus')
      ? 'video/webm;codecs=vp9,opus' : 'video/webm';
    this.recorder = new MediaRecorder(stream, { mimeType: mime, timeslice });
    this.chunks = [];
    this.recorder.ondataavailable = (e) => this.chunks.push(e.data);   // timeslice 分片
  }
  start() { this.recorder.start(this.timeslice); }
  stop() { return new Promise((res) => {
    this.recorder.onstop = () => {
      const blob = new Blob(this.chunks, { type: 'video/webm' });
      res({ blob, url: URL.createObjectURL(blob) });        // 下载/上传
    };
    this.recorder.stop();
  }); }
}
// 服务端录制：SFU（mediasoup plainTransport → ffmpeg/gstreamer）——客户端只上报录制指令
```
