---
title: [SCN-104] 公司要做 CSRF 攻击演练，前端如何复现攻击过程并给出修复方案？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-104：公司要做 CSRF 攻击演练，前端如何复现攻击过程并给出修复方案？
**答**：
- 复现：攻击页放一个自动提交的隐藏表单 POST 到转账接口；用户已登录且 Cookie 未配 SameSite 或配了 None 时，访问攻击页即中招；Lax 下 GET 顶层导航仍带 Cookie，有副作用的 GET 接口同样中招。
- 修复三件套：Cookie 加 SameSite=Lax/Strict；写操作走 CSRF token（服务端下发、前端放 header 回传，双重提交模式亦可）；服务端校验 Origin/Referer 白名单。
- token 用"cookie + header 双份比对"实现零存储成本，前端只需拦截器统一注入。

```javascript
// CSRF 修复：token 双重提交 + axios 拦截器自动携带
// 1) 服务端下发非 HttpOnly 的 XSRF-TOKEN cookie，前端读取
const csrfToken = getCookie('XSRF-TOKEN');

const http = axios.create();
http.interceptors.request.use((config) => {
  // 2) 写操作统一在 header 携带，服务端比对 cookie 与 header 中的 token
  if (['post', 'put', 'delete', 'patch'].includes(config.method)) {
    config.headers['X-CSRF-Token'] = csrfToken;
  }
  return config;
});

// 演练复现脚本（攻击者视角，仅内部演练使用）attack.html：
// <form action="https://bank.example.com/api/transfer" method="POST">
//   <input name="to" value="attacker"><input name="amount" value="10000">
// </form>
// <script>document.forms[0].submit()</script>   // 已登录用户访问即中招

// 服务端校验逻辑示意：Origin 校验 + token 比对双保险
app.use((req, res, next) => {
  const origin = req.headers.origin ?? req.headers.referer;
  if (req.method !== 'GET' && !isTrustedOrigin(origin)) {
    return res.status(403).end('csrf blocked');
  }
  if (req.get('X-CSRF-Token') !== req.cookies['XSRF-TOKEN']) {
    return res.status(403).end('csrf token mismatch');
  }
  next();
});
```
