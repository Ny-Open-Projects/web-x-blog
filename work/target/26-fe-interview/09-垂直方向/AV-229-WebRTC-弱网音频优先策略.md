---
title: [AV-229] WebRTC 弱网音频优先策略：Opus 参数调优
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-229：WebRTC 弱网音频优先策略：Opus 参数调优

**答**：
- 题目：极端弱网（带宽 < 100kbps）保音频通话——Opus 参数调优：降采样率（16kHz）、DTX（静音不发包）、FEC（前向纠错换抗丢包）。
- 思路：sender.setParameters 音频编码参数；Opus 的 DTX（静音期不发包省带宽）；inbandFec 换抗丢包（冗余加大码率但丢包可恢复）。
- 评分点：Opus 参数项；DTX/FEC 权衡；audioLevel 静音检测配合。

```javascript
async function optimizeAudioForBadNetwork(sender) {
  const p = sender.getParameters();
  const enc = p.encodings[0];
  enc.maxBitrate = 24000;                                   // 24kbps 语音够用
  // Opus 细节参数（浏览器支持有限，部分需 SDP 层）：
  // stereo=false（单声道）、maxaveragebandwidth=16000（16kHz 采样）
  // useinbandfec=1（FEC：用冗余换抗丢包）、usedtx=1（DTX：静音不发包）
  await sender.setParameters(p);
  // SDP 层修改（munging，浏览器允许的有限场景）：
  // offer.sdp = offer.sdp.replace('useinbandfec=0', 'useinbandfec=1;usedtx=1');
}
// DTX 生效时：静音期 packetsSent 停止增长 → getStats 可验证（带宽节省 50%+）
```
