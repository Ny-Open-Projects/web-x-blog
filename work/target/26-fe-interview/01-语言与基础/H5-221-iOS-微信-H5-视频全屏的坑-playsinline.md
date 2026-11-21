---
title: [H5-221] iOS/微信 H5 视频全屏的坑（playsinline/x5）
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-221：iOS/微信 H5 视频全屏的坑（playsinline/x5）

**答**：
- iOS 默认点播视频直接接管全屏（弹系统播放器），页面内播放必须加 `playsinline` + `webkit-playsinline` 属性
- 微信安卓（X5 内核历史行为）会强制全屏同层播放，需要 `x5-video-player-type="h5"` + `x5-video-player-fullscreen`，新内核已逐步标准化
- iOS 键盘/横屏联动：全屏播放后旋转回来页面 viewport 可能错乱，需监听 resize 修正
- 自动播放叠加：iOS 上 playsinline + muted + autoplay 是「页面内自动播」的必要组合
- 排查思路：先区分「接管全屏」（属性缺失）vs「黑屏有声」（编解码不支持，如 H.265/AV1 在老设备）

```html
<video playsinline webkit-playsinline x5-video-player-type="h5"
       x5-video-orientation="portraint" muted autoplay loop poster="cover.jpg">
  <source src="a.mp4" type="video/mp4">
</video>
```
