---
title: [JS-027] hasOwnProperty 与 for...in 遍历有什么坑？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-027：hasOwnProperty 与 for...in 遍历有什么坑？

**答**：
- for...in 会遍历对象及**原型链上所有可枚举属性**，继承来的方法也会被列出。
- 安全做法：`Object.keys` / `Object.entries`（仅自身可枚举）或 for...in + hasOwnProperty 过滤。
- `hasOwnProperty` 可被覆盖，稳妥写法用 `Object.prototype.hasOwnProperty.call(o, k)`。
- Symbol 键用 `Object.getOwnPropertySymbols` 获取，常规枚举方法都不包含。

```javascript
const base = { inherited: 1 };
const obj = Object.create(base);
obj.own = 2;
obj[Symbol('s')] = 3;

for (const k in obj) console.log(k); // own, inherited —— 含原型属性

for (const k in obj) {
  if (Object.prototype.hasOwnProperty.call(obj, k)) {
    console.log('own:', k); // own
  }
}
console.log(Object.keys(obj));        // ["own"]，仅自身
console.log(Object.getOwnPropertySymbols(obj)); // [Symbol(s)]

// JSON.stringify 与 Object.keys 一样忽略 symbol
```
