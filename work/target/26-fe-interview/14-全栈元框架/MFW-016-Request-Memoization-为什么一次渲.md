---
title: [MFW-016] Request Memoization 是怎么实现的？为什么是「单次请求」生命周期？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-016：Request Memoization 是怎么实现的？为什么是「单次请求」生命周期？
**答**：
- 实现：Next 以 **AsyncLocalStorage（ALS）** 为每次请求建独立工作区，在其中包一层 fetch——同请求内同 URL+选项的调用直接复用返回中的 Promise（注意：缓存的是 **Promise 本身**，发起中的请求也能被复用）。
- 为什么按请求隔离：数据 freshness 的合理默认——一次页面渲染内多处取同一数据应去重；跨请求是否缓存属于业务决策（交给 Data Cache/revalidate 显式控制），不能默认。
- 对比 React `cache()`：`cache(fn)` 是通用函数级去重（同样基于 ALS 请求作用域），fetch memo 是对 fetch 的内置特化。
- 陷阱：ALS 作用域外的调用（如顶层模块、事件回调、定时器）不属于任何请求，memo 不生效；POST 请求不参与 memoization（语义是变更）。
- 追问钩子：ALS 也是「请求级上下文传递」的通用手段（日志 traceId、租户信息），面试可类比。

```jsx
// lib/data.ts
import { cache } from 'react';

// cache()：同请求内多次调用 fn 只执行一次，结果共享
export const getUser = cache(async (id) => {
  const rows = await db.user.findUnique({ where: { id } });
  return rows;
});

// app/layout.tsx 与 page.tsx 各调一次 getUser('42') —— 只查一次库
```

```javascript
// fetch memo 的极简实现示意（帮助理解 ALS）
const { AsyncLocalStorage } = require('async_hooks');
const requestStore = new AsyncLocalStorage();

const realFetch = globalThis.fetch;
globalThis.fetch = function memoFetch(url, opts = {}) {
  const store = requestStore.getStore();
  if (!store || (opts.method || 'GET').toUpperCase() !== 'GET') return realFetch(url, opts);
  const key = url + JSON.stringify(opts);
  if (!store.memo.has(key)) {
    store.memo.set(key, realFetch(url, opts)); // 缓存的是进行中的 Promise
  }
  return store.memo.get(key);
};

// server 入口
requestStore.run({ memo: new Map() }, () => renderApp(req, res));
// 响应结束，ALS 作用域销毁，memo 随之失效 —— 单次请求生命周期
```
