---
title: [DP-063] axios 拦截器为什么是职责链？和 Koa 的链有何不同？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-063：axios 拦截器为什么是职责链？和 Koa 的链有何不同？
**答**：
- axios 的 request/response interceptors 都是队列：请求拦截器**后注册先执行**（unshift），响应拦截器先注册先执行。
- 与 Koa 区别：axios 链没有洋葱的"回程"——它把请求拦截器和响应拦截器拼接成**单向链**，`dispatchRequest`（真实请求）在中间。
- 源码形态：`chain = [...requestInterceptors, dispatchRequest, ...responseInterceptors]`，用 `promise = promise.then(chain.shift(), chain.shift())` 逐环连接。
- 每个拦截器都可以改写 config 或直接 reject——节点可短路（如 401 拦截器直接跳登录）。

```javascript
// axios 简化的拦截器链（对照源码 Axios.prototype.request）
class Axios {
  constructor() {
    this.interceptors = {
      request: new InterceptorManager(), // 队列
      response: new InterceptorManager(),
    };
  }
  request(config) {
    // 1. 组链：请求拦截器倒序（后注册先执行） + 真实请求 + 响应拦截器正序
    const chain = [];
    this.interceptors.request.handlers.forEach((h) => chain.unshift(h)); // 注意 unshift
    chain.push(dispatchRequest, undefined);           // 中点：真实请求
    this.interceptors.response.handlers.forEach((h) => chain.push(h, h.rejected));
    // 2. 逐环 .then 连接 —— 单向职责链
    let promise = Promise.resolve(config);
    while (chain.length) {
      promise = promise.then(chain.shift(), chain.shift());
    }
    return promise;
  }
}
class InterceptorManager {
  constructor() { this.handlers = []; }
  use(fulfilled, rejected) { this.handlers.push({ fulfilled, rejected }); }
}
async function dispatchRequest(config) {
  console.log('发起请求', config.url);
  return { config, status: 200, data: { ok: true } }; // 适配器见 DP-027
}
// 使用
const ax = new Axios();
ax.interceptors.request.use((c) => { c.headers = { token: 'x', ...c.headers }; return c; });
ax.interceptors.request.use((c) => { console.log('时间戳拦截器（后注册，先执行）'); return c; });
ax.interceptors.response.use(
  (res) => { console.log('统一剥壳', res.status); return res.data; },  // 成功链
  (err) => { if (err?.status === 401) console.log('跳登录'); throw err; } // 失败链
);
ax.request({ url: '/api/a' }).then((d) => console.log(d));
// 时间戳拦截器（后注册，先执行） -> 发起请求 /api/a -> 统一剥壳 200 -> {ok: true}
```
