---
title: [WEB-114] WebRTC DataChannel 的定位和基本用法是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-114：WebRTC DataChannel 的定位和基本用法是什么？
**答**：
- DataChannel 是 WebRTC 的数据通道：浏览器间 P2P 直连（经 STUN 打洞、TURN 中继兜底），延迟低于任何中转服务器方案。
- 通道可配置有序/无序、可靠（重传）或不可靠（maxRetransmits/maxPacketLifeTime）——游戏帧同步用不可靠低延迟，聊天用可靠有序。
- 建连需要信令：交换 SDP offer/answer 与 ICE candidate，通常走任意现成通道（WebSocket/HTTP）完成，信令服务器不参与数据面。
- 前端场景：多人游戏、P2P 文件传输、协同白板的低延迟通道。

```javascript
// 发起方
const pc = new RTCPeerConnection({ iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] });
const dc = pc.createDataChannel('game', { ordered: false, maxRetransmits: 0 }); // 不可靠低延迟
dc.onopen = () => dc.send(JSON.stringify({ type: 'move', x: 10, y: 20 }));
dc.onmessage = (e) => console.log('对端数据', e.data);

// 信令交换：offer/answer 与 ICE 通过任意后端通道转发
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);
signaling.send({ type: 'offer', sdp: offer }); // 发给对端

// 接收方
peerPc.ondatachannel = (e) => e.channel.onmessage = (m) => console.log(m.data);
await peerPc.setRemoteDescription(remoteOffer);
const answer = await peerPc.createAnswer();
await peerPc.setLocalDescription(answer);
signaling.send({ type: 'answer', sdp: answer });
// 双方互发 ICE candidate（pc.onicecandidate），打洞完成后通道打通
```
