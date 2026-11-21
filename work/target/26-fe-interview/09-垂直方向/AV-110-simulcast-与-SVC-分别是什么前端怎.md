---
title: [AV-110] simulcast 与 SVC 分别是什么？前端怎么用？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-110：simulcast 与 SVC 分别是什么？前端怎么用？（高频压轴）
**答**：
- simulcast：同一画面编码出 2-3 档独立码流（q/h/f），一起发给 SFU，SFU 按订阅者网络与能力选流转发。
- SVC：一路可分级码流（时间层 T/空间层 S/质量层 Q），SFU 丢高层即降档，编码一次冗余小，但链路与解码器要求高。
- 前端开启：addTransceiver + sendEncodings 配 rid/scaleResolutionDownBy/maxBitrate；setParameters 可动态开关档位。
- 上行带宽代价：simulcast 上行约翻倍，发送端弱网时先关最高档（active: false）。
- 与 AV-035 的区别：这里落到 API 与参数层面，能说出 rid 与 setParameters 才算会。

```javascript
// 开启 simulcast 三档 + 动态调档
const pc = new RTCPeerConnection();
const { sender } = pc.addTransceiver(cameraTrack, {
  direction: 'sendonly',
  sendEncodings: [
    { rid: 'q', maxBitrate: 150_000,  scaleResolutionDownBy: 4 }, // 180p
    { rid: 'h', maxBitrate: 500_000,  scaleResolutionDownBy: 2 }, // 360p
    { rid: 'f', maxBitrate: 1_500_000, scaleResolutionDownBy: 1 },// 720p
  ],
});
// 弱网时降上行：关掉最高档，SFU 侧只剩 q/h 可转发
async function capToLow() {
  const p = await sender.getParameters();
  p.encodings = p.encodings.map((e) => e.rid === 'f' ? { ...e, active: false } : e);
  await sender.setParameters(p);
}
// SVC（VP9/AV1）：在 encoding 上声明 scalabilityMode，如 'L1T3'（1 空间层 3 时间层）
// const p = await sender.getParameters(); p.encodings[0].scalabilityMode = 'L1T3'; await sender.setParameters(p);
```
