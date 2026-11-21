---
title: "[SP-055] 事务·timeout（属性）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · timeout（属性）

- **事实**：@Transactional(timeout=5) 限定事务从开始到提交的最长时间
- **原理**：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待
- **常见误区**：
  1. timeout 默认 60 秒（错）
  2. 超时后立即中断正在执行的 SQL（错）
  3. timeout 是连接池参数（错）
- **工程用法**：防大事务的标准配置
- **版本锚点**：Spring 文档
