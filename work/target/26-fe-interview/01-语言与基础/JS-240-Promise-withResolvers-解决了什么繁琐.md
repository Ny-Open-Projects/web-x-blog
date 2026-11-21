---
title: [JS-240] Promise.withResolvers：解决了什么繁琐
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-240：Promise.withResolvers 解决了什么繁琐

**答**：
- ES2024：`const { promise, resolve, reject } = Promise.withResolvers()`——resolve/reject 提到外部作用域
- 替代的旧模式：let res, rej; new Promise((r, j) => { res = r; rej = j; })——变量提升 hack 终于退役
- 高频场景：把「事件驱动」转成 Promise（等待某个回调发生）、任务队列的完成通知、与外部系统交互的桥接
- 与手动 deferred 类库的替代关系：不再需要自写 deferred 工具

```javascript
function waitForOpen(ws) {
  const { promise, resolve, reject } = Promise.withResolvers();
  ws.addEventListener('open', () => resolve(ws), { once: true });
  ws.addEventListener('error', () => reject(new Error('连接失败')), { once: true });
  return promise;
}
// 旧写法对比
function waitForOpenOld(ws) {
  let res, rej;
  const promise = new Promise((r, j) => { res = r; rej = j; });
  ws.addEventListener('open', () => res(ws), { once: true });
  return { promise };
}
```
