---
title: "[MY-073] 字符集·utf8mb4（utf8mb4）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 字符集 · utf8mb4（utf8mb4）

- **事实**：MySQL 的 utf8 是不完整实现（最多 3 字节），存 emoji 必须 utf8mb4
- **原理**：utf8mb4 是真 UTF-8（4 字节），建表默认 utf8mb4+utf8mb4_0900_ai_ci（8.0 默认排序规则），老库迁移要评估索引长度变化
- **常见误区**：
  1. MySQL utf8 就是标准 UTF-8（错）
  2. utf8mb4 存中文占 4 字节（错）
  3. 排序规则不影响索引长度（utf8mb4 下联合索引长度易超限）（错）
- **工程用法**：建表规范第一条
- **版本锚点**：实战共识
