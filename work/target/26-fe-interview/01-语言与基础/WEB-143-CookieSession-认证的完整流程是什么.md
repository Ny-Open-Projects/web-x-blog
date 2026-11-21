---
title: [WEB-143] Cookie-Session 认证的完整流程是什么？分布式下怎么做？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-143：Cookie-Session 认证的完整流程是什么？分布式下怎么做？
**答**：
- 流程：登录成功 → 服务端生成 SessionId → Set-Cookie 下发 → 之后每次请求浏览器自动带上 → 服务端按 SessionId 查会话数据。
- Cookie 只存无意义的 Id，敏感数据在服务端；HttpOnly 防 XSS 偷、Secure 只走 HTTPS、SameSite 防 CSRF。
- 集群问题：Session 存在单机内存会在负载均衡下失效。方案有粘性会话（ip_hash）、Session 复制、集中存储（Redis，主流）。
- Redis 方案的代价：每次鉴权多一次网络查询，要考虑超时与续期策略。
- 登出与踢人简单可靠：删 Redis 记录即全局生效，这是对比 JWT 的核心优势之一。

```javascript
// Express + Redis 集中式 Session：任意节点都能鉴权
const express = require('express');
const session = require('express-session');
const RedisStore = require('connect-redis').default;
const app = express();
app.use(session({
  store: new RedisStore({ client: redisClient }),   // 会话集中存 Redis
  secret: process.env.SESSION_SECRET,              // 签名 Cookie 用的密钥
  resave: false,
  saveUninitialized: false,
  cookie: { httpOnly: true, secure: true, sameSite: 'lax', maxAge: 7 * 86400_000 },
}));
app.get('/me', (req, res) => {
  if (!req.session.userId) return res.status(401).end();
  res.json({ userId: req.session.userId });
});
```
