---
title: [H5-224] WebRTC 的三个 API 层是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, RTC]
type: 面试题
---

## H5-224：WebRTC 的三个 API 层是什么

**答**：
- getUserMedia：拿本地音视频流（输入层）
- RTCPeerConnection：P2P 连接核心——编解码协商、加密传输（DTLS/SRTP）、NAT 穿透、带宽自适应全在这一层
- RTCDataChannel：基于 SCTP 的数据通道，低延迟双向任意数据（游戏状态、文件），可配置有序/无序、可靠/不可靠
- 三层关系：媒体流从 getUserMedia 流入 PeerConnection，DataChannel 独立于媒体传输
- 面试钩子：DataChannel 的「不可靠模式」可用于游戏实时状态（丢帧无所谓），可靠模式才类似 TCP

```javascript
const pc = new RTCPeerConnection();
const stream = await navigator.mediaDevices.getUserMedia({ video: true });
stream.getTracks().forEach(t => pc.addTrack(t, stream));
const dc = pc.createDataChannel('game', { ordered: false, maxRetransmits: 0 });
dc.onopen = () => dc.send(JSON.stringify({ x: 1, y: 2 })); // 不可靠但低延迟
```
