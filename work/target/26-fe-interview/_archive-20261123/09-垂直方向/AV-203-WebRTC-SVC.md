---
title: [AV-203] WebRTC SVC：可分级视频编码与 Simulcast 对比
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-203：WebRTC SVC：可分级视频编码与 Simulcast 对比

**答**：
- SVC（ Scalable Video Coding）：一条流内部分层（时间/空间/质量层），SFU 丢弃高层即可降级——上行带宽只需一路。
- 对比 Simulcast：Simulcast 多路独立编码（上行带宽 ×3 但兼容性好）；SVC 一路上行（省带宽）但需要编码器支持（VP9/H265 SVC）。
- 前端关注：encodings 里 temporalLayer/spatialLayer 参数；VP9 SVC 在 Chrome 可用。

```javascript
// VP9 SVC：单流分层
const transceiver = pc.addTransceiver(track, {
  sendEncodings: [{
    scalabilityMode: 'L3T3',                              // 3 空间层 × 3 时间层
    maxBitrate: 1500000,
  }],
  codec: vp9Codec,                                        // 需要 VP9 支持协商
});
// SFU 丢弃高层（Dropping layers）即可适配带宽——上行只有 1 路
// 选型：SFU 支持好 + 兼容优先 → Simulcast；带宽敏感 + VP9 可用 → SVC
```
