---
title: "[MY-108] 实践·DB 保护（限流）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 实践 · DB 保护（限流）

- **事实**：数据库保护三板斧：应用层限流（保护连接池）、连接池上限（HikariCP maximumPoolSize）、DB 层 max_connections
- **原理**：雪崩链路：慢 SQL→连接耗尽→全部服务超时，限流+熔断（快速失败）+慢 SQL 治理三管齐下
- **常见误区**：
  1. 连接数越大吞吐越高（错）
  2. max_connections 设 1 万即可（错）
  3. 连接池与 DB 限流是重复配置（错）
- **工程用法**：高可用防护体系
- **版本锚点**：实战方法论
