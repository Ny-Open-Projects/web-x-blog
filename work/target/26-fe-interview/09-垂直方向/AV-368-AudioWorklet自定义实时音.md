---
title: [AV-368] AudioWorklet：自定义实时音频处理
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-368：AudioWorklet：自定义实时音频处理

**答**：
- AudioWorklet：主线程外音频线程跑 DSP（降噪/变调/分析），比 ScriptProcessor 稳定无卡顿。
- 通信：port 消息传参数（控制）；音频 buffer 用 Float32Array 处理。
- 坑：worklet 内不能访问 DOM/网络——纯计算；参数用 AudioParam 平滑避免爆音。

```javascript
// AudioWorklet 降噪骨架
// processor.js
class DenoiseProcessor extends AudioWorkletProcessor {
  static get parameterDescriptors() {
    return [{ name: 'amount', defaultValue: 0.5, minValue: 0, maxValue: 1 }];
  }
  process(inputs, outputs, params) {
    const input = inputs[0][0], output = outputs[0][0];
    for (let i = 0; i < output.length; i++) {
      const a = params.amount[0];
      output[i] = input[i] * (1 - a * 0.3);            // 简化处理
    }
    return true;                                        // 保持活跃
  }
}
registerProcessor('denoise', DenoiseProcessor);
```
