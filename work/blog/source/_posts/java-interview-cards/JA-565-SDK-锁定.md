---
title: "[JA-565] 工程·SDK 锁定（依赖）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · SDK 锁定（依赖）

- **事实**：供应商 SDK 版本锁定：SDK breaking change（响应类重构）与框架绑定关系，SDK 升级走回归（JA-211）
- **原理**：AI-066 SDK 细节的版本面：SDK 与框架版本矩阵对齐（JA-105 BOM 联动），锁定+评估后升级
- **常见误区**：
  1. SDK 随便升级（错）
  2. SDK 与框架无关（错）
  3. breaking change 不存在（错）
- **工程用法**：SDK 治理
- **版本锚点**：实战共识
