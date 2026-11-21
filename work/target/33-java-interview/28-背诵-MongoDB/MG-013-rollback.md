---
title: "[MG-013] 副本集·rollback（回滚）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · rollback（回滚）

- **事实**：主挂时未被多数派确认的写在切主后被回滚（写进 rollback 目录）
- **原理**：异步复制固有风险，人工可从 rollback 文件恢复，工程防御是 w:majority 让写确认前不返回
- **常见误区**：
  1. 回滚自动合并进新主（错）
  2. 回滚的数据永久丢失无法恢复（错）
  3. 回滚只在网络分区发生（错）
- **工程用法**：数据丢失风险评估
- **版本锚点**：官方文档
