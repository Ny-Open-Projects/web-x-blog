---
title: [JS-116] 如何封装 cookie 操作？哪些安全属性必须掌握？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-116：如何封装 cookie 操作？哪些安全属性必须掌握？

**答**：
- document.cookie 是字符串接口，读写都要 encodeURIComponent 防注入与特殊字符问题。
- 删除 = 设置一个已过期的 expires；domain/path 必须与写入时一致才能删干净。
- 安全三件套：HttpOnly（JS 读不到，XSS 防护）、Secure（仅 HTTPS 传输）、SameSite（CSRF 防护）。
- HttpOnly 只能由服务端 Set-Cookie 设置，前端封装永远管不到它。

```javascript
const cookie = {
  set(name, value, { days = 7, path = '/', domain, secure = true, sameSite = 'Lax' } = {}) {
    const exp = new Date(Date.now() + days * 864e5).toUTCString();
    let s = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`
          + `; expires=${exp}; path=${path}; SameSite=${sameSite}`;
    if (domain) s += `; domain=${domain}`;
    if (secure) s += '; Secure';
    document.cookie = s; // 注意：一次只能写一个 cookie
  },

  get(name) {
    const prefix = encodeURIComponent(name) + '=';
    const found = document.cookie
      .split('; ')
      .find((c) => c.startsWith(prefix));
    // value 里可能含编码后的 '='，所以要按第一个 = 切
    return found ? decodeURIComponent(found.slice(prefix.length)) : null;
  },

  remove(name, path = '/') { this.set(name, '', { days: -1, path }); },
};

cookie.set('token', 'a=b&c', { days: 1 });
console.log(cookie.get('token')); // a=b&c
cookie.remove('token');

// SameSite 取值：
// Strict  — 完全禁止第三方携带（跳转过来也没有，体验有坑）
// Lax     — 默认值，顶级导航 GET 请求携带，其他第三方不带
// None    — 允许跨站携带，必须同时 Secure
console.log(document.cookie); // HttpOnly 的 cookie 不会出现在这里
```
