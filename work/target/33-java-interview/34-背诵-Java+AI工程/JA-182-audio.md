---
title: "[JA-182] Spring AI·audio（音频）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · audio（音频）

- **事实**：OpenAI starter 内含音频模型能力（语音转写与 TTS，OpenAiAudioModel 族）
- **原理**：多模态不止图像：语音输入转写后进对话、TTS 合成输出，与 AI-041 多模态管线联动
- **常见误区**：
  1. 音频能力不在 OpenAI starter（错）
  2. 转写必须外接服务（错）
  3. TTS 输出无法流式（错）
- **工程用法**：语音交互接入
- **版本锚点**：Spring AI 1.0 GA
