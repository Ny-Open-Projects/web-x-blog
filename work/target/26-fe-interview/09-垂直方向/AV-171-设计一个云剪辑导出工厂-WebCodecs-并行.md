---
title: [AV-171] 设计一个云剪辑导出工厂（WebCodecs 并行渲染）。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-171：设计一个云剪辑导出工厂（WebCodecs 并行渲染）。（高频）
**答**：
- 痛点：MediaRecorder 是实时导出（1 分钟视频导 1 分钟）；WebCodecs + OfflineAudioContext 可数倍速并行渲染。
- 管线：时间轴 → 渲染计划 → 逐段解码（VideoDecoder）→ Canvas/WebGL 特效合成 → VideoEncoder 编码 → mp4 mux（mp4box.js）。
- 并行：按 GOP/时间段分段并行，各段独立编码后拼接；段任务表支持断点续导与段级重试。
- 音频：OfflineAudioContext 离线渲染整条音轨，与视频时间戳对齐封装。
- 资源管理：VideoFrame/VideoDecoder 用完必须 close，长任务要监控内存。

```javascript
// WebCodecs 导出管线核心（分段并行）
async function exportSegment(plan, range) {
  const frames = [];
  for (const clip of plan.clipsInRange(range)) {
    const decoder = new VideoDecoder({ output: (f) => frames.push(f), error: console.error });
    decoder.configure({ codec: 'avc1.42001f' });
    for (const sample of clip.samples(range)) decoder.decode(sample);
    await decoder.flush();
    decoder.close();
  }
  const encoder = new VideoEncoder({
    output: (chunk, meta) => muxer.addVideoChunk(chunk, meta),
    error: console.error,
  });
  encoder.configure({ codec: 'avc1.640028', width: 1280, height: 720, bitrate: 3_000_000 });
  for (const frame of frames) {                  // 特效合成后编码
    const processed = await applyEffects(frame, plan.effects);
    encoder.encode(processed, { keyFrame: false });
    frame.close();
    processed.close();                           // 及时释放
  }
  await encoder.flush();
  encoder.close();
}
// 分段任务 Promise.all 并行 + 段级重试 全部完成后 mp4 拼接
```
