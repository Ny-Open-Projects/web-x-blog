---
title: [JS-145] 严格模式与非严格模式下 this 的差异输出题？class 里为什么 this 更容易报错？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-145：严格模式与非严格模式下 this 的差异输出题？class 里为什么 this 更容易报错？

**答**：
- 非严格模式独立调用时 this 被包装为 globalThis（浏览器是 window）；严格模式保持 undefined，不包装。
- `call(null/undefined)` 非严格下替换为 globalThis，严格下原样传递。
- 严格模式下原始值 this 不装箱：`call(42)` 的 this 就是数字 42；非严格会装箱成 Number 对象。
- class 内部自动启用严格模式，方法提取后独立调用 this 为 undefined，访问属性直接抛 TypeError。
- 严格模式的 this 规则让「无意的全局污染」和「隐式指向 window」在开发期就暴露为错误。

```javascript
function sloppy() {
  console.log('sloppy', this);   // globalThis（浏览器是 window）
}
function strict() {
  'use strict';
  console.log('strict', this);   // undefined：独立调用不包装全局
}
sloppy();
strict();
sloppy.call(null);   // 仍是 globalThis：null/undefined 被替换为全局
strict.call(null);   // null 原样传递
strict.call(42);     // 42：严格模式原始值不装箱

class Box {
  constructor() { this.v = 1; }
  get() { return this.v; }       // class 体内自动严格模式
}
const box = new Box();
const g = box.get;
try {
  g();                            // this === undefined
} catch (e) {
  console.log('class 方法提取调用报错：', e.message); // Cannot read properties of undefined
}
```
