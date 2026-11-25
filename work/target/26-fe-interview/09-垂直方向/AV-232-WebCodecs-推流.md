---
title: [AV-232] WebCodecs 推流：VideoEncoder 硬编码接入
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-232：WebCodecs 推流：VideoEncoder 硬编码接入

**答**：
- 题目：用 WebCodecs 实现「采集 → 硬编码 → RTP/RTMP 封装」的自定义推流（绕过 MediaRecorder 局限）。实现编码器接线与码率控制。
- 思路：VideoTrackProcessor（帧获取）→ VideoEncoder（configure 码率/关键帧间隔）→ encoded chunks → 封装推流。
- 评分点：VideoEncoder configure；关键帧请求（encode 时 keyFrame）；码率动态调整。

```javascript
const encoder = new VideoEncoder({
  output: (chunk, metadata) => {
    // chunk: EncodedVideoChunk（含 key_frame 标记/timestamp）
    muxer.addChunk(chunk, metadata);                       // 送封装器（muxer）
  },
  error: (e) => report('encoder-error', { msg: e.message }),
});
encoder.configure({
  codec: 'avc1.640028',                                     // H264 High Profile
  width: 1280, height: 720,
  bitrate: 2000000,                                         // 2Mbps
  framerate: 30,
  latencyMode: 'realtime',                                  // 低延迟模式
});
// 帧驱动：处理管线读取 VideoFrame → encoder.encode(frame, { keyFrame: every2s })
// 码率动态调整：encoder.encode 不可直接改 → reconfigure（短暂重置，避峰切换）
```
