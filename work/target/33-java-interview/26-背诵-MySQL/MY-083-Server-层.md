---
title: "[MY-083] 架构·Server 层（分层）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · Server 层（分层）

- **事实**：MySQL 架构分层：Server 层（连接器/分析器/优化器/执行器）+ 存储引擎层（InnoDB）
- **原理**：连接器管连接与权限、分析器词法语法、优化器选索引与 join 顺序、执行器调引擎接口，缓存（query cache）8.0 已移除
- **常见误区**：
  1. query cache 在 8.0 默认开启（错）
  2. 存储引擎负责 SQL 解析（错）
  3. 权限校验只在连接时做（每查询也校验）（错）
- **工程用法**：架构总图题
- **版本锚点**：MySQL 8.0
