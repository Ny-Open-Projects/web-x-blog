---
title: [AV-152] 实时字幕与翻译的架构怎么搭？ASR 流式怎么接入？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-152：实时字幕与翻译的架构怎么搭？ASR 流式怎么接入？（高频压轴）
**答**：
- 链路：音频流（采 Opus/PCM 帧）→ 流式 ASR（增量返回 partial→final）→ 翻译（可流式）→ 字幕广播（信令/IM 通道）→ 各端渲染。
- 流式语义：partial 是持续被修正的中间结果，final 是句级确定结果；前端渲染 partial 但标记"未确定"，final 落定替换。
- 前端接入：getUserMedia → AudioWorklet 采 16k PCM → WebSocket 二进制送云 ASR（讯飞/火山/Azure）。
- 时序对齐：ASR 返回带媒体时间戳，字幕与画面同步；回放场景按 currentTime 定位字幕（可做成字幕轨）。
- 合规：开启字幕即上传音频，必须明示（AV-145）；ASR 按时长计费，要有限流与开关。

```javascript
// 流式 ASR 接入：AudioWorklet 采帧 + WS 送识别
class LiveCaptioner {
  constructor(wsUrl, lang = 'zh') {
    this.ws = new WebSocket(wsUrl);
    this.lang = lang;
  }
  start(stream) {
    const ctx = new AudioContext({ sampleRate: 16000 });   // 多数 ASR 要求 16k
    ctx.audioWorklet.addModule('pcm-capture.js').then(() => {
      const node = new AudioWorkletNode(ctx, 'pcm-capture', { outputChannelCount: [1] });
      ctx.createMediaStreamSource(stream).connect(node);
      node.port.onmessage = ({ data }) => {
        if (this.ws.readyState === WebSocket.OPEN) this.ws.send(data); // 二进制 PCM 帧
      };
      stream.getAudioTracks()[0].addEventListener('ended', () => ctx.close());
    });
    this.ws.onmessage = (ev) => {
      const { mode, text, ts } = JSON.parse(ev.data);      // mode: partial | final
      captionStore.upsert({ lang: this.lang, text, ts, tentative: mode === 'partial' });
    };
  }
}
```
