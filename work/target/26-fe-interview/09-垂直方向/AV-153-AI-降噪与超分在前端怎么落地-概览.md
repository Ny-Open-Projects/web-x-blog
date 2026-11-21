---
title: [AV-153] AI 降噪与超分在前端怎么落地？（概览）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-153：AI 降噪与超分在前端怎么落地？（概览）
**答**：
- AI 降噪：RNNoise-wasm 跑在 AudioWorklet，逐帧推理输出增益，对非稳态噪声（键盘/人声）优于传统 ANS。
- 超分（SR）：ESRGAN 类模型对低清视频上采样；端上实时 720p 仍吃力，多用于点播离线增强或云端推理。
- 运行环境：WebGPU + WASM SIMD 让端上推理可行；音频在 AudioWorklet、视频在 OffscreenCanvas worker，主线程零阻塞。
- 接入形态：降噪做成本地处理开关（用户可关）；超分做成云端转码选项（成本在服务端）。
- 评估：降噪看 PESQ/STOI 提升，超分看 VMAF（AV-130）提升；端上方案必须 A/B 电量与发热。

```javascript
// denoise-worklet.js：RNNoise-wasm 降噪节点（骨架）
class DenoiseWorklet extends AudioWorkletProcessor {
  static get parameterDescriptors() { return [{ name: 'bypass', defaultValue: 0 }]; }
  constructor() {
    super();
    this.enabled = true;
    import('rnnoise-wasm').then((m) => { this.denoiser = new m.Denoiser(480); }); // 48k 下 10ms 帧 480 采样
    this.port.onmessage = ({ data }) => { if (data.cmd === 'toggle') this.enabled = data.on; };
  }
  process(inputs, outputs, params) {
    const input = inputs[0][0], output = outputs[0][0];
    if (params.bypass[0] || !this.enabled || !this.denoiser || input.length !== 480) {
      output.set(input);
      return true;
    }
    const gain = this.denoiser.computeFrame(input);       // 模型输出逐频点抑制增益
    for (let i = 0; i < input.length; i++) output[i] = input[i] * gain;
    return true;
  }
}
registerProcessor('denoise-worklet', DenoiseWorklet);
```
