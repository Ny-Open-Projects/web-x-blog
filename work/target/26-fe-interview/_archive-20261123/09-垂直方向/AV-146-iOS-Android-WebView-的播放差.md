---
title: [AV-146] iOS/Android WebView 的播放差异有哪些？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-146：iOS/Android WebView 的播放差异有哪些？（高频压轴）
**答**：
- iOS：video 默认全屏接管（必须 playsinline）、无声才允许自动播（muted+autoplay）、低电量模式拦 autoplay、Safari 上 play() 必须在用户手势调用栈内。
- 安卓：各厂商 WebView 内核差异大（X5/UC），HLS 与 MSE 支持不齐，需运行时探测降级；硬件加速关闭会花屏。
- 内嵌 App：iOS WKWebView 要 native 配 allowsInlineMediaPlayback；安卓 X5 用 x5-playsinline 等私有属性。
- 实用策略：能力探测 + 全屏兜底（inline 不行就 Fullscreen API）+ 静音自动播 + 首次触摸解锁声音。
- 兜底心智：所有"自动播失败"都要有视觉降级（封面 + 播放按钮），而不是黑屏等待。

```html
<!-- 移动端兼容性最全的 video 标签写法 -->
<video id="player"
  playsinline
  webkit-playsinline
  x5-playsinline="true"
  x5-video-player-type="h5"
  x5-video-orientation="portrait|landscape"
  muted
  autoplay
  preload="metadata"
  controls></video>
<script>
  // iOS 自动播被拦（低电量模式等）的兜底：首次触摸解锁并开声
  document.body.addEventListener('touchstart', function unlock() {
    const v = document.getElementById('player');
    v.play().catch(() => {});
    v.muted = false;
    document.body.removeEventListener('touchstart', unlock);
  }, { once: true });
</script>
```
