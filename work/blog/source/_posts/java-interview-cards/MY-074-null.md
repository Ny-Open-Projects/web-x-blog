---
title: "[MY-074] 类型·null（null）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 类型 · null（null）

- **事实**：列默认尽量 NOT NULL：null 影响索引统计、count(col) 忽略 null、is null 判断易错
- **原理**：null 参与比较结果为 unknown、聚合跳过 null、可空列索引需要额外标记，默认 NOT NULL+默认值是规范，但 is null 查询可以走索引
- **常见误区**：
  1. null 不能走索引（错）
  2. NOT NULL 会提升插入性能一个量级（错）
  3. null 不占存储空间（错）
- **工程用法**：建表规范的原理依据
- **版本锚点**：实战共识
