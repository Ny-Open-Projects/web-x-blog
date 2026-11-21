---
title: [JS-008] Symbol 和 BigInt 分别解决什么问题？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-008：Symbol 和 BigInt 分别解决什么问题？

**答**：
- Symbol 创建全局唯一的值，主要用途：对象“隐藏”键名、防止属性冲突、定义协议（Symbol.iterator、Symbol.toPrimitive）。
- `Symbol.for` 注册全局可复用的 symbol，`Symbol.keyFor` 反查。
- BigInt 表示任意精度整数，解决 number 超过 `Number.MAX_SAFE_INTEGER` 后的精度丢失。
- BigInt 与 number 不能直接混合运算，序列化 JSON 也不支持，需要转字符串。

```javascript
const id = Symbol('id');
const user = { [id]: 42, name: 'Tom' };
console.log(Object.keys(user));   // ["name"]，symbol 键不进常规枚举
console.log(user[id]);            // 42

const s1 = Symbol.for('app.key');
const s2 = Symbol.for('app.key');
console.log(s1 === s2);           // true，全局注册表

console.log(9007199254740993 === 9007199254740992); // true，精度丢失
console.log(9007199254740993n === 9007199254740992n); // false
console.log(1n + 1);              // TypeError，不能混算
console.log(1n + BigInt(1));      // 2n
```
