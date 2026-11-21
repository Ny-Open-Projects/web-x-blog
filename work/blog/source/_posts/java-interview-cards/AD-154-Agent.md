---
title: "[AD-154] 演进·Agent（语音）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 演进 · Agent（语音）

- **事实**：语音 Agent：ASR→Agent→TTS 管线（JA-432），语音延迟要求高（交互体验），Agent 循环的延迟预算更紧
- **原理**：语音场景的延迟约束（JA-423 TTFT 同样适用），打断处理（用户说话中断 Agent），与语音管线知识联动
- **常见误区**：
  1. 语音 Agent 延迟无要求（错）
  2. 管线与 Agent 无关（错）
  3. 打断不需要处理（错）
- **工程用法**：语音 Agent 设计
- **版本锚点**：实战共识
