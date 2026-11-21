---
title: "[JA-084] LangChain4j·timeout（可靠性）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · timeout（可靠性）

- **事实**：LangChain4j 模型 builder 可配 .timeout(Duration) 与 .maxRetries(n) 控制超时与重试
- **原理**：构建期声明可靠性参数（AI-046 超时知识联动），重试幂等前提（JA-056）依旧成立
- **常见误区**：
  1. LC4j 无超时参数（错）
  2. 重试默认无限（错）
  3. timeout 单位是毫秒整数（错）
- **工程用法**：客户端可靠性参数
- **版本锚点**：LangChain4j 1.0
