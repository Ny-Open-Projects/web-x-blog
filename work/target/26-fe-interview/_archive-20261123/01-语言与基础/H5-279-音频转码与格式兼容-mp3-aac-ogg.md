---
title: [H5-279] 音频格式兼容：mp3/aac/ogg 什么时候需要
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-279：音频格式兼容：mp3/aac/ogg 什么时候需要

**答**：
- 支持矩阵：MP3/AAC（AAC 更高效）全平台支持；OGG Vorbis/Opus 不被老 Safari 支持；FLAC 不被老安卓支持
- 决策顺序：语音场景 AAC-HE（低码率高质量）优先；音乐场景 MP3/AAC 双源兜底足够；播客/直播用 Opus（低延迟）
- 运行时探测：`audio.canPlayType('audio/ogg; codecs="opus"')` 返回 probably/probably-not，据返回值选源
- 双源写法：多个 source 标签按顺序探测，浏览器选第一个能播的
- 服务端转码还是双源存储：流量大的核心内容双源存储，长尾内容服务端实时转码 + CDN 缓存

```html
<audio controls>
  <source src="a.aac" type="audio/aac">
  <source src="a.mp3" type="audio/mpeg">
  您的浏览器不支持音频播放
</audio>
```
```javascript
const supportOpus = document.createElement('audio').canPlayType('audio/ogg; codecs="opus"') !== '';
```
