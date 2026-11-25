---
title: [AV-254] WebRTC 与 MSE 混合播放：低延迟 + 大规模同屏
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-254：WebRTC 与 MSE 混合播放：低延迟 + 大规模同屏

**答**：
- 混合场景：主播画面 WebRTC（300ms 互动），观众端同时混入 MSE 流（CDN 回放/广告）——同页双播放器音频混音（AV-244）。
- 切换场景：WebRTC 断流 → MSE 流无缝接管（时间戳对齐跳播）。
- 实现：双 video 元素叠层 + 音频 AudioContext 混合（同一 destination）。

```javascript
class HybridPlayer {
  constructor() {
    this.webrtc = createWebRTCPlayer();                     // 主画面（低延迟）
    this.mse = createMSEPlayer();                           // 兜底/混合
    this.mixer = new AudioMixer2();                         // 音频混合（AV-244）
  }
  async onWebRTCStall() {                                    // WebRTC 卡死：MSE 接管
    const lastTs = this.webrtc.currentTimeEstimate;
    await this.mse.play(lastTs);                            // 时间对齐续播
    this.mse.video.style.opacity = 1;                       // 交叉淡入
    this.webrtc.video.style.opacity = 0;
    report('fallback-to-mse', { at: lastTs });
  }
  async onWebRTCRecovered() {                                // 恢复：切回 WebRTC
    this.webrtc.syncTo(this.mse.currentTime);                // 追平进度
    this.mse.video.style.opacity = 0;
    this.webrtc.video.style.opacity = 1;
  }
}
```
