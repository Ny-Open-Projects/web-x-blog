---
title: [DP-204] 源码识别：Axios 源码中的适配器与拦截器链？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-204：源码识别：Axios 源码中的适配器与拦截器链？
**答**：
- 适配器模式：adapter（xhr/http/fetch）统一 promise 接口，浏览器与 Node 共用同一套上层逻辑——换环境只换适配器。
- 职责链+装饰：request 拦截器**从后往前**入栈、response 拦截器从前往后，最终拼接成 `chain = [...req.interceptors.reverse(), dispatchRequest, ...res.interceptors]`，用 promise.then 链依次穿过——拦截器本质是对"发送"的洋葱装饰。
- 合并策略：mergeConfig 是策略模式的参数化（deep/浅合并/数组特殊处理），headers 策略按 method/URL 分桶。
- 识别要点：能默写 chain 组装顺序（请求拦截器倒序的原因：后注册先执行，贴近业务）。

```javascript
// Axios dispatchRequest 前的链组装
class InterceptorManager {
  constructor() { this.handlers = []; }
  use(f, r) { this.handlers.push({ fulfilled: f, rejected: r }); }
}
function axios(config) {
  const chain = [dispatchRequest.bind(null, adapter), undefined];     // 核心节点
  request.interceptors.handlers.forEach(h => chain.unshift(h.fulfilled, h.rejected));  // 倒序插入
  response.interceptors.handlers.forEach(h => chain.push(h.fulfilled, h.rejected));
  let promise = Promise.resolve(config);
  while (chain.length) promise = promise.then(chain.shift(), chain.shift());  // 职责链穿行
  return promise;
}
// 适配器统一签名：config => Promise<response>（xhr/http 都实现这个接口）
```
