---
title: [JS-001] JavaScript 有哪些数据类型？typeof 的返回值有什么坑？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-001：JavaScript 有哪些数据类型？typeof 的返回值有什么坑？

**答**：
- 基本类型 7 种：number、string、boolean、undefined、symbol、bigint、null；引用类型 object。
- `typeof null` 返回 `"object"`，是历史遗留 bug，无法修复。
- `typeof fn` 返回 `"function"`，其余对象都返回 `"object"`。
- `typeof` 对未声明变量不报错，返回 `"undefined"`，可用于安全探测。

```javascript
console.log(typeof 1);            // "number"
console.log(typeof 'a');          // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof null);         // "object"  经典坑
console.log(typeof Symbol());     // "symbol"
console.log(typeof 10n);          // "bigint"
console.log(typeof {});           // "object"
console.log(typeof []);           // "object"  数组需要 Array.isArray
console.log(typeof function(){}); // "function"
console.log(typeof notDeclared);  // "undefined" 不报错
```
