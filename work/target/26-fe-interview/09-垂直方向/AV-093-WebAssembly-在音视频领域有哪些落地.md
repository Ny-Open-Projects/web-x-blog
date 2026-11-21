---
title: [AV-093] WebAssembly 在音视频领域有哪些落地？（ffmpeg.wasm/解码器）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-093：WebAssembly 在音视频领域有哪些落地？（ffmpeg.wasm/解码器）
**答**：
- 典型场景：ffmpeg.wasm（浏览器内转码/抽帧/合成，纯前端剪辑导出）、自研解码器（软解 AV1/H265 覆盖不支持硬解的设备）、Web Audio 自研 DSP（降噪模型/混响）。
- 与 WebCodecs 关系：WebCodecs 走硬件加速优先；WASM 解码器是"硬解不支持时"的软件兜底，也用于 MSE/WEbCodecs 不覆盖的格式（如 TS 直解、RMVB 老格式）。
- 性能与代价：SIMD + 线程（SharedArrayBuffer 需要 COOP/COEP 头）后接近原生 50-80%；代价是体积（ffmpeg.wasm 核心约 25MB，按模块裁剪）与首载时间。
- 工程要点：Worker 中运行防阻塞主线程、分片流式处理控内存、按需加载（用户点导出才拉 wasm）。
- 边界认知：能拿到的 ffmpeg.wasm 是 LGPL 裁剪版，商业编解码器（H264 编码）要注意授权问题。

```javascript
// ffmpeg.wasm 抽帧 + WASM 软解码兜底
import { FFmpeg } from '@ffmpeg/ffmpeg';
import { fetchFile } from '@ffmpeg/util';

async function extractFramesWithFFmpeg(videoUrl) {
  const ffmpeg = new FFmpeg();
  await ffmpeg.load(); // 首次加载 wasm 核心（建议提前预热）
  await ffmpeg.writeFile('in.mp4', await fetchFile(videoUrl));
  await ffmpeg.exec(['-i', 'in.mp4', '-vf', 'fps=1/5', '-q:v', '5', 'frame_%03d.jpg']);
  const frames = [];
  for (let i = 1; ; i++) {
    const name = `frame_${String(i).padStart(3, '0')}.jpg`;
    try {
      const data = await ffmpeg.readFile(name);
      frames.push(URL.createObjectURL(new Blob([data.buffer], { type: 'image/jpeg' })));
      await ffmpeg.deleteFile(name);
    } catch { break; }
  }
  return frames; // 用于进度条缩略图（AV-060 的服务端方案替代）
}

// WASM 软解兜底：优先 WebCodecs 硬解
async function pickDecoder(codec) {
  const hw = await VideoDecoder.isConfigSupported({ codec });
  return hw.supported ? 'webcodecs' : 'wasm-decoder'; // 按机型自动选择
}
```
