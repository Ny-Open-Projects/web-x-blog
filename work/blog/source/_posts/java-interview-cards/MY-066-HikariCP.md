---
title: "[MY-066] 连接·HikariCP（池）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 连接 · HikariCP（池）

- **事实**：HikariCP 是 Spring Boot 2.0+ 默认连接池（字节码优化+FastList+无锁设计最快）
- **原理**：关键参数：maximumPoolSize（经验公式 core×2+磁盘数，连接不是越大越好）、connectionTimeout、maxLifetime（小于 MySQL wait_timeout）
- **常见误区**：
  1. 连接池越大性能越好（错）
  2. HikariCP 是 Boot 1.x 默认（错）
  3. maxLifetime 可以大于 MySQL wait_timeout（错）
- **工程用法**：连接池调优标准参数组
- **版本锚点**：HikariCP 文档
