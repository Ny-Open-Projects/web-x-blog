---
title: [AV-119] 媒体服务器要监控哪些指标？怎么发现"SFU 不转发"这类暗故障？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-119：媒体服务器要监控哪些指标？怎么发现"SFU 不转发"这类暗故障？（高频）
**答**：
- 四层指标：机器层（CPU/网卡带宽/内存）、链路层（NACK/PLI/重传率/RTT）、会话层（建房数/断连率/协商失败率）、体验层（端到端延迟/卡顿率抽样）。
- SFU 特有暗故障：Consumer 字节数为 0（发了没人收）、Producer 无流量（说了没人听）——机器监控全绿但用户体验已坏。
- 端到端拨测：定时机器人进房推拉流，验证"发布→订阅"全链路，比机器监控更能抓真故障。
- 告警分级：协商失败率突增 P0；单节点 Consumer 零流量 P1；RTT 抬升 P2 观察项。
- 前端配合：getStats 关键字段定时上报，服务端聚合出"用户视角"的可用性（关联 AV-067）。

```typescript
// SFU 会话健康探针：字节级暗故障发现
interface SessionHealth { outBytes: number; inBytes: number; ts: number; }
class SfuSessionProbe {
  private sessions = new Map<string, SessionHealth>();
  async probeAll(clients: Map<string, RTCPeerConnection>) {
    const now = Date.now();
    for (const [peerId, pc] of clients) {
      const s = await pc.getStats();
      let out = 0, inn = 0;
      s.forEach((r) => {
        if (r.type === 'outbound-rtp') out += r.bytesSent ?? 0;
        if (r.type === 'inbound-rtp') inn += r.bytesReceived ?? 0;
      });
      const prev = this.sessions.get(peerId);
      if (prev) {
        const dt = (now - prev.ts) / 1000;
        const outKbps = ((out - prev.outBytes) * 8) / dt / 1000;
        const inKbps = ((inn - prev.inBytes) * 8) / dt / 1000;
        if (outKbps === 0 && prev.outBytes > 0) alertP1(`peer ${peerId} 上行断流`);
        if (inKbps === 0 && prev.inBytes > 0) alertP1(`peer ${peerId} 下行断流`);
      }
      this.sessions.set(peerId, { outBytes: out, inBytes: inn, ts: now });
    }
  }
}
```

## 十四、播放器深度工程（AV-120 ~ AV-126）
