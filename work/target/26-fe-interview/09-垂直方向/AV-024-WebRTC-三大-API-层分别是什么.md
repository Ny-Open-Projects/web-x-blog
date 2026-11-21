---
title: [AV-024] WebRTC 三大 API 层分别是什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-024：WebRTC 三大 API 层分别是什么？
**答**：
- `getUserMedia`：采集层，拿到音视频 MediaStream（麦克风/摄像头/屏幕）。
- `RTCPeerConnection`：传输层，负责编码、加密、NAT 穿透、P2P/SFU 传输与带宽自适应。
- `RTCDataChannel`：数据通道，可靠/不可靠可配（类 TCP/UDP），传消息、文件、游戏状态、白板指令。
- 三层可独立使用：只采集不连（录制）、只 DataChannel 不传媒体（P2P 棋类游戏）。
- 附加 API：`getDisplayMedia`（屏幕）、`RTCRtpSender/Receiver`（轨道级控制）、`getStats`（监控）。

```javascript
// 三大 API 各自的最小演示
async function demoThreeLayers() {
  // 1. 采集层
  const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

  // 2. 传输层
  const pc = new RTCPeerConnection({ iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] });
  stream.getTracks().forEach((t) => pc.addTrack(t, stream));
  pc.ontrack = (e) => (document.querySelector('video').srcObject = e.streams[0]);

  // 3. 数据通道
  const dc = pc.createDataChannel('chat', { ordered: true });
  dc.onmessage = (e) => console.log('收到消息', e.data);
  pc.ondatachannel = (e) => e.channel.send('hello');

  return { stream, pc, dc };
}
```
