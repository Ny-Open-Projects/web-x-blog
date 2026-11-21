---
title: [H5-143] 视频 seek 为什么会"卡一下"？前端如何优化？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-143：视频 seek 为什么会"卡一下"？前端如何优化？
**答**：
- 根因：seek 目标帧前若无关键帧，解码器要从上一个关键帧逐帧解码到目标帧——GOP（关键帧间隔）越长随机 seek 越慢，根本优化在服务端转码（GOP 控制在 1~2s）。
- `seeked` 事件只代表解码完成，画面可能尚未渲染；精确"看到目标帧"用 `requestVideoFrameCallback` 等真实呈现。
- `fastSeek()` 快速但低精度（跳到目标附近关键帧），适合拖动预览。
- 进度条缩略图不要反复 seek 主视频：预生成雪碧图按时间取背景位置，零解码成本。

```html
<video id="v" controls preload="metadata" src="movie.mp4"></video>
<div id="tip"></div>
<script>
const v = document.getElementById('v');

// 1) 精确 seek：seeked 只代表解码完成，画面可能还没渲染；
//    requestVideoFrameCallback 等"真正渲染出目标帧"
function preciseSeek(t) {
  return new Promise((resolve) => {
    const onSeeked = () => {
      if ('requestVideoFrameCallback' in v) {
        v.requestVideoFrameCallback(() => resolve());   // 新帧真正呈现
      } else resolve();
    };
    v.addEventListener('seeked', onSeeked, { once: true });
    v.currentTime = t;
  });
}

// 2) 快速但低精度：fastSeek 跳到目标附近的关键帧（部分浏览器支持）
function fastSeek(t) { v.fastSeek ? v.fastSeek(t) : (v.currentTime = t); }

// 3) 缩略图预览不 seek 主视频：预生成雪碧图，按时间换 background-position
const cols = 10, fw = 160, fh = 90;
function seekPreview(el, t, duration) {
  const total = cols * 10;
  const idx = Math.min(total - 1, Math.floor((t / duration) * total));
  el.style.backgroundImage = 'url(sprite.jpg)';   // 10 行 x 10 列帧图
  el.style.width = fw + 'px'; el.style.height = fh + 'px';
  el.style.backgroundPosition =
    `-${(idx % cols) * fw}px -${Math.floor(idx / cols) * fh}px`;
}

// 4) 拖动进度条节流：input 高频触发只做预览，change/落点才真正 seek
// 根本优化在服务端：转码时把 GOP 控制在 1~2s，或另出一条长 GOP 关键帧流供专业播放器
</script>
```
