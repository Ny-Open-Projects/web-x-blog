---
title: "[JA-077] Spring AI·finishReason（元数据）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · finishReason（元数据）

- **事实**：响应元数据含 finishReason（STOP 正常结束/LENGTH 触达 maxTokens/工具调用待续等）
- **原理**：finishReason 驱动业务分支：LENGTH 需截断提示或续写，工具调用需等待下一轮，比只看文本更稳
- **常见误区**：
  1. finishReason 不重要（错）
  2. LENGTH 表示出错（错）
  3. 只有 OpenAI 有该字段（错）
- **工程用法**：生成边界处理
- **版本锚点**：Spring AI 1.0 GA
