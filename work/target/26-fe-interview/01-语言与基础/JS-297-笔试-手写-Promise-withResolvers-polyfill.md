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

## 变体与延伸（补充）

**变体与延伸**：

1. 有了 Promise 构造函数为什么还需要 withResolvers？ → 构造函数把 resolve/reject 困在 executor 内，要在外部作用域触发就得先把它们存出来，withResolvers 正是把 deferred 模式标准化。
2. 重复调用 resolve 为什么不会抛错？ → Promise 规范规定状态落定后后续 resolve/reject 被静默忽略，这由内置语义保证，polyfill 不需要也不应该额外报错。
3. 为什么用 `new this(...)` 而不是 `new Promise(...)`？ → 让子类调用 `Sub.withResolvers()` 时得到子类实例，保持原型链与 instanceof 正确，硬编码 Promise 会破坏继承。
