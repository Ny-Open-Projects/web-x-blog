---
title: [AV-348] WebRTC 的 ICE/STUN/TURN 连接流程
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-348：WebRTC 的 ICE/STUN/TURN 连接流程

**答**：
- ICE：收集候选（host/srflx/relay），按优先级配对连通性检查——直连优先，失败走 TURN 中继。
- STUN：获取公网映射（免费，打通率 ~80%）；TURN：中继（成本按流量，打通率 100%）。
- 优化：候选收集并行（ICE gathering timeout 1s 截断）、直连失败快速切换 TURN（Trickle ICE）。

```javascript
// ICE 状态监控
function monitorIce(pc) {
  pc.addEventListener('iceconnectionstatechange', () => {
    const s = pc.iceConnectionState;
    if (s === 'checking') report({ type: 'ice-checking' });
    if (s === 'connected') report({ type: 'ice-ok',
      pair: pc.selectedCandidatePair });
    if (s === 'failed') {
      report({ type: 'ice-failed' });
      restartIce(pc);                                 // 348 续：重试
    }
  });
}
async function restartIce(pc) {
  const offer = await pc.createOffer({ iceRestart: true });
  await pc.setLocalDescription(offer);
  sendSignal({ type: 'offer', sdp: offer.sdp, restart: true });
}
```
