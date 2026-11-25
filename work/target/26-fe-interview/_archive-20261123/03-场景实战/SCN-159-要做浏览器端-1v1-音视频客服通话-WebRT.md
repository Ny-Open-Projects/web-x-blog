---
title: [SCN-159] 要做浏览器端 1v1 音视频客服通话，WebRTC 的前端流程和关键坑有哪些？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-159：要做浏览器端 1v1 音视频客服通话，WebRTC 的前端流程和关键坑有哪些？
**答**：
- 流程五步：取媒体（getUserMedia）→ 本地预览 → 创建 RTCPeerConnection 生成 offer/answer（SDP 协商，经信令服务器转发）→ 双向交换 ICE candidate（打洞）→ ontrack 渲染远端流。
- 信令只管"介绍认识"，媒体数据 P2P 直连；NAT 打不通时走 TURN 中继，TURN 配额是成本大头，前端要上报连接类型便于监控。
- 经典坑：协商期间不要重复 createOffer（glare，用 perfect negotiation 规则）；设备热插拔要监听 devicechange 重建流；静音检测与网络质量（getStats）驱动 UI 提示。
- 关闭要彻底：先 stop 所有 track 再 close 连接，否则摄像头指示灯不灭、内存泄漏。

```javascript
// WebRTC 1v1 通话：信令协商 + ICE 交换 + 质量监控
export async function startCall(roomId, signaling) {
  const localStream = await navigator.mediaDevices.getUserMedia({
    video: { width: 1280 }, audio: { echoCancellation: true, noiseSuppression: true },
  });
  document.getElementById('local').srcObject = localStream;

  const pc = new RTCPeerConnection({ iceServers: [{ urls: 'turn:turn.example.com', username: 'u', credential: 'p' }] });
  localStream.getTracks().forEach(t => pc.addTrack(t, localStream));
  pc.ontrack = e => { document.getElementById('remote').srcObject = e.streams[0]; };

  // ICE candidate 逐个经信令转发给对端
  pc.onicecandidate = e => e.candidate && signaling.send('ice', roomId, e.candidate.toJSON());
  // 连接状态驱动 UI：检查中/已连接/断开
  pc.onconnectionstatechange = () => emit('state', pc.connectionState);

  // 发起方：createOffer -> setLocal -> 经信令发给对端
  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer);
  signaling.send('sdp', roomId, offer);

  // 收对端 answer 与 ice（信令路由省略）
  signaling.on('sdp', async desc => {
    if (desc.type === 'answer') await pc.setRemoteDescription(desc);
    if (desc.type === 'offer') {                       // 被叫分支
      await pc.setRemoteDescription(desc);
      const answer = await pc.createAnswer();
      await pc.setLocalDescription(answer);
      signaling.send('sdp', roomId, answer);
    }
  });
  signaling.on('ice', c => pc.addIceCandidate(c).catch(console.warn));

  // 质量监控：getStats 上报 RTT 与丢包，差网络提示用户
  setInterval(async () => {
    const stats = await pc.getStats();
    stats.forEach(r => r.type === 'inbound-ratio' || (r.type === 'inbound-rtp' &&
      report({ type: 'rtc-quality', rtt: r.jitterBufferDelay, lost: r.packetsLost })));
  }, 5000);

  return () => endCall(pc, localStream);              // 挂断句柄
}

export function endCall(pc, stream) {
  stream.getTracks().forEach(t => t.stop());          // 先停轨：摄像头灯灭
  pc.close();                                         // 再关连接
}
```
