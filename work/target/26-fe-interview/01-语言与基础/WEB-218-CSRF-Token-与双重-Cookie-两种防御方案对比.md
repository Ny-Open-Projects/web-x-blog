---
title: [WEB-218] CSRF Token 与双重 Cookie 两种防御方案对比？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-218：CSRF Token 与双重 Cookie 两种防御方案对比？

**答**：
- CSRF Token：服务端下发随机 token，前端表单隐藏域或请求头携带，服务端比对。攻击者跨站拿不到 token（受同源策略限制读不到目标站页面内容），无法伪造有效请求。最标准，但要维护 token 生命周期（每会话/每请求刷新）。
- 双重 Cookie：token 同时写在 cookie 和请求参数/头里，服务端比对两者一致。利用「跨站请求会自动带 cookie 但攻击者读不到 cookie」的漏洞。实现简单但依赖前端 JS 从 cookie 读值写进自定义头——cookie 若被 XSS 读走则失效，且子域 cookie 污染会出问题。
- 现代组合：SameSite=Lax 默认值 + 自定义头（X-Requested-With）+ 关键操作二次验证，弱化了显式 token 的必要性，但银行/支付类仍要求 token。
- 无状态 API（JWT 放 localStorage）：不自动带 cookie，天然免疫 CSRF，但把风险转移到 XSS。

```javascript
// 双重 Cookie 实现示意
function getCookie(name) {
  return document.cookie.match(new RegExp(`(?:^|; )${name}=([^;]*)`))?.[1];
}
fetch('/api/transfer', {
  method: 'POST',
  headers: { 'X-CSRF-Token': getCookie('csrf_token') }, // 服务端比对头与 cookie
});
// 服务端: req.headers['x-csrf-token'] === req.cookies.csrf_token
```
