---
title: "[JA-105] 依赖·spring-ai-bom（BOM）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 依赖 · spring-ai-bom（BOM）

- **事实**：Spring AI 用 spring-ai-bom 统一各模块版本（Maven dependencyManagement 导入）
- **原理**：多 starter 项目版本对齐防冲突（SP-107 依赖治理联动），升级只改 BOM 版本号
- **常见误区**：
  1. 各 starter 版本独立管理（错）
  2. BOM 不支持 Maven（错）
  3. 版本不对齐也能用（错）
- **工程用法**：依赖治理
- **版本锚点**：Spring AI 1.0 GA
