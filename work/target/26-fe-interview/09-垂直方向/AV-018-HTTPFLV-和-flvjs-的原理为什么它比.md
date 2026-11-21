---
title: [AV-018] HTTP-FLV 和 flv.js 的原理？为什么它比 HLS 延迟低？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-018：HTTP-FLV 和 flv.js 的原理？为什么它比 HLS 延迟低？（高频压轴）
**答**：
- FLV 是把 H264/AAC 裸流加上轻量 tag 头的封装，HTTP-FLV 用 chunked transfer 长连接持续下发，天然流式、无分片等待，延迟 1~3s。
- 浏览器原生不认 FLV（除老旧 Flash 时代），flv.js 的核心 = JS 端 demux（FLV tag 解析出 H264 NALU/AAC 帧、重建时间戳）+ 封装成 fMP4 + MSE appendBuffer。
- 所以 flv.js 依赖：① 浏览器支持 MSE；② 服务器支持 HTTP chunked 流式响应。
- 与 HLS 比：少分片/索引开销，延迟低；缺点：不支持 Safari iOS（无 MSE 于老版本）、CDN 缓存命中差、断流恢复要自己处理。
- 进阶话题：FLV 的 AV packet 时间戳基线不统一时会造成音画不同步，flv.js 有时间戳补偿逻辑。

```javascript
// flv.js 标准用法与内部管线示意
import flvjs from 'flv.js';

flvjs.isSupported() && flvjs.getFeatureList().mseLivePlayback; // 能力检测
const player = flvjs.createPlayer({
  type: 'flv',
  url: 'https://cdn.example.com/live/stream.flv',
  isLive: true,
  hasAudio: true,
}, {
  enableStashBuffer: false, // 关闭内部缓冲以降低延迟（直播关键参数）
  lazyLoad: false,
  autoCleanupSourceBuffer: true, // 自动清 MSE 旧数据防内存膨胀
});
player.attachMediaElement(document.querySelector('video'));
player.load();
player.play();

// 直播追帧：flv.js 暴露延迟估算，超阈值跳到边缘
setInterval(() => {
  const latency = player.statisticsInfo.totalVideoFrames
    ? 0 : player.getMediaInfo().duration; // 实际用 buffered 末尾 - currentTime
  const video = document.querySelector('video');
  const bufEnd = video.buffered.length ? video.buffered.end(video.buffered.length - 1) : 0;
  if (bufEnd - video.currentTime > 3) {
    video.currentTime = bufEnd - 0.5; // 丢弃积压回到直播边缘
  }
}, 5000);
```
