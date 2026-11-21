---
title: "[MY-061] 分库分表·ShardingSphere（中间件）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分库分表 · ShardingSphere（中间件）

- **事实**：分库分表中间件：ShardingSphere-JDBC（客户端）与 Proxy（代理层）
- **原理**：JDBC 版无中间层低延迟但接入每应用，Proxy 独立部署语言无关但多一跳，ShardingSphere 是 Apache 顶级项目国内主流
- **常见误区**：
  1. Proxy 版性能一定更好（错）
  2. 中间件能解决跨片事务（错）
  3. 客户端版需要改 SQL（错）
- **工程用法**：选型按运维能力与延迟敏感度
- **版本锚点**：ShardingSphere 文档
