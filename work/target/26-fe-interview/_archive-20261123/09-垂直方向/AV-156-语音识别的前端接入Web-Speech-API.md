---
title: [AV-156] 语音识别的前端接入：Web Speech API 与云服务怎么选？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-156：语音识别的前端接入：Web Speech API 与云服务怎么选？（高频）
**答**：
- Web Speech API：免费零依赖，但只有 Chrome 系实现稳定、流式格式不可控、无 SLA——适合 demo/轻量场景。
- 云 ASR（讯飞/火山/Azure）：流式 partial/final、领域热词、SLA 保障——生产选择。
- 本地 wasm（whisper.cpp）：隐私最好可离线，但模型大（75MB-1.5GB）、速度慢，适合短音频与隐私敏感场景。
- 选型四维：延迟（流式首字 <500ms）、准确率（热词支持）、成本、离线能力。
- 组合策略：会议实时字幕走云流式；录音文件转写走批量接口；隐私场景本地 whisper 兜底。

```javascript
// Web Speech API 实时识别（对照实现，与云 ASR 的 partial/final 语义对齐）
const SR = window.SpeechRecognition ?? window.webkitSpeechRecognition;
const rec = new SR();
rec.continuous = true;
rec.interimResults = true;
rec.lang = 'zh-CN';
let finalText = '';
rec.onresult = (e) => {
  let partial = '';
  for (let i = e.resultIndex; i < e.results.length; i++) {
    const r = e.results[i];
    if (r.isFinal) finalText += r[0].transcript;   // final 落定
    else partial += r[0].transcript;               // partial 中间态
  }
  render(finalText, partial);
};
rec.onerror = (e) => { if (e.error === 'not-allowed') showMicGuide(); };
rec.onend = () => { if (!stopped) rec.start(); };  // Chrome 会自动停 需要重启
rec.start();
```
