---
title: [AV-091] WebCodecs API 概览：比 MSE 更底层的能力能做什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-091：WebCodecs API 概览：比 MSE 更底层的能力能做什么？（高频）
**答**：
- 定位：直接暴露编码器/解码器（VideoDecoder/VideoEncoder/AudioEncoder/AudioDecoder），输入输出是原始帧（VideoFrame/AudioData），跳过容器与播放器黑盒。
- 与 MSE 区别：MSE 喂封装流、浏览器决定解码时机；WebCodecs 由 JS 完全控制每一帧——可实现自定义播放器、低延迟渲染、逐帧处理、录制编码。
- 典型应用：视频剪辑导出（AV-075）、云游戏解码渲染、实时滤镜后重编码、超低延迟播放（配合 WebTransport 传裸帧）。
- 关键概念：configure（codec 字符串/码率/硬件偏好）、decode 队列（decodeQueueSize 背压控制）、VideoFrame 的 timestamp/duration 与 close()（必须手动释放，否则内存爆）。
- 兼容性：Chrome/Edge 全支持，Safari 16.4+，Firefox 部分支持；硬解能力用 isConfigSupported 预检。

```javascript
// WebCodecs 解码 + Canvas 渲染最小示例
async function decodeWithWebCodecs(demuxedSamples) {
  const support = await VideoDecoder.isConfigSupported({
    codec: 'avc1.640028', // 需与流参数一致
  });
  if (!support.supported) throw new Error('本机不支持该解码配置');

  const canvas = document.querySelector('canvas').transferControlToOffscreen();
  const ctx = canvas.getContext('2d');
  const decoder = new VideoDecoder({
    output: (frame) => {           // 解码出的 VideoFrame
      ctx.drawImage(frame, 0, 0);
      frame.close();               // 必须释放！
    },
    error: (e) => console.error('decode error', e),
  });
  decoder.configure({ codec: 'avc1.640028', optimizeForLatency: true }); // 低延迟模式
  for (const sample of demuxedSamples) { // 由 demuxer（如 mp4box.js）提供
    decoder.decode(new EncodedVideoChunk({
      type: sample.isSync ? 'key' : 'delta',
      timestamp: sample.pts,
      data: sample.data,
    }));
    // 背压控制：队列过深时等待
    while (decoder.decodeQueueSize > 10) await new Promise((r) => setTimeout(r, 5));
  }
  await decoder.flush();
}
```
