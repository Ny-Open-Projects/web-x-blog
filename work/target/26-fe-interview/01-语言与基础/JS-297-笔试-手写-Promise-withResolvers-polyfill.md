---
title: [JS-297] 笔试：手写 Promise.withResolvers 的 polyfill
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-297：笔试：Promise.withResolvers polyfill

**题目**：实现 `withResolvers()`：返回 { promise, resolve, reject }；resolve/reject 可在任意作用域调用；重复调用按 Promise 语义只认首次；对比 deferred 模式。

**答**：
```javascript
if (!Promise.withResolvers) {
  Promise.withResolvers = function () {
    let resolve, reject;
    const promise = new this((res, rej) => {   // this 指向类（支持子类）
      resolve = res; reject = rej;
    });
    return { promise, resolve, reject };
  };
}

// 验证
const { promise, resolve, reject } = Promise.withResolvers();
resolve('ok');
resolve('later');       // 忽略（Promise 状态锁定）
promise.then(console.log); // 'ok'

// 典型用法：事件→Promise 桥
function once(el, type) {
  const { promise, resolve } = Promise.withResolvers();
  el.addEventListener(type, resolve, { once: true });
  return promise;
}
await once(button, 'click');
```

**评分点**：
- new this(...) 而非硬编码 Promise（子类继承友好）——细节判分
- 重复 resolve 的状态锁定语义（天然由 Promise 保证，需说明）
- 事件桥接用法展示价值
- ES2024 已内置，生产先特性检测（polyfill 只兜底老环境）
