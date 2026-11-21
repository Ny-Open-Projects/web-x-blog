---
title: [H5-019] 浏览器的自动播放策略是什么？autoplay 为什么经常失效？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-019：浏览器的自动播放策略是什么？autoplay 为什么经常失效？
**答**：
- 为避免打扰用户，Chrome 等浏览器规定：有声视频不允许无手势自动播放；`muted` 的视频可以自动播。
- 失效时 `play()` 返回的 Promise 会 reject（NotAllowedError），这是标准行为不是 bug。
- 常用方案：首屏自动播的短视频统一 `autoplay muted playsinline`；或先静音自动播，右上角提供"开启声音"按钮（用户点击即手势，可 unmute）。
- `playsinline` 防 iOS 自动全屏；播放起量广告/直播都会做这套兜底。

```html
<!-- 静音自动播放的标准三件套 -->
<video autoplay muted playsinline loop src="/bg.mp4"></video>
```

```javascript
// 带降级策略的自动播放
const video = document.querySelector('video');
video.muted = true; // 先静音争取播放权

video
  .play()
  .then(() => {
    showUnmuteButton(); // 播放成功后引导用户开声音
  })
  .catch((err) => {
    if (err.name === 'NotAllowedError') {
      // 被策略拦截：等待用户任意手势后再播
      const resume = () => {
        video.play();
        document.removeEventListener('click', resume);
        document.removeEventListener('touchstart', resume);
      };
      document.addEventListener('click', resume);
      document.addEventListener('touchstart', resume);
    }
  });

// 用户的"开声音"点击本身就是手势，可以解除静音
unmuteBtn.addEventListener('click', () => {
  video.muted = false;
  unmuteBtn.hidden = true;
});
```

## 四、Canvas 2D
