---
title: [BAS-085] structuredClone 和 JSON 深拷贝有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-085：structuredClone 和 JSON 深拷贝有什么区别？
**答**：
- structuredClone 是原生深拷贝：支持循环引用、Map/Set、Date、RegExp、ArrayBuffer、Blob 等。
- JSON.stringify/parse 会丢 undefined/function/Symbol，Date 变字符串，NaN/Infinity 变 null，循环引用直接抛错。
- structuredClone 也有限制：不能拷贝函数、DOM 节点，原型链方法丢失（拷贝后变普通对象）。

```javascript
const src = { date: new Date(), list: new Set([1, 2]) };
src.self = src;                                  // 循环引用
const a = structuredClone(src);
console.log(a.date instanceof Date, a.list instanceof Set); // true true
try {
  JSON.parse(JSON.stringify(src));               // 循环引用直接抛错
} catch (e) {
  console.log('JSON 深拷贝失败，且类型信息本就会丢失');
}
```
