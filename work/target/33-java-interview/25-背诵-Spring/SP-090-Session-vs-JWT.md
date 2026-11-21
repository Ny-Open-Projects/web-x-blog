---
title: "[SP-090] 安全·Session vs JWT（认证）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 安全 · Session vs JWT（认证）

- **事实**：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含
- **原理**：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token
- **常见误区**：
  1. Session 方案无法水平扩展（错）
  2. JWT 无任何中心依赖（刷新仍需存储）（错）
  3. 两方案性能差距是主因（错）
- **工程用法**：按业务需求选型（可撤销性）
- **版本锚点**：实战共识
