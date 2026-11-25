---
title: [MFW-529] React cache() 与 Request Memoization：作用域与实现原理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-529：React cache() 与 Request Memoization 的原理

**答**:
- cache() 的作用域：**单次渲染请求**（AsyncLocalStorage 存储的请求级 Map——同请求内同参数调用返回同一 Promise）；跨请求不缓存（区别于 Data Cache RBL-508）。
- 实现原理：`cache(fn)` 返回包装函数——包装内查「请求级缓存表」（键 = 参数浅比较 + 函数引用）→ 命中返回既有 Promise（去重的关键是返回**同一个 Promise**——并发调用共享一个 pending，而不是各自 fetch）；未命中调用原 fn 并记录。
- 用途场景：generateMetadata 与 page 都要 product 数据 → 同 fetch 自动去重（fetch 的 request memoization 同理，cache() 是通用版）；解决「props 层层传递 vs 各处自取」的架构争论——自取 + cache() = 数据单源且解耦。
- 注意点：参数是「浅比较」（对象参数每次新引用 = 缓存失效——传 id 不传对象）；错误不缓存（失败的 Promise 不进表——重试语义 RBL-856：失败可重调）。
- 追问钩子：为什么「返回同一个 Promise」是去重的核心？——两个组件同时 await：若各自拿到不同 Promise = 双倍请求 + 双倍等待；同一 Promise = 并发共享 pending（单飞 RBL-738 的语言内建版）——「并发合并」是缓存设计的普适需求，cache() 把它内建进语言层而非框架层。

```javascript
// cache() 概念实现
import { cache } from 'react';
const requestMap = new Map();                            // 实际由 ALS 提供作用域
function cache(fn) {
  return (...args) => {
    const key = fn.name + JSON.stringify(args);          // 浅序列化
    if (requestMap.has(key)) return requestMap.get(key); // 同一 Promise
    const p = Promise.resolve(fn(...args)).catch(e => {
      requestMap.delete(key);                            // 失败不缓存（可重试）
      throw e;
    });
    requestMap.set(key, p);
    return p;
  };
}
// 使用：数据单源 + 解耦
const getProduct = cache(async (id) => db.products.find(id));
// metadata 与 page 各自调用，一次查询
export async function generateMetadata({ params }) {
  return { title: (await getProduct(params.id)).name };
}
export default async function Page({ params }) {
  return <h1>{(await getProduct(params.id)).summary}</h1>;
}
```
