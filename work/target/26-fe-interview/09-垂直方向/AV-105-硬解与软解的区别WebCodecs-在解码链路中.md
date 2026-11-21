---
title: [AV-105] 硬解与软解的区别？WebCodecs 在解码链路中扮演什么角色？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-105：硬解与软解的区别？WebCodecs 在解码链路中扮演什么角色？（高频）
**答**：
- 硬解走 GPU/专用解码器，功耗低性能高但只认特定 profile/分辨率；软解 CPU 通用实现，兼容性强但耗电发热。
- 浏览器分层：video 标签解码对 JS 黑盒；MSE 只控制到封装层；WebCodecs VideoDecoder 把"逐帧解码"直接暴露给 JS。
- WebCodecs 角色：剪辑导出（解码→处理→重编码）、逐帧分析（AI/截图）、超低延迟自渲染管线（绕过播放器）。
- 用法三步：configure（codec 字符串+分辨率+description）→ decode（EncodedVideoChunk）→ output 回调拿 VideoFrame，必须 close() 否则内存泄漏。
- 背压控制：看 decodeQueueSize 决定喂帧节奏，别把队列堆爆。

```javascript
// WebCodecs VideoDecoder 最小可用示例
const decoder = new VideoDecoder({
  output: (frame) => {            // VideoFrame 用完必须 close
    drawToCanvas(frame);
    frame.close();
  },
  error: (e) => console.error('decode error', e),
});
decoder.configure({
  codec: 'avc1.42001f',           // H264 Constrained Baseline
  codedWidth: 1280, codedHeight: 720,
  description: avccConfigBytes,   // AVCC 格式传 SPS+PPS；AnnexB 不需要
});
// 逐帧喂入（数据来自 demux 或 WebCodecs 上游）
// decoder.decode(new EncodedVideoChunk({ type: 'key',   timestamp: 0,  data: idrBytes }));
// decoder.decode(new EncodedVideoChunk({ type: 'delta', timestamp: 33, data: pBytes }));
console.log(decoder.state, decoder.decodeQueueSize); // 'configured' + 队列深度做背压
```
