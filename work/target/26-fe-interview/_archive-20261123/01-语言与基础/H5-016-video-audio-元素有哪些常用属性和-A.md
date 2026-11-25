---
title: [H5-016] video/audio 元素有哪些常用属性和 API？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-016：video/audio 元素有哪些常用属性和 API？
**答**：
- 属性：`controls` 显示原生控制条、`autoplay`、`muted`、`loop`、`poster` 封面、`preload`（none/metadata/auto）控制预加载策略。
- 常用 API：`play()/pause()`（返回 Promise）、`currentTime/duration`、`volume`、`playbackRate`、`muted`。
- 事件：`loadedmetadata`（拿到时长）、`timeupdate`（进度）、`ended`、`error`、`waiting/playing`（缓冲状态）。
- `preload="none"` 用于列表页省流量，点击后再 `load()+play()`。

```html
<video
  id="player"
  src="/media/lesson.mp4"
  poster="/media/cover.jpg"
  preload="metadata"
  controls
></video>

<script>
  const video = document.getElementById('player');

  video.addEventListener('loadedmetadata', () => {
    console.log('时长:', video.duration); // 元数据就绪后才有值
  });

  video.addEventListener('timeupdate', () => {
    const pct = (video.currentTime / video.duration) * 100;
    document.querySelector('.progress').style.width = `${pct}%`; // 自定义进度条
  });

  // play 返回 Promise：被自动播放策略拦截时会在 reject 里体现
  async function togglePlay() {
    try {
      if (video.paused) await video.play();
      else video.pause();
    } catch (e) {
      console.warn('播放被浏览器策略阻止，需要用户手势:', e.name);
    }
  }

  // 倍速与音量
  video.playbackRate = 1.5;
  video.volume = 0.6;
</script>
```
