---
title: [PER-069] JWT 无法主动失效，吊销方案有哪些？如何对比选型？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-069：JWT 无法主动失效，吊销方案有哪些？如何对比选型？

**答**：
- JWT 的代价是**无状态即不可吊销**，常用四方案：短过期 + refresh 旋转、黑名单（Redis 记 jti 直到 exp）、版本号（用户表存 tokenVersion，签发时写入，校验时比对）、网关会话层统一校验。
- 选型：安全敏感系统用**短过期（5-15 分钟）+ refresh 旋转 + 登出黑名单**，兼顾失效速度与性能；黑名单只存登出/被踢的 jti，量小；改密等场景 bump tokenVersion 一键失效全部旧 token。
- refresh 旋转要检测重用：refresh token 用过即作废，重放旧的说明泄露，触发全端下线。
- 不要把敏感数据放 JWT payload（Base64 可逆），只放 uid/角色等标识。

```javascript
// 服务端（Express + Redis）：短过期 JWT + 登出黑名单 + 重放检测
const jwt = require('jsonwebtoken');
const redis = require('redis'); const rds = redis.createClient();

function signAccessToken(user) {
  return jwt.sign({ uid: user.id, ver: user.tokenVersion }, process.env.JWT_SECRET, {
    expiresIn: '10m',      // 短过期：泄露窗口被限制在 10 分钟
    jwtid: crypto.randomUUID(), // jti 用于黑名单
  });
}

async function authMiddleware(req, res, next) {
  try {
    const payload = jwt.verify(req.headers.authorization.slice(7), process.env.JWT_SECRET);
    if (await rds.get(`jwt:bl:${payload.jti}`)) return res.status(401).end(); // 黑名单命中即失效
    req.user = payload;
    next();
  } catch { res.status(401).end(); }
}

app.post('/logout', authMiddleware, async (req, res) => {
  const decoded = jwt.decode(req.headers.authorization.slice(7));
  const ttl = decoded.exp - Math.floor(Date.now() / 1000);
  await rds.setEx(`jwt:bl:${decoded.jti}`, Math.max(ttl, 1), '1'); // 黑名单只存到自然过期为止
  res.end();
});
```
