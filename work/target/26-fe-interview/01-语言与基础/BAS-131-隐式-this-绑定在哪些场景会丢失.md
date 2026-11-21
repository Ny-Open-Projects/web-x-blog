---
title: [BAS-131] 隐式 this 绑定在哪些场景会丢失？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-131：隐式 this 绑定在哪些场景会丢失？
**答**：
- 方法赋值给变量再调用、方法作为回调传入（forEach/addEventListener/setTimeout）、解构取出方法，这三类都会让 this 脱离原对象。
- 非严格模式下退化为全局对象，严格模式下是 undefined。
- 修复手段：bind 固定 this、箭头函数捕获外层 this、调用时保持 obj.fn() 形式。

```javascript
const obj = { name: 'a', getName() { return this.name; } };
const lost = obj.getName;               // 场景1：赋值给变量
console.log(lost());                    // undefined，this 已丢失
[obj.getName].forEach(fn => console.log(fn())); // 场景2：作为回调传入
const fixed = obj.getName.bind(obj);    // 修复：bind 固定 this
console.log(fixed());                   // 'a'
```
