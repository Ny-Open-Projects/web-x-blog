---
title: "[JA-569] 工程·schema 键（缓存）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · schema 键（缓存）

- **事实**：结构化输出缓存与 schema 联动：schema 变更=缓存键变化（旧缓存结果形状不匹配），缓存键纳入 schema hash
- **原理**：JA-155 缓存键的结构化补充：schema 是输出"契约"（JA-308 同思想），契约变更即缓存失效
- **常见误区**：
  1. 缓存键与 schema 无关（错）
  2. schema 稳定不变（错）
  3. 旧缓存可复用（错）
- **工程用法**：缓存正确性
- **版本锚点**：实战共识
