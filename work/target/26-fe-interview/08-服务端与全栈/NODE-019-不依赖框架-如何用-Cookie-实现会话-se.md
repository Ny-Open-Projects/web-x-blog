---
title: [NODE-019] 不依赖框架，如何用 Cookie 实现会话（session）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-019：不依赖框架，如何用 Cookie 实现会话（session）？
**答**：
- 流程：登录成功 → 服务端生成 `sessionId`，把用户状态存入 store（Map/Redis）→ `Set-Cookie` 下发 `sid`（`HttpOnly` 防 XSS 读、`Secure` 仅 HTTPS、`SameSite=Lax` 防 CSRF）→ 后续请求读 cookie 查 store。
- 生产要求：sessionId 用 `crypto.randomBytes` 生成（防猜解）；store 用 Redis + TTL（内存 Map 重启丢失且无法多实例共享）；滑动过期（每次访问刷新 TTL）。

```javascript
const http = require('node:http');
const crypto = require('node:crypto');

const store = new Map(); // 生产替换为 Redis：redis.setex(`sess:${sid}`, 1800, JSON.stringify(user))

function parseCookies(req) {
  return Object.fromEntries(
    (req.headers.cookie || '').split(';').filter(Boolean)
      .map((p) => p.trim().split('=').map(decodeURIComponent))
      .map(([k, ...v]) => [k, v.join('=')]),
  );
}

http.createServer((req, res) => {
  const cookies = parseCookies(req);

  if (req.url === '/login') {
    const sid = crypto.randomBytes(24).toString('hex');   // 不可预测
    store.set(sid, { uid: 42, role: 'admin', createdAt: Date.now() });
    res.setHeader('set-cookie',
      `sid=${sid}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800`);
    return res.writeHead(200).end('登录成功');
  }

  const sid = cookies.sid;
  const session = sid && store.get(sid);
  if (!session) return res.writeHead(401).end('未登录');

  // 滑动过期：续期
  store.delete(sid);
  store.set(sid, session);
  res.setHeader('set-cookie', `sid=${sid}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1800`);

  if (req.url === '/me') {
    res.writeHead(200, { 'content-type': 'application/json' });
    return res.end(JSON.stringify(session));
  }
  res.writeHead(200).end(`hello uid ${session.uid}`);
}).listen(3000);
```
