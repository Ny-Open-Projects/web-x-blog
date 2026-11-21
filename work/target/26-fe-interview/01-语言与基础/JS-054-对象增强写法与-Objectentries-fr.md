---
title: [JS-054] 对象增强写法与 Object.entries/fromEntries 有什么用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-054：对象增强写法与 Object.entries/fromEntries 有什么用？

**答**：
- 属性简写 `{ name }`、方法简写 `{ fn() {} }`、计算属性名 `{ [key]: v }`。
- `Object.entries` 把对象转 [key, value] 数组，配合解构遍历。
- `Object.fromEntries` 是 entries 的逆操作，Map 与对象互转利器。
- `Object.fromEntries` 不改变原对象，注意嵌套仍是浅层处理。

```javascript
const key = 'score';
const student = {
  name: 'Tom',            // 简写
  [`top_${key}`]: true,   // 计算属性名
  run() {},               // 方法简写
  get info() { return this.name; },
};

const obj = { a: 1, b: 2 };
for (const [k, v] of Object.entries(obj)) {
  console.log(k, v);
}

const doubled = Object.fromEntries(
  Object.entries(obj).map(([k, v]) => [k, v * 2])
);
console.log(doubled); // { a: 2, b: 4 }

// Map ↔ 对象互转
const m = new Map([['x', 1], ['y', 2]]);
const plain = Object.fromEntries(m);
const m2 = new Map(Object.entries(plain));
console.log(m2.get('x')); // 1
```
