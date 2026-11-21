---
title: [JS-096] 属性描述符全解？get/set 与 value 为什么互斥？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-096：属性描述符全解？get/set 与 value 为什么互斥？

**答**：
- 描述符分两类：数据描述符（value + writable）与访问器描述符（get + set），二者不能混合定义。
- 混用直接抛 TypeError；同一属性要么存值，要么走 getter/setter，不能两者兼得。
- enumerable 决定能否被 for-in/keys 枚举；configurable 为 false 后不能再改回，也不能删除。
- get/set 的 this 是访问属性的对象，可以借此实现“计算属性”或单向只读字段。

```javascript
const obj = {};

// 数据描述符：不可写、不可枚举、不可配置
Object.defineProperty(obj, 'value', {
  value: 1, writable: false, enumerable: false, configurable: false,
});
obj.value = 2;                              // 非严格模式静默失败
console.log(obj.value, Object.keys(obj));   // 1 [] — 不可枚举

// 访问器描述符：get/set
Object.defineProperty(obj, 'access', {
  get() { return this._v ?? 0; },
  set(v) { this._v = Math.max(0, v); },     // 借机做数据校验
  enumerable: true, configurable: true,
});
obj.access = -5;
console.log(obj.access); // 0 — setter 内的约束生效

// 互斥验证：get/set 与 value 混用直接抛 TypeError
try {
  Object.defineProperty(obj, 'bad', { get() {}, value: 1 });
} catch (e) {
  console.log(e instanceof TypeError); // true
}

// 查看描述符
console.log(Object.getOwnPropertyDescriptor(obj, 'access'));
// { get: f, set: f, enumerable: true, configurable: true } — 没有 value/writable
```
