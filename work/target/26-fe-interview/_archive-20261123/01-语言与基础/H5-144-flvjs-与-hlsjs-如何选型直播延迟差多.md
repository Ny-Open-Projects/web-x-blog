---
title: [H5-144] flv.js 与 hls.js 如何选型？直播延迟差多少？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-144：flv.js 与 hls.js 如何选型？直播延迟差多少？
**答**：
- **HLS**（.m3u8 + ts/fMP4 切片）：CDN 与生态最友好、Safari 原生支持，延迟 6~30s（LL-HLS 可压到 2s 左右）；点播/兼容性场景首选。
- **HTTP-FLV**：延迟 1~3s，国内直播 CDN 主流；浏览器不原生支持，靠 flv.js 基于 MSE 实时转封装。
- 都基于 MSE（MediaSource Extensions）——iPhone 上不支持 MSE，只能走原生 HLS，这是选型必须写进结论的平台约束。
- 超低延迟（连麦、<1s）直接上 WebRTC；两者都要处理 fatal 错误自动重连，直播场景没有恢复逻辑等于不可用。

```html
<!-- 选型口径：
     HLS  m3u8 切片   延迟 6~30s  LL-HLS 约 2s   CDN 生态最广  Safari 原生
     FLV  http-flv 流  延迟 1~3s                国内直播 CDN 主流  靠 MSE 转封装
     WebRTC            延迟 1s 内               连麦 超低延迟 成本高
     点播优先 HLS（兼容/CDN/缓存友好），低延迟直播选 http-flv，连选用 WebRTC -->
<video id="player" controls autoplay muted></video>
<script src="https://cdn.example.com/hls.min.js"></script>
<script src="https://cdn.example.com/flv.min.js"></script>
<script>
const video = document.getElementById('player');

function play(url) {
  if (url.endsWith('.m3u8')) {
    if (video.canPlayType('application/vnd.apple.mpegurl') && !window.Hls) {
      video.src = url;                       // iOS Safari 原生 HLS
    } else {
      const hls = new Hls({ lowLatencyMode: true, backBufferLength: 30 });
      hls.loadSource(url);
      hls.attachMedia(video);                // MSE：hls.js 拉切片转 fMP4 喂给 video
      hls.on(Hls.Events.ERROR, (_, data) => {
        if (data.fatal) hls.startLoad();     // 直播必须做 fatal 恢复，否则卡死
      });
    }
  } else if (url.endsWith('.flv')) {
    const flv = flvjs.createPlayer({ type: 'flv', isLive: true, url });
    flv.attachMediaElement(video);           // flv.js 实时转封装进 MSE
    flv.load();
    flv.on(flvjs.Events.ERROR, () => flv.unload());
  } else {
    video.src = url;                         // 普通 mp4 直出
  }
}
// 共同前提：MSE。iPhone 不支持 MSE 只能原生 HLS（延迟受切片策略限制）——
// 这是选型时必须写进结论的平台约束
</script>
```
