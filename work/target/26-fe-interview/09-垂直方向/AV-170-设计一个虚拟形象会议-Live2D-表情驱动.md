---
title: [AV-170] 设计一个虚拟形象会议（Live2D/表情驱动）。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-170：设计一个虚拟形象会议（Live2D/表情驱动）。（高频）
**答**：
- 隐私动机：不想露脸但要有临场感——摄像头视频在本地转成表情参数，只传参数 + 音频，带宽极低且隐私好。
- 链路：本地人脸关键点（MediaPipe FaceMesh）→ 表情参数（嘴型/眉毛/头部姿态）→ 渲染 Live2D/VRM → 合成会议流。
- 两种传输：传合成后的画面（兼容性最好）或只传参数（接收端渲染，最省带宽）；音频照常 RTC。
- 同步：表情参数 15-30Hz 更新；嘴型用音频能量驱动最稳（不需要精确音素）。
- 性能：推理放 worker/OffscreenCanvas，低端机降帧到 15Hz。

```javascript
// 摄像头 → 表情参数 → 虚拟形象合成
async function avatarPipeline(cameraStream) {
  const mesh = await loadFaceMesh();               // MediaPipe wasm
  const canvas = document.createElement('canvas'); // 形象渲染层
  (async function loop() {
    const pts = await mesh.detect(cameraStream);
    const params = {                               // 关键参数映射
      mouthOpen: pts.mouthGap,
      browUp: pts.browRaise,
      headYaw: pts.yaw,
      headPitch: pts.pitch,
    };
    renderL2D(canvas, params);                     // 驱动 Live2D 模型
    paramChannel.send(params);                     // 可选：只传参数 30Hz
    requestAnimationFrame(loop);
  })();
  return canvas.captureStream(30);                 // 作为 video 轨入会
}
```
