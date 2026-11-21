---
title: [WEB-508] 笔试：手写 fetch 拦截器（注入 token + 401 刷新重放）
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 鉴权]
type: 笔试题
---

## WEB-508：笔试：手写 fetch 拦截器

**题目**：实现拦截器层 `http(url, opts)`：请求前注入 Authorization；响应 401 时自动刷新 token 并重放一次（只重放一次防死循环）；刷新失败抛专用错误。

**答**：
```javascript
class AuthError extends Error { name = 'AuthError'; }
let refreshing = null;

async function http(url, opts = {}) {
  const res = await fetch(url, {
    ...opts,
    headers: { ...opts.headers, Authorization: `Bearer ${getToken()}` },
  });
  if (res.status !== 401) return res;

  if (opts._retried) throw new AuthError('刷新后仍 401'); // 只重放一次
  refreshing ??= doRefresh().finally(() => (refreshing = null));
  const ok = await refreshing;
  if (!ok) throw new AuthError('刷新失败');
  return http(url, { ...opts, _retried: true }); // 重放一次
}

async function doRefresh() {
  try {
    const r = await fetch('/api/refresh', { method: 'POST', credentials: 'include' });
    if (!r.ok) return false;
    const { access_token } = await r.json();
    localStorage.setItem('token', access_token);
    return true;
  } catch { return false; }
}
const getToken = () => localStorage.getItem('token');
```

**评分点**：
- _retried 内部标记防 401 死循环（重放后再 401 必须抛 AuthError）
- 并发 401 共享一次刷新（refreshing 单例 Promise）
- 刷新失败抛专用错误类型，调用方可精确 catch
- headers 合并保留调用方自定义头
