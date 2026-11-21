---
title: "[SP-056] 事务·readOnly（属性）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · readOnly（属性）

- **事实**：readOnly=true 是只读优化提示非强制约束
- **原理**：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置
- **常见误区**：
  1. readOnly 能强制只读（错）
  2. readOnly 对性能无影响（错）
  3. readOnly 只对 JPA 生效（错）
- **工程用法**：查询类事务标注 readOnly
- **版本锚点**：Spring 文档
