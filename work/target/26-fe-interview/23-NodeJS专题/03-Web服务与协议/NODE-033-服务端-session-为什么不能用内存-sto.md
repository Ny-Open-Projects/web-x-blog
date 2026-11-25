---
title: [NODE-033] 服务端 session 为什么不能用内存 store？Redis 方案怎么设计？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-033：服务端 session 为什么不能用内存 store？Redis 方案怎么设计？
**答**：
- 内存 Map 的缺陷：① **多实例不共享**——负载均衡把请求分到另一台机器就"丢登录"；② 重启即全部掉线；③ 无法主动过期，靠定时扫描，泄漏风险。
- Redis 方案：`sess:{sid}` → JSON（user + 角色 + 登录时间），`EXPIRE` 控制 TTL；滑动过期 = 每次访问 `EXPIRE` 续期；多实例共享只需同连一个 Redis（或 Redis Sentinel/Cluster）。
- 附加能力：服务端可**强制下线**（`DEL` 某用户全部 session，用 `user:{uid}:sessions` Set 索引）、单点登录互踢、异地登录检测。黏性会话（ip_hash）只是缓解，不是正解。

```javascript
const Koa = require('koa');
const Redis = require('ioredis');
const crypto = require('node:crypto');
const app = new Koa();
const redis = new Redis(); // 生产: new Redis({ host, port, keyPrefix: 'bff:' })

const SESSION_TTL = 30 * 60; // 30 分钟滑动过期

async function createSession(uid, role) {
  const sid = crypto.randomBytes(24).toString('hex');
  const sess = JSON.stringify({ uid, role, loginAt: Date.now() });
  await redis.setex(`sess:${sid}`, SESSION_TTL, sess);
  await redis.sadd(`user:${uid}:sessions`, sid);   // 索引：一个用户可能多个端登录
  return sid;
}

async function getSession(ctx) {
  const sid = ctx.cookies.get('sid', { signed: false });
  if (!sid) return null;
  const raw = await redis.get(`sess:${sid}`);
  if (!raw) return null;
  await redis.expire(`sess:${sid}`, SESSION_TTL);  // 滑动过期
  return JSON.parse(raw);
}

// 强制下线（封禁/改密码后）
async function kickout(uid) {
  const sids = await redis.smembers(`user:${uid}:sessions`);
  if (sids.length) {
    await redis.del(...sids.map((s) => `sess:${s}`), `user:${uid}:sessions`);
  }
}

app.use(async (ctx, next) => {
  if (ctx.path === '/login') {
    const sid = await createSession(42, 'admin');
    ctx.cookies.set('sid', sid, { httpOnly: true, sameSite: 'lax', maxAge: SESSION_TTL * 1000 });
    ctx.body = { ok: true };
    return;
  }
  const sess = await getSession(ctx);
  if (!sess) { ctx.status = 401; ctx.body = { code: 'AUTH_REQUIRED' }; return; }
  ctx.state.user = sess;
  await next();
});
app.listen(3000);
```
