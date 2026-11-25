---
title: [H5-226] WebCodecs 是什么，和 MSE 的分工
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-226：WebCodecs 是什么，和 MSE 的分工

**答**：
- WebCodecs：直接暴露底层编解码器（VideoEncoder/Decoder/AudioEncoder），拿原始帧、出编码帧，全由 JS 控制
- 与 MSE 的分工：MSE 是「喂封装好的容器数据给 video 标签」，流程黑盒；WebCodecs 是「帧级控制」——转码、剪辑、逐帧处理、低延迟直播（<100ms）才用它
- 典型场景：浏览器内视频剪辑导出（DecodeFrame → 加水印 → EncodeFrame → mux）、云游戏解码渲染
- 成本：要自己处理封装/解封装（mp4 box）、时间戳、关键帧与缓冲管理，门槛显著高于 MSE
- 面试话术：WebRTC 管实时传输、MSE 管流式播放、WebCodecs 管帧级加工，三者不是替代关系

```javascript
const encoder = new VideoEncoder({
  output: (chunk, meta) => saveChunk(chunk), // 编码后的 H264 帧
  error: console.error,
});
encoder.configure({ codec: 'avc1.64001f', width: 1280, height: 720, bitrate: 5e6 });
const frame = new VideoFrame(canvas, { timestamp: 0 });
encoder.encode(frame, { keyFrame: true });
frame.close();
await encoder.flush();
```
