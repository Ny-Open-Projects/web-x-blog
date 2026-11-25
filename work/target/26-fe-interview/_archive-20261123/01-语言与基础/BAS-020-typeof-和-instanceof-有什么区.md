---
title: [BAS-020] typeof 和 instanceof 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-020：typeof 和 instanceof 有什么区别？
**答**：
- typeof 返回类型字符串，用于原始类型与函数，写法简单但不精确。
- instanceof 检查构造函数的 prototype 是否在对象原型链上，只能用于对象/函数，跨 iframe 会失效（原型链不同）。
- 终极精确方案：`Object.prototype.toString.call(x)`。

```javascript
typeof 'a';                        // 'string'
'a' instanceof String;             // false，原始值不是对象
new String('a') instanceof String; // true
[] instanceof Object;              // true，原型链上能找到 Object.prototype
[] instanceof Array;               // true
```
