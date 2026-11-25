---
title: [PER-1124] 手写一个 CSRF token 校验中间件
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1124：手写一个 CSRF token 校验中间件

**答**：
- 需求：实现 csrfGuard(req, res, next)。对 method 非 GET/HEAD/OPTIONS 的请求：比较 cookie.csrf 与 header.x-csrf-token，不一致返回 403；GET 类请求跳过；Origin 存在时必须在白名单；校验通过挂 req.csrfValid = true。
- 边界：无 cookie 或无 header 都拒绝（双提交缺一不可）；Origin 缺失（老客户端）放行但记录；大小写无关比较用 timing-safe（简化为等长后逐位异或）。
- 评分点：方法白名单；双提交校验；timing-safe；Origin 检查

```javascript
function csrfGuard(WHITELIST) {
  return (req, res, next) => {
    if (['GET', 'HEAD', 'OPTIONS'].includes(req.method)) return next();
    const origin = req.headers.origin;
    if (origin && !WHITELIST.includes(origin))
      return res.status(403).json({ error: 'origin rejected' });
    const cookieT = parseCookie(req.headers.cookie).csrf;
    const headerT = req.headers['x-csrf-token'];
    if (!cookieT || !headerT || !safeEqual(cookieT, headerT))
      return res.status(403).json({ error: 'csrf mismatch' });
    req.csrfValid = true;
    next();
  };
}
function safeEqual(a, b) {
  if (a.length !== b.length) return false;
  let d = 0;
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return d === 0;                                          // 时序安全比较
}
function parseCookie(s) {
  return Object.fromEntries((s ?? '').split(';').filter(Boolean)
    .map(p => p.trim().split('=')));
}
```
