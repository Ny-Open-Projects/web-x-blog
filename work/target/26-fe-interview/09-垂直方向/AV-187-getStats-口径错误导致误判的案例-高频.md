---
title: [AV-187] getStats 口径错误导致误判的案例。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-187：getStats 口径错误导致误判的案例。（高频）
**答**：
- 现象：运维报表显示"RTT 200ms 严重劣化"，用户却无投诉；另一张报表 RTT 40ms。
- 归因：两处口径不同——一处把 TURN relay 链路 RTT 当端到端 RTT，一处把信令 RTT 当媒体 RTT；还有把累计 bytesSent 直接当速率（没做差分）。
- 正确口径：媒体 RTT 用当前选中 candidate-pair 的 currentRoundTripTime；速率必须差分（Δbytes/Δt）；丢包率用差分而非累计。
- 治理：统一 stats 采集 SDK（唯一负责差分与口径），所有报表只消费 SDK 输出，禁止散落 getStats 调用。
- 教训：指标先对口径再上大盘，否则监控本身会成为"故障源"。

```typescript
// 统一 getStats 采集组件：差分与口径唯一出处
class StatsSampler {
  private prev = new Map<string, { bytes: number; ts: number }>();
  async sample(pc: RTCPeerConnection) {
    const s = await pc.getStats();
    let pairRtt: number | undefined;
    let outKbps = 0;
    const now = performance.now();
    s.forEach((r: any) => {
      if (r.type === 'candidate-pair' && r.state === 'succeeded' && r.nominated) {
        pairRtt = r.currentRoundTripTime;                // 秒 正确口径
      }
      if (r.type === 'outbound-rtp' && r.kind === 'video') {
        const p = this.prev.get(r.id);
        if (p) outKbps += ((r.bytesSent - p.bytes) * 8) / ((now - p.ts) / 1000) / 1000; // 差分
        this.prev.set(r.id, { bytes: r.bytesSent, ts: now });
      }
    });
    return { rttMs: pairRtt != null ? Math.round(pairRtt * 1000) : null, outKbps: Math.round(outKbps) };
  }
}
```
