---
title: [WEB-020] 常见的 4xx 状态码分别代表什么？前端如何针对性处理？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-020：常见的 4xx 状态码分别代表什么？前端如何针对性处理？
**答**：
- 400 参数错误、401 未认证（缺 token 或 token 失效）、403 已认证但无权限、404 资源不存在、405 方法不支持、429 请求过于频繁。
- 401 通常触发"跳登录/刷新 token"，403 提示无权限界面，二者语义不能混用。
- 429 要读取 `Retry-After` 头做退避重试，而不是立即重发。
- 统一在请求层拦截处理，避免每个业务代码都写一遍。

```javascript
// 封装统一的状态码拦截处理
async function request(url, options = {}) {
  const res = await fetch(url, options);
  switch (res.status) {
    case 401: {
      // 尝试用 refresh token 换新 token 后重放请求
      const refreshed = await fetch('/api/auth/refresh', { method: 'POST' });
      if (refreshed.ok) return request(url, options); // 换到新 token，重发原请求
      location.href = '/login'; // 刷新也失败，跳登录
      return Promise.reject(new Error('unauthorized'));
    }
    case 403:
      return Promise.reject(new Error('没有权限执行此操作'));
    case 429: {
      const retryAfter = Number(res.headers.get('Retry-After') || 2);
      await new Promise((r) => setTimeout(r, retryAfter * 1000)); // 退避后重试
      return request(url, options);
    }
    default:
      if (!res.ok) return Promise.reject(new Error(`HTTP ${res.status}`));
      return res.json();
  }
}
```
