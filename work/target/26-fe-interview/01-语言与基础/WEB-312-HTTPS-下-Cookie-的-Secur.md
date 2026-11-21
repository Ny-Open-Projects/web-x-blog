---
title: [WEB-312] HTTPS 下 Cookie 的 Secure 和 __Host- 前缀有什么讲究？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-312：HTTPS 下 Cookie 的 Secure 和 __Host- 前缀有什么讲究？
**答**：
- Secure 只允许 HTTPS 传输，但旧接口 http://img.cdn 同域下仍可能被读走——所以关键 Cookie 还要配合 HttpOnly、SameSite。
- __Host- 前缀是浏览器强制约定：必须 Secure、必须 Path=/、不得带 Domain（防子域覆盖根域 Cookie）。
- 命名即安全：浏览器看到 __Host-token 就自动校验，任何不符直接拒绝写入，防"子域攻陷后覆盖主站会话"。

```javascript
// Set-Cookie 校验规则
function setCookie(name, opts) {
  if (name.startsWith('__Host-')) {
    if (!opts.secure || opts.path !== '/' || opts.domain) {
      return 'REJECT: __Host- 必须 Secure + Path=/ + 无 Domain';
    }
  }
  return 'OK';
}
console.log(setCookie('__Host-token', { secure: true, path: '/' }));        // OK
console.log(setCookie('__Host-token', { secure: true, path: '/', domain: 'a.example.com' })); // REJECT
```
