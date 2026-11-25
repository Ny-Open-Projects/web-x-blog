---
title: [AV-242] WebAudio 降噪进阶：自定义音频处理（AudioWorklet）
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-242：WebAudio 降噪进阶：自定义音频处理（AudioWorklet）

**答**：
- 题目：浏览器内置 NS 不够（现场噪音）——AudioWorklet 自定义降噪（谱减法简化版）接入采集链。
- 思路：AudioWorkletProcessor（128 帧/块回调）处理 PCM；谱减法：FFT → 减噪谱 → IFFT；简化版用「幅度门限」替代 FFT（性能优先）。
- 评分点：AudioWorklet 接线；处理块大小与延迟；门限降噪实现。

```javascript
// noise-processor.js（Worklet）
class NoiseGateProcessor extends AudioWorkletProcessor {
  static get parameterDescriptors() { return [{ name: 'threshold', defaultValue: 0.01 }]; }
  process(inputs, outputs, params) {
    const input = inputs[0][0], output = outputs[0][0];
    const th = params.threshold[0];
    // RMS 检测 + 软门限（简化谱减）
    let energy = 0;
    for (let i = 0; i < input.length; i++) energy += input[i] ** 2;
    const rms = Math.sqrt(energy / input.length);
    const gain = rms > th ? 1 : Math.max(0.1, rms / th);    // 软压制（硬切会有爆音）
    for (let i = 0; i < output.length; i++) output[i] = input[i] * gain;
    return true;
  }
}
registerProcessor('noise-gate', NoiseGateProcessor);
// 主线程：await ctx.audioWorklet.addModule('noise-processor.js');
// source → workletNode → destination（插在采集与编码之间）
```
