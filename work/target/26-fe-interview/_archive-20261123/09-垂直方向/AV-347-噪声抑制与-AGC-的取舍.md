---
title: [AV-347] 噪声抑制与 AGC 的取舍
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-347：噪声抑制与 AGC 的取舍

**答**：
- NS（噪声抑制）：消稳态噪声（风扇/空调）好，但损伤音乐（谐波被削）——会议开、音乐关。
- AGC：自动增益让音量一致，但音乐场景压缩动态范围（炸音）——同理分场景。
- 分级：WebRTC 降噪强度 0~3，高端会议产品用 AI 降噪（RNNoise 类）替代内置。

```javascript
// 分场景音频链
function audioChain(scene) {
  const chains = {
    meeting: { ns: 2, agc: true, aec: true },        // 会议全开
    music:   { ns: 0, agc: false, aec: true },       // 音乐关 NS/AGC
    live:    { ns: 1, agc: true, aec: true },        // 直播居中
  };
  return chains[scene] ?? chains.meeting;
}
```
