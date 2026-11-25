---
title: [AV-227] WebRTC 转推 RTMP：WebRTC 流转 CDN 直播
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-227：WebRTC 转推 RTMP：WebRTC 流转 CDN 直播

**答**：
- 架构：主播 WebRTC → SFU → 服务端转 RTMP → CDN（HLS/FLV 观看）——互动层与大规模层分离。
- 前端无关转推（SFU 侧），但前端可感知：转推状态事件（转推中/中断）、观看端协议切换提示。
- 转推质量：SFU 侧 RTP→RTMP 转封装（不重编码，低 CPU）或重编码（统一规格）。

```javascript
class LiveDistribution {
  onForwardState(state) {                                  // SFU 广播转推状态
    if (state === 'forwarding') showBadge('直播中（WebRTC+CDN 双链路）');
    if (state === 'interrupted') {
      showBanner('CDN 转推中断，互动层正常——正在恢复');
      this.scheduleRecheck();                               // 定期查转推恢复
    }
  }
  async switchToCDN() {                                     // 观众端降级到 CDN
    if (this.ws.readyState !== WebSocket.OPEN) {
      const hls = hlsjs_attach(this.cdnUrl);                 // HLS 拉流
      this.latencyIndicator = '10s+';
    }
  }
}
// 转推规格统一：SFU 侧选 Simulcast 最高层转推（720p），多主播混流需 MCU/ffmpeg 合流
```
