---
title: "[JA-096] 工程·base-url（网关）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · base-url（网关）

- **事实**：两框架都支持自定义 base-url 指向 OpenAI 兼容网关（Higress/OneAPI/LiteLLM 类），业务不改代码换供应商
- **原理**：网关统一鉴权/限流/计费/路由（AI-028 联动），Java 应用只认 OpenAI 协议，供应商策略收敛到网关层
- **常见误区**：
  1. base-url 只能官方地址（错）
  2. 网关会破坏框架功能（错）
  3. 切换供应商必须改代码（错）
- **工程用法**：供应商治理架构
- **版本锚点**：实战共识
