---
title: [JS-007] null 和 undefined 的区别与使用场景？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-007：null 和 undefined 的区别与使用场景？

**答**：
- undefined：变量已声明未赋值、函数缺参、对象缺属性、无 return 的函数返回值——系统级“没有值”。
- null：语义明确的“空值”，由开发者主动赋值，如清空引用、初始化对象占位。
- `typeof undefined === 'undefined'`，`typeof null === 'object'`。
- `null == undefined` 为 true 但 `null === undefined` 为 false；JSON 序列化会丢掉 undefined 属性而保留 null。

```javascript
let a;
console.log(a);            // undefined
function f(x) { return x; }
console.log(f());          // undefined
const o = { key: null };
console.log('missing' in o, 'key' in o); // false true

console.log(JSON.stringify({ u: undefined, n: null })); // {"n":null}

// 工程约定：参数默认用默认值语法，清空引用用 null
let cache = null;
cache = fetchData();
```
