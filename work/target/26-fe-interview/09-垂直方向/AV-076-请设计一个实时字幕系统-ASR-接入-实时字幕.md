---
title: [AV-076] 请设计一个实时字幕系统（ASR 接入/实时字幕/翻译）。
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-076：请设计一个实时字幕系统（ASR 接入/实时字幕/翻译）。
**答**：
- 语音输入：对端 WebRTC 音频轨 → AudioWorklet 抽取 PCM（16k 单声道）→ WebSocket 分片上传 ASR 引擎 → 流式返回中间/最终结果。
- 实时性策略：中间结果（partial）高频刷新上屏（灰色），最终结果（final）定稿上屏（白色）；延迟控制在 1s 内。
- 字幕渲染：贴在视频下沿，最长 N 字自动换行滚动；两人对话按说话人着色（服务端 speaker diarization）。
- 翻译：final 结果送翻译接口，双行显示原文/译文；翻译迟到时先显示原文再补译文。
- 工程要点：PCM 降采样（48k→16k，AudioWorklet 中做）、静音检测 VAD 省流量、字幕与音轨时间戳对齐（点播回放场景按 PTS 展示）。

```javascript
// PCM 抽取与 ASR 流式对接
class LiveCaptioner {
  async start(stream) {
    const ctx = new AudioContext({ sampleRate: 16000 });
    await ctx.audioWorklet.addModule('pcm-capture.js');
    const src = ctx.createMediaStreamSource(stream);
    this.node = new AudioWorkletNode(ctx, 'pcm-capture-processor');
    this.node.port.onmessage = ({ data }) => {
      if (data.rms > 0.01) this.ws.send(data.pcm.buffer); // VAD 过滤静音
    };
    src.connect(this.node); // 不连 destination，纯抽取
    this.ws = new WebSocket('wss://asr.example.com/stream');
    this.ws.onmessage = (e) => {
      const { partial, final, speaker } = JSON.parse(e.data);
      if (partial) this.renderPartial(partial, speaker);   // 灰色实时刷新
      if (final) this.commitFinal(final, speaker);         // 定稿 + 触发翻译
    };
  }
  commitFinal(text, speaker) {
    this.subtitleEl.renderFinal(text, speaker);
    fetch('/api/translate', { method: 'POST', body: JSON.stringify({ text, to: 'en' }) })
      .then((r) => r.json()).then(({ text: en }) => this.subtitleEl.renderTranslation(en));
  }
}
```

```javascript
// pcm-capture.js — AudioWorklet 降采样与分片
class PcmCaptureProcessor extends AudioWorkletProcessor {
  constructor() {
    super();
    this.ratio = sampleRate / 16000; // 48k→16k 抽取
    this.buffer = [];
    this.pos = 0;
  }
  process(inputs) {
    const ch = inputs[0][0];
    if (!ch) return true;
    for (let i = 0; i < ch.length; i += this.ratio) {
      this.buffer.push(ch[Math.floor(i)]); // 简单抽取降采样
    }
    if (this.buffer.length >= 1600) { // 100ms 一片
      const pcm = new Float32Array(this.buffer);
      this.buffer = [];
      let sum = 0;
      for (const v of pcm) sum += v * v;
      this.port.postMessage({ pcm, rms: Math.sqrt(sum / pcm.length) });
    }
    return true;
  }
}
registerProcessor('pcm-capture-processor', PcmCaptureProcessor);
```
