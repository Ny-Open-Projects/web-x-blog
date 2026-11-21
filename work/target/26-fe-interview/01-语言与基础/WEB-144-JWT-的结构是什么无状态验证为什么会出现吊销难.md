---
title: [WEB-144] JWT 的结构是什么？无状态验证为什么会出现"吊销难"？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-144：JWT 的结构是什么？无状态验证为什么会出现"吊销难"？
**答**：
- JWT 三段：Header（算法）.Payload（Claims）.Signature（对前两段签名）；前两段只是 Base64Url 编码不是加密，人人可解，所以不能放敏感信息。
- 服务端验签即信任，无需查库，天然适配水平扩展与微服务间调用。
- 代价：签发后无法单方面作废，登出/踢人/改密都拦不住，只能等 exp 自然过期。
- 业界折衷：短有效期（如 15 分钟）+ 服务端黑名单（只存"已签发未过期"的被吊销 token，Redis TTL 与剩余有效期对齐自动清理）。
- 算法注意：禁止 none 算法；RS256（非对称）适合多服务验签，HS256（对称）密钥分发要谨慎。

```javascript
const jwt = require('jsonwebtoken');
// 签发：payload 不要放手机号等敏感信息，只是"声明"
const token = jwt.sign({ sub: 'u_42', role: 'admin' }, process.env.JWT_SECRET, { expiresIn: '15m' });
// 验证：验签与过期检查一次完成，无状态可扩展
const payload = jwt.verify(token, process.env.JWT_SECRET);
// 吊销：黑名单只覆盖已签发未过期的 token，TTL 与剩余有效期对齐
await redis.set(`jwt:bl:${token}`, 1, 'EX', payload.exp - Math.floor(Date.now() / 1000));
```
