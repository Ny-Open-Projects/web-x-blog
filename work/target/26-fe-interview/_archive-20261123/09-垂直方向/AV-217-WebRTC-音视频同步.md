---
title: [AV-217] WebRTC 音视频同步：Lip Sync 机制
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-217：WebRTC 音视频同步：Lip Sync 机制

**答**：
- 音视频同步：RTP 时间戳基准映射到共同时钟（RTCP SR 报文 NTP 映射）；播放端 jitter buffer 各自缓冲后按 NTP 对齐。
-  Lipsync 异常现象：口型对不上——常见原因音视频 jitter buffer 延迟差异大。
- 前端观察：getStats 各自 jitterBufferDelay 对比；差 > 100ms 可感知。

```javascript
function checkLipSync(stats) {
  const audio = [...stats.values()].find(r => r.kind === 'audio' && r.type === 'inbound-rtp');
  const video = [...stats.values()].find(r => r.kind === 'video' && r.type === 'inbound-rtp');
  const audioDelay = audio.jitterBufferDelay / audio.jitterBufferEmittedCount;
  const videoDelay = video.jitterBufferDelay / video.jitterBufferEmittedCount;
  const skew = Math.abs(audioDelay - videoDelay);
  if (skew > 0.1) report('lip-sync-skew', { audioDelay, videoDelay, skew });   // >100ms
  // 修正方向：调大 jitter buffer 目标延迟（AudioContext/track 级能力有限——主要靠 SFU/浏览器自适应）
}
// RTP 播放同步本质：RTCP SR 把 RTP 时间戳映射到 NTP 墙钟 → 两流按同一墙钟对齐
```
