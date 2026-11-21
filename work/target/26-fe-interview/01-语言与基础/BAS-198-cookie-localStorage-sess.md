---
title: [BAS-198] cookie、localStorage、sessionStorage 一句话辨析？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-198：cookie、localStorage、sessionStorage 一句话辨析？
**答**：
- cookie：约 4KB、每个 HTTP 请求自动携带、可设过期与 HttpOnly——适合服务端会话凭证。
- localStorage：5~10MB、持久化、同源所有标签页共享、不随请求发送——适合主题、偏好等本地数据。
- sessionStorage：标签页级会话，关标签即清——适合一次性表单草稿、当页状态。

```javascript
document.cookie = 'sid=1; Max-Age=86400; Secure'; // 4KB，随请求自动携带
localStorage.setItem('theme', 'dark');            // 持久，同源跨标签共享
sessionStorage.setItem('draft', 'step2');         // 标签页关闭即清
// 速记：要跟请求走用 cookie，要长期本地存用 localStorage，会话级用 sessionStorage
```
