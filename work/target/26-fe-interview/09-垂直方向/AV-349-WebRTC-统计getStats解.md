---
title: [AV-349] WebRTC 统计（getStats）解读与网络诊断
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-349：WebRTC 统计（getStats）解读与网络诊断

**答**：
- 核心指标：RTT（STUN 探测）、丢包率（packetsLost/packetsReceived）、jitter、带宽估计（availableOutgoingBitrate）。
- 诊断路径：卡顿 -> 丢包/RTT -> 拥塞控制降码率；音质差 -> jitter buffer / 丢包隐藏。
- 上报：每 5s 采样 getStats 上报监控，按房间聚合网络分布。

```javascript
// getStats 采集
async function collectStats(pc, { intervalMs = 5000 } = {}) {
  const prev = { ts: 0, bytes: 0, lost: 0 };
  return setInterval(async () => {
    const stats = await pc.getStats();
    stats.forEach(r => {
      if (r.type === 'outbound-rtp' && r.kind === 'video') {
        const kbps = (r.bytesSent - prev.bytes) * 8 / ((r.timestamp - prev.ts) || 1);
        report({ type: 'rtp', kbps: Math.round(kbps / 1000),
          lost: r.packetsLost - prev.lost });
        Object.assign(prev, { ts: r.timestamp, bytes: r.bytesSent, lost: r.packetsLost });
      }
      if (r.type === 'candidate-pair' && r.state === 'succeeded')
        report({ rtt: r.currentRoundTripTime });
    });
  }, intervalMs);
}
```
