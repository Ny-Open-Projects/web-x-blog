---
title: [AV-351] 视频首帧耗时（Join to First Frame）的优化路径
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-351：视频首帧耗时（Join to First Frame）的优化路径

**答**：
- 链路分解：信令建连（ICE 0.5~2s）→ SDP 协商 → 首包到达 → 解码渲染。
- 优化：预建连（进入房间前 ICE 预热）、relay 直连（跳过 STUN 尝试）、首帧 I 帧立即请求（PLI）。
- 度量：P75 首帧 < 800ms 为佳；> 2s 说明 ICE 失败走了中继或网络差。

```javascript
// 首帧优化编排
async function joinWithFastFirstFrame(roomId, localStream) {
  t0 = performance.now();
  const pc = await prewarmedPC();                     // 预热连接池
  pc.addTrack(localStream.getTracks()[0], localStream);
  const remoteVideo = attachRemote(roomId);
  remoteVideo.onloadeddata = () =>
    report({ type: 'first-frame', ms: Math.round(performance.now() - t0) });
  await sendOffer(pc);                                // Trickle ICE
}
async function prewarmedPC() {
  const pc = new RTCPeerConnection({ iceServers: TURN_FIRST });  // TURN 优先
  await pc.setLocalDescription(await pc.createOffer({ offerToReceiveVideo: 1 }));
  return pc;
}
```
