---
title: [H5-070] 媒体加载失败的降级链怎么设计？error 事件如何排错？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-070：媒体加载失败的降级链怎么设计？error 事件如何排错？
**答**：
- 降级链路：**首选格式（H.265/AV1）→ 兼容格式（H.264）→ 提示文案**；用多个 `<source>` 让浏览器按序选择，或 JS 检测 `canPlayType` 决策。
- `<source>` 选择失败的报错**不在 video.error 上**，而是最后一个 source 失败后触发 video 的 `error` 事件；`video.error.code` 给出 1-4 的分类。
- error code 对照：1 中止（LOADING 被打断）、2 网络错误、3 解码错误、4 源不支持（格式/编码都不行，最常见的降级信号）。
- source 元素本身有 `onerror`：精确知道"第几个源挂了"，比只在 video 上监听更利于排错与统计。
- 运行时网络中断：监听 `stalled / waiting / error`，指数退避重试 `load()`，并上报 `NetworkError` 附带 `currentSrc`。

```html
<!-- 静态降级：按序尝试，HEVC 不支持则退到 H.264 -->
<video controls playsinline poster="/img/cover.jpg">
  <source src="/media/movie.hevc.mp4" type='video/mp4; codecs="hvc1"'>
  <source src="/media/movie.h264.mp4" type="video/mp4">
  您的浏览器不支持视频播放，<a href="/media/movie.h264.mp4">点此下载</a>
</video>

<script>
  const v = document.querySelector('video');

  v.addEventListener('error', () => {
    const code = v.error?.code;
    const reasons = { 1: '加载中止', 2: '网络错误', 3: '解码错误', 4: '格式不支持' };
    console.error(`媒体加载失败：${reasons[code] ?? code}`, v.currentSrc);

    if (code === 2) return retryWithBackoff();   // 网络 class：可重试
    if (code === 4) showFallback(v);             // 格式 class：换源或提示
  });

  // source 级监听：精确定位是哪个源失败
  v.querySelectorAll('source').forEach((s, i) => {
    s.addEventListener('error', () =>
      console.warn(`第 ${i + 1} 个源失败：`, s.src));
  });

  function retryWithBackoff(attempt = 1) {
    if (attempt > 3) return showFallback(v);
    setTimeout(() => {
      v.load();                                  // 重新触发加载流程
      v.play().catch(() => retryWithBackoff(attempt + 1));
    }, 2 ** attempt * 500);
  }

  function showFallback(v) {
    v.outerHTML = '<p class="media-fallback">视频暂时无法播放，请稍后再试</p>';
  }
</script>
```
