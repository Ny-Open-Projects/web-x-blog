---
title: "[AI-048] LLM·vLLM（推理）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LLM · vLLM（推理）

- **事实**：vLLM：PagedAttention 显存分页管理，吞吐比原生高数倍，生产推理主流引擎
- **原理**：KV cache 显存碎片是吞吐瓶颈（分页解决），连续批处理（continuous batching）动态插单，OpenAI 兼容接口（Java 无缝接入），与 Ollama（开发）分工
- **常见误区**：
  1. vLLM 是训练框架（错）
  2. 吞吐无提升（错）
  3. vLLM 只支持单模型（错）
- **工程用法**：推理引擎选型
- **版本锚点**：实战共识
