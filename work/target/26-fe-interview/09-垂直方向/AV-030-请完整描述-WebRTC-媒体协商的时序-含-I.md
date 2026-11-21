---
title: [AV-030] 请完整描述 WebRTC 媒体协商的时序（含 ICE）。
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-030：请完整描述 WebRTC 媒体协商的时序（含 ICE）。
**答**：
- 标准时序：A addTrack → createOffer → setLocalDescription(offer) → 信令发 offer → B setRemoteDescription(offer) → B addTrack → createAnswer → setLocalDescription(answer) → 回 answer → A setRemoteDescription(answer)。
- ICE 候选与 SDP 交换并行进行（trickle ICE）：收集到就发，不必等 SDP 完成。
- 全部完成后进入 DTLS 握手与媒体传输；`negotiationneeded` 事件是触发 offer 的官方信号。
- 易错点：answer 侧必须先 setRemoteDescription(offer) 再 createAnswer；双端同时 offer 会 glare，需要角色仲裁。

```mermaid
sequenceDiagram
    participant UA as 发起方A
    participant SIG as 信令服务器
    participant UB as 接收方B
    UA->>UA: getUserMedia 采集
    UA->>UA: createOffer 并 setLocalDescription
    UA->>SIG: 发送 offer SDP
    SIG->>UB: 转发 offer SDP
    UB->>UB: setRemoteDescription offer
    UB->>UB: createAnswer 并 setLocalDescription
    UB-->>SIG: 返回 answer SDP
    SIG-->>UA: 转发 answer SDP
    UA->>UA: setRemoteDescription answer
    UA->>SIG: ICE candidate trickle
    SIG->>UB: 转发候选
    UB->>UA: ICE candidate trickle
    UA->>UB: ICE 连通性检查
    UB-->>UA: DTLS 握手并建立 SRTP
    Note over UA,UB: 媒体开始传输
```

```javascript
// 发起方与应答方完整代码（与上图一一对应）
async function caller(pc, sig) {
  pc.onnegotiationneeded = async () => {
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    sig.send({ type: 'offer', sdp: pc.localDescription });
  };
  sig.on('answer', (m) => pc.setRemoteDescription(m.sdp));
  sig.on('candidate', (m) => pc.addIceCandidate(m.candidate));
}
async function callee(pc, sig) {
  sig.on('offer', async (m) => {
    await pc.setRemoteDescription(m.sdp);
    const answer = await pc.createAnswer();
    await pc.setLocalDescription(answer);
    sig.send({ type: 'answer', sdp: pc.localDescription });
  });
  sig.on('candidate', (m) => pc.addIceCandidate(m.candidate));
}
```
