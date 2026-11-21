---
title: [NODE-035] JWT 如何实现 token 刷新与黑名单（主动作废）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-035：JWT 如何实现 token 刷新与黑名单（主动作废）？
**答**：
- 双 token 方案：**access token 短命（15min）+ refresh token 长命（7d）**。access 过期后用 refresh 换新；refresh 存 Redis（可作废、可检测重放）。
- 黑名单：把"已登出/已作废"的 access token 的 `jti`（唯一 id）写入 Redis，TTL = 该 token 剩余寿命（过期后自动出列，无需清理）。校验时多查一次黑名单（可用本地缓存/布隆过滤降低 Redis 压力）。
- 关键细节：refresh token **一次性使用**（rotation），旧 refresh 被再次使用说明疑似被盗 → 作废整个用户会话族（token family）。

```javascript
const jwt = require('jsonwebtoken');
const Redis = require('ioredis');
const redis = new Redis();

const ACCESS_SECRET = process.env.JWT_SECRET;
const REFRESH_SECRET = process.env.REFRESH_SECRET;

// 登录：签发双 token
async function issueTokens(uid, role) {
  const jti = crypto.randomUUID();
  const access = jwt.sign({ uid, role, jti }, ACCESS_SECRET, { expiresIn: '15m' });
  const refresh = jwt.sign({ uid, typ: 'refresh' }, REFRESH_SECRET, { expiresIn: '7d' });
  await redis.set(`refresh:${uid}`, refresh, 'EX', 7 * 24 * 3600); // 服务端持有，可主动作废
  return { access, refresh };
}

// 中间件：验 access + 黑名单
async function auth(ctx, next) {
  const token = (ctx.get('authorization') || '').replace('Bearer ', '');
  try {
    const claims = jwt.verify(token, ACCESS_SECRET);
    if (await redis.get(`bl:${claims.jti}`)) ctx.throw(401, 'token 已作废');
    ctx.state.user = claims;
  } catch (e) {
    if (e.name === 'TokenExpiredError') { ctx.status = 401; ctx.body = { code: 'TOKEN_EXPIRED' }; return; }
    ctx.throw(401, 'token 无效');
  }
  await next();
}

// 刷新：rotation + 重放检测
app.post('/auth/refresh', async (ctx) => {
  const { refresh } = ctx.request.body;
  const claims = jwt.verify(refresh, REFRESH_SECRET); // 非法直接 401
  const stored = await redis.get(`refresh:${claims.uid}`);
  if (stored !== refresh) {                            // 旧 token 被重放 → 疑似盗用
    await redis.del(`refresh:${claims.uid}`);          // 作废整个会话族
    ctx.throw(401, '检测到重放，请重新登录');
  }
  ctx.body = await issueTokens(claims.uid, claims.role); // 换发新双 token
});

// 登出：access 进黑名单（TTL = 剩余寿命）+ refresh 删除
app.post('/auth/logout', auth, async (ctx) => {
  const { exp, jti, uid } = ctx.state.user;
  await redis.set(`bl:${jti}`, '1', 'EX', exp - Math.floor(Date.now() / 1000));
  await redis.del(`refresh:${uid}`);
  ctx.body = { ok: true };
});
```
