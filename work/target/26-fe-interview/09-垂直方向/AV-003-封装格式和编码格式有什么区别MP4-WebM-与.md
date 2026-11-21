---
title: [AV-003] 封装格式和编码格式有什么区别？MP4/WebM 与 H264/VP9/AV1 是什么关系？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-003：封装格式和编码格式有什么区别？MP4/WebM 与 H264/VP9/AV1 是什么关系？（高频压轴）
**答**：
- 编码格式（codec）是压缩算法，决定像素→比特流的压缩方式：H264/H265/VP8/VP9/AV1/AVS。
- 封装格式（container）是"盒子"，定义轨道、时间戳、索引的组织方式：MP4/WebM/MKV/FLV/TS。
- 一个封装可装多种编码：MP4 常装 H264/H265/AV1+AAC/Opus，WebM 只装 VP8/VP9/AV1+Vorbis/Opus。
- 浏览器支持矩阵高频结论：H264+AAC 凭 MP4 覆盖最广；WebM 主要服务 VP9/AV1；WebRTC 默认 VP8/H264+Opus。
- `canPlayType` / `MediaSource.isTypeSupported` 是判断兼容性的唯一可信方式。

```javascript
// 区分「容器支持」与「编码支持」的探测代码
const videoEl = document.createElement('video');

// 容器+编码组合探测（canPlayType 只返回 probably/likely/maybe/''）
function probeNative(codecs) {
  return videoEl.canPlayType(`video/mp4; codecs="${codecs}"`) || '不支持';
}
console.log('H264+AAC in MP4:', probeNative('avc1.42E01E, mp4a.40.2'));
console.log('H265 in MP4:', probeNative('hvc1.1.6.L93.B0'));

// MSE 场景必须用 isTypeSupported（决定能否喂给 SourceBuffer）
const mseCandidates = [
  'video/mp4; codecs="avc1.64001f, mp4a.40.2"', // H264 High + AAC-LC
  'video/webm; codecs="vp9, opus"',             // VP9 + Opus
  'video/mp4; codecs="av01.0.05M.08"',          // AV1
];
const supported = mseCandidates.filter((t) => MediaSource.isTypeSupported(t));
console.log('MSE 可用组合:', supported);

// 错误示范：把 .webm 容器当编码 —— 文件后缀≠编码
function guessRealCodec(mimeType) {
  const [, codecStr] = mimeType.split('codecs=');
  return codecStr ? codecStr.replace(/"/g, '') : '未知，需要 ffprobe 探测';
}
```
