---
title: [AV-420] 手写一个 WebRTC 连接建立封装（含 Trickle ICE）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-420：手写一个 WebRTC 连接建立封装（含 Trickle ICE）

**答**：
- 需求：implement createPeer(config)。创建 PC、监听 icecandidate（trickle 发送）、ontrack 回调、connectionState 变化上报；提供 addOffer(sdp)/createOffer 两个方向；失败自动 restart 一次。
- 边界：iceServers 必含至少一个 TURN；connectionState failed 触发 restart（限一次）；返回 { pc, api }。
- 评分点：Trickle ICE；状态上报；restart 一次；TURN 校验

```javascript
async function createPeer(config, { onTrack, onState, signal } = {}) {
  if (!config.iceServers?.some(s => s.urls.includes('turn')))
    throw new Error('必须配置 TURN');
  const pc = new RTCPeerConnection(config);
  let restarted = false;
  pc.ontrack = e => onTrack?.(e.streams[0]);
  pc.onicecandidate = e => e.candidate &&
    signal?.send({ type: 'candidate', candidate: e.candidate });
  pc.onconnectionstatechange = async () => {
    onState?.(pc.connectionState);
    if (pc.connectionState === 'failed' && !restarted) {
      restarted = true;
      const offer = await pc.createOffer({ iceRestart: true });
      await pc.setLocalDescription(offer);
      signal?.send({ type: 'offer', sdp: offer.sdp });
    }
  };
  return {
    pc,
    async acceptOffer(sdp) {
      await pc.setRemoteDescription({ type: 'offer', sdp });
      const answer = await pc.createAnswer();
      await pc.setLocalDescription(answer);
      signal?.send({ type: 'answer', sdp: answer.sdp });
    },
    async makeOffer() {
      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);
      signal?.send({ type: 'offer', sdp: offer.sdp });
    },
    async acceptAnswer(sdp) { await pc.setRemoteDescription({ type: 'answer', sdp }); },
  };
}
```
