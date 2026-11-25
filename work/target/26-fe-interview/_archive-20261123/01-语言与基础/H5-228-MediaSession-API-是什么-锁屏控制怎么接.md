---
title: [H5-228] MediaSession API 是什么，锁屏控制怎么接
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-228：MediaSession API 是什么，锁屏控制怎么接

**答**：
- MediaSession：把 Web 音频/视频接入系统媒体控制中心——锁屏界面、通知栏、耳机按键都能控制播放
- 元数据：`metadata.title/artist/album/artwork` 显示在系统 UI；artwork 多尺寸适配不同界面
- 动作处理：`setActionHandler('play' | 'pause' | 'nexttrack' | 'previoustrack' | 'seekto' ...)` 接管系统按键
- 移动端价值：音频类 H5（播客、音乐 App）没有它就没有后台播放体验，是「Web 能力接近原生」的代表 API
- 钩子：配合 Service Worker 的 MediaSession 可实现后台持续播放（PWA 音频场景）

```javascript
navigator.mediaSession.metadata = new MediaMetadata({
  title: '第 12 期', artist: '技术播客', album: '前端周刊',
  artwork: [{ src: 'cover.png', sizes: '512x512', type: 'image/png' }],
});
navigator.mediaSession.setActionHandler('nexttrack', playNext);
navigator.mediaSession.setActionHandler('pause', () => audio.pause());
navigator.mediaSession.playbackState = 'playing'; // 同步系统状态
```
