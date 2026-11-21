---
title: "[MY-037] 事务·RC vs RR（隔离）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · RC vs RR（隔离）

- **事实**：RC（读已提交）每条语句生成新 ReadView，RR（可重复读）事务内首次查询生成并复用
- **原理**：这就是 RC 能读到别人新提交、RR 全程快照一致的机制差异，参数 transaction_isolation 控制
- **常见误区**：
  1. RC 与 RR 用同一份 ReadView（错）
  2. RR 每语句刷新 ReadView（错）
  3. RR 是 SQL 标准默认（InnoDB 默认 RR 是 MySQL 实现选择）（错）
- **工程用法**：隔离级别差异的根本解释
- **版本锚点**：InnoDB 文档
