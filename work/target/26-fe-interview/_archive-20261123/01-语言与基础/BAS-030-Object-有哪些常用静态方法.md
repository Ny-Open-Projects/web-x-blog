---
title: [BAS-030] Object 有哪些常用静态方法？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-030：Object 有哪些常用静态方法？
**答**：
- keys/values/entries：拿键、值、键值对；Object.fromEntries 与 entries 互转。
- assign：浅合并对象；freeze：浅冻结（第一层不可改，嵌套对象仍可改）。
- hasOwn：安全判断自有属性，是 obj.hasOwnProperty 的推荐替代。

```javascript
const obj = { a: 1, b: 2 };
Object.keys(obj);                  // ['a', 'b']
Object.entries(obj);               // [['a', 1], ['b', 2]]
Object.fromEntries([['c', 3]]);    // { c: 3 }
Object.assign({}, obj, { b: 9 });  // { a: 1, b: 9 }，浅合并
Object.hasOwn(obj, 'a');           // true
```
