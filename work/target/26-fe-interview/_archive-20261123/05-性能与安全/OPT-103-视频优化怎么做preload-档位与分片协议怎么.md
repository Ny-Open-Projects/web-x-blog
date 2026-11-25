---
title: [OPT-103] 视频优化怎么做？preload 档位与分片协议怎么选？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-103：视频优化怎么做？preload 档位与分片协议怎么选？

**答**：
- `preload` 三档决策：首页非视频位 `none`（一点不拉）；可能播放的 `metadata`（只拉时长/尺寸）；确定首屏即播的才 `auto`。默认 auto 是流量黑洞。
- 长视频用 **HLS/DASH 分片**：按秒切片 + 自适应码率（弱网降清晰度不断流），首帧只要第一个分片；短视频（<2min）可以直接 MP4 但要用 `range` 请求支持。
- 首帧优化四件套：`poster` 占位图、`muted` + `playsinline`（自动播放条件）、封面用首帧截图而非加载视频后再解码、`mediafragments`（`#t=0.5` 预热 moov box）。
- MP4 注意 moov 前置（faststart），否则浏览器要下完整个文件才能播。

```html
<!-- 一一对应：视频加载策略三档落地 -->
<!-- 场景 1：非首屏视频位 —— 完全不预载，点击时才真正加载 -->
<video
  preload="none"
  poster="cover.avif"
  controls
  data-src="https://cdn.example.com/demo.mp4">
</video>
<script>
  // facade 模式：点击封面才注入 src，避免 preload=none 也被部分浏览器偷流
  document.querySelectorAll('video[data-src]').forEach((v) => {
    v.addEventListener('play', () => {
      if (!v.src) v.src = v.dataset.src;
    }, { once: true });
  });
</script>

<!-- 场景 2：列表中可能播放 —— 只取元数据 -->
<video preload="metadata" poster="cover.avif" muted playsinline></video>

<!-- 场景 3：首屏必播的背景视频 —— 立即加载但必须静音内联，否则自动播放被拒 -->
<video autoplay muted loop playsinline preload="auto" poster="first-frame.avif">
  <!-- source 顺序即格式协商：webm 体积更小优先 -->
  <source src="bg.webm" type="video/webm" />
  <source src="bg.mp4" type="video/mp4" />
</video>

<!-- 场景 4：长视频课程页 —— HLS 分片 + 自适应码率 -->
<!-- <video id="player" controls poster="cover.avif"></video> -->
<script type="module">
  import Hls from 'hls.js';
  const video = document.querySelector('#player');
  if (video.canPlayType('application/vnd.apple.mpegurl')) {
    video.src = 'https://cdn.example.com/lesson.m3u8'; // Safari 原生
  } else if (Hls.isSupported()) {
    const hls = new Hls({ startLevel: 0, capLevelToPlayerSize: true }); // 起播低码率秒开，分辨率对齐播放器尺寸
    hls.loadSource('https://cdn.example.com/lesson.m3u8');
    hls.attachMedia(video);
  }
</script>
```
