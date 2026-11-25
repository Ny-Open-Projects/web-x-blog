---
title: [AV-345] 音频编码：Opus 为什么是 WebRTC 默认
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-345：音频编码：Opus 为什么是 WebRTC 默认

**答**：
- Opus：可变码率 6~510kbps、帧长可变（2.5~60ms）、内建 FEC/DTX——为实时语音而生。
- 对比 AAC/MP3：延迟高（编码窗大）、无 FEC；AAC 适合点播 48kbps+ 音乐。
- 语音场景 24kbps Opus 质量接近 AAC 64kbps。

```javascript
// Opus 参数配置
function opusConfig(scene) {
  if (scene === 'voice')
    return { codec: 'opus', bitrate: 24_000, frameMs: 20,
      useinbandfec: 1, dtx: true };                  // 语音：FEC+DTX 省带宽
  if (scene === 'music')
    return { codec: 'opus', bitrate: 128_000, frameMs: 10,
      useinbandfec: 0, dtx: false };                 // 音乐：高码率低延迟
  return { codec: 'aac', bitrate: 128_000, note: '点播用 AAC' };
}
```
