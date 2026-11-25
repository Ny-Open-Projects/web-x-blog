---
title: [WEB-217] Cookie 的 SameSite 三个取值如何防 CSRF？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-217：Cookie 的 SameSite 三个取值如何防 CSRF？

**答**：
- CSRF 本质：浏览器会自动带 cookie，恶意站点诱导用户浏览器向目标站发请求，cookie 被附上从而冒用身份。
- SameSite=Strict：完全禁止第三方上下文携带，最安全但体验差（从外部链接点进来登录态丢失）。
- SameSite=Lax：导航类 GET 请求（a 标签跳转）可以带，跨站 POST/iframe/XHR 不带——Chrome 默认值，挡住了绝大多数 CSRF（因为 CSRF 攻击多用表单 POST 或 XHR）。
- SameSite=None：不限制，但必须同时加 Secure，否则被浏览器拒绝——第三方 SDK、跨站嵌入场景用。
- 注意 Lax 的缝隙：顶层导航的 GET 副作用请求（如 GET 删除数据）仍会带 cookie，所以副作用操作必须 POST + CSRF token 双保险。

```html
<!-- Set-Cookie 响应头示例 -->
<!-- Set-Cookie: session=abc; SameSite=Lax; Secure; HttpOnly -->

<!-- CSRF 攻击页面：Lax 下这个自动提交的跨站表单不带 cookie，攻击失败 -->
<form action="https://bank.com/transfer" method="POST">
  <input name="to" value="attacker">
  <input type="submit" hidden>
</form>
<script>document.forms[0].submit();</script>
```
