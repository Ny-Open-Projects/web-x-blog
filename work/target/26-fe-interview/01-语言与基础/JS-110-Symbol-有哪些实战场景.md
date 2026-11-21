---
title: [JS-110] Symbol 有哪些实战场景？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-110：Symbol 有哪些实战场景？

**答**：
- 伪私有属性：symbol 键不进入 Object.keys/for-in/JSON，外部“看不见”但反射仍可获取（非真私有）。
- 常量枚举：避免字符串值撞车，任何两个 Symbol 都不相等。
- 全局注册表：`Symbol.for(key)` 跨模块/跨 iframe 共享同一个 symbol，`Symbol.keyFor` 反查。
- 元编程钩子：`Symbol.toPrimitive`、`Symbol.iterator`、`Symbol.asyncIterator` 等注入语言行为。

```javascript
// 1. 伪私有属性
const _balance = Symbol('balance');
class Account {
  constructor(v) { this[_balance] = v; }
  get balance() { return this[_balance]; }
}
const acc = new Account(100);
console.log(Object.keys(acc));                  // [] — 常规枚举不可见
console.log(JSON.stringify(acc));               // {}
console.log(Object.getOwnPropertySymbols(acc)); // [Symbol(balance)] — 反射仍可拿到

// 2. 常量枚举：永不撞车
const Color = Object.freeze({
  RED: Symbol('red'),
  BLUE: Symbol('blue'),
});
console.log(Color.RED === Color.RED, Color.RED === Symbol('red')); // true false

// 3. 全局注册表：跨模块共享
const s1 = Symbol.for('app:theme');
const s2 = Symbol.for('app:theme');
console.log(s1 === s2, Symbol.keyFor(s1)); // true 'app:theme'

// 4. 元编程：自定义类型转换
const size = {
  [Symbol.toPrimitive](hint) {
    return hint === 'number' ? 42 : '42px';
  },
};
console.log(+size, `${size}`, size + ''); // 42 42px 42px
```
