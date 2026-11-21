---
title: "[SP-089] 安全·JWT（认证）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 安全 · JWT（认证）

- **事实**：JWT 无状态认证：签发→携带→过滤链校验签名
- **原理**：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）
- **常见误区**：
  1. JWT 服务端需存储 token（错）
  2. JWT 载荷加密不可读（错）
  3. JWT 天然防重放（错）
- **工程用法**：分布式会话方案对比
- **版本锚点**：实战共识
