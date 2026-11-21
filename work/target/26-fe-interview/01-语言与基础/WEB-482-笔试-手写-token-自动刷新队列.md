---
title: [WEB-482] 笔试：手写 token 自动刷新队列
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 鉴权]
type: 笔试题
---

## WEB-482：笔试：手写 token 自动刷新队列

**题目**：多个请求同时收到 401 时，只允许发起一次 refresh 请求，其余请求挂起等新 token 后自动重放。刷新失败则清空队列并统一登出。

**答**：
```javascript
let refreshing = null;
const pending = [];

async function fetchWithAuth(url, opt = {}) {
  const res = await fetch(url, {
    ...opt,
    headers: { ...opt.headers, Authorization: `Bearer ${getToken()}` },
  });
  if (res.status !== 401) return res;

  if (!refreshing) {
    refreshing = doRefresh().finally(() => (refreshing = null));
  }
  await refreshing; // 所有 401 请求等同一次刷新
  return fetch(url, { // 刷新成功后重放
    ...opt,
    headers: { ...opt.headers, Authorization: `Bearer ${getToken()}` },
  });
}

function doRefresh() {
  return fetch('/api/refresh', { method: 'POST', credentials: 'include' })
    .then(r => r.ok ? r.json() : Promise.reject(r.status))
    .then(({ access_token }) => localStorage.setItem('token', access_token))
    .catch(err => {
      pending.splice(0).forEach(rej => rej(err));
      localStorage.clear();
      location.href = '/login';
      throw err;
    });
}
```

**评分点**：
- 用单例 Promise（refreshing）做「只刷一次」，这是核心考点
- 刷新成功后必须重放原始请求，且用新 token
- 失败路径：清状态、跳登录，且不能让调用方拿到「假成功」
- 能指出多 tab 场景还需 Web Locks/存储事件协同（加分）
