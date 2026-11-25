---
title: [AV-211] WebRTC 连接建立延迟优化：预建连与候选预收集
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-211：WebRTC 连接建立延迟优化：预建连与候选预收集

**答**：
- 建连延迟构成：信令往返 + ICE 探测（1~3 秒）+ DTLS 握手——优化：预建连（进房前预热 PeerConnection）、候选预收集（iceCandidatePoolSize）、Trickle ICE（边收集边发）。
- 首帧延迟指标：join → 第一帧视频上屏；分解信令/ICE/DTLS/解码四段。
- 目标：P75 首帧 < 1.5s。

```javascript
class FastConnect {
  async prewarm() {                                        // 进房前预热
    this.pc = new RTCPeerConnection({ iceServers, iceCandidatePoolSize: 8 });
    this.pc.addTransceiver('audio', { direction: 'recvonly' });   // 预置收发（免再协商）
    this.pc.addTransceiver('video', { direction: 'recvonly' });
    await this.pc.setLocalDescription(await this.pc.createOffer());   // 提前开始 ICE 探测
    this.prewarmedAt = Date.now();
  }
  async join(roomId) {                                     // 真进房：复用预热 PC
    const answer = await signaling.join(roomId, this.pc.localDescription);
    await this.pc.setRemoteDescription(answer);            // ICE 已在探测中——秒连
    report('join-latency', { ms: Date.now() - this.prewarmedAt, stage: 'ice-done' });
  }
}
// Trickle ICE：onicecandidate 逐个发信令——不等全部收集（省 300~800ms）
```
