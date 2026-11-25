---
title: [JS-247] Object.groupBy 返回 null prototype 的原因
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-247：Object.groupBy 返回 null 原型对象的原因

**答**：
- 返回对象是 Object.create(null)：没有原型——安全考量是主因
- 原因一：防原型污染/键冲突——分组键来自数据，若用户数据含 "constructor"/"__proto__"，普通对象会命中原型属性产生诡异的「假分组」
- 原因二：干净遍历——for-in 不会意外枚举到原型链（虽然自有枚举也安全，null 原型彻底杜绝）
- 使用注意：没有 Object 原型方法（hasOwnProperty 要用 Object.hasOwn）；JSON.stringify 正常；解构正常
- 通用教训：凡「键来自不可信数据」的对象，都用 null 原型（qs 库的历史 CVE 教训）

```javascript
const g = Object.groupBy(items, i => i.type); // i.type 来自用户数据
g['__proto__'];     // undefined —— 不会命中 Object.prototype
Object.hasOwn(g, 'fruit');  // ✅ 检查分组用 hasOwn
```
