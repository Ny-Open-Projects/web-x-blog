---
title: "[JA-608] LangChain4j·provider 数（广度）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · provider 数（广度）

- **事实**：LC4j 的 provider 广度：数十个 provider 模块（OpenAI/Ollama/Anthropic/通义/百川等各有 ChatLanguageModel 实现）
- **原理**：provider 广度是 LC4j 核心卖点（JA-039 对比面），评估 provider 覆盖先查模块清单，新 provider 社区跟进快
- **常见误区**：
  1. LC4j 只有 OpenAI（错）
  2. provider 数量无关紧要（错）
  3. 广度与维护质量冲突（有抽象层对冲）（错）
- **工程用法**：框架广度认知
- **版本锚点**：LangChain4j 1.0
