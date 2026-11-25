---
title: [AV-207] WebRTC 屏幕共享：getDisplayMedia 与内容优化
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-207：WebRTC 屏幕共享：getDisplayMedia 与内容优化

**答**：
- 屏幕共享：getDisplayMedia({video: {displaySurface: "monitor", frameRate: 5}})；文档场景 5fps 足够（省带宽），游戏 30fps。
- 内容提示：contentHint 属性（"text" 高细节低帧 / "motion" 低细节高帧）——浏览器编码器据此调参。
- 区域捕获：CropTarget + CropTrack（Chrome）只共享窗口区域。

```javascript
const displayStream = await navigator.mediaDevices.getDisplayMedia({
  video: { displaySurface: 'monitor', frameRate: { ideal: 5 }, cursor: 'always' },
  audio: false,                                           // 系统音频可选
});
const track = displayStream.getVideoTracks()[0];
track.contentHint = 'text';                               // 文档共享：编码器保细节
// 动态切换内容提示（检测画面变化率）：
// 静态画面多 → 'text'；视频播放中 → 'motion'
track.onended = () => stopSharingUI();                     // 用户点浏览器停止共享
// 区域捕获（Chrome 116+）：
// const target = await CropTarget.fromRegion(el);
// track = await produceCrop(track, target);               // 只共享 DOM 区域
```
