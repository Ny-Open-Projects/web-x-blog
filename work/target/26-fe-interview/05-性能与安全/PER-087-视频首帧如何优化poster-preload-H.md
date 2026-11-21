---
title: [PER-087] 视频首帧如何优化？poster/preload/HLS 各自怎么配置？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-087：视频首帧如何优化？poster/preload/HLS 各自怎么配置？

**答**：
- 首屏视频的优先级排序：**poster 图**（毫秒级可见，代替黑屏）→ `preload="metadata"` 或 `none`（不预载整个视频）→ 用户滚动到视口才开始播放（IntersectionObserver）。
- 首帧优化的服务端配合：视频切片用 HLS/DASH，**首片时长做短**（2 秒或更小）、关键帧前置、CDN 预热热门片头；码率自适应首片给低码率档，快速出画再升档。
- hls.js 调优：`startLevel: 0` 从最低档起播、`maxBufferLength` 控制预缓冲、开启 worker 解封装避免主线程阻塞。
- 自动播放带声音被浏览器禁止，必须 `muted` + `playsinline`，播不出去时回退 poster。

```html
<!-- 首帧三件套：poster + 轻预载 + 内联静音自动播放 -->
<!-- poster 毫秒级可见代替黑屏，preload=metadata 只取元数据不拉全片，muted+playsinline 才允许自动播放 -->
<video
  id="hero-video"
  poster="/img/hero-poster.avif"
  preload="metadata"
  muted autoplay playsinline loop
  src="">
</video>
```

```javascript
// hls.js：首帧优先配置 —— 低档起播 + 短缓冲 + worker
import Hls from 'hls.js';
const video = document.querySelector('#hero-video');
if (Hls.isSupported()) {
  const hls = new Hls({
    startLevel: 0,          // 从最低码率档起播，首帧最快
    capLevelToPlayerSize: true,
    maxBufferLength: 10,    // 缓冲 10 秒足够，少占内存与带宽
    enableWorker: true,     // 解封装放 worker，不卡主线程
    lowLatencyMode: false,  // 点播场景关闭低延迟模式，换取稳定起播
  });
  hls.loadSource('/videos/hero/master.m3u8');
  hls.attachMedia(video);
  hls.on(Hls.Events.MANIFEST_PARSED, () => video.play().catch(() => {}));
} else if (video.canPlayType('application/vnd.apple.mpegurl')) {
  video.src = '/videos/hero/master.m3u8'; // Safari 原生 HLS
}

// 视口外不加载：滚动进入视口才初始化
const io = new IntersectionObserver(([e]) => {
  if (e.isIntersecting) { io.disconnect(); initHls(); }
}, { threshold: 0.25 });
io.observe(document.querySelector('#hero-video'));
```
