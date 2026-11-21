---
title: "[JA-502] Agent·verifier（验证）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · verifier（验证）

- **事实**：结果验证器：独立 verifier（规则校验+LLM 交叉验证）检查 Agent 产出，不通过回炉
- **原理**：自我验证（AI-043 失败模式防线）的独立化：生产者与验证者分离（防自欺），验证器可以是规则或另一个模型
- **常见误区**：
  1. Agent 自检足够（错）
  2. verifier 是过度设计（错）
  3. 验证与生成同模型最好（错）
- **工程用法**：结果验证架构
- **版本锚点**：实战共识
