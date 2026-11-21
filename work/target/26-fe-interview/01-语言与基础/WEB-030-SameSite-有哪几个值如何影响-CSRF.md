---
title: [WEB-030] SameSite 有哪几个值？如何影响 CSRF 防御？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-030：SameSite 有哪几个值？如何影响 CSRF 防御？
**答**：
- `SameSite=Strict`：完全禁止跨站携带，最安全但从外站点链接进来会丢登录态。
- `SameSite=Lax`：允许顶级导航的 GET 请求携带（点链接进来保持登录），禁止表单 POST、img/iframe 等携带；是现代浏览器默认值。
- `SameSite=None`：不做限制，但必须配合 `Secure`，用于需要跨站携带的场景（如第三方支付嵌入）。
- CSRF 的攻击本质是借受害者浏览器自动携带的 Cookie 发请求，SameSite=Lax 已挡住绝大多数；配合 CSRF Token 和校验 Origin/Referer 双保险。

```html
<!-- 攻击原理示意：恶意站点诱导已登录用户打开此页，
     img 标签的 GET 和 form 的 POST 会自动携带目标站 Cookie -->
<form method="POST" action="https://bank.example.com/transfer">
  <input type="hidden" name="to" value="attacker" />
  <input type="hidden" name="amount" value="10000" />
</form>
<script>document.forms[0].submit();</script>
<!-- 防御一：目标站 Cookie 设置 SameSite=Lax，这个跨站 POST 不再携带 Cookie -->
<!-- 防御二：CSRF Token，攻击者拿不到 -->
```

```javascript
// 防御二实现：服务端渲染时注入一次性 CSRF Token，请求头校验
const csrfToken = 'random-per-session-token';

// 前端：从 meta 里取 token，放进自定义请求头
const token = document.querySelector('meta[name="csrf-token"]').content;
fetch('/api/transfer', {
  method: 'POST',
  headers: { 'X-CSRF-Token': token, 'Content-Type': 'application/json' },
  body: JSON.stringify({ to: 'friend', amount: 100 }),
});

// 服务端（Express 中间件）：校验请求头与 Session 中 Token 一致
app.use((req, res, next) => {
  if (req.method === 'POST' && req.headers['x-csrf-token'] !== req.session.csrfToken) {
    return res.status(403).json({ error: 'csrf token invalid' });
  }
  next();
});
```
