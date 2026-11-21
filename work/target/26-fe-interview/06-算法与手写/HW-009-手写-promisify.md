---
title: [HW-009] 手写 promisify
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-009：手写 promisify

**答**：
- 评分点：核心是「回调转 Promise」：返回一个新函数，内部 new Promise，在末尾追加 errfirst 风格的 callback（Node.js 约定 `(err, result) => {}`）；callback 里 err 非空 → reject，否则 resolve；要用 `fn.call(this, ...)` 保留原函数的 this；注意 callback 只能被调用一次（有些库会多次回调，需要加 once 保护）；进阶：支持自定义回调位置 / 多参收集（multiArgs）。

```javascript
// ===== 5 分钟速写版 =====
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn.call(this, ...args, (err, data) => {
        err ? reject(err) : resolve(data);
      });
    });
  };
}
// 用法：const readFile = promisify(fs.readFile); readFile('a.txt', 'utf8').then(console.log)

// ===== 标准完整版（含边界处理）=====
function promisifyPro(fn, { multiArgs = false } = {}) {
  if (typeof fn !== 'function') throw new TypeError('fn must be a function');
  return function promisified(...args) {
    return new Promise((resolve, reject) => {
      const callback = (...results) => {
        // once 保护：防止底层多次调用回调导致重复 settle
        if (callback.done) return;
        callback.done = true;
        const err = results[0];
        if (err) return reject(err);
        // multiArgs：resolve(results.slice(1))，如 dns.lookup 返回 [address, family]
        multiArgs ? resolve(results.slice(1)) : resolve(results[1]);
      };
      try {
        fn.call(this, ...args, callback);
      } catch (e) { reject(e); } // 同步抛错也要走 Promise 通道
    });
  };
}
// 自定义回调位置的变体（如 axios 风格 callback 在中间）：
function promisifyWith(fn, cbIndex) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      const cb = (err, data) => (err ? reject(err) : resolve(data));
      args.splice(cbIndex, 0, cb); // 把 callback 插到指定位置
      fn.apply(this, args);
    });
  };
}
```

---
