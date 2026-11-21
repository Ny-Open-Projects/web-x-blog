---
title: [H5-238] AudioWorklet 是什么，为什么替代 ScriptProcessor
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-238：AudioWorklet 是什么，为什么替代 ScriptProcessor

**答**：
- ScriptProcessor（已废弃）：音频处理回调跑在主线程，处理函数卡顿直接爆音，且抢主线程资源
- AudioWorklet：自定义音频处理代码跑在独立的音频渲染线程，与主线程隔离，回调稳定不丢帧
- 结构：AudioWorkletNode（主线程节点）+ AudioWorkletProcessor（worklet 线程里的处理器，128 样本一帧回调）
- 通信：node.port 与 processor.port 之间 MessagePort 传参（如实时调节增益）
- 用途：实时变声、均衡器、自定义合成器、录音实时处理——DSP 爱好者与语音类应用必备

```javascript
// processor.js
class Gain2 extends AudioWorkletProcessor {
  static get parameterDescriptors() { return [{ name: 'gain', defaultValue: 1 }]; }
  process(inputs, outputs, params) {
    const g = params.gain;               // 可音频级自动化
    const [input, output] = [inputs[0][0], outputs[0][0]];
    for (let i = 0; i < output.length; i++)
      output[i] = input[i] * (g.length > 1 ? g[i] : g[0]);
    return true; // 保持存活
  }
}
registerProcessor('gain2', Gain2);
// main.js
await audioContext.audioWorklet.addModule('processor.js');
new AudioWorkletNode(audioContext, 'gain2');
```
