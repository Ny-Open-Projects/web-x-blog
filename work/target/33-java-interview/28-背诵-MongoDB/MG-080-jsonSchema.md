---
title: "[MG-080] 建模·$jsonSchema（校验）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 建模 · $jsonSchema（校验）

- **事实**：$jsonSchema 集合校验器（validationLevel/validationAction 可配）约束文档结构
- **原理**：无 schema 不等于无约束：validator 在插入/更新时校验（可选 warn 只告警或 error 拒绝），渐进收紧用 validationLevel moderate
- **常见误区**：
  1. 集合校验默认严格拒绝所有写入（错）
  2. jsonSchema 校验影响已存在文档（错）
  3. 无 schema 就无法校验（错）
- **工程用法**：团队规范落地的服务端保障
- **版本锚点**：官方文档
