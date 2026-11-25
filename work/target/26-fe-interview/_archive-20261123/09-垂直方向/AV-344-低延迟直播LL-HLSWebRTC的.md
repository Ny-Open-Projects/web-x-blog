---
title: [AV-344] 低延迟直播（LL-HLS/WebRTC）的技术路线
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-344：低延迟直播（LL-HLS/WebRTC）的技术路线

**答**：
- WebRTC：亚秒延迟（200~500ms），代价：转协议成本、CDN 分发弱、并发扩展难（SFU）。
- LL-HLS：2~5s，HTTP 分发成本低，CDN 兼容，是普通直播性价比解。
- 选型：连麦/互动课用 WebRTC；万人直播用 LL-HLS/LL-DASH。

```javascript
// 延迟-成本决策
function liveProtocol({ latencyNeed, audience, budget } = {}) {
  if (latencyNeed < 1) return { proto: 'webrtc',
    note: 'SFU 成本随并发线性涨', limit: '单房间 < 10k' };
  if (latencyNeed < 5) return { proto: 'll-hls',
    partSegments: true, note: 'CDN 直发，成本低' };
  return { proto: 'hls', partSegments: false, note: '传统 6~15s' };
}
```
