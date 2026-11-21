---
title: "[JA-075] Spring AI·embedding 声明（配置）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · embedding 声明（配置）

- **事实**：embedding provider 用 spring.ai.model.embedding 属性独立声明（与 chat 分开）
- **原理**：chat 与 embedding 可用不同 provider（chat 用云端、embedding 用本地），按属性独立路由
- **常见误区**：
  1. chat 与 embedding 必须同 provider（错）
  2. embedding 无 provider 选择（错）
  3. 属性只控制 chat（错）
- **工程用法**：混合部署配置
- **版本锚点**：Spring AI 1.0 GA
