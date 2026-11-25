---
title: [AV-202] WebRTC Simulcast：多码率上行与 SFU 按需转发
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-202：WebRTC Simulcast：多码率上行与 SFU 按需转发

**答**：
- Simulcast：发送端同时编码 2~3 层（高/中/低分辨率），SFU 按接收端带宽/设备选择转发哪层。
- 优点：接收端无需协商降级；SFU 切层实时（带宽下降立即切低层）。
- 前端实现：addTransceiver sendEncodings [{scaleResolutionDownBy: 4}, {..2}, {}]；观察 encodings 层状态（rid）。

```javascript
const stream = await navigator.mediaDevices.getUserMedia({ video: true });
const transceiver = pc.addTransceiver(stream.getVideoTracks()[0], {
  direction: 'sendonly',
  sendEncodings: [
    { rid: 'low', scaleResolutionDownBy: 4, maxBitrate: 150000 },    // 25% 分辨率
    { rid: 'mid', scaleResolutionDownBy: 2, maxBitrate: 500000 },
    { rid: 'high', maxBitrate: 1500000 },                            // 原始
  ],
});
// SFU 根据各订阅者带宽决定转发哪层——接收端可监听 layerIndex 变化
// 大会场景：观众端只收 activeSpeaker 的高层 + 其余人低层（服务端策略）
```
