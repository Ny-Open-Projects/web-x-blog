---
title: [AV-205] WebRTC 重传机制：NACK/RTX 与 PLI/FIR
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-205：WebRTC 重传机制：NACK/RTX 与 PLI/FIR

**答**：
- 丢包恢复三层：NACK（接收端请求重传指定序号，低延迟）、RTX（独立重传流）、PLI/FIR（关键帧请求——丢关键帧时让发送端重发 I 帧）。
- 前端观察：getStats 的 nackCount/pliCount/firCount——pliCount 高 = 频繁请求关键帧（卡顿根因）。
- 抖动缓冲：jitterBufferDelay——音视频平滑队列延迟，getResults 可读目标延迟。

```javascript
function diagnosePacketLoss(stats) {
  const video = stats.get(videoReceiver.ssrc);
  if (video.pliCount - lastPli > 3) {                     // 每秒 PLI 增量
    report('frequent-keyframe-req', { ssrc: video.ssrc });   // 网络差导致频繁 I 帧
    hintUI('网络不稳定，画面可能反复模糊');
  }
  if (video.nackCount > threshold) {                      // 重传多
    // 小丢包靠 NACK 秒恢复；大丢包触发 PLI（1~2 帧空白）
  }
  // jitterBufferDelay / jitterBufferEmittedCount = 平均缓冲延迟
  const latency = video.jitterBufferDelay / video.jitterBufferEmittedCount;
}
// 优化方向：pliCount 高 → 检查上行丢包率（sender 端）；或降分辨率减重传压力
```
