---
title: [MP-085] 请求层如何封装（拦截器、token、重试）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-085：请求层如何封装（拦截器、token、重试）？
**答**：
- 封装 request(options)：自动拼 baseUrl/环境、统一注入 token header、统一错误码处理（401 重登、业务码分发）、超时与重试（幂等 GET 才重试）。
- 支持 abort（防竞态：路由切换取消旧请求）、loading 分级控制。
- Promise 化 + 泛型（TS 项目），与登录态刷新（refresh token 或静默 wx.login）联动。

```javascript
// utils/request.js
function request(options) {
  const task = wx.request({
    url: BASE_URL + options.url,
    method: options.method || 'GET',
    data: options.data,
    header: { Authorization: wx.getStorageSync('token') },
    timeout: 10000,
    success: (res) => {
      if (res.statusCode === 401) return reloginAndRetry(options)
      if (res.data.code !== 0) return handleError(res.data)
      options.resolve(res.data.data)
    },
    fail: (e) => {
      if (options.method === 'GET' && options.retry < 2) {
        return request({ ...options, retry: (options.retry || 0) + 1 }) // 幂等重试
      }
      options.reject(e)
    }
  })
  return task   // 返回 task 支持 abort 防竞态
}
```
