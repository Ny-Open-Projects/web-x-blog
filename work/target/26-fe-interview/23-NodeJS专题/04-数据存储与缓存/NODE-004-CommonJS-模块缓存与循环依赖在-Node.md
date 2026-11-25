---
title: [NODE-004] CommonJS 模块缓存与循环依赖在 Node 中的行为？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-004：CommonJS 模块缓存与循环依赖在 Node 中的行为？
**答**：
- CJS 模块首次加载后写入 `require.cache`（`Module._cache`），再次 `require` 返回**同一实例**——这就是单例模式的天然实现。
- 循环依赖：Node 的 `Module` 在加载前就把模块放入缓存（**部分导出 partial exports**）。A require B、B 又 require A 时，B 拿到的是 A **尚未执行完的部分导出**（只含已赋值的属性），不会死循环，但可能拿到 `undefined`。
- 最佳实践：循环依赖尽量重构消除；确需共享，把公共逻辑抽到第三个模块，或在函数调用时**延迟取值**（函数内再 require / 导出 getter）。

```javascript
// a.js
console.log('a 开始');
exports.name = 'a-name';            // 已完成的导出
const b = require('./b');           // 进入 b.js，b 又 require a → 拿到部分导出
console.log('a 中拿到 b:', b);       // { fromB: 'b-value' }
exports.fromB = b.fromB;
console.log('a 结束');

// b.js
console.log('b 开始');
const a = require('./a');           // a 已在缓存中（执行到一半），拿到部分导出
console.log('b 中拿到 a.name:', a.name); // 'a-name'（赋值在 require b 之前，可取到）
console.log('b 中拿到 a.fromB:', a.fromB); // undefined（还没执行到）
exports.fromB = 'b-value';
console.log('b 结束');

// node a.js 输出：a 开始 → b 开始 → b 中拿到 a.name a-name → b 中拿到 a.fromB undefined
//                → b 结束 → a 中拿到 b fromB b-value → a 结束
```
