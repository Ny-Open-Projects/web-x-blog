---
title: [DP-027] axios 的 adapter 为什么是适配器模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-027：axios 的 adapter 为什么是适配器模式？（高频）
**答**：
- 同一份 axios API，浏览器端走 XMLHttpRequest，Node 端走 http 模块——两个环境"能力相同、接口不同"，adapter 负责抹平。
- 源码结构：`config.adapter || getDefaultAdapter()`，按 `process.env.TRACK`/`typeof XMLHttpRequest` 判定环境选择适配器。
- 收益：上层拦截器/取消/进度逻辑只写一次；可自定义 adapter 注入 mock（测试）或 RPC（内网直连）。
- 面试可补充：自定义 adapter 只需实现 `dispatchRequest` 期望的 `(config) => Promise<response>` 协议。

```javascript
// axios 简化的适配器选择逻辑（对照源码 lib/adapters/adapters.js）
const knownAdapters = {
  xhr: typeof XMLHttpRequest !== 'undefined', // 浏览器
  http: typeof process !== 'undefined' && typeof process.versions === 'object'
        && process.versions.node,             // Node
};
function getDefaultAdapter() {
  let adapter;
  if (knownAdapters.xhr) adapter = 'xhr';
  else if (knownAdapters.http) adapter = 'http';
  return adapter;
}

// 适配器统一协议：config -> Promise<{ data, status, headers }>
function xhrAdapter(config) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open(config.method, config.url);
    Object.entries(config.headers || {}).forEach(([k, v]) => xhr.setRequestHeader(k, v));
    xhr.onload = () => resolve({ data: JSON.parse(xhr.responseText), status: xhr.status, headers: {} });
    xhr.onerror = () => reject(new Error('Network Error'));
    xhr.send(config.data);
  });
}
function httpAdapter(config) { // Node 端实现签名一致，内部用 http.request（此处示意）
  return Promise.resolve({ data: { mock: 'node', url: config.url }, status: 200, headers: {} });
}

// 派发层：调用方完全不感知环境差异（适配器模式的核心价值）
function axios(config) {
  const name = config.adapter || getDefaultAdapter();
  // adapter 支持两种形态：字符串名（选内置适配器）或直接注入函数（测试 mock）——
  // 漏掉函数分支会让注入的 mock 走进内置表查找拿到 undefined，调用即 TypeError
  const adapter = typeof name === 'function' ? name : { xhr: xhrAdapter, http: httpAdapter }[name];
  return adapter(config);
}
axios({ method: 'GET', url: '/api/user' }).then((r) => console.log(r.status));
// 自定义 adapter：单测注入 mock，不真正发请求
axios({ method: 'GET', url: '/x', adapter: async (c) => ({ data: { ok: 1 }, status: 200, headers: {} }) })
  .then((r) => console.log(r.data)); // { ok: 1 }
```
