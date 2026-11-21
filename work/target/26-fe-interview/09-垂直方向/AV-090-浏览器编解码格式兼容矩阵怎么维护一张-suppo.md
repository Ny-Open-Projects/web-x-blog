---
title: [AV-090] 浏览器编解码格式兼容矩阵？怎么维护一张 support 表？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-090：浏览器编解码格式兼容矩阵？怎么维护一张 support 表？（高频）
**答**：
- 关键矩阵维度：容器（MP4/WebM/TS）× 编码（H264 profile/level、H265、VP8/VP9/AV1、AAC/Opus/FLAC）× 场景（原生 canPlayType / MSE isTypeSupported / WebRTC codec）。
- 已知重点：Safari 无 MSE（旧版）但原生 HLS；H265 仅 Safari 与部分硬解设备；AV1 Chrome/安卓新版可解、iOS 17+ 才支持；WebRTC 音频强制 Opus。
- 动态探测而非硬编码：用 `MediaSource.isTypeSupported` + `RTCReceiver.getCapabilities(kind)` 运行时构建支持表，缓存到 sessionStorage。
- 服务端配合：转码输出按 UA/能力接口返回对应格式清单（内容协商），而不是客户端碰运气。
- 维护方式：caniuse + 内部真机矩阵定期回归 + 能力上报聚合生成真实分布报表。

```javascript
// 运行时构建编解码支持矩阵并上报
async function buildCodecSupportMatrix() {
  const videoCodecs = ['avc1.42E01E', 'avc1.640028', 'hvc1.1.6.L93.B0',
    'vp09.00.10.08', 'av01.0.05M.08'];
  const audioCodecs = ['mp4a.40.2', 'opus', 'flac'];
  const matrix = { video: {}, audio: {}, webrtc: {} };
  const hasMSE = typeof MediaSource !== 'undefined';
  for (const c of videoCodecs) {
    matrix.video[c] = {
      mp4Mse: hasMSE && MediaSource.isTypeSupported(`video/mp4; codecs="${c}"`),
      webmMse: hasMSE && MediaSource.isTypeSupported(`video/webm; codecs="${c}"`),
      native: document.createElement('video').canPlayType(`video/mp4; codecs="${c}"`) !== '',
    };
  }
  for (const c of audioCodecs) {
    matrix.audio[c] = hasMSE && MediaSource.isTypeSupported(`audio/mp4; codecs="${c}"`);
  }
  // WebRTC 接收能力（rVFC 时代最准的来源）
  if (window.RTCRtpReceiver?.getCapabilities) {
    matrix.webrtc.video = RTCRtpReceiver.getCapabilities('video').codecs.map((c) => c.mimeType);
    matrix.webrtc.audio = RTCRtpReceiver.getCapabilities('audio').codecs.map((c) => c.mimeType);
  }
  await fetch('/api/codec-report', { method: 'POST', body: JSON.stringify({ ua: navigator.userAgent, matrix }) });
  return matrix;
}
```
