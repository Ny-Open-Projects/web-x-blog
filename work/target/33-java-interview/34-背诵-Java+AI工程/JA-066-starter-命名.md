---
title: "[JA-066] Spring AI·starter 命名（依赖）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · starter 命名（依赖）

- **事实**：Spring AI 1.0 起 model starter 统一命名 spring-ai-starter-model-{provider}（如 spring-ai-starter-model-openai）
- **原理**：1.0 规范了 starter 命名（旧版 spring-ai-openai-spring-boot-starter 已迁移），升级按新名替换依赖
- **常见误区**：
  1. 旧 starter 名在 1.0 继续有效（错）
  2. starter 名与 0.8 相同（错）
  3. 一个项目只能一个 model starter（错）
- **工程用法**：1.0 依赖迁移
- **版本锚点**：Spring AI 1.0 GA
