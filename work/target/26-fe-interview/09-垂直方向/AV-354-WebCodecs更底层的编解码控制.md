---
title: [AV-354] WebCodecs：更底层的编解码控制
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-354：WebCodecs：更底层的编解码控制

**答**：
- VideoEncoder/VideoDecoder：直接编解码帧（不经容器/MSE）——实时转码/录制/推流场景。
- 与 WebRTC 差异：WebRTC 端到端（含网络），WebCodecs 只管编解码（传输自己实现）。
- 典型：浏览器端录制（帧级控制）、AI 前处理（帧级注入特效）后编码。

```javascript
// WebCodecs 编码器
async function encodeFrames(canvasTrack, { kbps = 4000 } = {}) {
  const encoder = new VideoEncoder({
    output: (chunk, meta) => mux(chunk, meta),        // 喂 muxer
    error: e => report({ type: 'enc-error', msg: e.message }),
  });
  encoder.configure({ codec: 'avc1.640028',
    width: 1280, height: 720, bitrate: kbps * 1000, framerate: 30 });
  const reader = canvasTrack.readable.getReader();
  while (true) {
    const { value: frame, done } = await reader.read();
    if (done) break;
    encoder.encode(frame, { keyFrame: frame.timestamp % 2000_000 < 33_000 });
    frame.close();                                    // 必须手动关闭防泄漏
  }
  await encoder.flush();
}
```
