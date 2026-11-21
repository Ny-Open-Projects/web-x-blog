---
title: "[JA-269] 工程·prompt 压缩（压缩）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · prompt 压缩（压缩）

- **事实**：prompt 压缩技术：选择性删词压缩器（LLMLingua 思路）在保语义下降 token，Java 侧以预处理器接入
- **原理**：长上下文成本压缩（AI-075/103 联动），压缩有语义损失风险需评估回归（AI-077），按收益启用
- **常见误区**：
  1. prompt 压缩不存在（错）
  2. 压缩无损无风险（错）
  3. 压缩只能删句（错）
- **工程用法**：token 压缩手段
- **版本锚点**：实战共识
