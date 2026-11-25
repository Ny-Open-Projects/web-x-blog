---
title: [AV-224] WebRTC 性能剖析：卡顿根因分类树
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-224：WebRTC 性能剖析：卡顿根因分类树

**答**：
- 卡顿根因树：网络（丢包/带宽/RTT）→ 设备（编解码 CPU 满载/解码掉帧）→ 服务端（SFU 转发瓶颈）→ 应用（主线程阻塞渲染）。
- 前端归因：framesDropped（解码端丢弃）、freezeCount、framesPerSecond 骤降、getStats 的 encoderImplementation（硬编/软编）。
- 分类处置：网络 → 降码率；设备 → 降分辨率减 CPU；应用 → 渲染优化。

```javascript
function diagnoseStall(stats) {
  const video = [...stats.values()].find(r => r.type === 'inbound-rtp' && r.kind === 'video');
  const reasons = [];
  if (video.framesDropped > 10) reasons.push('decode-drop');   // 解码丢帧：设备性能
  if (video.freezeCount > 3) reasons.push('freeze');          // 冻结：网络/关键帧
  if (video.jitterBufferDelay / video.jitterBufferEmittedCount > 0.3) reasons.push('jitter');   // 缓冲膨胀
  if (video.packetsLost / video.packetsReceived > 0.05) reasons.push('loss');   // 丢包
  const sender = [...stats.values()].find(r => r.type === 'media-source');
  return { reasons, advice: reasons.includes('decode-drop')
    ? '降分辨率减解码负担' : reasons.includes('loss')
    ? '降码率/开 FEC' : '检查主线程阻塞' };
}
```
