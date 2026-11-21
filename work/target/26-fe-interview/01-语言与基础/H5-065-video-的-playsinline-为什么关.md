---
title: [H5-065] video 的 playsinline 为什么关键？iOS 上不加会发生什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-065：video 的 playsinline 为什么关键？iOS 上不加会发生什么？
**答**：
- iOS Safari 里内联播放是被"选择加入"的：不加 `playsinline`，视频播放时会**全屏接管**整个界面，退出需要用户手动点"完成"。
- `playsinline` 让视频在页面内嵌位置播放，是所有 H5 视频流（信息流、商品主图视频、直播小窗）在 iOS 上正常工作的前提。
- 历史包袱：iOS 10 之前需要私有属性 `webkit-playsinline`，现在标准属性已全覆盖；Android 上一直内联，无需处理。
- 组合：`playsinline` + `muted` + `autoplay` 才能静默自动播放（尤其 iOS）；三者缺一自动播放大概率被拦截。
- 与全屏的配合：需要全屏时**显式**调 `requestFullscreen()` 或 `webkitEnterFullscreen()`（后者仅 iOS 原生控件可用），把选择权还给代码。

```html
<!-- 信息流视频的标准三件套：内联 + 静音 + 自动播放 -->
<video id="feed-video"
       playsinline
       muted
       autoplay
       loop
       webkit-playsinline
       preload="metadata"
       poster="/img/cover.jpg"
       src="/media/clip.mp4"></video>

<script>
  const v = document.getElementById('feed-video');

  // 用户点了"开声音"：解除静音后 iOS 允许继续播放
  document.getElementById('unmute').addEventListener('click', () => {
    v.muted = false;
    v.play().catch(console.warn);
  });

  // 想全屏：显式请求，而不是依赖 iOS 的自动全屏接管
  document.getElementById('fs').addEventListener('click', () => {
    if (v.requestFullscreen) v.requestFullscreen();
    else if (v.webkitEnterFullscreen) v.webkitEnterFullscreen(); // iOS 原生全屏
  });

  // iOS 低电量模式会拦 autoplay：统一 catch 后降级为点击起播
  v.play().catch(() => {
    v.controls = true;
    v.addEventListener('click', () => v.play(), { once: true });
  });
</script>
```
