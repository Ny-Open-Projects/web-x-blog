---
title: "[MQ-058] 安全·ACL（权限）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 安全 · ACL（权限）

- **事实**：MQ 安全：SASL 认证+ACL 授权（按 topic/消费组）+传输加密（TLS）
- **原理**：生产集群多业务共享时按 topic 授权（读写分离），防止误消费/误生产，Kafka SASL/SCRAM 与 ACL 配置
- **常见误区**：
  1. MQ 默认无安全也不需要（错）
  2. ACL 只管生产（错）
  3. TLS 是性能优化（错）
- **工程用法**：安全基线
- **版本锚点**：官方文档
