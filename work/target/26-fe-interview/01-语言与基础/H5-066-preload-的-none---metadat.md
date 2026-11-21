---
title: [H5-066] preload 的 none / metadata / auto 真实行为是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-066：preload 的 none / metadata / auto 真实行为是什么？
**答**：
- `none`：**一个字节都不加载**，posters 照常显示，`duration` 等元数据在 `preload` 前不可读；适合列表页几十个视频的弱网场景。
- `metadata`（Chrome 等浏览器的默认值）：只取容器头部的时长、尺寸、轨道信息，触发 `loadedmetadata`；正片不缓冲。
- `auto`：浏览器"尽力"多缓冲，**没有强保证**——移动端浏览器普遍降级为 metadata 甚至 none 省流量，且 WiFi/蜂窝策略不同。
- preload 是**提示不是命令**：`autoplay` 会无视 preload，`userAgent` 也可能基于省电模式覆盖它。
- 工程实践：瀑布流封面用 none，进入视口再切 `preload="metadata"` 或直接 `play()`；详情页大视频用 metadata + 起播后监听 `buffered` 做进度兜底。

```html
<!-- 列表页：一律 none，不产生任何视频流量 -->
<video class="feed-item" preload="none"
       playsinline muted loop
       poster="/img/thumb-1.jpg"
       data-src="/media/clip-1.mp4"></video>

<script>
  const io = new IntersectionObserver((entries) => {
    for (const en of entries) {
      const v = en.target;
      if (!en.isIntersecting) { v.pause(); continue; }

      // 进入视口：懒挂载真实源并请求元数据
      if (!v.src) v.src = v.dataset.src;
      v.preload = 'metadata';                 // 升级为只取头信息
      io.unobserve(v);
    }
  }, { threshold: 0.5 });

  document.querySelectorAll('.feed-item').forEach(v => io.observe(v));

  // 真要起播时，元数据可能还没到：readyState 分级兜底
  document.addEventListener('click', (e) => {
    const v = e.target.closest('video');
    if (!v) return;
    if (v.readyState >= 3) v.play();
    else v.addEventListener('canplay', () => v.play(), { once: true });
  });

  // auto 的缓冲进度监控：buffered 是多段区间，取包含播放头的段
  function bufferedAhead(v) {
    for (let i = 0; i < v.buffered.length; i++) {
      if (v.buffered.start(i) <= v.currentTime &&
          v.currentTime <= v.buffered.end(i)) {
        return v.buffered.end(i) - v.currentTime; // 秒
      }
    }
    return 0;
  }
</script>
```
