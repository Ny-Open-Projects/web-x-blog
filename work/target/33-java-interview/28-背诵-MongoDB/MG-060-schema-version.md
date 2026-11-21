---
title: "[MG-060] 建模·schema_version（演进）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 建模 · schema_version（演进）

- **事实**：文档加 schema_version 字段支持多版本共存灰度迁移
- **原理**：新结构新版本写入，旧版本懒迁移（读时转换+回写），避免停机全量改写，与接口版本演进同理
- **常见误区**：
  1. schema 改动需全量刷数据（错）
  2. schema_version 无必要（错）
  3. 多版本共存不可能（错）
- **工程用法**：大集合 schema 演进技巧
- **版本锚点**：实战方法论
