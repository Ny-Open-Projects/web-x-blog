---
title: [WEB-152] 写一个 CSRF 攻击示例，三层防御分别怎么配？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-152：写一个 CSRF 攻击示例，三层防御分别怎么配？
**答**：
- 攻击：受害者登录了 bank.com 后访问恶意页，恶意页自动向 bank.com 提交转账表单——浏览器自动带上 Cookie，请求看起来"完全合法"。
- 防御 1：SameSite Cookie（Lax 默认挡住跨站 POST；关键站点显式配 Lax/Strict）。
- 防御 2：CSRF Token——服务端发随机 token，表单或请求头必带，攻击者读不到别的域下的 token。
- 防御 3：校验 Origin/Referer 头，非本站来源直接拒绝；JSON API 可要求自定义头，跨站伪造请求带不出去。

```html
<!-- 攻击页：受害者带着已登录 Cookie 自动提交跨站表单 -->
<form id="evil" method="POST" action="https://bank.example.com/transfer">
  <input type="hidden" name="to" value="attacker">
  <input type="hidden" name="amount" value="10000">
</form>
<script>document.getElementById('evil').submit();</script>
<!-- 防御后：bank.example.com 配 SameSite=Lax，跨站 POST 不会自动带 Cookie -->
<!-- 且服务端要求请求头 X-CSRF-Token 与会话绑定的 token 一致，攻击页拿不到该 token -->
```
