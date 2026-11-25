---
title: [AV-435] 手写一个 WebRTC 重协商处理器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-435：手写一个 WebRTC 重协商处理器

**答**：
- 需求：implement Renegotiator(pc, signal)。addTrack 时若 pc 已有 localDescription 需重新协商（createOffer -> setLocal -> 发送 -> 等回答）；防并发（一次只有一个 pending negotiation，排队）；输出 { negotiated, queue }。
- 边界：ice gathering 完成后才发 offer（waitIce）；回答迟到校验匹配；排队上限 3 拒绝新请求。
- 评分点：协商互斥；排队上限；ICE 等待；迟到校验

```javascript
class Renegotiator {
  constructor(pc, signal) {
    this.pc = pc; this.signal = signal;
    this.pending = false; this.queue = [];
  }
  async renegotiate() {
    if (this.pending) {
      if (this.queue.length >= 3) throw new Error('协商队列满');
      return new Promise(r => this.queue.push(r));
    }
    this.pending = true;
    try {
      const offer = await this.pc.createOffer();
      await this.pc.setLocalDescription(offer);
      await waitIceGathering(this.pc);                // 等 candidate 收集完
      this.signal.send({ type: 'offer', sdp: this.pc.localDescription.sdp });
      const answer = await this.signal.waitAnswer();  // 等回答
      await this.pc.setRemoteDescription(answer);
      return { negotiated: true };
    } finally {
      this.pending = false;
      const next = this.queue.shift();
      if (next) next(this.renegotiate());             // 处理排队
    }
  }
}
async function waitIceGathering(pc, timeout = 2000) {
  if (pc.iceGatheringState === 'complete') return;
  await new Promise(r => {
    const t = setTimeout(r, timeout);                 // 超时兜底
    pc.onicegatheringstatechange = () => {
      if (pc.iceGatheringState === 'complete') { clearTimeout(t); r(); }
    };
  });
}
```
