---
title: [HW-035] 手写 cookie 读写
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-035：手写 cookie 读写

**答**：
- 评分点：写入是给 `document.cookie` 赋单条字符串 `name=value; path=/; max-age=xxx`（一次只能设一条）；name/value 必须 `encodeURIComponent`（中文与 `=` `;` 等特殊字符）；过期控制两种写法——`expires`（GMT 字符串，`toUTCString()`）或 `max-age`（秒数）；删除 = 设同名 cookie 过期时间为过去（`max-age: 0`）；读取要按 `'; '` 分割并 trim（有的浏览器分隔带空格）。

```javascript
// ===== 5 分钟速写版 =====
const cookieUtil = {
  set(name, value, days = 7) {
    const exp = new Date(Date.now() + days * 864e5);
    document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; expires=${exp.toUTCString()}; path=/`;
  },
  get(name) {
    const match = document.cookie
      .split('; ')
      .find(row => row.startsWith(encodeURIComponent(name) + '='));
    return match ? decodeURIComponent(match.split('=').slice(1).join('=')) : null;
  },
  del(name) { this.set(name, '', -1); } // 设为过去时间即删除
};

// ===== 标准完整版（含边界处理）=====
const cookieUtilPro = {
  set(name, value, { maxAge, expires, path = '/', domain, secure = false, sameSite = 'Lax' } = {}) {
    if (typeof name !== 'string' || name === '') throw new TypeError('cookie name required');
    let str = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
    if (maxAge !== undefined) str += `; max-age=${Math.floor(maxAge)}`;
    if (expires instanceof Date) str += `; expires=${expires.toUTCString()}`;
    if (path) str += `; path=${path}`;
    if (domain) str += `; domain=${domain}`;
    if (secure) str += '; secure';
    str += `; SameSite=${sameSite}`; // 防 CSRF 的基本配置
    document.cookie = str;
  },
  get(name) {
    const prefix = encodeURIComponent(name) + '=';
    for (const row of document.cookie.split(';')) {
      const trimmed = row.trim();        // 分隔符后可能带空格
      if (trimmed.startsWith(prefix)) {
        // 值本身可能含编码后的 = 号，取第一个 = 之后全部
        return decodeURIComponent(trimmed.slice(prefix.length));
      }
    }
    return null;
  },
  getAll() {
    const result = {};
    document.cookie.split(';').forEach(row => {
      const trimmed = row.trim();
      if (!trimmed) return;
      const idx = trimmed.indexOf('=');
      if (idx === -1) return;
      result[decodeURIComponent(trimmed.slice(0, idx))] = decodeURIComponent(trimmed.slice(idx + 1));
    });
    return result;
  },
  del(name, { path = '/', domain } = {}) {
    // 删除必须与原 cookie 的 path/domain 完全一致才能真正删除
    this.set(name, '', { path, domain, maxAge: 0 });
  }
};
```

---
