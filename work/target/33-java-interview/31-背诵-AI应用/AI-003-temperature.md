---
title: "[AI-003] LLM·temperature（参数）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LLM · temperature（参数）

- **事实**：temperature 控制随机性：0 近似确定性输出，越高越发散
- **原理**：事实问答/代码生成用低温（0-0.3），创意写作高温（0.7-1.0），同一问题不同 temperature 结果不同（可复现性依赖低温+种子）
- **常见误区**：
  1. temperature 越高越准（错）
  2. 0 表示不输出（错）
  3. temperature 只影响长度（错）
- **工程用法**：输出稳定性调参
- **版本锚点**：通用
