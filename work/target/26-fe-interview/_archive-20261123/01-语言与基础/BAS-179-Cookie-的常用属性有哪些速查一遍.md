---
title: [BAS-179] Cookie 的常用属性有哪些？速查一遍。
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-179：Cookie 的常用属性有哪些？速查一遍。
**答**：
- 生命周期：Expires（绝对时间）/ Max-Age（秒数，优先级更高；0 或负数即删除）。
- 作用域：Domain（省略则不含子域）、Path；安全：Secure（仅 HTTPS）、HttpOnly（JS 不可读）、SameSite（Lax/Strict/None 防 CSRF）。
- 单条约 4KB、每域数量有限；设置了 Domain 的 cookie 才会带去子域。

```http
Set-Cookie: sid=abc123; Max-Age=3600; Domain=example.com; Path=/;
  Secure; HttpOnly; SameSite=Lax
# Max-Age=0 即删除；Domain 省略则仅当前主机，不含子域
# HttpOnly 防 XSS 读，Secure 仅 HTTPS 传输，SameSite=Lax 拦大部分跨站请求
# 单条上限约 4KB，超出会被静默丢弃
```
