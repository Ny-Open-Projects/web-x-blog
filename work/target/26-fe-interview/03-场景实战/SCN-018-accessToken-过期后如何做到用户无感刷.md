---
title: [SCN-018] accessToken 过期后如何做到用户无感刷新？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-018：accessToken 过期后如何做到用户无感刷新？
**答**：
- 双 Token：accessToken 短期有效随业务请求携带，refreshToken 长期有效仅用于换新。
- 拦截器捕获 401：用 refreshToken 换新 Token，成功后重放原请求；refreshToken 也失效才踢回登录页。
- 并发 401 只触发一次刷新：用"刷新进行中"的 Promise 复用，所有挂起请求等同一个结果，完成后统一带新 Token 重放。

Token 无感刷新时序：

```mermaid
sequenceDiagram
    participant P as 页面业务代码
    participant I as 请求拦截器
    participant A as 认证接口
    participant B as 业务接口
    P->>I: 发起请求
    I->>B: 携带旧 accessToken
    B-->>I: 401 过期
    I->>I: 挂起原请求<br/>并发 401 共享同一次刷新
    I->>A: 用 refreshToken 换新
    A-->>I: 返回新 accessToken
    I->>B: 带新 Token 重放原请求
    B-->>I: 200 业务数据
    I-->>P: 返回数据<br/>用户全程无感知
```

```javascript
let refreshing = null; // 复用同一次刷新，并发 401 只打一次认证接口
async function request(config) {
  try {
    return await axios(config);
  } catch (err) {
    if (err.response?.status !== 401) throw err;
    refreshing ??= fetch('/api/auth/refresh', {
      method: 'POST',
      body: localStorage.getItem('refreshToken'),
    })
      .then((r) => r.json())
      .then(({ accessToken }) => {
        localStorage.setItem('accessToken', accessToken);
        return accessToken;
      })
      .finally(() => { refreshing = null; }); // 刷新结束清空，下次过期重新刷新
    const token = await refreshing;           // 并发 401 共享同一个 Promise
    config.headers.Authorization = `Bearer ${token}`;
    return axios(config);                     // 重放原请求
  }
}
```
