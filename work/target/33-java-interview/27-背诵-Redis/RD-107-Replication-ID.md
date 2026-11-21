---
title: "[RD-107] 复制·Replication ID（原理）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 复制 · Replication ID（原理）

- **事实**：主从复制以 Replication ID + offset 定位复制进度（PSYNC 基础）
- **原理**：每个主库有唯一 replication id，从库携带 id+offset 请求增量，id 匹配且 offset 在 backlog 内则部分重同步，id 变了（切主/重启）触发全量
- **常见误区**：
  1. 复制进度只靠 offset（错）
  2. id 是随机的无语义（错）
  3. 部分重同步与 id 无关（错）
- **工程用法**：复制协议深入
- **版本锚点**：官方文档
