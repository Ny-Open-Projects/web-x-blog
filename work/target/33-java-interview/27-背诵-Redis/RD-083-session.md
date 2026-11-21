---
title: "[RD-083] 场景·session（分布式 Session）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 场景 · session（分布式 Session）

- **事实**：分布式会话：Spring Session Data Redis 集中存 session
- **原理**：水平扩容免粘性路由，session 过期靠 Redis TTL，敏感信息加密，与 JWT 方案对比（可撤销性）
- **常见误区**：
  1. 分布式 session 需要粘性路由（错）
  2. Spring Session 自动序列化安全无配置（错）
  3. session 在本地+Redis 双写（错）
- **工程用法**：会话方案选型
- **版本锚点**：实战共识
