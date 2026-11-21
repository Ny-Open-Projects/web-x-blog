---
title: [JS-084] 如何手写 promisify？回调转 Promise 的关键是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-084：如何手写 promisify？回调转 Promise 的关键是什么？

**答**：
- 约定：node 风格回调第一个参数是 error，其余是结果（只取第一个结果值）。
- 实现：返回一个新函数，内部把原函数最后一个参数替换为 `err => err ? reject : resolve`。
- 保持 this 透传（`fn.call(this, ...)`），支持 `custom` 符号让特殊函数自定义包装行为。

```javascript
function promisify(fn) {
  function promisified(...args) {
    return new Promise((resolve, reject) => {
      fn.call(this, ...args, (err, data) => (err ? reject(err) : resolve(data)));
    });
  }
  // 仿照 util.promisify.custom：允许目标函数声明自己的 promise 版本
  promisified.custom = Symbol('promisify.custom');
  return promisified;
}

// 模拟一个 fs.readFile 风格 API
const readFileCb = (path, cb) => setTimeout(() => cb(null, `content of ${path}`), 50);
const readFile = promisify(readFileCb);
readFile('./a.txt').then(console.log); // content of ./a.txt

// 多结果回调：只 resolve 第一个结果（与 node 一致）
const multi = (cb) => setTimeout(() => cb(null, 'a', 'b'), 0);
promisify(multi)().then(console.log); // a

// 更通用的变体：全部结果以数组返回
const promisifyAll = (fn) => (...args) =>
  new Promise((resolve, reject) =>
    fn(...args, (err, ...rest) => (err ? reject(err) : resolve(rest.length > 1 ? rest : rest[0]))));
```
