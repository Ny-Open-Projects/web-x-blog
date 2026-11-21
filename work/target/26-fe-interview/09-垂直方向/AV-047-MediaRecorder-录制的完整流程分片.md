---
title: [AV-047] MediaRecorder 录制的完整流程？分片、暂停与格式怎么选？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-047：MediaRecorder 录制的完整流程？分片、暂停与格式怎么选？
**答**：
- 流程：new MediaRecorder(stream, options) → ondataavailable 收 chunk → start(timeslice) 定时分片 → stop 结束 → Blob 合成下载/上传。
- timeslice（如 1000ms）周期性吐分片：防内存峰值、支持边录边传（分片直接 POST 到服务端拼接）。
- 格式选择：`MediaRecorder.isTypeSupported` 探测，优先 `video/mp4;codecs=h264`（新 Chrome 支持），兜底 webm/vp9 → vp8；音频单独录可用 audio/webm;codecs=opus。
- 暂停/恢复：pause()/resume() 不产生新文件；`onstop` 后才能构造最终 Blob。
- 坑：Safari 旧版只支持 mp4 录制；录制 MSE 流（srcObject 必须是真实 MediaStream，video src 不行）。

```javascript
// 分片录制 + 边录边传
class ChunkUploader {
  constructor(stream, uploadUrl) {
    const mime = ['video/mp4;codecs=h264,aac', 'video/webm;codecs=vp9,opus', 'video/webm']
      .find((m) => MediaRecorder.isTypeSupported(m)) ?? '';
    this.recorder = new MediaRecorder(stream, { mimeType: mime, videoBitsPerSecond: 2_000_000 });
    this.uploadUrl = uploadUrl; this.seq = 0;
    this.recorder.ondataavailable = (e) => {
      if (!e.data.size) return;
      // 分片直传，服务端按 seq 拼接（注意 mp4 分片需 fMP4 才能独立解码）
      fetch(`${uploadUrl}?seq=${this.seq++}`, {
        method: 'POST',
        headers: { 'Content-Type': e.data.type },
        body: e.data,
      }).catch(console.error);
      this.chunks ??= []; this.chunks.push(e.data); // 本地留档
    };
  }
  start() { this.recorder.start(1000); } // 1s 分片
  pause() { this.recorder.pause(); }
  resume() { this.recorder.resume(); }
  stop() {
    return new Promise((resolve) => {
      this.recorder.onstop = () => resolve(new Blob(this.chunks, { type: this.recorder.mimeType }));
      this.recorder.stop();
    });
  }
}
```

---

## 七、Web Audio（AV-048 ~ AV-053）
