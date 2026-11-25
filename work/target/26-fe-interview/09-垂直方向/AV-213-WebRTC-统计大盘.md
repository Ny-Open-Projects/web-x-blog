---
title: [AV-213] WebRTC 统计大盘：会议质量指标体系
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-213：WebRTC 统计大盘：会议质量指标体系

**答**：
- 质量指标：首帧延迟、卡顿率（帧率骤降/冻结）、音频断续、丢包率、端到端延迟——按房间/用户/地域聚合。
- MOS 评分：基于 RTT/丢包/抖动的经验公式（E-model）输出 1~5 分主观质量估计。
- 大盘消费：运营看整体质量、研发看劣化归因、客服看单用户诊断。

```javascript
function collectCallQuality(pc, interval = 5000) {
  const samples = [];
  const timer = setInterval(async () => {
    const stats = await pc.getStats();
    const video = [...stats.values()].find(r => r.type === 'inbound-rtp' && r.kind === 'video');
    const audio = [...stats.values()].find(r => r.type === 'inbound-rtp' && r.kind === 'audio');
    samples.push({
      ts: Date.now(),
      fps: video?.framesPerSecond,
      freezeCount: video?.freezeCount,                     // 冻结次数（卡顿直指）
      packetLoss: video?.packetsLost / (video?.packetsReceived ?? 1),
      rtt: video?.roundTripTime,
      audioLevel: audio?.audioLevel,                       // 对方说话音量（静音检测）
    });
  }, interval);
  return { stop: () => clearInterval(timer), samples };
}
// MOS 简化：mos = 4.5 - 丢包率 × 30 - max(0, rtt-0.2) × 10（clamp 1~5）
```
