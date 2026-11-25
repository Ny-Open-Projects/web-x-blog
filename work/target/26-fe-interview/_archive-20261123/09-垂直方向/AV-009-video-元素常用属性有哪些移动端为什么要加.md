---
title: [AV-009] video 元素常用属性有哪些？移动端为什么要加 playsinline？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-009：video 元素常用属性有哪些？移动端为什么要加 playsinline？
**答**：
- 核心属性：`src/poster/preload/controls/loop/muted/autoplay`，以及移动端专属 `playsinline`、`x5-video-player-type`。
- `preload="none|metadata|auto"`：列表页多视频必须 none/metadata，避免带宽与内存浪费。
- `playsinline` 防止 iOS Safari 点击播放后强制全屏接管；iOS 低版本还需 `webkit-playsinline`。
- 安卓微信/X5 内核用 `x5-video-player-type="h5-page"` 进入同层播放器，否则视频置顶遮盖 DOM。
- `muted + autoplay` 是自动播放的通行证；内联播放 + 自绘控制条是移动端播放器标配。

```html
<!-- 移动端兼容三件套的标准写法 -->
<video
  id="player"
  src="https://cdn.example.com/demo.m3u8"
  poster="https://cdn.example.com/cover.jpg"
  preload="metadata"
  playsinline
  webkit-playsinline
  x5-playsinline
  x5-video-player-type="h5-page"
  x5-video-orientation="portraint"
  muted
></video>
<script>
  const video = document.getElementById('player');
  // iOS 静音自动播放，用户手势后再取消静音
  video.play().catch(() => {
    document.addEventListener('touchstart', () => video.play(), { once: true });
  });
</script>
```
