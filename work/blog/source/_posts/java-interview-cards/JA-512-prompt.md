---
title: "[JA-512] 模型·prompt（多语言）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 模型 · prompt（多语言）

- **事实**：prompt 语言与性能：英文 prompt 在多数模型更稳（训练分布），中文 prompt 经测试决定（模型中文能力演进快）
- **原理**："英文 prompt 更稳"是经验规律而非铁律（JA-216 token 联动），用评估集 A/B 实测决定，与 AI-217 i18n 联动
- **常见误区**：
  1. prompt 必须英文（错）
  2. 中文 prompt 一样好（错）
  3. 无需实测（错）
- **工程用法**：prompt 语言策略
- **版本锚点**：实战共识
