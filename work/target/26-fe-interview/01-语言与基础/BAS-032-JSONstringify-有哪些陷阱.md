---
title: [BAS-032] JSON.stringify 有哪些陷阱？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-032：JSON.stringify 有哪些陷阱？
**答**：
- undefined、函数、Symbol 属性会被静默丢弃（数组中变 null）；NaN/Infinity 变 null。
- Date 对象会转成 ISO 字符串；循环引用直接抛 TypeError；BigInt 也抛 TypeError。
- 对象定义了 toJSON 会先被调用；用 JSON 做深拷贝会丢失 undefined 和函数，现代项目优先 structuredClone。

```javascript
JSON.stringify({ a: undefined, b: () => 1, c: NaN });
// '{"c":null}'：a、b 被丢弃，NaN 变 null
JSON.stringify(new Date('2026-01-01')); // '"2026-01-01T00:00:00.000Z"'
const o = {}; o.self = o;
JSON.stringify(o); // TypeError: Converting circular structure to JSON
```
