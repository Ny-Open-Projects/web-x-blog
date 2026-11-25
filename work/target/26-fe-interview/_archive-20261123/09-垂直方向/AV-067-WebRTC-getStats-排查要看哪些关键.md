---
title: [AV-067] WebRTC getStats 排查要看哪些关键指标？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-067：WebRTC getStats 排查要看哪些关键指标？（高频压轴）
**答**：
- 连接层：candidate-pair（是否 succeeded、nominated、当前 RTT）、local/remote-candidate 类型（relay = 走中继）、DTLS/ICE 状态。
- 发送侧：outbound-rtp 的 targetBitrate/framesPerSecond/encoderImplementation、retransmittedPacketsOut（重传比例）。
- 接收侧：inbound-rtp 的 packetsLost/丢包率、jitter（抖动）、jitterBufferDelay（端到端延迟主要增量）、framesDropped（解码跟不上）。
- 音频专项：audioLevel、concealedSamples（PLC 掩盖的丢包时长，听感"机器人声"的元凶）。
- 方法论：定时采样存时间序列 → 定位拐点（丢包陡增/带宽骤降）→ 结合 candidate 类型与时间点还原现场。

```javascript
// WebRTC 健康采样器：关键指标时间序列
class WebRTCHealthProbe {
  constructor(pc, { interval = 2000 } = {}) {
    this.pc = pc;
    this.timer = setInterval(() => this.sample(), interval);
    this.series = [];
  }
  async sample() {
    const stats = await this.pc.getStats();
    const snap = { ts: Date.now() };
    stats.forEach((r) => {
      switch (r.type) {
        case 'candidate-pair':
          if (r.state === 'succeeded' && r.nominated) {
            snap.rttMs = Math.round((r.currentRoundTripTime ?? 0) * 1000);
            snap.outboundBps = r.availableOutgoingBitrate ?? 0;
          }
          break;
        case 'inbound-rtp':
          if (r.kind === 'video') {
            snap.lossRate = +(r.packetsLost /
              Math.max(1, (r.packetsLost ?? 0) + (r.packetsReceived ?? 0)) * 100).toFixed(1);
            snap.jitterMs = Math.round((r.jitter ?? 0) * 1000);
            snap.jbDelaySec = +(r.jitterBufferDelay / Math.max(1, r.jitterBufferEmittedCount)).toFixed(3);
            snap.fps = r.framesPerSecond;
            snap.dropped = r.framesDropped;
          }
          if (r.kind === 'audio') snap.concealRatio = r.concealedSamples / Math.max(1, r.totalSamplesReceived);
          break;
      }
    });
    this.series.push(snap);
    if (this.series.length > 300) this.series.shift(); // 10 分钟窗口
    if ((snap.lossRate ?? 0) > 15 || (snap.rttMs ?? 0) > 500) this.onDegraded?.(snap);
  }
  stop() { clearInterval(this.timer); }
}
```

---

## 十、综合实战（AV-068 ~ AV-100）
