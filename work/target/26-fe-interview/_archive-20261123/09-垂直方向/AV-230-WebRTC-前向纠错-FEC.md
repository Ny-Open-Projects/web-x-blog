---
title: [AV-230] WebRTC 前向纠错 FEC：冗余与抗丢包权衡
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-230：WebRTC 前向纠错 FEC：冗余与抗丢包权衡

**答**：
- FEC（Forward Error Correction）：发送冗余数据使接收端丢包后自行恢复（不用等重传）——视频 ULPFEC/FLEXFEC、音频 Opus 内嵌 FEC。
- 权衡：FEC 增加码率（冗余 20~50%）但消重传延迟——高 RTT 链路 FEC 优于 NACK。
- 自适应：按丢包率动态调 FEC 冗余度（丢包高加冗余）。

```javascript
function adaptiveFec(packetLossRate) {                     // 丢包率 → FEC 冗余
  if (packetLossRate < 0.02) return { fec: false };         // < 2%：不需要
  if (packetLossRate < 0.1)
    return { fec: true, redundancy: 0.2 };                  // 20% 冗余
  return { fec: true, redundancy: 0.5, alsoNack: true };    // 高丢包：FEC + NACK 双保险
}
// 音频 Opus FEC：帧内嵌前一帧冗余——丢 1 帧可用 FEC 重建（几乎无感）
// 视频 FEC：ULPFEC 包级纠错——SFU/浏览器自动协商（SDP ulpfec/flexfec-03）
```
