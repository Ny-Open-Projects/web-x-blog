---
title: "[JA-173] 工程·schema（结构化）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · schema（结构化）

- **事实**：结构化输出的 schema 注入方式：提示词内嵌 JSON Schema（框架自动生成）约束输出格式
- **原理**：entity/POJO 返回背后是 schema 注入而非"魔法"，理解机制才能排查转换失败（JA-099 联动）
- **常见误区**：
  1. schema 由数据库生成（错）
  2. 注入是可选开关（错）
  3. 框架不生成 schema（错）
- **工程用法**：结构化机制理解
- **版本锚点**：实战共识
