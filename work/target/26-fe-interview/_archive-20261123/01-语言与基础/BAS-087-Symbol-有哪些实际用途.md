---
title: [BAS-087] Symbol 有哪些实际用途？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-087：Symbol 有哪些实际用途？
**答**：
- 创建全局唯一值作对象键，避免属性名冲突；`Symbol.for('key')` 走全局注册表，可跨模块共享。
- 访问语言内置协议：Symbol.iterator、Symbol.toPrimitive、Symbol.asyncIterator 等让对象接入迭代、类型转换机制。
- 作为"半私有"属性：不出现在 for...in 和 Object.keys 中（仍可用 getOwnPropertySymbols 取到），JSON.stringify 也会忽略。

```javascript
const CACHE = Symbol('cache');
class Store {
  [CACHE] = new Map();               // 不会被 Object.keys 枚举
  get(k) { return this[CACHE].get(k); }
}
console.log(Object.keys(new Store()));             // []
console.log(Symbol('a') === Symbol('a'));          // false，每次唯一
console.log(Symbol.for('a') === Symbol.for('a'));  // true，注册表共享
```
