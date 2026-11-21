---
title: "[JA-162] 工程·maxTokens（成本）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · maxTokens（成本）

- **事实**：maxTokens 设业务合理值：防失控长文（成本）与 LENGTH 截断（JA-110）之间的平衡
- **原理**：无上限 maxTokens 是成本事故源，过小则频繁 LENGTH，按任务类型分档配置
- **常见误区**：
  1. maxTokens 不设也安全（错）
  2. 越大越好（错）
  3. 与 finishReason 无关（错）
- **工程用法**：成本与完整性平衡
- **版本锚点**：实战共识
