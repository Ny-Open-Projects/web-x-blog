---
title: "[JA-568] 安全·Agent 身份（身份）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 安全 · Agent 身份（身份）

- **事实**：Agent 作为一等调用者的身份与授权：Agent 调工具/系统经 OAuth client 身份（非共享超级账号）
- **原理**：JA-235 越权防线的身份面：Agent 有独立身份才能审计与限权（A2A/MCP 生态的身份基座），与零信任思想联动
- **常见误区**：
  1. Agent 用共享账号即可（错）
  2. 身份与审计无关（错）
  3. 授权是可选项（错）
- **工程用法**：Agent 身份体系
- **版本锚点**：实战共识
