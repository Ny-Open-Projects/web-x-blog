---
title: [AV-422] 手写一个录制器（MediaRecorder + 分段保存）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-422：手写一个录制器（MediaRecorder + 分段保存）

**答**：
- 需求：implement Recorder(stream)。start({ timeslice }) 分段产出 chunk 到 IndexedDB；pause/resume；stop() 返回 { url, size, durationMs }（合并 Blob 生成对象 URL）。
- 边界：mime 探测降级（vp9 -> vp8 -> 默认）；未 start 调 stop 报错；durationMs 用 performance.now 差值（不含暂停）。
- 评分点：mime 降级；分段落盘；暂停计时；合并导出

```javascript
class Recorder {
  constructor(stream) {
    this.stream = stream;
    this.mime = ['video/webm;codecs=vp9', 'video/webm;codecs=vp8', 'video/webm']
      .find(m => MediaRecorder.isTypeSupported(m));
    this.pausedMs = 0; this._pauseAt = null; this.started = false;
  }
  start({ timeslice = 5000 } = {}) {
    this.started = true;
    this.t0 = performance.now();
    this.rec = new MediaRecorder(this.stream, { mimeType: this.mime });
    this.rec.ondataavailable = e => e.data.size &&
      idbAppend('rec-chunks', e.data);
    this.rec.start(timeslice);
  }
  pause() { this._pauseAt = performance.now(); this.rec.pause(); }
  resume() { this.pausedMs += performance.now() - this._pauseAt;
    this.rec.resume(); }
  async stop() {
    if (!this.started) throw new Error('未开始');
    await new Promise(r => { this.rec.onstop = r; this.rec.stop(); });
    const chunks = await idbAll('rec-chunks');
    const blob = new Blob(chunks, { type: this.mime });
    return { url: URL.createObjectURL(blob), size: blob.size,
      durationMs: Math.round(performance.now() - this.t0 - this.pausedMs) };
  }
}
```
