---
title: "[AI-017] Agent·function calling（工具）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · function calling（工具）

- **事实**：function calling：模型输出结构化工具调用（函数名+JSON 参数）而非自然语言，执行后回填结果
- **原理**：工具定义（name/description/参数 schema）质量决定调用准确率，参数校验在应用层（模型可能给错），工具描述写清"什么时候用/不用"
- **常见误区**：
  1. 工具调用参数由代码生成（错）
  2. 工具越多模型越聪明（错）
  3. 无需参数校验（错）
- **工程用法**：Agent 工具层标准机制
- **版本锚点**：实战共识
