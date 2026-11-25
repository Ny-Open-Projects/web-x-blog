---
title: [H5-017] 为什么用 source 提供多个媒体源？type 有什么用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-017：为什么用 source 提供多个媒体源？type 有什么用？
**答**：
- 不同浏览器支持的容器/编码不同，`<source>` 按顺序提供候选，浏览器选第一个"认识"的格式。
- `type` 属性声明 MIME + codecs（如 `video/mp4; codecs="avc1.42E01E"`），浏览器可以不下载就判断支持性。
- 老浏览器或编码不支持的场景，video 标签内的兜底内容会显示。
- 现代编码建议：优先 WebM（VP9/AV1），兼容回退 H.264 MP4。

```html
<!-- 浏览器从上到下探测，命中第一个支持的格式 -->
<video controls poster="/media/cover.jpg" width="640">
  <source src="/media/demo.webm" type="video/webm; codecs=vp9,opus" />
  <source src="/media/demo.mp4" type="video/mp4; codecs=avc1.42E01E,mp4a.40.2" />
  <!-- 以上都不支持时，标签内的内容作为兜底 -->
  <p>你的浏览器不支持 video，<a href="/media/demo.mp4">点此下载</a>观看。</p>
</video>

<!-- 音频同理 -->
<audio controls>
  <source src="/media/episode.ogg" type="audio/ogg; codecs=vorbis" />
  <source src="/media/episode.mp3" type="audio/mpeg" />
</audio>
```
