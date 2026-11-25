---
title: [AV-201] WebRTC SFU 架构：为什么 SFU 取代 MCU 成为主流
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-201：WebRTC SFU 架构：为什么 SFU 取代 MCU 成为主流

**答**：
- SFU（Selective Forwarding Unit）：服务器只转发不编解码——延迟低、服务器 CPU 低、端到端加密（DTLS-SRTP 全程）；MCU 需服务端混流转码（CPU 贵、延迟高）。
- 代价：客户端上行 N 路扇出（N 人会议上行 N-1 条流带宽）——Simulcast 缓解。
- 前端关注：每远端一个 RTCPeerConnection 或统一收流、track 订阅管理、inactive 流处理。

```javascript
// SFU 客户端订阅模型（mediasoup 风格）
const device = new mediasoup.Device();
const recvTransport = device.createRecvTransport(sfuParams);
async function subscribe(producerId) {
  const consumer = await recvTransport.consume({ producerId, appData: { kind } });
  const video = document.createElement('video');
  video.srcObject = new MediaStream([consumer.track]);
  video.play();
  consumer.on('transportclose', () => video.remove());
  // SFU 会暂停不活跃流（audioLevel 检测）→ activeSpeaker 事件驱动 UI 高亮
}
// N 人会议带宽：上行 = 收 N-1 路 = (N-1) × 码率 —— Simulcast 下收层自适应
```
