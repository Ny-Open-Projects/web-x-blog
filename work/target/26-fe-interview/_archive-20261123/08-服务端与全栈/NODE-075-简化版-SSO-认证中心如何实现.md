---
title: [NODE-075] 简化版 SSO 认证中心如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-075：简化版 SSO 认证中心如何实现？
**答**：
- 单点登录核心：认证中心维护**全局会话**，各子系统通过授权码/票据（ticket）换取本地会话。流程：子系统发现未登录 → 302 到 SSO 登录页（带 return url）→ 用户在 SSO 登录（建立全局会话 cookie，`.sso.com` 顶层域）→ SSO 302 回子系统并带一次性 **ticket** → 子系统后端拿 ticket 换用户信息 → 建立子系统本地 session。
- 单点登出：SSO 登出时销毁全局会话，并回调各子系统登出地址（注册的 logout 回调）销毁本地会话；或子系统每次请求校验中心会话有效性（集中校验模式）。
- 生产实现即 OAuth2/OIDC（NODE-036）：简化版考察能否说清 ticket 的一次性、时效与 redirect 校验。

```javascript
// SSO 认证中心（sso.example.com）
const globalSessions = new Map();   // sid → uid（生产 Redis）
const tickets = new Map();          // ticket → { uid, clientUrl, expires }

app.get('/login', async (ctx) => {
  const { redirect_uri } = ctx.query;              // 子系统回调地址
  // 已有全局会话：直接发 ticket 免登录
  const sid = ctx.cookies.get('sso_sid');
  if (sid && globalSessions.has(sid)) {
    const ticket = crypto.randomBytes(16).toString('hex');
    tickets.set(ticket, { uid: globalSessions.get(sid), redirect_uri, expires: Date.now() + 60_000 });
    return ctx.redirect(`${redirect_uri}?ticket=${ticket}`);
  }
  ctx.body = loginPageHtml;                        // 渲染登录表单，redirect_uri 藏在隐藏域
});

app.post('/login', async (ctx) => {
  const { username, password, redirect_uri } = ctx.request.body;
  const uid = await checkPassword(username, password);
  if (!uid) { ctx.status = 401; ctx.body = '账号或密码错误'; return; }
  const sid = crypto.randomBytes(24).toString('hex');
  globalSessions.set(sid, uid);
  // 全局会话 cookie：.sso.com 顶层域，各子系统跳 SSO 时自动带上
  ctx.cookies.set('sso_sid', sid, { domain: '.sso.com', httpOnly: true, sameSite: 'lax' });
  const ticket = crypto.randomBytes(16).toString('hex');
  tickets.set(ticket, { uid, redirect_uri, expires: Date.now() + 60_000 });
  ctx.redirect(`${redirect_uri}?ticket=${ticket}`);
});

// 子系统后端拿 ticket 换用户信息（服务端对服务端）
app.post('/sso/verify', async (ctx) => {
  const { ticket } = ctx.request.body;
  const record = tickets.get(ticket);
  if (!record || record.expires < Date.now()) ctx.throw(401, 'ticket 无效'); // 一次性 + 60s 时效
  tickets.delete(ticket);
  ctx.body = { uid: record.uid, name: await getUserName(record.uid) };
});

// 单点登出：销毁全局会话 + 通知各子系统
app.post('/logout', async (ctx) => {
  const sid = ctx.cookies.get('sso_sid');
  const uid = globalSessions.get(sid);
  globalSessions.delete(sid);
  ctx.cookies.set('sso_sid', '', { domain: '.sso.com', maxAge: 0 });
  const clients = await db.query('SELECT logout_url FROM sso_clients WHERE uid = ?', [uid]);
  await Promise.allSettled(clients.map((c) => fetch(c.logout_url, { method: 'POST' })));
  ctx.body = { ok: true };
});
```
