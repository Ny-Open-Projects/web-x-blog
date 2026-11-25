---
title: [AV-210] WebRTC NAT 穿透实战：STUN/TURN 的成本与策略
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-210：WebRTC NAT 穿透实战：STUN/TURN 的成本与策略

**答**：
- 穿透成功率：P2P 直连约 80%（STUN 足够），对称 NAT/企业防火墙 → TURN 中继（约 20% 流量走 TURN，带宽成本大头）。
- TURN 策略： TURN 仅作兜底（iceTransportPolicy 默认含）；监控 relay 类型连接占比与带宽成本；TURN 集群按地域部署。
- ICE 状态机：checking → connected/completed → failed/disconnected——failed 触发候选补齐或 TURN 强制。

```javascript
const pc = new RTCPeerConnection({
  iceServers: [
    { urls: 'stun:stun.example.com:3478' },               // 免费：穿透尝试
    { urls: 'turn:turn.example.com:3478',
      username: 'user', credential: 'pass',
      credentialType: 'password' },                        // 兜底：中继
  ],
  iceCandidatePoolSize: 4,                                 // 预收集候选（加速建连）
});
pc.oniceconnectionstatechange = () => {
  if (pc.iceConnectionState === 'failed') {
    pc.restartIce();                                       // 重试穿透
    report('ice-failed', { roomId });
  }
};
// 成本监控：getStats 找 selected-candidate-pair → local/remote candidateType
// relay 占比 > 40% → 评估 TURN 集群扩容
```
