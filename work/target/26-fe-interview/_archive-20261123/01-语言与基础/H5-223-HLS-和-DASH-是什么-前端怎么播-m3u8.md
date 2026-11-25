---
title: [H5-223] HLS 和 DASH 是什么，前端怎么播 m3u8
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-223：HLS 和 DASH 是什么，前端怎么播 m3u8

**答**：
- HLS（Apple）：m3u8 索引 + ts/fMP4 分片（典型 6s 一片）；iOS 原生支持，其他平台靠 hls.js（MSE）
- DASH（国际标准）：mpd 清单 + 分片，Google 生态（YouTube）使用广泛，无原生支持全靠 dash.js
- 自适应原理：清单里列出多档码率；播放器实时测网速，按带宽选分片档位，实现「越网快越清晰」
- 直播 vs 点播：直播 m3u8 是滚动窗口（持续追加），点播是完整列表；直播要处理「追帧」（落后于最新分片时跳播）
- 前端集成：hls.js 判断 `Hls.isSupported()`，不支持时回退原生 video.src = m3u8（iOS）

```javascript
if (Hls.isSupported()) {
  const hls = new Hls({ maxBufferLength: 30 });
  hls.loadSource('live.m3u8');
  hls.attachMedia(video);
  hls.on(Hls.Events.ERROR, (_, data) => {
    if (data.fatal) hls.recoverMediaError(); // 自动恢复
  });
} else {
  video.src = 'live.m3u8'; // iOS 原生
}
```
