---
title: [AV-094] AI 与音视频结合有哪些方向？（超分/降噪/虚拟人）（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-094：AI 与音视频结合有哪些方向？（超分/降噪/虚拟人）（高频）
**答**：
- 增强类：视频超分（低清→高清，边缘侧 onnxruntime-web/WebGPU）、实时降噪（RNNoise 类模型跑 AudioWorklet/WASM）、插帧（24→60fps 丝滑）。
- 生成类：虚拟人（AV-077）、AI 换背景（AV-045）、实时字幕/翻译（AV-076）、AI 剪辑（粗剪/精彩片段自动定位）。
- 质量类：无参考画质评估（VQA 模型做 QoE 监控）、卡顿/花屏自动识别（替代用户投诉驱动）。
- 部署形态：端侧（隐私好、零成本、算力受限，onnxruntime-web + WebGPU）、边缘/云侧（模型大、延迟要求高时走 RTC 把帧推上去算完拉回）。
- 工程要点：模型量化（int8）、帧间复用推理结果降频跑、算子兼容性验证（WebGPU 后端对某些算子缺失）。

```javascript
// onnxruntime-web 视频超分管线（WebGPU EP）
import * as ort from 'onnxruntime-web';

class SuperResolution {
  async init() {
    this.session = await ort.InferenceSession.create('/models/espcn-x2.onnx', {
      executionProviders: ['webgpu'], // GPU 加速，回退 wasm
      graphOptimizationLevel: 'all',
    });
  }
  async enhance(videoEl, outCanvas) {
    const ctx = outCanvas.getContext('2d');
    const input = new ort.Tensor('float32', this.preprocess(videoEl), [1, 3, 360, 640]);
    const { output } = await this.session.run({ input }); // 每帧推理
    ctx.putImageData(this.postprocess(output), 0, 0);
  }
  preprocess(video) { // video → NHWC → NCHW float32
    const c = document.createElement('canvas');
    c.width = 640; c.height = 360;
    const d = c.getContext('2d').drawImage(video, 0, 0) ?? c.getContext('2d');
    const px = c.getContext('2d').getImageData(0, 0, 640, 360).data;
    const out = new Float32Array(3 * 360 * 640);
    for (let i = 0; i < 640 * 360; i++) {
      out[i] = px[i * 4] / 255;                       // R
      out[640 * 360 + i] = px[i * 4 + 1] / 255;       // G
      out[2 * 640 * 360 + i] = px[i * 4 + 2] / 255;   // B
    }
    return out;
  }
  postprocess(tensor) { /* tensor → ImageData */ return new ImageData(640, 360); }
}
```
