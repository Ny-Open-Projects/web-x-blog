---
title: "[JA-065] Spring AI·Usage（元数据）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Usage（元数据）

- **事实**：ChatResponse.getMetadata().getUsage() 取 token 用量（promptTokens/generationTokens/totalTokens）
- **原理**：成本归集与预算控制的数据源（AI-045 联动），响应元数据自带无需额外计费接口
- **常见误区**：
  1. token 用量无法获取（错）
  2. Usage 只有总 token（错）
  3. 用量单位是字符数（错）
- **工程用法**：成本工程数据源
- **版本锚点**：Spring AI 1.0 GA
