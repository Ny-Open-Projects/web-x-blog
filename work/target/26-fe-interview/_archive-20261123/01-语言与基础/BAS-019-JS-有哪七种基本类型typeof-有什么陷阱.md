---
title: [BAS-019] JS 有哪七种基本类型？typeof 有什么陷阱？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-019：JS 有哪七种基本类型？typeof 有什么陷阱？
**答**：
- 七种原始类型：string、number、bigint、boolean、undefined、symbol、null，其余都是 object。
- 陷阱一：`typeof null === 'object'`，历史遗留 bug；陷阱二：`typeof function(){}` 返回 'function' 而非 'object'。
- typeof 区分不了数组和普通对象，要用 Array.isArray 或 Object.prototype.toString.call。

```javascript
typeof 1n === 'bigint';            // true
typeof Symbol() === 'symbol';      // true
typeof null === 'object';          // 历史遗留 bug
typeof [] === 'object';            // 数组和对象无法区分
Array.isArray([]);                 // true，判断数组的正确姿势
Object.prototype.toString.call(new Date()); // '[object Date]'
```
