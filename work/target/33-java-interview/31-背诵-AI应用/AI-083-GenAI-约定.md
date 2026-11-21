---
title: "[AI-083] Agent·GenAI 约定（观测）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · GenAI 约定（观测）

- **事实**：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）
- **原理**：跨框架可对比（LangChain/Spring AI 一套仪表盘），属性含 model/input tokens/cost，与通用 trace 融合（Agent 步骤与 HTTP 调用同链路），是观测标准化方向
- **常见误区**：
  1. GenAI 约定是某厂商私有（错）
  2. 只支持 Python（错）
  3. 观测与 trace 无关（错）
- **工程用法**：Agent 观测落地（AI-042 实现）
- **版本锚点**：2024-2025
